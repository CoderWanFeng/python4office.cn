'use strict';

/**
 * 为静态资源预生成 .gz 和 .br 文件，让 CDN/源站透传压缩版本
 *
 * 工作原理：
 * 1. 扫描 public/ 下的 .html / .css / .js / .svg / .xml / .json / .txt 文件
 * 2. 跳过 mtime 较新（已压缩）的文件（hexo server watch 时只压新文件）
 * 3. 每个文件生成同名的 .gz（gzip level 9）和 .br（brotli level 6）
 * 4. 部署时一起上传到源站
 *
 * 性能权衡：
 * - brotli level 6（不是 11）：压缩比差 1-2%，速度快 4 倍
 * - 增量：mtime 比压缩文件新的才压（避免每次 watch 触发时全量重压）
 * - 并行：默认单线程。HEXO_PRECOMPRESS_CONCURRENCY=N 可设并行
 *
 * 注意：
 * - 不会覆盖原始 .css / .js / .html 文件本身
 * - 小于 MIN_SIZE 的文件不压缩（gzip 反而更大）
 * - 写入失败的资源不影响其他资源
 *
 * 环境变量：
 * - FORCE_RECOMPRESS=1  忽略 mtime 强制全量重压
 * - HEXO_PRECOMPRESS_LEVEL=N  覆盖默认 brotli level 6
 * - HEXO_PRECOMPRESS_CONCURRENCY=N  并行 worker 数（默认 1）
 */

const FS = require('fs');
const PATH = require('path');
const ZLIB = require('zlib');

const TARGET_EXTS = new Set(['.html', '.htm', '.css', '.js', '.svg', '.xml', '.json', '.txt']);
const MIN_SIZE = 1024;            // 1KB 以下的文件不压缩
const GZIP_LEVEL = 9;
const DEFAULT_BROTLI_LEVEL = 6;   // 11 太慢（首次 5-10 分钟），6 平衡

const FORCE = process.env.FORCE_RECOMPRESS === '1';
const BROTLI_LEVEL = Math.max(1, Math.min(11,
  parseInt(process.env.HEXO_PRECOMPRESS_LEVEL, 10) || DEFAULT_BROTLI_LEVEL
));
const CONCURRENCY = Math.max(1,
  parseInt(process.env.HEXO_PRECOMPRESS_CONCURRENCY, 10) || 1
);

function shouldProcess(filename) {
  const ext = PATH.extname(filename).toLowerCase();
  return TARGET_EXTS.has(ext);
}

function needsCompress(filepath) {
  if (FORCE) return true;
  const stat = FS.statSync(filepath);
  if (!stat.isFile() || stat.size < MIN_SIZE) return false;
  // 增量：如果 .gz 比源文件新，跳过
  const gzPath = filepath + '.gz';
  const brPath = filepath + '.br';
  let gzNew = false, brNew = false;
  try { gzNew = FS.statSync(gzPath).mtimeMs >= stat.mtimeMs; } catch (_) {}
  try { brNew = FS.statSync(brPath).mtimeMs >= stat.mtimeMs; } catch (_) {}
  return !(gzNew && brNew);
}

function compressFile(filepath) {
  const stat = FS.statSync(filepath);
  if (!stat.isFile() || stat.size < MIN_SIZE) return null;

  const buf = FS.readFileSync(filepath);

  const gz = ZLIB.gzipSync(buf, { level: GZIP_LEVEL });
  FS.writeFileSync(filepath + '.gz', gz);

  if (stat.size > 16 * 1024 * 1024) {
    return { original: stat.size, gz: gz.length, br: null };
  }
  const br = ZLIB.brotliCompressSync(buf, {
    params: { [ZLIB.constants.BROTLI_PARAM_QUALITY]: BROTLI_LEVEL },
  });
  FS.writeFileSync(filepath + '.br', br);

  return { original: stat.size, gz: gz.length, br: br.length };
}

function walk(dir, out) {
  out = out || [];
  for (const name of FS.readdirSync(dir)) {
    const p = PATH.join(dir, name);
    const s = FS.statSync(p);
    if (s.isDirectory()) walk(p, out);
    else out.push(p);
  }
  return out;
}

function fmtSize(n) {
  if (n == null) return 'n/a';
  if (n < 1024) return n + 'B';
  if (n < 1024 * 1024) return (n / 1024).toFixed(1) + 'K';
  return (n / 1024 / 1024).toFixed(2) + 'M';
}

function runSequential(targets) {
  let skipCount = 0;
  let compressed = 0;
  const byExt = {};
  const bigHits = [];
  for (const f of targets) {
    try {
      if (!needsCompress(f)) {
        skipCount++;
        continue;
      }
      const r = compressFile(f);
      if (!r) {
        skipCount++;
        continue;
      }
      compressed++;
      const ext = PATH.extname(f).toLowerCase();
      if (!byExt[ext]) byExt[ext] = { count: 0, original: 0, gz: 0, br: 0 };
      byExt[ext].count++;
      byExt[ext].original += r.original;
      byExt[ext].gz += r.gz;
      if (r.br) byExt[ext].br += r.br;
      bigHits.push({
        path: f.replace(hexo.public_dir, ''),
        ...r,
        ratio: r.br ? r.br / r.original : (r.gz / r.original),
      });
    } catch (e) {
      hexo.log.warn('[precompress] 跳过 %s: %s', f, e.message);
    }
  }
  return { skipCount, compressed, byExt, bigHits };
}

function run() {
  // 用绝对路径兜底：hexo.public_dir 在某些钩子时序下可能未解析或目录尚未就绪
  const publicDir = PATH.resolve(hexo.base_dir || process.cwd(), hexo.config.public_dir || 'public');

  if (!FS.existsSync(publicDir)) {
    hexo.log.warn('[precompress] 目录不存在，跳过: %s', publicDir);
    return;
  }

  const t0 = Date.now();
  hexo.log.info(
    '[precompress] 扫描 %s（brotli level %d, %s）...',
    publicDir,
    BROTLI_LEVEL,
    FORCE ? '强制全量' : '增量（mtime 检查）'
  );

  let allFiles, targets;
  try {
    allFiles = walk(publicDir);
    targets = allFiles.filter(shouldProcess);
  } catch (e) {
    hexo.log.warn('[precompress] walk 失败，跳过: %s', e.message);
    return;
  }
  hexo.log.info('[precompress] walk 找到 %d 个文件，待处理 %d 个', allFiles.length, targets.length);

  const { skipCount, compressed, byExt, bigHits } = runSequential(targets);

  // 输出汇总
  const elapsed = ((Date.now() - t0) / 1000).toFixed(1);
  hexo.log.info(
    '[precompress] 用时 %ss  压缩 %d，跳过 %d',
    elapsed,
    compressed,
    skipCount
  );
  if (compressed > 0) {
    hexo.log.info('[precompress] === 汇总 ===');
    for (const ext of Object.keys(byExt).sort()) {
      const s = byExt[ext];
      const gzRatio = ((1 - s.gz / s.original) * 100).toFixed(1);
      const brRatio = s.br ? ((1 - s.br / s.original) * 100).toFixed(1) : 'n/a';
      const extPad = (ext + '      ').slice(0, 6);
      hexo.log.info(
        '  ' + extPad + ' ' + s.count + ' 个   原 ' + fmtSize(s.original) +
        '  →  gz ' + fmtSize(s.gz) + ' (-' + gzRatio + '%)  br ' +
        (s.br ? fmtSize(s.br) : 'n/a') + ' (-' + brRatio + '%)'
      );
    }
    // 收益 top 5
    bigHits.sort((a, b) => a.ratio - b.ratio);
    hexo.log.info('[precompress] === 收益 top 5 ===');
    for (const h of bigHits.slice(0, 5)) {
      hexo.log.info(
        '  ' + h.path + '   ' + fmtSize(h.original) + ' → ' + fmtSize(h.br) +
        ' (-' + ((1 - h.ratio) * 100).toFixed(1) + '%)'
      );
    }
  }
}

hexo.extend.filter.register('after_generate', run);

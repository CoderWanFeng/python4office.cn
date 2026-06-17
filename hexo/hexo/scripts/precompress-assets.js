'use strict';

/**
 * 为静态资源预生成 .gz 和 .br 文件，让 CDN/源站透传压缩版本
 *
 * 工作原理：
 * 1. 扫描 public/ 下的 .html / .css / .js / .svg / .xml / .json / .txt 文件
 * 2. 每个文件生成同名的 .gz（gzip）和 .br（brotli）版本
 * 3. 部署时一起上传到源站
 * 4. CDN 配置回源协商 Accept-Encoding: br, gzip 后，源站 nginx 可：
 *    - 用 gzip_static on; 找到 .css.gz 并以 Content-Encoding: gzip 返回
 *    - 用 brotli_static on; 找到 .css.br 并以 Content-Encoding: br 返回
 *    - 都未配则不生效（fallback 到原始文件）
 * 5. CDN 把 origin 的 Content-Encoding 头透传给客户端，客户端解压渲染
 *
 * 注意：
 * - 不会覆盖原始 .css / .js / .html 文件本身
 * - 小于 MIN_SIZE 的文件不压缩（gzip 反而更大）
 * - 写入失败的资源不影响其他资源
 */

const FS = require('fs');
const PATH = require('path');
const ZLIB = require('zlib');

const TARGET_EXTS = new Set(['.html', '.htm', '.css', '.js', '.svg', '.xml', '.json', '.txt']);
const MIN_SIZE = 1024;            // 1KB 以下的文件不压缩
const GZIP_LEVEL = 9;
const BROTLI_LEVEL = 11;          // 最高质量（hexo 一次性构建，可重）

function shouldProcess(filename) {
  const ext = PATH.extname(filename).toLowerCase();
  return TARGET_EXTS.has(ext);
}

function compressFile(filepath) {
  const stat = FS.statSync(filepath);
  if (!stat.isFile() || stat.size < MIN_SIZE) return null;

  const buf = FS.readFileSync(filepath);

  const gz = ZLIB.gzipSync(buf, { level: GZIP_LEVEL });
  FS.writeFileSync(filepath + '.gz', gz);

  // brotli 拒绝太小或太大的文件，给个宽限
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

function run() {
  const publicDir = hexo.public_dir;
  hexo.log.info('[precompress] 扫描 %s ...', publicDir);

  const allFiles = walk(publicDir);
  const targets = allFiles.filter(shouldProcess);
  hexo.log.info('[precompress] walk 找到 %d 个文件，待压缩 %d 个', allFiles.length, targets.length);

  // 统计：按扩展名汇总
  const byExt = {};
  const bigHits = [];  // 收益最大的前 10 个

  let skipCount = 0;
  for (const f of targets) {
    try {
      const r = compressFile(f);
      if (!r) {
        skipCount++;
        continue;
      }
      const ext = PATH.extname(f).toLowerCase();
      if (!byExt[ext]) byExt[ext] = { count: 0, original: 0, gz: 0, br: 0 };
      byExt[ext].count++;
      byExt[ext].original += r.original;
      byExt[ext].gz += r.gz;
      if (r.br) byExt[ext].br += r.br;

      bigHits.push({
        path: f.replace(publicDir, ''),
        ...r,
        ratio: r.br ? r.br / r.original : (r.gz / r.original),
      });
    } catch (e) {
      hexo.log.warn('[precompress] 跳过 %s: %s', f, e.message);
    }
  }

  // 输出汇总
  hexo.log.info('[precompress] 跳过 %d 个（<1KB 或不支持）', skipCount);
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

  // 收益 top 10
  bigHits.sort((a, b) => a.ratio - b.ratio);
  hexo.log.info('[precompress] === 收益 top 10（br 压缩比最低）===');
  for (const h of bigHits.slice(0, 10)) {
    hexo.log.info(
      '  ' + h.path + '   ' + fmtSize(h.original) + ' → ' + fmtSize(h.br) +
      ' (-' + ((1 - h.ratio) * 100).toFixed(1) + '%)'
    );
  }
}

function fmtSize(n) {
  if (n == null) return 'n/a';
  if (n < 1024) return n + 'B';
  if (n < 1024 * 1024) return (n / 1024).toFixed(1) + 'K';
  return (n / 1024 / 1024).toFixed(2) + 'M';
}

hexo.extend.filter.register('after_generate', run);

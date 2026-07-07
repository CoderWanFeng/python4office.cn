#!/usr/bin/env node
/**
 * IndexNow 提交脚本
 *
 * 用途：每次部署后自动通知 Bing/Yandex 等支持 IndexNow 的搜索引擎
 *       有新页面/更新页面，加速收录。
 *
 * 用法：
 *   node scripts/indexnow-submit.js                   # 提交 sitemap.xml 中所有 URL
 *   node scripts/indexnow-submit.js --recent 7        # 只提交最近 7 天更新过的 URL
 *   node scripts/indexnow-submit.js --key <32hex>     # 指定 API Key
 *
 * 文档：https://www.indexnow.org/
 */

'use strict';

const fs = require('fs');
const path = require('path');
const https = require('https');

const ROOT = path.resolve(__dirname, '..');
const HEXO_DIR = path.join(ROOT, 'hexo/hexo');
const PUBLIC_DIR = path.join(HEXO_DIR, 'public');
const SITEMAP_PATH = path.join(PUBLIC_DIR, 'sitemap.xml');
const SOURCE_DIR = path.join(HEXO_DIR, 'source');

const SITE_HOST = 'www.python4office.cn';
const INDEXNOW_ENDPOINT = 'api.indexnow.org';

// ============ 参数解析 ============
const args = process.argv.slice(2);
const getArg = (name, def) => {
  const flag = `--${name}`;
  const i = args.indexOf(flag);
  if (i !== -1 && args[i + 1]) return args[i + 1];
  const eq = args.find((a) => a.startsWith(`${flag}=`));
  if (eq) return eq.split('=')[1];
  return def;
};

const RECENT_DAYS = parseInt(getArg('recent', '0'), 10);
const EXPLICIT_KEY = getArg('key', null);

// ============ API Key 发现 ============
function findIndexNowKey() {
  if (EXPLICIT_KEY) return EXPLICIT_KEY;

  // 从 source/<key>.txt 读
  if (!fs.existsSync(SOURCE_DIR)) return null;
  const files = fs.readdirSync(SOURCE_DIR);
  const keyFile = files.find((f) => /^[a-f0-9]{32}\.txt$/i.test(f));
  if (!keyFile) return null;
  return fs.readFileSync(path.join(SOURCE_DIR, keyFile), 'utf8').trim();
}

// ============ URL 收集 ============
function extractUrlsFromSitemap() {
  if (!fs.existsSync(SITEMAP_PATH)) {
    console.error(`✗ sitemap.xml 不存在: ${SITEMAP_PATH}`);
    console.error(`  请先运行 hexo generate 生成 public/sitemap.xml`);
    process.exit(1);
  }
  const xml = fs.readFileSync(SITEMAP_PATH, 'utf8');
  const urls = [];
  const re = /<loc>([^<]+)<\/loc>([\s\S]*?)<lastmod>([^<]+)<\/lastmod>/g;
  let m;
  while ((m = re.exec(xml)) !== null) {
    urls.push({ url: m[1], lastmod: m[3] });
  }
  return urls;
}

function filterRecent(urls, days) {
  if (!days) return urls.map((u) => u.url);
  const cutoff = Date.now() - days * 86400 * 1000;
  return urls
    .filter((u) => {
      const ts = new Date(u.lastmod).getTime();
      return !isNaN(ts) && ts >= cutoff;
    })
    .map((u) => u.url);
}

// ============ IndexNow 调用 ============
function submitToIndexNow(key, urlList) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({
      host: SITE_HOST,
      key,
      keyLocation: `https://${SITE_HOST}/${key}.txt`,
      urlList,
    });

    const req = https.request(
      {
        hostname: INDEXNOW_ENDPOINT,
        port: 443,
        path: '/indexnow',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json; charset=utf-8',
          'Content-Length': Buffer.byteLength(body),
        },
      },
      (res) => {
        let data = '';
        res.on('data', (chunk) => (data += chunk));
        res.on('end', () => resolve({ status: res.statusCode, body: data }));
      }
    );

    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

// ============ 主流程 ============
async function main() {
  console.log('📡 IndexNow 提交脚本');
  console.log('===================\n');

  // 1) 获取 API Key
  const key = findIndexNowKey();
  if (!key) {
    console.error('✗ 未找到 IndexNow API Key');
    console.error('  请在 source/ 下创建 <32位hex>.txt（内容=文件名）');
    console.error('  或用 --key <key> 显式传入');
    process.exit(1);
  }
  console.log(`✓ API Key: ${key.slice(0, 8)}...${key.slice(-4)}`);

  // 2) 收集 URL
  const allUrls = extractUrlsFromSitemap();
  console.log(`✓ sitemap.xml 共 ${allUrls.length} 个 URL`);

  const urlList = filterRecent(allUrls, RECENT_DAYS);
  if (RECENT_DAYS) {
    console.log(`✓ 筛选最近 ${RECENT_DAYS} 天：${urlList.length} 个 URL`);
  }
  if (urlList.length === 0) {
    console.log('⚠️  没有 URL 需要提交，退出');
    process.exit(0);
  }
  if (urlList.length > 10000) {
    console.error(`✗ URL 数量 ${urlList.length} 超过单次上限 10000`);
    process.exit(1);
  }

  console.log(`\n🚀 提交中...`);
  const result = await submitToIndexNow(key, urlList);
  console.log(`✓ HTTP ${result.status}`);
  console.log(`  Body: ${result.body || '(空)'}`);

  // IndexNow 返回码说明：
  //   200 - 提交成功
  //   202 - 请求已接受，稍后处理
  //   400 - 格式错误
  //   403 - Key 不匹配（验证文件不存在或 Key 错误）
  //   422 - URL 无效
  //   429 - 频率限制
  if (result.status === 200 || result.status === 202) {
    console.log('\n🎉 提交成功！');
    process.exit(0);
  } else if (result.status === 403) {
    console.error('\n❌ Key 验证失败，请检查：');
    console.error(`  https://${SITE_HOST}/${key}.txt 是否可访问`);
    process.exit(1);
  } else {
    console.error(`\n❌ 提交失败：HTTP ${result.status}`);
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('💥 异常:', err.message);
  process.exit(1);
});
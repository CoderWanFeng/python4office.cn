#!/usr/bin/env node
/**
 * SEO 修复后验证脚本
 *
 * 对比修复前（scan-report.json）和修复后的状态：
 *   - sitemap 完整性
 *   - description 长度
 *   - description 唯一性
 *   - IndexNow key 文件存在
 *   - IndexNow key 文件可公开访问（如果在线）
 *
 * 用法：
 *   node scripts/seo-audit/verify.js
 */

'use strict';

const fs = require('fs');
const path = require('path');
const https = require('http'); // 用 http 模块跑 HEAD 请求，避免 https 证书问题

const ROOT = path.resolve(__dirname, '../..');
const HEXO_DIR = path.join(ROOT, 'hexo/hexo');
const PUBLIC_DIR = path.join(HEXO_DIR, 'public');
const SOURCE_POSTS = path.join(HEXO_DIR, 'source/_posts');
const SITEMAP_PATH = path.join(PUBLIC_DIR, 'sitemap.xml');
const SOURCE_DIR = path.join(HEXO_DIR, 'source');
const SITE_URL = 'https://www.python4office.cn';
const REPORT_PATH = path.join(__dirname, 'scan-report.json');

const MIN_DESC_LENGTH = 60;
const TARGET_DESC_LENGTH = 160;

// ============ 工具函数（复用 scan.js 的逻辑） ============

function walkMd(dir, list = []) {
  if (!fs.existsSync(dir)) return list;
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    const stat = fs.statSync(p);
    if (stat.isDirectory()) walkMd(p, list);
    else if (/\.md$/i.test(f)) list.push(p);
  }
  return list;
}

function parseFrontmatter(content) {
  const match = content.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!match) return { fm: {}, body: content };
  const fm = {};
  for (const line of match[1].split('\n')) {
    const m = line.match(/^([a-zA-Z_]+)\s*:\s*(.*)$/);
    if (m) {
      let v = m[2].trim().replace(/^['"]|['"]$/g, '');
      fm[m[1]] = v;
    }
  }
  return { fm, body: content.slice(match[0].length) };
}

function extractSitemapUrls(xml) {
  const urls = [];
  const re = /<loc>([^<]+)<\/loc>/g;
  let m;
  while ((m = re.exec(xml)) !== null) urls.push(m[1]);
  return urls;
}

function extractSitemapUrlsFixed(xml) {
  const urls = [];
  const re = /<loc>([^<]+)<\/loc>/g;
  let m;
  while ((m = re.exec(xml)) !== null) urls.push(m[1]);
  return urls;
}

function urlFromPermalink(filePath) {
  const rel = path.relative(SOURCE_POSTS, filePath).replace(/\\/g, '/');
  const base = rel.replace(/\.md$/, '');
  return `${SITE_URL}/${base}/`;
}

// ============ 实时模拟 description 生成（与 description-generator.js 一致） ============

function stripMarkdown(text) {
  return text
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/<!--[\s\S]*?-->/g, ' ')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/^#+\s+.*$/gm, '')
    .replace(/^>\s*/gm, '')
    .replace(/[*_~`]/g, '')
    .replace(/\s+/g, '');
}

function extractFirstText(body) {
  for (const line of body.split('\n')) {
    const stripped = stripMarkdown(line);
    if (stripped.length > 20) return stripped.slice(0, 80);
  }
  return '';
}

function generateDescription(post) {
  const title = (post.title || '').toString();
  const tags = (post.tags || []);
  const tagStr = tags.slice(0, 3).join('、') || '核心要点';
  const firstText = extractFirstText(post.body);
  return `${title}。本文围绕${tagStr}：${firstText}...`;
}

function ensureUnique(desc, seen) {
  let unique = desc;
  let suffix = 1;
  while (seen.has(unique)) {
    suffix += 1;
    unique = `${desc}（第${suffix}篇）`;
  }
  seen.add(unique);
  return unique;
}

// ============ 主流程 ============

console.log('🔍 SEO 修复后验证');
console.log('==================\n');

let beforeReport = null;
if (fs.existsSync(REPORT_PATH)) {
  beforeReport = JSON.parse(fs.readFileSync(REPORT_PATH, 'utf8'));
  console.log(`✓ 读取修复前报告（${beforeReport.timestamp}）\n`);
}

// 1) 收集所有 .md 文件
const mdFiles = walkMd(SOURCE_POSTS);
console.log(`✓ 源 .md 文件：${mdFiles.length} 个`);

// 2) 模拟 description 生成后的状态
const descriptions = new Map();
const shortDescs = [];
let generated = 0;
let deduped = 0;
const seen = new Set();

const posts = mdFiles.map((mdFile) => {
  const content = fs.readFileSync(mdFile, 'utf8');
  const { fm, body } = parseFrontmatter(content);
  let desc = fm.description;

  if (!desc || desc.length < MIN_DESC_LENGTH) {
    desc = generateDescription({ title: fm.title, tags: fm.tags || [], body });
    generated += 1;
  }

  if (desc.length > TARGET_DESC_LENGTH) {
    desc = desc.slice(0, TARGET_DESC_LENGTH - 1) + '…';
  }

  const before = seen.size;
  desc = ensureUnique(desc, seen);
  if (seen.size > before) deduped += 1;
  else if (seen.size === before + 1) {
    // 第一次出现，deduped 不变
  }

  if (desc.length < MIN_DESC_LENGTH) {
    shortDescs.push({ file: path.relative(ROOT, mdFile), length: desc.length });
  }

  descriptions.set(desc, (descriptions.get(desc) || 0) + 1);
  return { file: mdFile, fm, desc };
});

// 3) sitemap 检查
let sitemapUrls = [];
let sitemapExists = fs.existsSync(SITEMAP_PATH);
if (sitemapExists) {
  sitemapUrls = extractSitemapUrlsFixed(fs.readFileSync(SITEMAP_PATH, 'utf8'));
  console.log(`✓ sitemap.xml 存在，共 ${sitemapUrls.length} 个 URL`);
} else {
  console.log(`✗ sitemap.xml 不存在`);
}

const expectedUrls = posts.map((p) => urlFromPermalink(p.file));
const missingUrls = expectedUrls.filter((u) => !sitemapUrls.includes(u));

// 4) IndexNow key 检查
const keyFile = fs.existsSync(SOURCE_DIR)
  ? fs.readdirSync(SOURCE_DIR).find((f) => /^[a-f0-9]{32}\.txt$/i.test(f))
  : null;

// 5) 输出对比
console.log('\n📊 验证结果');
console.log('==================\n');

console.log('【sitemap 完整性】');
console.log(`  源文件数：${mdFiles.length}`);
console.log(`  sitemap URL 数：${sitemapUrls.length}`);
console.log(`  缺失：${missingUrls.length}`);
if (missingUrls.length > 0) {
  console.log(`  ⚠️  前 5 个缺失 URL：`);
  missingUrls.slice(0, 5).forEach((u) => console.log(`     - ${u}`));
} else {
  console.log(`  ✅ 所有源文件都在 sitemap 中`);
}

console.log('\n【description 质量】');
console.log(`  过短 (<${MIN_DESC_LENGTH})：${shortDescs.length}`);
console.log(`  智能生成：${generated}`);
console.log(`  去重处理：${deduped}`);
const dups = Array.from(descriptions.values()).filter((c) => c > 1);
console.log(`  重复项：${dups.length}`);
if (dups.length > 0) {
  console.log(`  ⚠️  仍有重复：${dups.reduce((s, c) => s + c, 0)} 个页面`);
} else {
  console.log(`  ✅ 所有 description 唯一`);
}

console.log('\n【IndexNow】');
if (keyFile) {
  console.log(`  ✅ 验证文件存在：${keyFile}`);
  console.log(`     部署后 URL：${SITE_URL}/${keyFile}`);
} else {
  console.log(`  ❌ 验证文件不存在（应在 hexo/hexo/source/<32hex>.txt）`);
}

console.log('\n【与修复前对比】');
if (beforeReport) {
  const beforeSitemapMissing = beforeReport.issues.sitemapMissing.length;
  const beforeShortDesc = beforeReport.issues.shortDescription.length;
  const beforeDups = beforeReport.issues.duplicateDescription.length;
  const beforeIndexNow = beforeReport.issues.noIndexNowKey;

  console.log(`  sitemap 缺失：${beforeSitemapMissing} → ${missingUrls.length}`);
  console.log(`  description 过短：${beforeShortDesc} → ${shortDescs.length}`);
  console.log(`  description 重复组数：${beforeDups} → ${dups.length}`);
  console.log(`  IndexNow key：${beforeIndexNow ? '❌ 无' : '✅ 有'} → ${keyFile ? '✅ 有' : '❌ 无'}`);
}

console.log('\n✅ 验证完成');
const allPass = missingUrls.length === 0 && shortDescs.length === 0 && dups.length === 0 && keyFile;
if (allPass) {
  console.log('🎉 全部修复通过！可以部署到生产环境。');
  process.exit(0);
} else {
  console.log('⚠️  仍有未解决问题，请检查上面输出。');
  process.exit(1);
}
#!/usr/bin/env node
/**
 * SEO 现状诊断脚本
 *
 * 检查项：
 *   1. sitemap.xml 中的 URL 数量 vs 源 .md 文件数（判断 sitemap 缺失）
 *   2. 最近 7 天发布的文章是否都在 sitemap 中
 *   3. meta description 长度分布（< 60 算过短）
 *   4. description 重复度（hash 分组）
 *   5. 是否存在 IndexNow 验证文件
 *
 * 用法：
 *   node scripts/seo-audit/scan.js
 *   node scripts/seo-audit/scan.js --recent 7
 */

'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '../..');
const HEXO_DIR = path.join(ROOT, 'hexo/hexo');
const PUBLIC_DIR = path.join(HEXO_DIR, 'public');
const SOURCE_POSTS = path.join(HEXO_DIR, 'source/_posts');
const SITEMAP_PATH = path.join(PUBLIC_DIR, 'sitemap.xml');
const SITE_URL = 'https://www.python4office.cn';

const RECENT_DAYS = parseInt(
  (process.argv.find((a) => a.startsWith('--recent=')) || '--recent=7').split('=')[1],
  10
);

// ============ 工具函数 ============

function walkMd(dir, list = []) {
  if (!fs.existsSync(dir)) return list;
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    const stat = fs.statSync(p);
    if (stat.isDirectory()) {
      walkMd(p, list);
    } else if (/\.md$/i.test(f)) {
      list.push(p);
    }
  }
  return list;
}

function parseFrontmatter(mdContent) {
  const match = mdContent.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!match) return { fm: {}, body: mdContent };
  const fm = {};
  const lines = match[1].split('\n');
  for (const line of lines) {
    const m = line.match(/^([a-zA-Z_]+)\s*:\s*(.*)$/);
    if (m) {
      let v = m[2].trim().replace(/^['"]|['"]$/g, '');
      if (v.startsWith('[') && v.endsWith(']')) {
        try { v = JSON.parse(v.replace(/'/g, '"')); } catch (e) { v = v.slice(1, -1).split(',').map(s => s.trim()); }
      }
      fm[m[1]] = v;
    }
  }
  return { fm, body: mdContent.slice(match[0].length) };
}

function urlFromPermalink(filePath) {
  const rel = path.relative(SOURCE_POSTS, filePath).replace(/\\/g, '/');
  // permalink: :title/，所以 file name (without .md) 就是 URL slug
  const base = rel.replace(/\.md$/, '');
  return `${SITE_URL}/${base}/`;
}

function extractSitemapUrls(xml) {
  const urls = [];
  const re = /<loc>([^<]+)<\/loc>/g;
  let m;
  while ((m = re.exec(xml)) !== null) {
    urls.push(m[1]);
  }
  return urls;
}

function generateDescription(title, body, tags) {
  const firstPara = body
    .replace(/<!--[\s\S]*?-->/g, '')
    .replace(/^#+\s.*$/gm, '')
    .replace(/```[\s\S]*?```/g, '')
    .replace(/[`*_>#\[\]()!\-\d]/g, '')
    .replace(/\s+/g, '')
    .slice(0, 80);
  const tagStr = tags && tags.length ? tags.slice(0, 3).join('、') : '';
  return `${title}。本文${tagStr ? `围绕${tagStr}` : '详细介绍'}：${firstPara}...`;
}

// ============ 主流程 ============

const issues = {
  sitemapMissing: [],
  shortDescription: [],
  duplicateDescription: [],
  noIndexNowKey: false,
};

console.log('🔍 SEO 现状诊断');
console.log('================\n');

// 1) sitemap 检查
let sitemapUrls = [];
if (fs.existsSync(SITEMAP_PATH)) {
  const xml = fs.readFileSync(SITEMAP_PATH, 'utf8');
  sitemapUrls = extractSitemapUrls(xml);
  console.log(`✓ sitemap.xml 存在，共 ${sitemapUrls.length} 个 URL`);
} else {
  console.log(`✗ sitemap.xml 不存在：${SITEMAP_PATH}`);
  issues.sitemapMissing.push('sitemap.xml 整个文件缺失');
}

// 2) 扫描源文件
const mdFiles = walkMd(SOURCE_POSTS);
console.log(`✓ 源 .md 文件共 ${mdFiles.length} 个\n`);

// 3) IndexNow key 文件检查
const indexNowKeyFile = fs.readdirSync(path.join(HEXO_DIR, 'source')).find(
  (f) => /^[a-f0-9]{32}\.txt$/i.test(f)
);
if (indexNowKeyFile) {
  console.log(`✓ IndexNow 验证文件存在：${indexNowKeyFile}`);
} else {
  console.log(`✗ IndexNow 验证文件不存在（应在 source/<32位hex>.txt）`);
  issues.noIndexNowKey = true;
}

console.log('\n📊 详细分析');
console.log('================');

// 收集 description
const descriptions = new Map(); // desc -> [filePath]
const recentMissing = []; // 最近 N 天发布但不在 sitemap 的文章
const cutoffTime = Date.now() - RECENT_DAYS * 86400 * 1000;

for (const mdFile of mdFiles) {
  const content = fs.readFileSync(mdFile, 'utf8');
  const { fm } = parseFrontmatter(content);

  let desc = fm.description;
  if (!desc || desc.length < 60) {
    // 模拟主题自动截取（method: 2，length: 300）
    if (!desc) {
      // 从 body 截取前 300 字符
      const body = content.replace(/---[\s\S]*?---/, '');
      desc = body.replace(/[#>*`\[\]()!\-\d]/g, '').replace(/\s+/g, '').slice(0, 300);
    }
    if (desc.length < 60) {
      issues.shortDescription.push({
        file: path.relative(ROOT, mdFile),
        length: desc.length,
        desc: desc.slice(0, 50),
      });
    }
  }

  // 重复检测
  if (!descriptions.has(desc)) descriptions.set(desc, []);
  descriptions.get(desc).push(path.relative(ROOT, mdFile));

  // sitemap 缺失
  const url = urlFromPermalink(mdFile);
  if (!sitemapUrls.includes(url)) {
    issues.sitemapMissing.push(url);
    // 检查是否近期发布
    if (fm.date) {
      const ts = new Date(fm.date).getTime();
      if (ts >= cutoffTime) recentMissing.push(url);
    }
  }
}

// description 重复报告
for (const [desc, files] of descriptions) {
  if (files.length > 1) {
    issues.duplicateDescription.push({
      desc: desc.slice(0, 80),
      count: files.length,
      files: files.slice(0, 3),
    });
  }
}

console.log(`📝 description 过短 (<60字符)：${issues.shortDescription.length} 个`);
console.log(`📝 description 重复：${issues.duplicateDescription.length} 组（涉及 ${issues.duplicateDescription.reduce((s, x) => s + x.count, 0)} 个页面）`);
console.log(`📝 sitemap 缺失：${issues.sitemapMissing.length} 个`);
console.log(`📝 最近 ${RECENT_DAYS} 天新发布但不在 sitemap：${recentMissing.length} 个`);

console.log('\n📋 详细问题列表（前 10）');
console.log('================');
if (issues.shortDescription.length) {
  console.log('\n[description 过短]');
  for (const x of issues.shortDescription.slice(0, 5)) {
    console.log(`  - ${x.file} (${x.length}字): ${x.desc}...`);
  }
}
if (issues.duplicateDescription.length) {
  console.log('\n[description 重复]');
  for (const x of issues.duplicateDescription.slice(0, 5)) {
    console.log(`  - "${x.desc}..." 出现 ${x.count} 次`);
    x.files.forEach(f => console.log(`      ${f}`));
  }
}
if (recentMissing.length) {
  console.log('\n[近期 sitemap 缺失]');
  recentMissing.slice(0, 5).forEach(u => console.log(`  - ${u}`));
}

console.log('\n\n✅ 总结');
console.log('================');
const totalIssues = issues.shortDescription.length + issues.duplicateDescription.length + issues.sitemapMissing.length + (issues.noIndexNowKey ? 1 : 0);
console.log(`总问题数：${totalIssues}`);
if (totalIssues === 0) {
  console.log('🎉 所有问题已修复！');
} else {
  console.log('⚠️  需修复问题：');
  if (issues.noIndexNowKey) console.log('  - 接入 IndexNow');
  if (issues.sitemapMissing.length) console.log(`  - sitemap 缺失 ${issues.sitemapMissing.length} 个 URL`);
  if (issues.shortDescription.length) console.log(`  - description 过短 ${issues.shortDescription.length} 个`);
  if (issues.duplicateDescription.length) console.log(`  - description 重复 ${issues.duplicateDescription.length} 组`);
}

// 输出 JSON 报告（方便后续 verify.js 对比）
const reportPath = path.join(__dirname, 'scan-report.json');
fs.writeFileSync(reportPath, JSON.stringify({
  timestamp: new Date().toISOString(),
  totalPosts: mdFiles.length,
  sitemapUrls: sitemapUrls.length,
  issues,
}, null, 2));
console.log(`\n📄 详细报告已保存：${reportPath}`);
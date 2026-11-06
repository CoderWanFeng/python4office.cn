#!/usr/bin/env node
/**
 * 离线 SEO 回归：使用 Hexo 的真实路由和模板，不按文件名猜测 URL。
 * 不发布、不提交收录、不请求网络、不改 source/ 或现有 public/。
 *
 * 用法（先建立基线，再修改生成器，最后对比）：
 *   node --max-old-space-size=16384 scripts/seo-audit/verify.js --snapshot
 *   node --max-old-space-size=16384 scripts/seo-audit/verify.js
 * 基线保存在项目 .cache/seo-audit/baseline.json，已有基线不会被覆盖。
 * --self-test：运行离线单元测试；不构建站点。
 * --unminified：仅诊断已有 HTML 压缩故障，基线和对比都需带此参数。
 * 此诊断模式不代表常规压缩构建通过，也不会修改项目压缩配置。
 */

'use strict';

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { createRequire } = require('module');
const ROOT = path.resolve(__dirname, '../..');
const HEXO_DIR = path.join(ROOT, 'hexo/hexo');
const localRequire = createRequire(path.join(HEXO_DIR, 'package.json'));
const cheerio = localRequire('cheerio');
const BASELINE = path.join(ROOT, '.cache/seo-audit/baseline.json');
const hash = data => crypto.createHash('sha256').update(data).digest('hex');

function sourceHashes() {
  const result = {};
  function walk(dir) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const file = path.join(dir, entry.name);
      if (entry.isDirectory()) walk(file);
      else if (/\.md$/i.test(entry.name)) result[path.relative(ROOT, file)] = hash(fs.readFileSync(file));
    }
  }
  walk(path.join(HEXO_DIR, 'source'));
  for (const file of ['hexo/hexo/_config.yml', 'scripts/indexnow-submit.js',
    'scripts/deploy/deploy.py', 'scripts/cdn/purge_static_assets.py']) {
    result[file] = hash(fs.readFileSync(path.join(ROOT, file)));
  }
  return result;
}

function readRoute(route, name) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    route.get(name).on('data', chunk => chunks.push(Buffer.from(chunk)))
      .on('error', reject).on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
  });
}

function inspectHtml(html) {
  const $ = cheerio.load(html);
  const article = $('#article-container');
  const schema = $('#page-structured-data').html();
  return {
    canonical: $('link[rel="canonical"]').attr('href') || '',
    title: $('title').text(),
    articleTitle: $('h1.post-title').text(),
    article: article.length > 0 && $('meta[property="og:type"]').attr('content') === 'article',
    bodyHash: article.length ? hash(article.html()) : '',
    description: $('meta[name="description"]').attr('content') || '',
    published: $('meta[property="article:published_time"]').attr('content') || '',
    modified: $('meta[property="article:modified_time"]').attr('content') || '',
    schemaCount: $('#page-structured-data').length,
    noindex: $('meta').toArray().some(node => {
      const name = ($(node).attr('name') || '').toLowerCase();
      return /^(robots|googlebot|bingbot)$/.test(name) && /\b(noindex|none)\b/i.test($(node).attr('content') || '');
    }),
    schema: schema ? JSON.parse(schema) : null
  };
}

function localRoute(url, siteUrl) {
  try {
    const parsed = new URL(url);
    const base = new URL(siteUrl);
    if (parsed.origin !== base.origin || !parsed.pathname.startsWith(base.pathname)) return null;
    let relative = decodeURIComponent(parsed.pathname.slice(base.pathname.length));
    if (!relative || relative.endsWith('/')) relative += 'index.html';
    return relative;
  } catch (_) { return null; }
}

function blockNetwork() {
  const blocked = () => { throw new Error('离线校验禁止网络连接'); };
  for (const name of ['http', 'https']) {
    const module = require(name);
    module.request = blocked;
    module.get = blocked;
  }
  require('net').Socket.prototype.connect = blocked;
  require('tls').connect = blocked;
  if (global.fetch) global.fetch = blocked;
}

async function buildSnapshot({ unminified = false } = {}) {
  blockNetwork();
  const Hexo = localRequire('hexo');
  const hexo = new Hexo(HEXO_DIR, { silent: true });
  const sources = sourceHashes();
  await hexo.init();
  // 仅诊断模式跳过已有压缩错误，不改项目配置；基线与回归必须使用同一模式。
  if (unminified) {
    hexo.extend.filter.unregister('after_render:html', localRequire('hexo-html-minifier/lib/filter'));
  }
  // 仅在内存里渲染路由；避免已有预压缩钩子读写正式 public/。
  hexo.config.public_dir = path.join(ROOT, '.cache/seo-audit/render-only');
  hexo.public_dir = hexo.config.public_dir + path.sep;
  await hexo.load();
  const routes = hexo.route.list().sort();
  const pages = {};
  for (const name of routes.filter(name => /\.html?$/.test(name))) {
    pages[name] = inspectHtml(await readRoute(hexo.route, name));
  }
  const posts = {};
  hexo.locals.get('posts').forEach(post => {
    posts[post.source] = { path: post.path, permalink: post.permalink };
  });
  const sitemaps = {};
  for (const name of [hexo.config.sitemap.path, hexo.config.baidusitemap.path]) {
    if (!routes.includes(name)) throw new Error(`缺少本地站点地图：${name}`);
    const $ = cheerio.load(await readRoute(hexo.route, name), { xmlMode: true });
    if (!$('urlset').length) throw new Error(`站点地图不是 urlset：${name}`);
    sitemaps[name] = $('url > loc').toArray().map(node => $(node).text().trim());
  }
  const after = sourceHashes();
  if (JSON.stringify(sources) !== JSON.stringify(after)) throw new Error('构建期间源文件发生变化，不能建立可信基线');
  return { version: 1, created: new Date().toISOString(), siteUrl: hexo.config.url,
    unminified, sources, routes, posts, pages, sitemaps };
}

function compare(before, current) {
  const errors = [];
  const fail = message => errors.push(message);
  function compareMap(label, a, b) {
    for (const key of new Set([...Object.keys(a), ...Object.keys(b)])) {
      if (JSON.stringify(a[key]) !== JSON.stringify(b[key])) fail(`${label}发生变化：${key}`);
    }
  }
  if (before.unminified !== current.unminified) fail('基线与回归的压缩模式不一致');
  compareMap('源文件/受保护配置', before.sources, current.sources);
  compareMap('文章 URL 或输出路径', before.posts, current.posts);
  if (JSON.stringify(before.routes) !== JSON.stringify(current.routes)) fail('生成路由集合发生变化');
  for (const [name, old] of Object.entries(before.pages)) {
    const page = current.pages[name];
    if (!page) { fail(`原页面丢失：${name}`); continue; }
    for (const field of ['canonical', 'title', 'articleTitle', 'bodyHash', 'article', 'noindex']) {
      if (old[field] !== page[field]) fail(`${field} 发生变化：${name}`);
    }
  }
  for (const [name, urls] of Object.entries(current.sitemaps)) {
    const original = new Set(before.sitemaps[name] || []);
    const kept = new Set(urls);
    if (kept.size !== urls.length) fail(`sitemap 仍有重复 URL：${name}`);
    for (const url of kept) {
      if (!original.has(url)) fail(`sitemap 改写或新增地址：${url}`);
      const page = current.pages[localRoute(url, current.siteUrl)];
      if (page && page.noindex) fail(`sitemap 仍含 noindex 页面：${url}`);
    }
    for (const url of original) {
      const page = current.pages[localRoute(url, current.siteUrl)];
      if (!kept.has(url) && !(page && page.noindex)) fail(`错误移除了非 noindex 地址：${url}`);
    }
    const duplicates = before.sitemaps[name].length - original.size;
    const excluded = [...original].filter(url => !kept.has(url)).length;
    console.log(`${name}：${before.sitemaps[name].length} → ${urls.length} 个条目（去重 ${duplicates}，排除 noindex ${excluded}）`);
  }
  const descriptions = new Map();
  let articles = 0;
  for (const [name, page] of Object.entries(current.pages)) {
    if (!page.article) continue;
    articles++;
    if (!page.description.trim()) fail(`文章缺少摘要：${name}`);
    descriptions.set(page.description, (descriptions.get(page.description) || 0) + 1);
    const graph = page.schema && page.schema['@graph'];
    const article = graph && graph.find(item => item['@type'] === 'BlogPosting');
    const breadcrumb = graph && graph.find(item => item['@type'] === 'BreadcrumbList');
    if (!article || article.url !== page.canonical || article.headline !== page.articleTitle ||
      !article.author || !article.author.name || !breadcrumb || page.schemaCount !== 1) {
      fail(`文章结构化数据不完整或地址不一致：${name}`);
      continue;
    }
    if (article.description !== page.description) fail(`结构化摘要与 meta 不一致：${name}`);
    for (const [field, expected] of [['datePublished', page.published], ['dateModified', page.modified]]) {
      if (expected && article[field] !== expected) fail(`结构化日期不一致：${name}`);
    }
    const items = breadcrumb.itemListElement;
    if (!Array.isArray(items) || items.length !== 2 || items[1].item !== page.canonical ||
      items[1].name !== page.articleTitle || !current.pages[localRoute(items[0].item, current.siteUrl)]) {
      fail(`面包屑地址不对应实际页面：${name}`);
    }
  }
  const duplicates = [...descriptions.values()].filter(count => count > 1).length;
  console.log(`文章 ${articles} 篇；摘要重复 ${duplicates} 组（仅提示，不用编号伪造唯一性）`);
  return errors;
}

async function runSelfTests() {
  const assert = require('assert/strict');
  const vm = require('vm');
  let passed = 0;
  const test = async (name, fn) => { await fn(); passed++; console.log(`通过：${name}`); };
  function loadPlugin(relative) {
    const file = path.join(HEXO_DIR, relative);
    const filters = {}, helpers = {};
    const context = {
      require: createRequire(file), process, console, URL, Buffer,
      hexo: {
        extend: {
          filter: { register(name, fn) { (filters[name] ||= []).push(fn); } },
          helper: { register(name, fn) { helpers[name] = fn; } }
        },
        log: { info() {} }
      }
    };
    vm.runInNewContext(fs.readFileSync(file, 'utf8'), context, { filename: file });
    return { context, filters, helpers };
  }
  const desc = loadPlugin('scripts/description-generator.js');
  const inject = desc.filters.template_locals[0];
  await test('人工短摘要、长摘要和相同摘要均原样保留', () => {
    for (const description of ['简短人工摘要', '人工摘要'.repeat(100), '重复摘要', '重复摘要']) {
      const locals = { page: { __post: true, title: '测试', description, content: '<p>正文</p>' } };
      inject(locals);
      assert.equal(locals.page.description, description);
    }
  });
  await test('提取真实正文，过滤推广、徽章、脚本和问候', () => {
    const body = '<div class="promo-banner"><p>扫码领取资料加入微信群</p></div>' +
      '<p><a href="/badge"><img src="/badge.png" alt="badge"></a></p>' +
      '<script>不应进入摘要</script><style>不应进入摘要</style>' +
      '<h2>章节标题</h2><p>大家好，我是程序员晚枫。</p>' +
      '<p>Python office 保留英文空格，介绍 Excel 自动化与数据处理。</p>';
    const locals = { page: { __post: true, title: '测试', content: body } };
    inject(locals);
    assert.equal(locals.page.description, 'Python office 保留英文空格，介绍 Excel 自动化与数据处理。');
    assert.equal(locals.page.content, body);
    const other = { page: { __page: true, content: body } };
    inject(other);
    assert.equal(other.page.description, undefined);
  });
  await test('纯图片回退原标题；emoji 截断不破坏字符', () => {
    assert.equal(desc.context.generateDescription({ title: '图片教程', content: '<img src="/a.png">' }), '图片教程');
    const result = desc.context.generateDescription({ title: '测试', content: `<p>${'😀'.repeat(200)}</p>` });
    assert.equal(Array.from(result).length, 160);
    assert.equal(result.endsWith('…'), true);
    assert.equal(desc.context.generateDescription({ content: '<p>👩‍💻 学习 Python 自动化</p>' }), '👩‍💻 学习 Python 自动化');
    assert.equal(/[\uD800-\uDFFF]/u.test(result.replace(/😀/g, '')), false);
  });
  const { helpers } = loadPlugin('themes/butterfly/scripts/helpers/page.js');
  const canonical = 'https://example.test/旧路径/';
  const env = {
    page: { __post: true, title: '</script><img src=x> & 测试', description: '人工摘要',
      date: new Date('2024-01-02T03:04:05Z'), updated: new Date('2024-02-03T04:05:06Z'), author: '真实作者' },
    config: { author: '站点作者', url: 'https://example.test/', title: '站点' },
    urlNoIndex: () => canonical, full_url_for: () => 'https://example.test/',
    page_description: () => '人工摘要', _p: () => '无题'
  };
  await test('JSON-LD 安全转义、原 canonical、作者与真实日期', () => {
    const json = helpers.page_structured_data.call(env);
    assert.equal(json.includes('</script>'), false);
    const data = JSON.parse(json);
    const article = data['@graph'].find(item => item['@type'] === 'BlogPosting');
    assert.equal(article.url, canonical);
    assert.equal(article.headline, env.page.title);
    assert.equal(article.author.name, '真实作者');
    assert.equal(article.datePublished, env.page.date.toISOString());
    assert.equal(article.dateModified, env.page.updated.toISOString());
    const breadcrumb = data['@graph'].find(item => item['@type'] === 'BreadcrumbList');
    assert.equal(breadcrumb.itemListElement[1].item, canonical);
    assert.equal(helpers.page_structured_data.call({ ...env, page: {} }), '');
    const compressed = localRequire('html-minifier').minify(`<head><script id="page-structured-data" type="application/ld+json">${json}</script></head>`,
      { minifyJS: true, removeScriptTypeAttributes: true });
    const parsed = cheerio.load(compressed);
    assert.equal(parsed('#page-structured-data').attr('type'), 'application/ld+json');
    assert.deepEqual(JSON.parse(parsed('#page-structured-data').html()), data);
  });
  const sitemapPlugin = loadPlugin('scripts/noindex-thin-tags.js');
  const sitemap = sitemapPlugin.context;
  await test('robots 属性顺序、大小写、爬虫专属规则及 none', () => {
    for (const meta of ['<meta content="NOINDEX,follow" name="robots">',
      "<meta name='googlebot' content='none'>", '<meta name="bingbot" content="noindex">']) {
      assert.equal(sitemap.isNoindex(`<html><head>${meta}</head></html>`), true);
    }
    assert.equal(sitemap.isNoindex('<head><meta name="robots" content="index,follow"></head>'), false);
    assert.equal(sitemap.isNoindex('<head></head><script>"<meta name=robots content=noindex>"</script>'), false);
  });
  await test('sitemap 仅去重与剔除 noindex，保留原始 XML 条目', () => {
    const keep = '<url><loc>https://example.test/旧路径/index.html?a=1&amp;b=2</loc><lastmod>2024-01-02</lastmod></url>';
    const drop = '<url><loc>https://example.test/tags/thin/</loc></url>';
    const noindex = new Set(['https://example.test/tags/thin/']);
    const result = sitemap.cleanSitemap(`<urlset>${keep}${drop}${keep}</urlset>`, noindex);
    assert.equal(result.xml, `<urlset>${keep}</urlset>`);
    assert.equal(result.duplicates, 1);
    assert.equal(result.excluded, 1);
    assert.equal(sitemap.cleanSitemap(result.xml, noindex).xml, result.xml);
  });
  await test('本地 URL 解码不改变源地址或误匹配外域', () => {
    assert.equal(localRoute('https://example.test/%E4%B8%AD%E6%96%87/', 'https://example.test/'), '中文/index.html');
    assert.equal(localRoute('https://other.test/a/', 'https://example.test/'), null);
    assert.equal(localRoute('invalid', 'https://example.test/'), null);
  });
  await test('真实路由流清理两份 sitemap，增量生成不残留 noindex 状态', async () => {
    const Router = localRequire('hexo/dist/hexo/router');
    const route = new Router();
    const xml = '<urlset><url><loc>https://example.test/文章/</loc></url>' +
      '<url><loc>https://example.test/tags/thin/</loc></url>' +
      '<url><loc>https://example.test/文章/</loc></url></urlset>';
    const articleHtml = '<html><head></head><body>原始正文</body></html>';
    route.set('文章/index.html', articleHtml);
    route.set('tags/thin/index.html', '<head><meta name="robots" content="noindex,follow"></head>');
    for (const name of ['sitemap.xml', 'baidusitemap.xml']) route.set(name, xml);
    const originalRoutes = route.list().sort();
    Object.assign(sitemap.hexo, { route, config: { url: 'https://example.test/',
      sitemap: { path: 'sitemap.xml' }, baidusitemap: { path: 'baidusitemap.xml' } } });
    const cleanup = sitemapPlugin.filters.after_generate[0];
    await cleanup();
    assert.deepEqual(route.list().sort(), originalRoutes);
    assert.equal(await readRoute(route, '文章/index.html'), articleHtml);
    assert.equal((await readRoute(route, 'sitemap.xml')).includes('/tags/thin/'), false);
    assert.equal(await readRoute(route, 'sitemap.xml'), await readRoute(route, 'baidusitemap.xml'));
    route.set('tags/thin/index.html', '<head><meta name="robots" content="index,follow"></head>');
    for (const name of ['sitemap.xml', 'baidusitemap.xml']) route.set(name, xml);
    await cleanup();
    assert.equal((await readRoute(route, 'sitemap.xml')).includes('/tags/thin/'), true);
  });
  await test('回归保护拒绝正文、标题、原链接及源文件变化', () => {
    const before = { unminified: true, sources: { 'source.md': '原始哈希' }, routes: ['a/index.html'],
      posts: { 'source.md': { path: 'a/index.html', permalink: 'https://example.test/a/' } },
      pages: { 'a/index.html': { canonical: 'https://example.test/a/', title: '原标题',
        articleTitle: '原标题', bodyHash: '原始正文', article: false, noindex: false } }, sitemaps: {} };
    for (const mutate of [current => { current.sources['source.md'] = '已改'; },
      current => { current.posts['source.md'].path = 'new/index.html'; },
      current => { current.posts['source.md'].permalink = 'https://example.test/new/'; },
      current => { current.pages['a/index.html'].canonical += 'new/'; },
      current => { current.pages['a/index.html'].bodyHash = '已改'; },
      current => { current.pages['a/index.html'].title = '已改'; },
      current => { current.routes = []; }, current => { current.unminified = false; }]) {
      const current = JSON.parse(JSON.stringify(before));
      mutate(current);
      assert.ok(compare(before, current).length > 0);
    }
  });
  console.log(`离线单元测试通过：${passed} 组`);
}

async function main() {
  if (process.argv.includes('--self-test')) return runSelfTests();
  const snapshot = process.argv.includes('--snapshot');
  if (snapshot && fs.existsSync(BASELINE)) throw new Error('基线已存在，拒绝覆盖；请确认旧基线用途后再处理');
  if (!snapshot && !fs.existsSync(BASELINE)) throw new Error('缺少基线；请先在优化前运行 --snapshot');
  console.log('开始全站离线渲染；网络连接已禁止，不写正式 public/');
  const unminified = process.argv.includes('--unminified');
  if (unminified) console.log('诊断模式：仅本进程跳过 HTML 压缩；不代表常规压缩构建通过');
  const current = await buildSnapshot({ unminified });
  console.log(`源文件/配置 ${Object.keys(current.sources).length} 个；文章 ${Object.keys(current.posts).length} 篇；HTML ${Object.keys(current.pages).length} 个`);
  if (snapshot) {
    fs.mkdirSync(path.dirname(BASELINE), { recursive: true });
    fs.writeFileSync(BASELINE, JSON.stringify(current), { flag: 'wx' });
    console.log('基线已保存：.cache/seo-audit/baseline.json');
    return;
  }
  const before = JSON.parse(fs.readFileSync(BASELINE, 'utf8'));
  const errors = compare(before, current);
  if (errors.length) {
    errors.slice(0, 20).forEach(error => console.error(error));
    throw new Error(`本地回归失败，共 ${errors.length} 项`);
  }
  console.log('通过：全部文章源文件、访问 URL、输出路径、canonical 和正文保持不变；本地 SEO 校验通过。');
}

module.exports = { compare, inspectHtml, localRoute, buildSnapshot };
if (require.main === module) main().catch(error => {
  console.error(String(error.stack || error).slice(0, 2000));
  process.exitCode = 1;
});
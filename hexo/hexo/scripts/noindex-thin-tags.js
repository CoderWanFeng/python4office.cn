'use strict';

/**
 * 给低质 tag 页自动注入 noindex meta 标签
 *
 * 背景：站点有 2434 个 tag，其中 ~77.7%（1891 个）只挂 1-2 篇文章，
 * 这种 "thin content" 会被搜索引擎判定为低质内容，拉低整个站点质量评分。
 *
 * 策略：文章数 < MIN_ARTICLES 的 tag，注入
 *   <meta name="robots" content="noindex,follow">
 * - noindex：告诉搜索引擎不要索引
 * - follow：允许搜索引擎继续抓取页面内的链接（保留内链权重传递）
 * - URL 保留不变，外部链接、外链权重不丢
 *
 * 实现：hexo 主题 view 渲染后会触发 `after_render:html`
 * （hexo 7.x 由 dist/theme/view.js 调用），data.path 为相对于 public 的路径。
 * 匹配 tags/<slug>/(page/N/)?index.html 即视为 tag 页（layout 字段在
 * butterfly 主题下不可靠，不依赖）。
 *
 * 阈值：默认 3 篇。可通过环境变量 HEXO_NOINDEX_MIN_ARTICLES 调整（≥1 整数）。
 */

const cheerio = require('cheerio');
const NOINDEX_META = '<meta name="robots" content="noindex,follow">';
const DEFAULT_MIN_ARTICLES = 3;

function getMinArticles() {
  const env = process.env.HEXO_NOINDEX_MIN_ARTICLES;
  const n = parseInt(env, 10);
  return Number.isFinite(n) && n >= 1 ? n : DEFAULT_MIN_ARTICLES;
}

function injectNoindex(html) {
  if (/<meta\s+name=["']robots["']/i.test(html)) return null;
  return html.replace('</head>', NOINDEX_META + '</head>');
}

function extractTagSlug(path) {
  if (!path) return null;
  // 匹配 tags/<slug>/index.html 与 tags/<slug>/page/N/index.html
  const m = String(path).match(/^tags\/([^/]+)\/(?:page\/\d+\/)?index\.html$/);
  if (!m) return null;
  try {
    return decodeURIComponent(m[1]);
  } catch (_) {
    return m[1];
  }
}

function findTag(tags, slug) {
  // hexo 的 tag.slug 对英文是 URL-safe，对中文常是原汉字名
  let tag = tags.findOne({ slug: slug });
  if (tag) return tag;
  tag = tags.findOne({ name: slug });
  if (tag) return tag;
  return null;
}

hexo.extend.filter.register(
  'after_render:html',
  function (content, data) {
    if (!data) return content;

    const slug = extractTagSlug(data.path);
    if (!slug) return content;

    const tags = hexo.locals.get('tags');
    if (!tags || !tags.length) return content;

    const tag = findTag(tags, slug);
    if (!tag) return content;

    const count = tag.length || 0;
    if (count >= getMinArticles()) return content;

    return injectNoindex(content);
  },
  10
);

function isNoindex(html) {
  const head = String(html).match(/<head\b[^>]*>[\s\S]*?<\/head\s*>/i);
  if (!head) return false;
  const $ = cheerio.load(head[0]);
  return $('meta').toArray().some(node => {
    const name = ($(node).attr('name') || '').toLowerCase();
    return /^(robots|googlebot|bingbot)$/.test(name) &&
      /\b(noindex|none)\b/i.test($(node).attr('content') || '');
  });
}

function sitemapRoute(url, siteUrl) {
  try {
    const parsed = new URL(url);
    const base = new URL(siteUrl);
    if (parsed.origin !== base.origin || !parsed.pathname.startsWith(base.pathname)) return null;
    let name = decodeURIComponent(parsed.pathname.slice(base.pathname.length));
    if (!name || name.endsWith('/')) name += 'index.html';
    return name;
  } catch (_) { return null; }
}

function readRoute(route, name) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    const stream = route.get(name);
    if (!stream) return reject(new Error(`站点地图引用的本地路由不存在：${name}`));
    stream.on('data', chunk => chunks.push(Buffer.from(chunk)))
      .on('error', reject).on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
  });
}

function cleanSitemap(xml, noindexUrls) {
  const seen = new Set();
  let duplicates = 0, excluded = 0;
  const result = xml.replace(/<url\b[^>]*>[\s\S]*?<\/url\s*>/gi, block => {
    const $ = cheerio.load(block, { xmlMode: true });
    const url = $('url > loc').text().trim();
    if (!url) return block;
    if (seen.has(url)) { duplicates++; return ''; }
    seen.add(url);
    if (noindexUrls.has(url)) { excluded++; return ''; }
    // 保留整个原始 XML 条目，不重编码 loc，不变更 lastmod。
    return block;
  });
  return { xml: result, duplicates, excluded };
}

// 路由已建立后读取实际 HTML；仅替换 XML 路由内容，绝不删除页面路由。
hexo.extend.filter.register('after_generate', async function () {
  const routes = new Set(hexo.route.list());
  const checked = new Map();
  const paths = [hexo.config.sitemap && hexo.config.sitemap.path,
    hexo.config.baidusitemap && hexo.config.baidusitemap.path].flat().filter(Boolean);
  for (const name of new Set(paths)) {
    if (!routes.has(name)) continue;
    const xml = await readRoute(hexo.route, name);
    const $ = cheerio.load(xml, { xmlMode: true });
    const urls = new Set($('urlset > url > loc').toArray().map(node => $(node).text().trim()));
    const noindexUrls = new Set();
    for (const url of urls) {
      const pagePath = sitemapRoute(url, hexo.config.url);
      if (!pagePath || !routes.has(pagePath) || !/\.html?$/.test(pagePath)) continue;
      if (!checked.has(pagePath)) checked.set(pagePath, isNoindex(await readRoute(hexo.route, pagePath)));
      if (checked.get(pagePath)) noindexUrls.add(url);
    }
    const cleaned = cleanSitemap(xml, noindexUrls);
    if (cleaned.xml !== xml) hexo.route.set(name, cleaned.xml);
    hexo.log.info('[sitemap-cleanup] %s：去重 %d 条，排除 noindex %d 条', name, cleaned.duplicates, cleaned.excluded);
  }
}, 100);

hexo.extend.filter.register('after_generate', function () {
  try {
    const tags = hexo.locals.get('tags');
    if (!tags || !tags.length) return;
    const threshold = getMinArticles();
    let total = 0;
    let thinned = 0;
    tags.forEach(function (t) {
      total++;
      if ((t.length || 0) < threshold) thinned++;
    });
    hexo.log.info(
      '[noindex-thin-tags] 共 %d 个 tag，%d 个低于阈值 (%d 篇) 将被 noindex，%d 个保持正常索引。',
      total,
      thinned,
      threshold,
      total - thinned
    );
  } catch (_) {
    /* 忽略 */
  }
});

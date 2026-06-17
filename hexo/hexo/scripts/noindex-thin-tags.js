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

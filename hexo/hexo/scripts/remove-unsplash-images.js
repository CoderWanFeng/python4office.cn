'use strict'

/**
 * replace-unsplash-with-default.js
 *
 * 作用：渲染每篇 .md 的 HTML 时，把所有指向 `images.unsplash.com` 的图片
 *       **替换为 Butterfly 主题默认占位图 `/img/background.jpg`**
 *       （一份 168KB 程序员办公场景图，已经部署在 origin + CDN）。
 *
 * 这样：
 *   - 不再下载 unsplash（美国 fastly 节点 1-3s/张）
 *   - 浏览器直接拉 `/img/background.jpg`（国内 CDN 100-300ms）
 *   - 所有 cover 缩略图统一风格（同图重用）
 *
 * 同时清理：
 *   1. <img src="https://images.unsplash.com/..."> → 改 src 为 /img/background.jpg
 *   2. <img data-src="...unsplash..."> → 改 src
 *   3. <a class="thumbnail" href="..."><img ...></a> → 整段保留但 img 改 src
 *   4. data-image="...unsplash..." → 改为 /img/background.jpg
 *   5. background-image:url(unsplash...) → 改为 url(/img/background.jpg)
 *   6. <meta og:image> / <meta twitter:image> → 整条删除
 *
 * 预期收益（实测 Round 3 数据）：
 *   - 替换前：每张 unsplash 1-3s，13 张共 4.9s
 *   - 替换后：每张 /img/background.jpg 100-300ms（CDN 缓存后约 0ms 命中）
 *   - 单页面可省 3-4 秒
 *
 * 关闭/还原方法：
 *   - 把 ENABLED 改 false → 保留原图不替换
 *   - 把 REPLACE_URL 改 '' → 替换成空 src（彻底不下载，保留 img 标签）
 *   - 改 REPLACE_URL 为别的图（如 /img/knowledge.png）→ 换成别的占位
 */

const ENABLED = true
const REPLACE_URL = '/img/background.jpg'

function replaceUnsplash(html) {
  if (!ENABLED) return html
  if (typeof html !== 'string' || !html) return html

  let count = 0

  // 1. 主流：<img src="https://images.unsplash.com/..." ...>
  //    替换 src（注意 onerror 不要丢，否则部分主题会一直空着）
  html = html.replace(
    /(<img\b[^>]*?\bsrc\s*=\s*["'])(https?:\/\/(?:images\.)?unsplash\.com\/[^"']+)(["'][^>]*?>)/gi,
    (m, prefix, _url, suffix) => { count++; return prefix + REPLACE_URL + suffix }
  )

  // 2. 懒加载备用：data-src / data-original
  html = html.replace(
    /(<img\b[^>]*?\bdata-(?:src|original)\s*=\s*["'])(https?:\/\/(?:images\.)?unsplash\.com\/[^"']+)(["'][^>]*?>)/gi,
    (m, prefix, _url, suffix) => { count++; return prefix + REPLACE_URL + suffix }
  )

  // 3. <a class="thumbnail" href=".."><img ...></a>：替换 img 的 src，a 标签保留
  //    （无需特殊处理，第 1 步的 regex 已经会匹配里面的 img）

  // 4. div/a 等元素的 data-image 属性
  html = html.replace(
    /\b(data-(?:image|original|src))\s*=\s*["'](https?:\/\/(?:images\.)?unsplash\.com\/[^"']+)["']/gi,
    (m, attr, _url) => { count++; return `${attr}="${REPLACE_URL}"` }
  )

  // 5. inline style 里的 background-image:url(...)  → 替换 URL
  html = html.replace(
    /(background-image\s*:\s*url\s*\(\s*["']?)(https?:\/\/(?:images\.)?unsplash\.com\/[^"')]+)(["']?\s*\))/gi,
    (m, prefix, _url, suffix) => `${prefix}${REPLACE_URL}${suffix}`
  )

  // 6. og:image / twitter:image meta → 整条删除（避免 SEO 抓取无效图）
  html = html.replace(
    /<meta\b[^>]*?\b(?:property|name)\s*=\s*["'](?:og:image|twitter:image)["'][^>]*>\s*/gi,
    ''
  )

  return html
}

function applyReplace(data) {
  if (data && typeof data === 'object' && data.content) {
    data.content = replaceUnsplash(data.content)
  } else if (typeof data === 'string') {
    return replaceUnsplash(data)
  }
  return data
}

hexo.extend.filter.register('after_render:html', applyReplace)
hexo.extend.filter.register('_after_html_render', applyReplace)

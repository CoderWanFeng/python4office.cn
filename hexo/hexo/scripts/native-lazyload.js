'use strict'

/**
 * 给所有 <img> 自动加 loading="lazy" decoding="async"
 *
 * 必须在主题的 lazyload 关闭（lazyload.enable: false）时使用，
 * 否则主题会把 src 替换成 base64 占位符。
 *
 * 收益：
 * - 节省 7.3KB vanilla-lazyload.js
 * - 节省 27 个 data-lazy-src 替换开销
 * - 浏览器原生懒加载，零依赖
 */
const IMG_RE = /<img(?![^>]*\sloading=)[^>]*>/gi

function addLazyAttr(data) {
  // 兼容两种调用形式：对象 { content } 或字符串
  if (data && typeof data === 'object' && data.content) {
    data.content = data.content.replace(
      IMG_RE,
      m => m.replace(/<img\b/i, '<img loading="lazy" decoding="async"')
    )
    return data
  }
  if (typeof data === 'string') {
    return data.replace(
      IMG_RE,
      m => m.replace(/<img\b/i, '<img loading="lazy" decoding="async"')
    )
  }
  return data
}

// 注册到多个 hook：post + html（覆盖所有渲染路径）
hexo.extend.filter.register('after_post_render', addLazyAttr)
hexo.extend.filter.register('_after_html_render', addLazyAttr)
hexo.extend.filter.register('after_render:html', addLazyAttr)

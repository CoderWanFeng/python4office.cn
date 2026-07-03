'use strict'

/**
 * 延迟加载 busuanzi 计数脚本
 *
 * 主题会在 head 里同步注入 <script async src="...busuanzi...">，但 busuanzi.ibruce.info
 * 后端响应慢（实测 1s+），会占用浏览器连接池。
 *
 * 这个过滤器把那个立即加载的 script 标签替换为一个空标签，然后在 inject.bottom
 * 里注入的延后钩子（通过 requestIdleCallback）会在浏览器空闲时再加载真正的脚本。
 *
 * 依赖：必须在 _config.butterfly.yml 的 inject.bottom 里挂上延后加载代码（见下）。
 */
const BUSUANZI_RE = /<script[^>]*src=["'][^"']*busuanzi[^"']*["'][^>]*><\/script>/i

function deferBusuanzi(data) {
  if (data && typeof data === 'object' && data.content) {
    data.content = data.content.replace(BUSUANZI_RE, '<script data-deferred-busuanzi="true"></script>')
  } else if (typeof data === 'string') {
    return data.replace(BUSUANZI_RE, '<script data-deferred-busuanzi="true"></script>')
  }
  return data
}

hexo.extend.filter.register('after_render:html', deferBusuanzi)
hexo.extend.filter.register('_after_html_render', deferBusuanzi)

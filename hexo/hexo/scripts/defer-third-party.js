'use strict'

/**
 * 把第三方（统计/广告）脚本从「render-blocking」改为「async/defer 不阻塞」。
 *
 * 主页实测数据（之前的会话记录）：
 *   pagead2.googlesyndication.com (Google Ads)       ~0.60s
 *   hm.baidu.com (百度统计)                          ~0.33s
 *   www.googletagmanager.com (gtag)                  ~0.51s
 *   cdn.jsdelivr.net (jquery 3.6.0)                  ~1.04s
 *   busuanzi.ibruce.info (不蒜子)                     ~1.27s  ← 单独脚本已 defer
 *   www.clarity.ms (Clarity)                         ~0.54s
 *
 * 策略：
 *   - adsbygoogle / googletagmanager 用 defer（保证初始化顺序）
 *   - 其余用 async（纯统计，不影响页面渲染）
 *
 * 实现思路（v2 改进）：
 *   - 旧的思路：解析 src 重新构造。但 src 可能在 type/async/defer 之后，位置不固定。
 *   - 新的思路：直接给 <script ...> 加 async/defer 属性，**不重写整个 tag**。
 *     - 用 regex 定位 <script ... host ... ></script> 整段
 *     - 检查是否已经有 async/defer，没有的话在 src 后插入属性
 *
 * 注意：defer-busuanzi.js 已经处理过 busuanzi，这里不再处理 busuanzi（本函数的 ASYNC 列表也不含它）。
 *      确保重复运行幂等（已有 async 就不重复添加）。
 */

const DEFER_HOSTS = [
  'googletagmanager.com',
  'googlesyndication.com',
  'pagead2.googlesyndication.com',  // adsbygoogle.js（这个用 defer 更稳）
]

const ASYNC_HOSTS = [
  'hm.baidu.com',
  'www.clarity.ms',
  'cdn.jsdelivr.net',               // jquery
]

const ASYNC_PATHS = [
  // 本地 hexo 主题工具函数（不依赖 DOM，加 async 让它们并行下载）
  '/js/utils.js',
]

const DEFER_PATHS = [
  // 本地 hexo 主题主脚本（main.js 监听 DOMContentLoaded，加 defer 最合适）
  '/js/main.js',
]

// 匹配 <script ...>...</script> 整段，含 src 包含指定 host 的
// 用 [\s\S] 不含贪婪，避免吞掉多行
function scriptRe(host) {
  const esc = host.replace(/\./g, '\\.')
  return new RegExp(
    `(<script\\b[^>]*?\\s+src=["'][^"']*?${esc}[^"']*["'][^>]*>)` +
    `([\\s\\S]*?</script>)`,
    'gi'
  )
}

function pathScriptRe(path) {
  // 匹配 <script src="/js/utils.js" ...></script> 或 /js/utils.js?v=xxx
  const esc = path.replace(/\//g, '\\/').replace(/\./g, '\\.')
  return new RegExp(
    `(<script\\b[^>]*?\\s+src=["']${esc}(?:\\?[^"']*)?["'][^>]*>)` +
    `([\\s\\S]*?</script>)`,
    'gi'
  )
}

function addAttr(match, attr, hosts, paths) {
  let result = match
  if (hosts && hosts.length) {
    for (const host of hosts) {
      const re = scriptRe(host)
      result = result.replace(re, (m, openingTag, body) => {
        if (/\b(?:async|defer)\b/i.test(openingTag)) return m
        const newTag = openingTag.replace(
          /(\s+src=["'][^"']*["'])/i,
          `$1 ${attr.trim()}`
        )
        return newTag + body
      })
    }
  }
  if (paths && paths.length) {
    for (const path of paths) {
      const re = pathScriptRe(path)
      result = result.replace(re, (m, openingTag, body) => {
        if (/\b(?:async|defer)\b/i.test(openingTag)) return m
        const newTag = openingTag.replace(
          /(\s+src=["'][^"']*["'])/i,
          `$1 ${attr.trim()}`
        )
        return newTag + body
      })
    }
  }
  return result
}

function deferThirdParty(data) {
  // hexo 的 data 对象（post 渲染）或 string（顶级 hook）
  let content
  if (data && typeof data === 'object' && data.content) {
    content = data.content
  } else if (typeof data === 'string') {
    content = data
  } else {
    return data
  }

  let html = content
  html = addAttr(html, ' defer', DEFER_HOSTS, DEFER_PATHS)
  html = addAttr(html, ' async', ASYNC_HOSTS, ASYNC_PATHS)

  if (data && typeof data === 'object' && data.content) {
    data.content = html
    return data
  }
  return html
}

hexo.extend.filter.register('after_render:html', deferThirdParty)
hexo.extend.filter.register('_after_html_render', deferThirdParty)

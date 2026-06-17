'use strict';

/**
 * 首页 HTML 体积优化
 *
 * 删冗余 meta 标签：
 *   - og: 套件里 article:author / article:tag 用在首页是冗余的
 *     （首页是 website 类型，不是 article 类型）
 *   - meta name="copyright" 在 author 之后重复
 *
 * 权衡说明：原计划把 promo.css (~1.1KB gzip) 内联到首页减少 RTT，
 * 实测内联后 HTML gzip 体积反而 +1.1KB。在 HTTP/2 + 现代浏览器场景下，
 * 1 个 RTT 的节省抵不上 HTML 体积膨胀带来的传输成本，所以取消内联。
 *
 * 实现：跟 noindex-thin-tags.js 一样用 after_render:html
 */

function isHomepage(data) {
  return data && data.path === 'index.html';
}

function removeRedundantMeta(html) {
  // 1) 删 og:article:*（首页是 website 类型）
  html = html.replace(
    /\s*<meta\s+property=["']og:article:[^"']+["'][^>]*>/gi,
    ''
  );
  // 2) 删重复的 copyright（author 已包含）
  html = html.replace(
    /\s*<meta\s+name=["']copyright["'][^>]*>/gi,
    ''
  );
  return html;
}

hexo.extend.filter.register(
  'after_render:html',
  function (content, data) {
    if (!isHomepage(data)) return content;

    const before = content.length;
    content = removeRedundantMeta(content);
    const after = content.length;

    hexo.log.info(
      '[optimize-homepage] 冗余 meta 清理，HTML %d → %d 字节（Δ %d 字节）',
      before,
      after,
      before - after
    );
    return content;
  },
  20
);

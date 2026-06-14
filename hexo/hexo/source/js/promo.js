/*
 * 全站推广脚本（4 种广告形式，B 端友好）
 *
 *   ① 顶部公告条      — 全站每页（× 关闭后 24h 重新出现，轻量样式，不影响 AdSense 审核）
 *   ⑥ 文中段落广告    — 长文（每 5 段一条，最多 2 条）
 *   ② 文末 CTA 卡片   — 文章/独立页底部
 *
 * 配套样式：/css/promo.css
 * 所有外链均带 rel="nofollow sponsored noopener"，符合 Google AdSense 政策
 */
(function () {
  'use strict';

  var PROMO = {
    // ① 顶部公告条 → 腾讯 WorkBuddy 邀请通道
    topUrl: 'https://www.codebuddy.cn/events/invite?inviteCode=bflfcx96gj',
    topText: '🎁 腾讯 WorkBuddy 邀请通道 | 领 2000 积分',
    topCta: '领取 →',
    topStorageKey: 'promo_top_closed_at',
    topCloseDays: 1,

    // ⑥ 文中段落广告 → B 站课程
    inlineUrl: 'https://www.bilibili.com/cheese/play/ep2342243',
    inlineEvery: 5,
    inlineMax: 1,
    inlineMinParas: 5,
    inlineVariants: [
      { icon: '🎬', text: 'B 站免费试听课：<strong>AI 编程 + 自动化办公 + AI 工具</strong>三合一，从零到一系统讲解。', btn: '立即试听 →' }
    ],

    // ② 文末 CTA → 秒级部署 DeepSeek 版 Claude Code（腾讯云）
    footerUrl: 'https://curl.qcloud.com/I4IFQqEG',
    footerTitle: '🚀 1 分钟部署 DeepSeek 版 Claude Code',
    footerDesc: '腾讯云官方镜像，秒级开通，国内直连，团队可统一管理账号、配额与日志。',
    footerBtn: '立即开通 →'
  };

  var REL_ATTR = 'nofollow sponsored noopener';

  // ===== 公共：判断是否列表页 =====
  function isListPage() {
    return !!document.querySelector(
      '#recent-posts, #archive-result, #category-list, #tag-page-name, #page'
    ) && !document.querySelector('#article-container .post-content');
  }

  // ===== ① 顶部公告条（× 关闭后 24h 重新出现） =====
  function shouldShowTopBar() {
    try {
      var closedAt = localStorage.getItem(PROMO.topStorageKey);
      if (!closedAt) return true;
      return (Date.now() - parseInt(closedAt, 10)) / 86400000 > PROMO.topCloseDays;
    } catch (e) { return true; }
  }

  function renderTopBar() {
    if (document.querySelector('.promo-top-bar')) return;
    if (!shouldShowTopBar()) return;

    var bar = document.createElement('div');
    bar.className = 'promo-top-bar';
    bar.innerHTML =
      '<span class="promo-text">' + PROMO.topText + '</span>' +
      '<a class="promo-cta-link" href="' + PROMO.topUrl + '" target="_blank" rel="' + REL_ATTR + '">' + PROMO.topCta + '</a>' +
      '<button type="button" class="promo-close" aria-label="关闭推广，24小时后自动重新出现" title="关闭推广，24小时后自动重新出现">×</button>';
    document.body.insertBefore(bar, document.body.firstChild);
    document.body.classList.add('promo-top-active');
    bar.style.display = 'block';

    bar.querySelector('.promo-close').addEventListener('click', function () {
      bar.style.display = 'none';
      document.body.classList.remove('promo-top-active');
      try { localStorage.setItem(PROMO.topStorageKey, Date.now().toString()); } catch (e) {}
    });
  }

  // ===== ⑥ 文中段落广告 =====
  function buildInlineAdNode(index) {
    var v = PROMO.inlineVariants[index % PROMO.inlineVariants.length];
    var box = document.createElement('div');
    box.className = 'promo-inline';
    box.innerHTML =
      '<span class="promo-inline-icon">' + v.icon + '</span>' +
      '<span class="promo-inline-text">' + v.text + '</span>' +
      '<a class="promo-inline-btn" href="' + PROMO.inlineUrl + '" target="_blank" rel="' + REL_ATTR + '">' + v.btn + '</a>';
    return box;
  }

  function renderInlineAds() {
    var article = document.querySelector('#article-container');
    if (!article || isListPage() || article.querySelector('.promo-inline')) return;

    var paras = Array.prototype.filter.call(
      article.children,
      function (el) { return el.tagName === 'P' && el.textContent.trim().length > 30; }
    );
    if (paras.length < PROMO.inlineMinParas) return;

    var inserted = 0;
    for (var i = PROMO.inlineEvery - 1; i < paras.length; i += PROMO.inlineEvery) {
      if (inserted >= PROMO.inlineMax) break;
      var anchor = paras[i];
      var next = anchor.nextElementSibling;
      if (next && /^H[1-3]$/.test(next.tagName)) continue;
      anchor.parentNode.insertBefore(buildInlineAdNode(inserted), anchor.nextSibling);
      inserted++;
    }
  }

  // ===== ② 文末 CTA 卡片 =====
  function renderFooterCta() {
    var article = document.querySelector('#article-container');
    if (!article || isListPage() || article.querySelector('.promo-footer-cta')) return;

    var cta = document.createElement('div');
    cta.className = 'promo-footer-cta';
    cta.innerHTML =
      '<h3 class="promo-title">' + PROMO.footerTitle + '</h3>' +
      '<p class="promo-desc">' + PROMO.footerDesc + '</p>' +
      '<a class="promo-btn" href="' + PROMO.footerUrl + '" target="_blank" rel="' + REL_ATTR + '">' + PROMO.footerBtn + '</a>';
    article.appendChild(cta);
  }

  // ===== 初始化 =====
  function init() {
    renderTopBar();
    renderInlineAds();
    renderFooterCta();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // pjax 切换：仅重新注入文章页内容（顶部条不重新注入）
  document.addEventListener('pjax:complete', function () {
    renderInlineAds();
    renderFooterCta();
  });
})();

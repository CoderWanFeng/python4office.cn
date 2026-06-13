/*
 * 全站推广脚本（4 种广告形式，B 端友好）
 *
 *   ① 顶部公告条      — 全站每页（7 天关闭记忆）
 *   ⑥ 文中段落广告    — 长文（每 5 段一条，最多 2 条）
 *   ② 文末 CTA 卡片   — 文章/独立页底部
 *
 * 配套样式：/css/promo.css
 * 所有外链均带 rel="nofollow sponsored noopener"，符合 Google AdSense 政策
 */
(function () {
  'use strict';

  var PROMO = {
    // ① 顶部公告条 → 微信文章
    topUrl: 'https://mp.weixin.qq.com/s/P_o6azd0AwuraLkQQg6t2Q',
    topText: '🚀 别一个人学AI | 晚枫300+人陪跑群',
    topCta: '加入 →',
    topStorageKey: 'promo_top_closed_at',
    topCloseDays: 7,

    // ⑥ 文中段落广告 → Hermes Agent（AI Agent 工程化平台）
    inlineUrl: 'https://www.codebuddy.cn/events/invite?inviteCode=bflfcx96gj',
    inlineEvery: 5,
    inlineMax: 1,
    inlineMinParas: 5,
    inlineVariants: [
      { icon: '🎁', text: '邀请体验 <strong>腾讯 WorkBuddy</strong>，<strong>我的专属通道</strong>点击立领 <strong>2000 积分</strong>，150+ AI 专家团一站搞定。', btn: '立即领取 →' }
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

  // ===== ① 顶部公告条 =====
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
      '<button type="button" class="promo-close" aria-label="关闭推广">×</button>';
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

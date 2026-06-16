# 站点推广位当前配置（备份）

> 用于轮播时快速回滚 / 参考。
>
> **配置源文件**
> - 脚本：`hexo/hexo/source/js/promo.js`（PROMO 对象）
> - 样式：`hexo/hexo/source/css/promo.css`
> - 注入配置：`hexo/hexo/_config.butterfly.yml` 的 `inject.head` / `inject.bottom`
> - AdSense：`hexo/hexo/_config.butterfly.yml` 的 `google_adsense`
> - AdSense 入口：`hexo/hexo/themes/butterfly/layout/includes/head/google_adsense.pug`

---

## ① 顶部公告条（fixed 顶部 · 全站每页）

| 字段 | 值 |
|---|---|
| 链接 URL | `https://codeflying.cgref.cn/s/20epp94ew1` |
| 文案 | `🎁 说中文，做应用 \| 一句话自动生成 App / 海报 / AI 客服` |
| CTA 按钮 | `立即体验 →` |
| 产品定位 | 「说中文，做应用」的 AI 应用生成器，不会代码也能一句话生成 App、海报、AI 客服 |
| 关闭后多久重出 | 1 天（`topCloseDays: 1`） |
| LocalStorage 键 | `promo_top_closed_at` |
| 影响 body | 出现时给 `body` 加 `promo-top-active`，下移 36px（移动端 32px） |

---

## ⑥ 文中段落广告（每 5 段一条 · 最多 1 条 · 至少 5 段才出现）

| 字段 | 值 |
|---|---|
| 链接 URL | `https://www.bilibili.com/cheese/play/ep2342243` |
| 插入间隔 | 5 段（`inlineEvery: 5`） |
| 最大插入数 | 1（`inlineMax: 1`） |
| 最小段落数 | 5（`inlineMinParas: 5`） |
| 排除规则 | 段落紧跟 `H1/H2/H3` 时跳过 |
| 显示页面 | 仅 `#article-container` 文章页（列表/归档/标签/分类页跳过） |

### 当前变体

```js
inlineVariants: [
  {
    icon: '🎬',
    text: '<strong>0 基础也能学</strong>：让 AI + 自动化办公 帮你做表、写文档、回邮件。',
    btn: '免费试听 →'
  }
]
```

---

## ② 文末 CTA 卡片（文章 / 独立页底部）

| 字段 | 值 |
|---|---|
| 链接 URL | `https://www.liblib.tv/?sourceid=005902&utm=cg&cgv=9omkl4jn4d` |
| 标题 | `想做视频号 / 抖音 / 小红书？` |
| 描述 | `AI 帮你一键生成，不用学剪辑，免费试用 3 次。` |
| CTA 按钮 | `免费试用 →` |
| 角标 | 右上角自动加 `推广` 灰色小标 |

---

## Google AdSense

| 字段 | 值 |
|---|---|
| 启用 | ✅ 是 |
| 客户端 ID | `ca-pub-3274762482246875` |
| 脚本 | `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js` |
| 自动广告 | ✅ 是（`auto_ads: true`） |
| 页面级广告 | ✅ 是 |
| 插入位置 | `<head>`，由 `google_adsense.pug` partial 注入 |

---

## 手动广告位（Butterfly 主题原生）

```yaml
ad:
  index:    # 首页（每 3 篇文章）—— 空
  aside:    # 侧边栏 —— 空
  post:     # 文章页（分页前）—— 空
```

> 目前都是空的，没有插任何内容。

---

## 🔁 轮播时怎么换 / 怎么回到当前这一版

### 1. 换广告

直接改 `hexo/hexo/source/js/promo.js` 顶部的 `PROMO` 对象：

| 字段 | 控制位置 |
|---|---|
| `topUrl` / `topText` / `topCta` | ① 顶部公告条 |
| `inlineUrl` / `inlineVariants` | ⑥ 文中段落广告（可放多个变体轮播） |
| `footerUrl` / `footerTitle` / `footerDesc` / `footerBtn` | ② 文末 CTA |

### 2. 回到当前这一版

把本文件里 **「当前配置」** 部分对应的值，粘回 `promo.js` 的 `PROMO` 对象即可。

### 3. 轮播变体的小技巧

`inlineVariants` 是一个数组，可以同时塞多条，脚本会按 `index % variants.length` 取，所以加新变体就能自动轮播：

```js
inlineVariants: [
  { icon: '🎬', text: '...', btn: '免费试听 →' },
  { icon: '📘', text: '...', btn: '立即查看 →' },
  { icon: '🚀', text: '...', btn: '马上体验 →' }
]
```

---

## ✅ 合规说明

- 所有外链统一带 `rel="nofollow sponsored noopener"`
- 自定义推广样式刻意做成「极简系统通知栏」风（浅灰底 + 蓝紫边），刻意弱化广告感
- 顶部公告条关闭后 24h 才重出，避免打扰
- 这一切都是为了和 AdSense 共存，不影响 AdSense 审核
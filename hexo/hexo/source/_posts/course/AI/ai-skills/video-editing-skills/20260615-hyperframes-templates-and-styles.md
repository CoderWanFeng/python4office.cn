---
title: Hyperframes 9 大模板详解：从暖色电影感到数据故事，一次讲清
date: 2026-06-15 23:10:00
tags: [Hyperframes, AI视频, 视频模板, 视频风格, 程序员晚枫]
categories: [AI Skills, 平台攻略]
cover: https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=1200&auto=format&fit=crop
---


大家好，我是程序员晚枫。

上次我们讲了 [Hyperframes 入门](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-quickstart/)——2 分钟出第一个 MP4。

这次来**深挖**一个问题：

> **Hyperframes 到底能生成多少风格的视频？**

答案是：**官方内置 8 个模板 + 1 个空白脚手架 = 9 种风格**。

每种都对应**特定的视觉语言和典型场景**。今天一篇文章全讲清。

---

## 一、9 个模板速查表

| 模板 | 风格 | 画面比例 | 适合做什么 |
|---|---|---|---|
| **warm-grain** | 暖色 + 颗粒纹理 | 横屏 16:9 | 生活方式、品牌片头 |
| **play-mode** | 弹性、动感、年轻 | 横屏 16:9 | 社交媒体、产品发布 |
| **swiss-grid** | 瑞士国际主义、网格 | 横屏 16:9 | 企业宣传、技术讲解 |
| **kinetic-type** | 戏剧性大字幕 | 横屏 16:9 | 标题卡、推广短片 |
| **decision-tree** | 流程图、渐进揭示 | 横屏 16:9 | 教程、决策树演示 |
| **product-promo** | 多场景产品展示 | 横屏 16:9 | 产品 demo、商业推广 |
| **nyt-graph** | 编辑级数据图 | 横屏 16:9 | 数据故事、报告可视化 |
| **vignelli** | 大胆排版 + 红色 | **竖屏 9:16** | 标题、公告 |
| **blank** | 纯脚手架 | 任意 | 完全自定义 / AI 生成 |

**8 个成品 + 1 个空白 = 9 种风格**。

---

## 二、怎么用这些模板？

一行命令：

```bash
npx hyperframes init my-video --example <name>
```

**替换 `<name>` 为模板名**（warm-grain / play-mode / ...）就行。

带已有视频（自动转字幕）：

```bash
npx hyperframes init my-video --example warm-grain --video ./intro.mp4
```

---

## 三、横屏 7 大模板详解

### 1. Warm Grain（暖色电影感）⭐ 推荐入门

**视觉语言**：
- 奶油色调（米色、暖灰、深棕）
- 胶片颗粒纹理叠加
- 柔和渐变转场

**它会生成**：
- 主视频 + 3 个子 composition（intro / graphics / captions）
- 内置字幕系统
- 自带 intro 片段

📺 **参考视频**：[Website → HyperFrames](https://github.com/heygen-com/hyperframes-launches/tree/main/website-to-hyperframes)（生活方式类风格最接近）

**适合**：
- 生活方式类 Vlog
- 品牌片头 / 片尾
- 时尚 / 美食 / 旅行内容
- 公众号深度长文配图

**典型场景**：
> "我开了一家咖啡店，想拍一段 30 秒的介绍视频。"

```bash
npx hyperframes init coffee-intro --example warm-grain
```

**项目结构**：
```
my-video/
├── meta.json
├── index.html
├── compositions/
│   ├── intro.html
│   ├── graphics.html
│   └── captions.html
└── assets/
```

---

### 2. Play Mode（弹性、动感）

**视觉语言**：
- 弹性缓动（spring / elastic）
- 高饱和度色彩
- 快速切换、跳切节奏
- 年轻、活泼

**它会生成**：
- 主视频 + 3 个子 composition（intro / stats / captions）
- 数字动画组件（适合做"涨了 X 倍"那种动效）

📺 **参考视频**：[Timeline Editor launch](https://github.com/heygen-com/hyperframes-launches/tree/main/timeline-launch)（社交媒体型产品发布最接近）

**适合**：
- 抖音 / 快手 / 小红书
- 产品发布 / 活动宣传
- 健身 / 美食 / 旅行类 UGC
- 年轻向品牌

**典型场景**：
> "我们 App 的 DAU 涨了 10 倍，做一段 15 秒的庆祝视频。"

**项目结构**：
```
my-video/
├── meta.json
├── index.html
├── compositions/
│   ├── intro.html
│   ├── stats.html
│   └── captions.html
└── assets/
```

---

### 3. Swiss Grid（瑞士国际主义）

**视觉语言**：
- 严格网格布局
- 无衬线字体（Helvetica 风格）
- 黑/白/红主色
- 信息层级清晰
- 大留白

**它会生成**：
- 主视频 + 3 个子 composition（intro / graphics / captions）
- 内置数据卡片组件

📺 **参考视频**：[Timeline Editor launch](https://github.com/heygen-com/hyperframes-launches/tree/main/timeline-launch)（结构化、专业感最接近）

**适合**：
- 企业宣传片
- 技术发布会
- 金融 / 咨询类内容
- 设计感强的产品

**典型场景**：
> "我们 SaaS 公司要做一支 B 端宣传片，体现专业感。"

---

### 4. Kinetic Type（戏剧性大字幕）

**视觉语言**：
- 超大字号
- 文字主导画面
- 戏剧性切入/飞出
- 文字动画（letter-by-letter 出现、错位、弹跳）

**它会生成**：
- 主视频 + 1 个子 composition（main-graphics）
- 极简结构，专注文字

📺 **参考视频**：[Texture launch](https://github.com/heygen-com/hyperframes-launches/tree/main/texture-launch-video)（文字 + 纹理特效最接近）

**适合**：
- 电影片头 / 预告片
- 课程章节标题
- 品牌口号强化
- 演讲开场

**典型场景**：
> "我想做一个在线课程的章节切换动画。"

---

### 5. Decision Tree（流程图 / 决策树）

**视觉语言**：
- 节点 + 连线
- 分支结构（if-then 流程）
- 渐进揭示（一次显示一层）
- 颜色编码路径

**它会生成**：
- 主视频 + 1 个子 composition（decision_tree）
- 动画化流程

📺 **参考视频**：[Website → HyperFrames](https://github.com/heygen-com/hyperframes-launches/tree/main/website-to-hyperframes)（结构化流程叙事最接近）

**适合**：
- 教程 / 教学视频
- 产品决策演示
- 工作流说明
- 故障排查指南

**典型场景**：
> "我做一个 Python 入门教程，要演示'选哪条学习路径'。"

---

### 6. Product Promo（多场景产品展示）

**视觉语言**：
- 多镜头切换（5 个 scene）
- SVG 矢量素材
- 镜头转场
- 中心产品 + 周围环境

**它会生成**：
- 主视频 + 5 个子 composition（5 个 scene）
- 3 个 SVG 素材（图标、Logo 部件、胶囊按钮）

📺 **参考视频**：[HyperFrames launch](https://github.com/heygen-com/hyperframes-launches/tree/main/hyperframes-launch)（完整产品发布叙事最接近）

**适合**：
- SaaS 产品发布
- 硬件产品发布
- App 推广
- Design Tool 演示

**典型场景**：
> "我们新做了一款设计工具，想拍 30 秒的发布短片。"

**项目结构**：
```
my-video/
├── meta.json
├── index.html
├── compositions/
│   ├── scene1-logo-intro.html
│   ├── scene2-4-canvas.html
│   └── scene5-logo-outro.html
└── assets/
    ├── figma-cursors.svg
    ├── figma-logo-pieces.svg
    └── figma-logo-pills.svg
```

---

### 7. NYT Graph（编辑级数据图）

**视觉语言**：
- 报纸排版风格
- 数据驱动的柱状图 / 折线图
- 印刷感的字号对比
- 极简配色（黑 + 1 个强调色）

**它会生成**：
- 主视频 + 1 个子 composition（nyt-chart）
- 动画化数据图表

📺 **参考视频**：[Website → HyperFrames](https://github.com/heygen-com/hyperframes-launches/tree/main/website-to-hyperframes)（数据展示 + 视觉化最接近）

**适合**：
- 数据新闻 / 报告
- 经济 / 财经分析
- 学术演示
- 行业研究

**典型场景**：
> "我写了份《中国 AI 行业 2026 报告》，想配一段 60 秒的数据可视化。"

---

## 四、竖屏模板：Vignelli

**视觉语言**：
- 大胆排版（Massimo Vignelli 风格）
- 红色高亮 + 黑色背景
- 1080×1920 竖屏
- 极简元素，超大字号

**它会生成**：
- 主视频 + 2 个子 composition（overlays / captions）
- 适合手机全屏

📺 **参考视频**：[Texture launch](https://github.com/heygen-com/hyperframes-launches/tree/main/texture-launch-video)（标题感 + 视觉冲击最接近）

**适合**：
- 抖音 / TikTok 开头
- 微信公众号头图
- 公告 / 通知
- 重大消息推送

**典型场景**：
> "我们公众号要发一篇关于新政策的解读，做个 9:16 头图。"

**项目结构**：
```
my-video/
├── meta.json
├── index.html
├── compositions/
│   ├── overlays.html
│   └── captions.html
└── assets/
```

---

## 五、空白：Blank

**是什么**：**只有脚手架，没有视觉设计**。

**包含**：
- `meta.json`
- `index.html`（空 composition）
- `compositions/captions.html`（字幕）
- `assets/`

📺 **参考视频**：[VFX × HeyGen combined](https://github.com/heygen-com/hyperframes-launches/tree/main/vfx-heygen-combined)（自定义 Three.js + 特效最接近）

**适合**：
- 完完全全自定义设计
- **AI 代理自动生成**（让 AI 从头设计）
- 工程师做精细控制

**典型场景**：
> "我自己做产品发布会，想要公司品牌色 VI 体系完全匹配。"

```bash
npx hyperframes init my-video --example blank
```

---

## 六、决策树：怎么选模板？

按你的**内容类型**选：

```
你的视频是什么？
│
├─ 生活方式 / 品牌片
│   └─ ✅ warm-grain
│
├─ 社交媒体 / 产品发布
│   └─ ✅ play-mode
│
├─ 企业 / 技术
│   └─ ✅ swiss-grid
│
├─ 标题 / 章节切换
│   └─ ✅ kinetic-type
│
├─ 教程 / 流程
│   └─ ✅ decision-tree
│
├─ 产品 demo
│   └─ ✅ product-promo
│
├─ 数据可视化
│   └─ ✅ nyt-graph
│
├─ 竖屏公告
│   └─ ✅ vignelli
│
└─ 完全自定义
    └─ ✅ blank
```

---

## 七、模板对应场景速查

| 我要做... | 用这个模板 |
|---|---|
| 公众号深度长文配视频 | `warm-grain` |
| 抖音 / 小红书短视频 | `play-mode` 或 `vignelli` |
| 公司 B 端宣传片 | `swiss-grid` |
| 课程章节标题动画 | `kinetic-type` |
| 教学流程演示 | `decision-tree` |
| App / 工具发布 | `product-promo` |
| 数据新闻 / 行业报告 | `nyt-graph` |
| 重大通知 / 公告 | `vignelli` |
| 自由设计 / 品牌定制 | `blank` |

---

## 八、自定义模板

你也可以**自己造模板**！

**3 个最低要求**：
1. `index.html` 含 `data-composition-id` 根元素
2. GSAP timeline 注册到 `window.__timelines`
3. 资源放在同目录或子目录

**最简骨架**：

```html
<div id="root" data-composition-id="my-template"
     data-start="0" data-width="1920" data-height="1080">

  <!-- 你的设计 -->

  <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
  <script>
    const tl = gsap.timeline({ paused: true });
    // 加你的动画...
    window.__timelines = window.__timelines || {};
    window.__timelines["my-template"] = tl;
  </script>
</div>
```

**验证模板**：
```bash
npx hyperframes lint
```

---

## 九、实战举例

### 例 1：做一份 SaaS 产品的发布视频

```bash
npx hyperframes init my-launch --example product-promo
cd my-launch
npx hyperframes preview
```

打开浏览器 → 改 `compositions/scene1-logo-intro.html` 里的 Logo 文字 → 保存 → **自动热重载**。

### 例 2：做一段 30 秒的数据新闻

```bash
npx hyperframes init data-story --example nyt-graph --non-interactive
cd data-story
# 编辑 nyt-chart.html，改成你自己的数据
npx hyperframes render --output data-story.mp4
```

### 例 3：AI 代理全自动出片

```bash
npx hyperframes init ai-video --example blank
# 把这个项目路径丢给 Claude Code：
# "用 /hyperframes 给我做一段 15 秒的产品介绍"
```

**AI 知道每个模板的结构和约定，一次就生成正确**。

---

## 十、📺 看真实视频（Showcase 案例）

光看模板名字看不出效果？直接看 **HeyGen 官方用 HyperFrames 做的 5 个真实 launch 视频**——每个都对应不同的视觉风格：

### 🎬 5 个 launch 视频（直接看效果）

| # | 视频 | 时长 | 风格特征 | 适合参考的模板 |
|---|---|---|---|---|
| 1 | **[HyperFrames launch](https://github.com/heygen-com/hyperframes-launches/tree/main/hyperframes-launch)** | 49.7s | 玻璃框架开场 + CSS/GSAP/Lottie/shader/Three.js 完整叙事 | `product-promo` + 多种混合 |
| 2 | **[Website → HyperFrames](https://github.com/heygen-com/hyperframes-launches/tree/main/website-to-hyperframes)** | 41.8s | 抓取网站 → AI 转视频 | `nyt-graph` / `play-mode` |
| 3 | **[Timeline Editor launch](https://github.com/heygen-com/hyperframes-launches/tree/main/timeline-launch)** | 60fps | UI 模拟 + 镜头拉近 + 故事线 | `swiss-grid` / `product-promo` |
| 4 | **[Texture launch](https://github.com/heygen-com/hyperframes-launches/tree/main/texture-launch-video)** | - | 纹理遮罩 + shader 背景 + 标题系统 | `kinetic-type` |
| 5 | **[VFX × HeyGen combined](https://github.com/heygen-com/hyperframes-launches/tree/main/vfx-heygen-combined)** | - | Three.js + HTML 嵌入 canvas + 特效链 | `product-promo` / 自定义 |

> **怎么看？** 仓库里有渲染好的 MP4 文件 + 源代码 + STORYBOARD/DESIGN/HANDOFF 文档。
> 复制链接 → GitHub 仓库 → 找到对应的项目目录 → `assets/` 里有成品视频。

### 🌐 Community Playground（社区项目）

[hyperframes.dev](https://www.hyperframes.dev/) 是官方**社区预览平台**：

- 看别人做的 HyperFrames 视频
- 一键打开在浏览器里编辑
- 分享你自己的项目
- 直接渲染 MP4

**这是**最直接的"参考视频"来源**——比官方 examples 丰富 100 倍**。

### 🗂 Launch Videos 深度解析

- **[Showcase 视觉画廊](https://hyperframes.mintlify.app/showcase)**：看效果
- **[Launch Videos 制作笔记](https://hyperframes.mintlify.app/launch-videos)**：看代码 + 设计稿 + 故事板
- **[Source 仓库](https://github.com/heygen-com/hyperframes-launches)**：5 个完整项目源码

### ⚠️ 注意

9 个 examples 是**脚手架模板**（结构 + 配置），不是成品视频。  
5 个 launch 视频是**完整产品**（可以直接看效果）。

**两者关系**：
- examples = 毛坯房（自己装修）
- launch 视频 = 样板间（看效果再决定装什么风格）

---

## 十一、总结

Hyperframes 提供 **8 个成品模板 + 1 个空白脚手架**：

- **生活/品牌** → `warm-grain`
- **社交/活力** → `play-mode`
- **企业/技术** → `swiss-grid`
- **文字/标题** → `kinetic-type`
- **流程/教程** → `decision-tree`
- **产品/商业** → `product-promo`
- **数据/编辑** → `nyt-graph`
- **竖屏/公告** → `vignelli`
- **完全自定义** → `blank`

**一行命令换风格**：
```bash
npx hyperframes init my-video --example <name>
```

**覆盖了 80% 的视频场景**——剩下 20% 用 `blank` 自由发挥。

不是"剪映替代品"，是"**结构化的视频创作框架**"。

**科技不高冷，AI 很好用。**
我是晚枫，关注我，带你一起玩 AI！

💬 **来评论区聊聊**

你做过哪类视频最多？哪个模板最戳你？
你希望官方再加什么样的模板？

---

## 🔗 快速链接

- 📖 官方 Examples：https://hyperframes.mintlify.app/examples
- 📖 Quickstart（上一篇教程）：https://hyperframes.mintlify.app/quickstart
- 💻 GitHub：https://github.com/heygen-com/hyperframes
- 🎬 Showcase：https://hyperframes.mintlify.app/showcase
- 🚀 Launch Videos：https://hyperframes.mintlify.app/launch-videos

---

*本文基于 Hyperframes 官方 Examples 文档（2026-06）整理。*

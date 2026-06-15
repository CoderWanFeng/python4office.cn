---
title: 2 分钟出第一个 AI 视频：Hyperframes 入门指南
date: 2026-06-15 22:30:00
tags: [Hyperframes, AI视频, AI Skills, 视频生成, 程序员晚枫]
categories: [AI Skills, 平台攻略]
cover: https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?q=80&w=1200&auto=format&fit=crop
---


大家好，我是程序员晚枫。

今天给大家介绍一个让我眼前一亮的工具——**Hyperframes**。

它做的事情很简单，也很颠覆：

> **用 HTML 写一个页面，就能渲染成 MP4 视频。**

而且全程有 AI 辅助，2 分钟出第一个视频。

---

## 一、Hyperframes 是什么？

**一句话**：用 HTML + AI 生成视频的工具。

跟你想过的视频创作方式都不同：

| 你熟悉的 | Hyperframes |
|---|---|
| 剪映/PR 拖时间线 | 写 HTML 标签 |
| 学 Keyframe 动画 | 用 GSAP 写 timeline |
| 调一帧调半天 | 改 HTML 立刻热重载 |
| 渲染慢、卡电脑 | `npx render` 一行命令出 MP4 |

本质上，**Hyperframes 把"做视频"变成了"写网页"**。

---

## 二、两种上手方式

Hyperframes 给了两条路：

### 路径 A：AI 代理模式（推荐）⭐

安装一组 skills，你就能在 Claude Code / Cursor / Codex 里**用自然语言出视频**。

```bash
npx skills add heygen-com/hyperframes
```

装完后，你会得到这些斜杠命令（以 Claude Code 为例）：

| 命令 | 干什么的 |
|---|---|
| `/hyperframes` | 写视频结构（composition）|
| `/hyperframes-cli` | init / lint / preview / render |
| `/hyperframes-media` | 资产预处理：TTS、字幕、抠图 |
| `/tailwind` | `init --tailwind` 项目 |
| `/gsap` | 时间轴动画 |
| `/lottie` `/three` `/waapi` | 其他动画库 |

**意味着**：你只要说"给我做一个 10 秒的产品开场动画"，AI 帮你搞定一切。

### 路径 B：手动模式

不用 AI，自己 `init` + `edit` + `render`。

适合想学原理、或者做精细控制的同学。

下面我两条路都讲一下。

---

## 三、路径 A 实操：AI 代理模式

### 1. 装 skills

```bash
npx skills add heygen-com/hyperframes
```

### 2. 试一下这些 prompt

复制任意一条到你的 AI 代理（Claude Code、Cursor、Codex 都行）：

**冷启动**（从头描述）：
```
用 /hyperframes 给我做一个 10 秒的产品开场动画：
深色背景，淡入标题，加点轻音乐。
```

**热启动**（基于已有素材）：
```
看看这个 GitHub 仓库 https://github.com/heygen-com/hyperframes
用 /hyperframes 介绍它的用途和架构，45 秒讲完。

把这个 PDF 总结成 45 秒的推介视频，用 /hyperframes。

把这个 CSV 做成一个会动的柱状图比赛动画，用 /hyperframes。
```

**格式控制**：
```
用 /hyperframes 做一个 9:16 的 TikTok 风格钩子视频，主题是 [xxx]，
要有弹跳的字幕，跟 TTS 旁白同步。
```

**迭代**（像跟剪辑师对话）：
```
把标题放大 2 倍，换成深色模式，结尾加个淡出。

在 0:03 那里加个 lower third，写上我的名字和职位。
```

AI 会帮你搞定 scaffolding、动画、渲染。**你只管"想视频"，它负责"做视频"**。

---

## 四、路径 B 实操：手动模式

### 第 0 步：准备环境

| 工具 | 版本 | 作用 |
|---|---|---|
| **Node.js** | 22+ | 跑 CLI 和 dev server |
| **FFmpeg** | 7+ | 本地视频编码 |
| **npm / bun** | 最新 | 包管理 |

**macOS**：
```bash
brew install ffmpeg
node --version  # 应 >= 22
ffmpeg -version  # 应输出 7.x
```

**Ubuntu/Debian**：
```bash
sudo apt update && sudo apt install -y ffmpeg
```

### 第 1 步：脚手架

```bash
npx hyperframes init my-video
cd my-video
```

会启动一个交互式向导，帮你选模板、导入媒体。

**跳过交互（CI / AI 代理友好）**：
```bash
npx hyperframes init my-video --non-interactive --example blank
```

**带已有视频**（自动转字幕）：
```bash
npx hyperframes init my-video --example warm-grain --video ./intro.mp4
```

生成的结构：
```
my-video/
├── meta.json             # 项目元信息
├── index.html            # 入口 composition
├── compositions/         # 子 composition
│   ├── intro.html
│   └── captions.html
└── assets/               # 视频/音频/图片
```

### 第 2 步：浏览器预览

```bash
npx hyperframes preview
```

会自动打开 Hyperframes Studio，**支持热重载**——改 `index.html` 立刻看到效果。

### 第 3 步：编辑 composition

最简版 HTML：

```html
<div id="root" data-composition-id="my-video"
     data-start="0" data-width="1920" data-height="1080">

  <!-- 1. 一个 5 秒的标题文字片段 -->
  <h1 id="title" class="clip"
      data-start="0" data-duration="5" data-track-index="0"
      style="font-size: 72px; color: white; text-align: center;
             position: absolute; top: 50%; left: 50%;
             transform: translate(-50%, -50%);">
    Hello, Hyperframes!
  </h1>

  <!-- 2. 加载 GSAP -->
  <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>

  <!-- 3. 创建暂停的时间轴并注册 -->
  <script>
    const tl = gsap.timeline({ paused: true });
    tl.from("#title", { opacity: 0, y: -50, duration: 1 }, 0);
    window.__timelines = window.__timelines || {};
    window.__timelines["my-video"] = tl;
  </script>
</div>
```

### 第 4 步：渲染 MP4

```bash
npx hyperframes render --output output.mp4
```

输出：
```
✔ Capturing frames... 150/150
✔ Encoding MP4...
✔ output.mp4 (1920x1080, 5.0s, 30fps)
```

**恭喜，你的第一个视频出来了！**

---

## 五、三条核心规则

不管用 AI 代理还是手动写，记住这三条：

| 元素 | 必需属性 |
|---|---|
| **根元素** | `data-composition-id`、`data-width`、`data-height` |
| **时间片段** | `data-start`、`data-duration`、`data-track-index`、`class="clip"` |
| **GSAP 时间轴** | `{ paused: true }` + 注册到 `window.__timelines` |

漏一个，渲染会报错或视频错位。

---

## 六、为什么用 skills 会更好？

直接让 AI 写 HTML，它大概率会忘加 `class="clip"`，或者时间轴不暂停。

**Skills 编码了 Hyperframes 的"内部约定"**：
- 必需的 `class="clip"`
- GSAP timeline 注册方式
- 适配器注册（如 `window.__hfLottie`）
- `data-*` 属性语义

**装了 skills，AI 一次就写对；不装，调试 5 次起步。**

---

## 七、依赖速查

| 依赖 | 必需？ | 说明 |
|---|---|---|
| Node.js 22+ | ✅ | CLI 和 dev server 运行时 |
| npm 或 bun | ✅ | 包管理 |
| FFmpeg | ✅ | 视频编码 |
| Docker | ❌ | 可选，做确定性/可复现的渲染 |

---

## 八、下一步

- 📚 **Catalog**：50+ 现成组件（转场、叠加、数据可视化、特效）
- 🎬 **GSAP 动画**：淡入、滑动、缩放、自定义动画
- 🎁 **Examples**：从 Warm Grain、Swiss Grid 这些模板开始
- 🚀 **Rendering**：质量预设、Docker 模式、GPU 加速

---

## 总结

Hyperframes = **用 AI + HTML 做视频**。

- 想快速出片？**装 skills，AI 代理帮你做**
- 想搞懂原理？**手动 init + edit + render**
- 不管哪条路，**2 分钟出第一个 MP4**

不是"剪映替代品"，是"**视频创作的新姿势**"。

**科技不高冷，AI 很好用。**
我是晚枫，关注我，带你一起玩 AI！

💬 **来评论区聊聊**

你试过哪些 AI 视频工具？跟 Hyperframes 比起来怎么样？
你最想用 AI 做什么类型的视频？

---

## 🔗 快速链接

- 📖 官方文档：https://hyperframes.mintlify.app
- 💻 GitHub 仓库：https://github.com/heygen-com/hyperframes
- ⚡ Skills 安装：`npx skills add heygen-com/hyperframes`
- 📝 Prompting 指南：https://hyperframes.mintlify.app/guides/prompting

---

*本文基于 Hyperframes 官方 Quickstart 文档（2026-06）整理。*

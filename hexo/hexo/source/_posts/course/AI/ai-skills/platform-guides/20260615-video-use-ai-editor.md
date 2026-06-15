---
title: video-use 入门指南：和 Claude Code 聊天，就把视频剪好了
date: 2026-06-15 22:55:00
tags: [video-use, AI视频编辑, browser-use, Claude Code, AI Skills, 程序员晚枫]
categories: [AI Skills, 平台攻略]
cover: https://images.unsplash.com/photo-1626785774573-4b799315345d?q=80&w=1200&auto=format&fit=crop
---


大家好，我是程序员晚枫。

如果说 **videocut-skills** 是"剪中文口播"专精，那今天介绍的这个——**video-use**——就是**通用视频剪辑的全自动 Agent**。

**一句话**：

> **把素材丢进文件夹，跟 Claude Code 聊几句，它给你 `final.mp4`。**

---

## 一、video-use 是什么？

来自 **browser-use 团队**（对，就是那个让 AI 操控浏览器的）的开源项目。

**完全本地运行**、**完全免费**、**完全对话式**。

| 工具 | 类型 | 怎么用 |
|---|---|---|
| 剪映 | 桌面软件 | 拖时间线 |
| Premiere | 桌面软件 | 拖时间线 |
| **video-use** | **AI Agent** | **跟 AI 聊天** |

**完全不同的剪辑范式**。

---

## 二、它能做什么？

来自官方 README：

- ✂️ **剪掉语气词**（umm、uh、false starts）和镜头间隙
- 🎨 **自动调色**（暖色电影感 / 中性清晰 / 自定义 ffmpeg 链）
- 🔊 **30ms 音频淡入淡出**（避免爆音）
- 📝 **烧录字幕**（2 词一组、全大写默认，可定制）
- 🎬 **生成动画叠加**（通过 HyperFrames / Remotion / Manim / PIL，并行子代理）
- 🔍 **自评估渲染输出**（每个剪辑点检查跳切、爆音）
- 💾 **会话记忆**（`project.md` 持久化，下次接着上次的）

**这不是个工具，是个完整的 AI 剪辑师**。

---

## 三、双层读取系统（核心创新）

video-use **不让 LLM 真的"看"视频**——视频太长了，token 不够。

它用的是**双层读取**：

### Layer 1：音频转录（始终加载）

ElevenLabs Scribe 一次调用 → 拿到：

- 字级时间戳
- 说话人分离
- 音频事件（`(laughter)`、`(applause)`、`(sigh)`）

打包成 ~12KB 的 `takes_packed.md`——**LLM 的主要阅读视图**：

```markdown
## C0103 (duration: 43.0s, 8 phrases)
[002.52-005.36] S0 Ninety percent of what a web agent does is completely wasted.
[006.08-006.74] S0 We fixed this.
```

### Layer 2：视觉合成（按需调用）

`timeline_view` 工具生成**胶片条 + 波形 + 字标签的 PNG**——任何时间段都行。

只在**决策点**调用（歧义停顿、镜头对比、剪辑点 sanity check）。

### 数据对比

| 方案 | Token 消耗 |
|---|---|
| 朴素方法：30,000 帧 × 1,500 token | **45M token**（噪音）|
| video-use：12KB 文本 + 几张 PNG | **12KB + 几张图** |

**和 browser-use 给 LLM 一个结构化 DOM 而不是截图，是同样的思路**——只不过用在视频上。

---

## 四、Pipeline：5 步全自动

```
Transcribe ──> Pack ──> LLM Reasons ──> EDL ──> Render ──> Self-Eval
                                              │
                                              └─ issue? fix + re-render (max 3)
```

每一步：
1. **Transcribe**：ElevenLabs 转录音频
2. **Pack**：打包成 12KB 文本
3. **LLM Reasons**：AI 分析要剪哪里
4. **EDL**：生成剪辑决策表
5. **Render**：FFmpeg 渲染
6. **Self-Eval**：自评估每个剪辑点（发现问题自动重渲，最多 3 次）

**你看到的预览，是通过自评估的版本**。

---

## 五、3 步快速开始

### 第 1 步：一句话让 AI 装好

把这个 prompt 丢给 Claude Code / Codex / Hermes：

```
Set up https://github.com/browser-use/video-use for me.

Read install.md first to install this repo, wire up ffmpeg, 
register the skill with whichever agent you're running under, 
and set up the ElevenLabs API key — ask me to paste it when 
you need it. Then read SKILL.md for daily usage, and always 
read helpers/ because that's where the editing scripts live. 
After install, don't transcribe anything on your own — just 
tell me it's ready and wait for me to drop footage into a folder.
```

**AI 会自动**：
- Clone 仓库
- 装 ffmpeg / 依赖
- 注册 Skill 到你的 AI 代理
- 提示你输入 ElevenLabs API Key

### 第 2 步：丢素材 + 聊天

```bash
cd /path/to/your/videos
claude   # 启动 Claude Code
```

在对话里说：

```
edit these into a launch video
```

AI 会：
- 列出所有素材
- 提出剪辑策略
- 等你 OK
- 生成 `edit/final.mp4`

**所有产物都在 `<videos_dir>/edit/`，skill 目录保持干净**。

### 第 3 步（可选）：手动安装

如果你想自己掌控：

```bash
# 1. 克隆 + 软链到 agent skills 目录
git clone https://github.com/browser-use/video-use ~/Developer/video-use
ln -sfn ~/Developer/video-use ~/.claude/skills/video-use   # Claude Code
# ln -sfn ~/Developer/video-use ~/.codex/skills/video-use  # Codex

# 2. 装依赖
cd ~/Developer/video-use
uv sync   # 或：pip install -e .
brew install ffmpeg
brew install yt-dlp   # 可选：下载在线素材

# 3. 填 ElevenLabs API Key
cp .env.example .env
$EDITOR .env   # 填 ELEVENLABS_API_KEY=...
```

---

## 六、5 条设计原则

来自官方 README：

1. **文本 + 按需视觉**。不堆帧。转录是主视图。
2. **音频优先，画面跟随**。剪辑点从语音边界和静音挑。
3. **问 → 确认 → 执行 → 自评估 → 持久化**。绝不没经你同意就剪。
4. **对内容类型零假设**。先看、先问、再剪。
5. **12 条硬规则 + 创意自由**。生产正确性不妥协；艺术感觉可以发挥。

---

## 七、支持的动画叠加

video-use 可以**并行生成动画**叠加到视频里：

| 工具 | 类型 | 适合 |
|---|---|---|
| **[HyperFrames](https://github.com/heygen-com/hyperframes)** | HTML → MP4 | 标题/转场 |
| **[Remotion](https://www.remotion.dev/)** | React → MP4 | 数据可视化 |
| **[Manim](https://www.manim.community/)** | Python 数学动画 | 公式/几何 |
| **PIL** | Python 图像库 | 简单文字/水印 |

**每个动画在并行子代理里跑**，AI 自动协调。

---

## 八、典型应用场景

来自官方 README：

- **知识博主量产**：每周 3 期口播，AI 帮你剪
- **产品更新视频 CI/CD**：每次 release 自动生成视频 changelog
- **播客剪辑**：多人对话，自动切说话人
- **采访剪辑**：自动去掉 Q/A 之间的停顿
- **Vlog 整理**：一天素材 → 1 分钟精华
- **Telegram/VPS 常驻编辑**：[Browser Use Box](https://browser-use.com/bux) 7×24 自动剪

---

## 九、依赖速查

| 依赖 | 必需？ | 说明 |
|---|---|---|
| **FFmpeg** | ✅ | 音视频处理 |
| **ElevenLabs API Key** | ✅ | 语音转录（[申请](https://elevenlabs.io/app/settings/api-keys)）|
| **yt-dlp** | ❌ | 可选，下载在线素材 |
| **Docker** | ❌ | 可选，确定性渲染 |

---

## 十、与 videocut-skills 对比

| 维度 | **video-use** | **videocut-skills** |
|---|---|---|
| **擅长** | 通用视频（采访/Vlog/口播）| 中文口播 |
| **转录** | ElevenLabs Scribe（云端）| 火山引擎 ASR（云端）|
| **核心** | LLM 决策 + 自评估 | 8 条规则 + 词典纠错 |
| **语言** | 英文优先（多语言支持）| 中文优先 |
| **价格** | ElevenLabs 收费（按字符）| 火山引擎收费（按字符）|

**两者不冲突**——中文口播用 videocut-skills，多语言/通用用 video-use。

---

## 常见问题

### Q: 不联网能用吗？

**不能**。需要 ElevenLabs API 做转录。

### Q: 多长视频能处理？

理论上**无限**——但越长的视频，AI 决策时间越长（几十分钟到几小时）。

### Q: 自评估会卡住吗？

最多 3 次重渲，如果 3 次都不过会停下来报告问题。

### Q: 怎么自定义字幕样式？

编辑 `helpers/` 里的脚本，或者改 SKILL.md 里的硬规则。

---

## 总结

video-use = **跟 AI 聊天，就把视频剪了**。

- **零学习成本**：会跟 AI 说话就行
- **全自动 Pipeline**：转录 → 决策 → 渲染 → 自评估
- **12KB 文本 + 几张图**搞定 1 小时视频
- **支持动画叠加**（HyperFrames / Remotion / Manim）

不是"剪映替代品"，是"**AI 时代的视频剪辑师**"。

**科技不高冷，AI 很好用。**
我是晚枫，关注我，带你一起玩 AI！

💬 **来评论区聊聊**

你愿意让 AI 帮你剪视频吗？
你最希望 AI 帮你自动化哪些剪辑工作？

---

## 🔗 快速链接

- 💻 GitHub：https://github.com/browser-use/video-use
- 📖 SKILL.md：https://github.com/browser-use/video-use/blob/main/SKILL.md
- 📖 install.md：https://github.com/browser-use/video-use/blob/main/install.md
- 🔑 ElevenLabs API：https://elevenlabs.io/app/settings/api-keys
- 🎬 Browser Use Box：https://browser-use.com/bux

---

*本文基于 video-use 官方 README（2026-06）整理。*

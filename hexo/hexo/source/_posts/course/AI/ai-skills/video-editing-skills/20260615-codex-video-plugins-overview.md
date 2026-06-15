---
title: 和 CodeX 聊个天，就把视频剪好了
date: 2026-06-15 23:30:00
tags: [Codex, AI视频， HyperFrames, Remotion, HeyGen, videocut-skills, video-use, AI Skills, 程序员晚枫]
categories: [AI Skills, 平台攻略]
cover: https://images.unsplash.com/photo-1611162616475-46b635cb6868?q=80&w=1200&auto=format&fit=crop
---


大家好，我是程序员晚枫。

最近 **Codex 视频插件**爆火了。

我也用它剪了一个视频，我感觉效果非常惊艳！

- 插入视频

身边好几个朋友都在问：

> "晚枫，HyperFrames、Remotion、HeyGen、videocut-skills、video-use……这些插件我都看到过，**到底应该用哪个？**"

今天一篇文章，把 **5 大主流 Codex 视频插件**讲清楚——**适合什么人、能做什么、怎么选、怎么装**。

---

## 一、5 个插件速览

| # | 插件 | 核心定位 | 一句话总结 |
|---|---|---|---|
| 1 | **HyperFrames** ⭐ 最火 | 用 HTML 做视频 | 让 AI 写 HTML/CSS/JS，渲染出 MP4 |
| 2 | **Remotion** | 用 React 做视频 | 工程化批量生成，1 模板 100 视频 |
| 3 | **HeyGen** | 数字人 + 全流程 | 配音、字幕、数字人、剪辑全自动 |
| 4 | **videocut-skills** | 中文口播专精 | AI 识别口误、停顿、重复句 |
| 5 | **video-use** | 多素材混合 | 多种素材自动混剪 |

---

## 二、HyperFrames（最火、核心推荐）⭐

**热度最高的视频插件**——4 月 28 日正式成为 Codex 官方插件，支持一键安装。

**核心逻辑**：AI 写 HTML/CSS/JS → 渲染成 MP4。

**为什么火**：
- HeyGen 出品（AI 视频界顶流）
- HTML 是程序员都懂的"原料"
- AI 代理（Codex / Claude Code / Cursor）写 HTML 比写 React 容易
- 9 个内置模板（暖色电影、瑞士网格、动感、数据图、竖屏...）

**适合**：
- ✓ 创意动画
- ✓ 知识卡片
- ✓ 产品宣传片
- ✓ 短视频动画
- ✓ 标题/转场/章节切换

**典型 prompt**：
```
@HyperFrames 给我做一段 10 秒的产品发布动画，深色背景，
标题淡入"AI 让一切重新发明"。
```

📺 [看 HyperFrames 真实效果：https://hyperframes.mintlify.app/showcase](https://hyperframes.mintlify.app/showcase)

📖 [Hyperframes 入门指南：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-quickstart/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-quickstart/)
� [9 大模板详解：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-templates-and-styles/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-templates-and-styles/)

---

## 三、Remotion（工程化批量生成）

**与 HyperFrames 齐名**——一样强大，只是"配方"不同。

**核心逻辑**：AI 写 React 组件 → 渲染成 MP4。

**为什么用 React 而不是 HTML**：
- 类型安全：props + TypeScript
- 工程化：复用组件、单元测试
- 批量化：1 模板 + 100 数据 = 100 视频
- 可控性强：精确到每一帧

**适合**：
- ✓ 模板化视频（每周固定栏目）
- ✓ 数据可视化排行榜（"百度热搜每日 TOP 10"）
- ✓ 每日资讯栏目
- ✓ 个性化营销（每个用户专属视频）
- ✓ GitHub 年度回顾这种"几百万人定制"的场景

**典型 prompt**：
```
@Remotion 用 React 给我做一段 30 秒的销售排行榜动画，
每年柱状图从下往上长出来，配数字滚动效果。
```

📺 真实案例：[Remotion Showcase（GitHub Unwrapped、Submagic、Hackreels...）：https://www.remotion.dev/showcase](https://www.remotion.dev/showcase)
📖 [Remotion React 视频框架入门：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-remotion-react-video-framework/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-remotion-react-video-framework/)

---

## 四、HeyGen（数字人 + 全流程）

不是"视频生成框架"——是**完整的 AI 视频制作平台**。

**核心能力**：
- 🤖 **数字人生成**（口型同步、动作自然）
- 🎙 **AI 配音**（多语言、多音色）
- 📝 **自动字幕**
- ✂️ **自动剪辑**
- 🎬 **场景合成**

**适合**：
- ✓ 想拍视频但**不想出镜**
- ✓ 想做**多语言版本**（一段中文 → 自动翻译 + 配音 + 数字人多语种版）
- ✓ 完整全流程（不只是"动画"或"剪辑"，是"从 0 到成片"）
- ✓ 营销视频、企业培训、产品介绍

**典型 prompt**：
```
@HeyGen 用我的数字人形象，把这段文字"AI 时代的商业机会..."
做成 60 秒中英双语视频。
```

⚠️ 注意：HeyGen 的核心是**云端 SaaS**，Codex 插件是 API 调用接口。

🌐 官网：https://www.heygen.com

---

## 五、videocut-skills（中文口播专精）

**唯一专门为中文口播设计**的视频剪辑插件。

**核心能力**：
- ✂️ **AI 识别口误**（说错后自动纠正）
- 🤐 **删除停顿**（>0.3s 自动标记，可调阈值）
- 🔁 **去除重复句**（"我们今天讲的是、我们今天讲的是" → 删前保后）
- 📝 **专业术语词典**（Claude Code 不再被识别成 cloud code）
- 💡 **自更新**（记住你的偏好，越用越准）

**适合**：
- ✓ 中文口播 UP 主
- ✓ 知识博主（有大量"嗯/啊/那个"语气词）
- ✓ 直播切片二次加工
- ✓ 课程录制后的精剪

**典型用法**：
```bash
# 在 Codex / Claude Code 里
/videocut:剪口播 我的录像.mp4
```

AI 自动：转录 → 识别问题 → 你审核 → 一键剪辑。

📖 [videocut-skills 入门指南：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-videocut-skills-tutorial/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-videocut-skills-tutorial/)

---

## 六、video-use（多素材混合）

来自 **browser-use 团队**的开源项目——和 videocut-skills 互补。

**核心能力**：
- 🎬 **多类型素材混剪**（口播 + 录屏 + Vlog + 图片）
- 🎨 **自动调色**
- 🔊 **30ms 音频淡入淡出**
- 📝 **烧录字幕**（2 词一组、全大写默认）
- 🎬 **生成动画叠加**（甚至能调用 HyperFrames / Remotion 做插画动画！）
- 🔍 **自评估**（每个剪辑点检查跳切、爆音）

**适合**：
- ✓ Vlog 整理（一天素材 → 1 分钟精华）
- ✓ 采访 / 播客（多人对话自动切说话人）
- ✓ 产品 demo（口播 + 录屏 + 截图混编）
- ✓ 多语言视频（不只是中文）

**典型 prompt**：
```
@video-use edit these into a launch video.
（看到一堆素材后，自动出片）
```

📺 [TikTok 15 秒官方 Demo：https://www.tiktok.com/@browser_use/video/7639824093721758989](https://www.tiktok.com/@browser_use/video/7639824093721758989)
📖 [video-use 入门指南：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-video-use-ai-editor/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-video-use-ai-editor/)

---

## 七、对比表（一图选型）

| 维度 | HyperFrames | Remotion | HeyGen | videocut-skills | video-use |
|---|---|---|---|---|---|
| **类型** | 框架 | 框架 | SaaS | 剪辑 Agent | 剪辑 Agent |
| **原料** | HTML/CSS/JS | React/TSX | 文字脚本 | 视频文件 | 视频文件 |
| **产物** | MP4 | MP4 | MP4 | 剪辑后 MP4 | 剪辑后 MP4 |
| **适合** | 创意动画 | 批量生成 | 数字人/全流程 | 中文口播 | 多素材混剪 |
| **学习曲线** | ⭐ 简单 | ⭐⭐ 需 React | ⭐ 简单 | ⭐ 简单 | ⭐ 简单 |
| **批量能力** | ⭐⭐ 中 | ⭐⭐⭐ 强 | ⭐⭐ 中 | ⭐ 单视频 | ⭐⭐ 中 |
| **是否要出镜** | 不要 | 不要 | **不要！** AI 数字人 | 要（你的口播）| 要（你的素材） |
| **付费？** | 部分免费 | 部分免费 | 按用量 | 火山引擎 API 收费 | ElevenLabs API 收费 |

---

## 八、决策树：我该用哪个？

```
你的需求是什么？
│
├─ 我想做创意动画 / 知识卡片 / 产品宣传片
│   └─ ✅ HyperFrames
│
├─ 我想做批量化、参数化的系列视频
│   └─ ✅ Remotion（如果会 React）
│      或 HyperFrames（如果只会 HTML）
│
├─ 我不想出镜，但想做有"人"的视频
│   └─ ✅ HeyGen（数字人）
│
├─ 我已经录了中文口播，要去口误/卡顿
│   └─ ✅ videocut-skills
│
├─ 我有一堆杂素材（口播 + 录屏 + Vlog）
│   └─ ✅ video-use
│
└─ 我啥都不会，想最快出片
    └─ ✅ HeyGen（最简单，会打字就行）
```

---

## 九、组合用法（高阶玩家必看）

5 个插件**不冲突**，反而能**串联组合**：

### 组合 1：知识博主完整流程

```
1. videocut-skills 剪掉中文口播的口误/停顿
   ↓
2. HyperFrames 生成知识卡片动画 / 转场
   ↓
3. video-use 把视频 + 卡片 + 字幕全混在一起
   ↓
4. 最终成片
```

### 组合 2：产品发布会

```
1. HeyGen 生成数字人主持开场
   ↓
2. Remotion 生成数据可视化片段
   ↓
3. HyperFrames 生成产品 UI 动画
   ↓
4. video-use 把所有片段缝合成完整发布会视频
```

### 组合 3：每日资讯栏目

```
1. Remotion 写好通用模板（标题、栏目片头/片尾）
   ↓
2. HeyGen 数字人念稿
   ↓
3. 每天传新数据 + 新文案 → 自动出片
```

---

## 十、安装与使用提示

### 1. 在 Codex 安装

> 参考用户提供的安装方式（Codex 实际安装步骤可能因版本变化）

1. 打开 Codex
2. 左侧边栏找 **"插件（Plugins）"**
3. 搜索插件名（如 `HyperFrames`）
4. 点 **"安装"**

### 2. 在新对话中使用

```
@HyperFrames 给我做一段 10 秒产品宣传片
@Remotion 用 React 做一段销售排行榜
@HeyGen 用我的数字人形象做中英双语视频
```

只要 **`@` 后面跟插件名**，AI 自动用对应插件生成视频。

### 3. 命令行模式（Claude Code）

如果你用的是 Claude Code（不是 Codex），上面 5 个插件都支持命令行模式：

```bash
# HyperFrames
npx skills add heygen-com/hyperframes
/hyperframes 做一个产品宣传片

# Remotion
npx skills add remotion-dev/skills
/remotion-cli 做一个数据可视化

# videocut-skills
git clone https://github.com/Ceeon/videocut-skills.git ~/.claude/skills/videocut
/videocut:剪口播 视频.mp4

# video-use
git clone https://github.com/browser-use/video-use ~/.claude/skills/video-use
edit these into a launch video
```

---

## 十一、常见问题

### Q: 5 个都要装吗？

**不用**。先想想"我主要做什么类型的视频"，挑 1-2 个开始。

**新手推荐**：HyperFrames 或 HeyGen（最容易上手）。
**程序员推荐**：HyperFrames 或 Remotion（可控性强）。
**口播 UP 主推荐**：videocut-skills。

### Q: 哪个最贵？

- HeyGen：按订阅或按用量，月度套餐 24-89 美元
- ElevenLabs（video-use 用的）：按字符数收费
- 火山引擎（videocut-skills 用的）：转录按字符数
- HyperFrames / Remotion：开源免费（小公司商用免费）

### Q: 这些插件能在国内用吗？

| 插件 | 国内可用 |
|---|---|
| HyperFrames | ✓ 开源框架，本地跑 |
| Remotion | ✓ 开源框架，本地跑 |
| HeyGen | ⚠️ 海外 SaaS，需要科学上网 |
| videocut-skills | ✓ 火山引擎在国内 |
| video-use | ⚠️ ElevenLabs 海外 SaaS |

### Q: 哪个出片最快？

**HeyGen 最快**——10 分钟从无到有。
**HyperFrames 第二快**——会写 prompt 就行。
**videocut-skills 最稳**——你已经有原片，只是清洗。

---

## 📚 想系统学习 Codex 插件？

如果你看完这篇文章，想要：

- ✓ **从 0 到 1 系统学** Codex 插件的使用
- ✓ 跟着实战案例**做出第一个 AI 视频**
- ✓ 掌握 **5 个插件的组合用法**
- ✓ 学会一套**完整的 AI 视频生产工作流**

欢迎加入我的 **AI 课程**——视频教学 + 实战项目 + 跟着做就上手：

🎓 [程序员晚枫 · AI 课程（B 站）：https://www.bilibili.com/cheese/play/ss982042944](https://www.bilibili.com/cheese/play/ss982042944)

课程内容覆盖 Codex 插件、HyperFrames / Remotion / HeyGen / videocut-skills / video-use 等热门工具的实战用法，**从入门到精通**。

---

## 总结

5 个 Codex 视频插件 = **5 种创作姿势**：

- **创意动画** → HyperFrames
- **批量生产** → Remotion
- **不想出镜** → HeyGen
- **中文口播** → videocut-skills
- **多素材混剪** → video-use

它们**不是替代关系**——是**互补**。

最强的玩家**组合用**——HeyGen 出数字人 + HyperFrames 出动画 + Remotion 出数据图 + video-use 缝合。

最弱的玩家**单点用**——挑一个最匹配你需求的，先把第一个视频做出来。

**科技不高冷，AI 很好用。**
我是晚枫，关注我，带你一起玩 AI！

💬 **来评论区聊聊**

你最想试哪个插件？
你做的什么类型视频最多？

---

## 🔗 快速链接（5 篇深度教程）

- 📖 [HyperFrames 入门指南：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-quickstart/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-quickstart/)

- 📖 [HyperFrames 9 大模板详解：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-templates-and-styles/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-templates-and-styles/)

- 📖 [Remotion 入门指南：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-remotion-react-video-framework/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-remotion-react-video-framework/)

- 📖 [videocut-skills 入门指南：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-videocut-skills-tutorial/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-videocut-skills-tutorial/)

- 📖 [video-use 入门指南：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-video-use-ai-editor/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-video-use-ai-editor/)

## 🌐 官方资源

- HyperFrames：https://hyperframes.mintlify.app
- Remotion：https://www.remotion.dev/
- HeyGen：https://www.heygen.com
- videocut-skills：https://github.com/Ceeon/videocut-skills
- video-use：https://github.com/browser-use/video-use
- Codex 插件市场：在 Codex 应用内的「Plugins」入口

---

*本文基于 5 个项目官方文档（2026-06）整理。*

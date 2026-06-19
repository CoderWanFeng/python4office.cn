---
title: Skill 文章创作指南：晚枫 7 步写作法
date: 2026-06-16 06:33:55
tags: [写作方法, AI Skills, 内容创作, SOP, 程序员晚枫]
categories: [AI Skills, 写作指南]
cover: https://images.unsplash.com/photo-1455390582262-044cdead277a?q=80&w=1200&auto=format&fit=crop
---


这是一份**给自己用的 Skill 文章写作 SOP**——以后写任何"AI 工具/插件介绍"类文章都按这个走。

基于刚写的 6 篇 Codex 视频插件文章（Hyperframes / Remotion / videocut-skills / video-use 等）总结而来。

---

## 一、文章定位：Skill 类文章解决什么？

写 Skill 类文章的**唯一目标**：

> **让一个之前没听过这个工具的读者，看完文章后能上手用。**

不是夸夸其谈、不是堆砌特性、不是搬官方文档——**让人会用**。

---

## 二、🎯 7 步写作框架

每篇 Skill 文章按这 7 步写，结构稳定：

```
1. 开篇钩子（30 秒抓住读者）
   ↓
2. 是什么（一句话定位）
   ↓
3. 为什么用（痛点 + 价值）
   ↓
4. 快速开始（3 步出第一个产品）
   ↓
5. 核心规则 / API 速查（表格化）
   ↓
6. 实战场景（多场景 + 真实案例）
   ↓
7. 决策对比 + FAQ + 总结 + 链接
```

---

## 三、每一步的具体要求

### 第 1 步：开篇钩子（30 秒）

**标准开头**：
```
大家好，我是程序员晚枫。

今天给大家介绍一个 [让我眼前一亮 / 让我兴奋] 的工具——**XXX**。

它做的事情很 [简单 / 颠覆 / 不可思议]：

> **一句话总结这个工具最牛的能力。**

[一句话感叹 / 反常识陈述]
```

**避免**：
- ❌ 长篇背景介绍
- ❌ 复制粘贴官方介绍
- ❌ 立刻进入技术细节

**好例子**：
```
今天给大家介绍一个让 React 工程师兴奋的工具——Remotion。

它做的事情很颠覆：

> 写 React 组件，渲染出 MP4 视频。
```

### 第 2 步：是什么（一句话定位）

**标准模板**：
```
## 一、XXX 是什么？

**一句话**：[最简单的描述]。

跟你想过的 [类似产品 / 传统方案] 都不同：

| 你熟悉的 | XXX |
|---|---|
| [传统方式 1] | [新方式 1] |
| [传统方式 2] | [新方式 2] |
| ... | ... |

**本质上**：[核心创新点]。
```

**关键**：用对比表突出"差异"，而不是"特性堆叠"。

### 第 3 步：为什么用（痛点 + 价值）

**列出 3-5 个用户痛点**——尽量是读者真实遇到过的。

**模板**：
```
## 二、为什么值得用？

### 1. [痛点关键词]（杀手锏）

[痛点描述]
[这个工具怎么解决]

**传统方式**：[痛苦的过程]
**XXX**：[轻松的过程]

### 2. [另一个痛点关键词]

...
```

**好例子**（来自 Remotion 文章）：
```
### 1. 批量生成（杀手锏）

写一个"GitHub 贡献墙"模板 → 传 100 个用户名 → 一键出 100 个个性化视频。

传统方式：100 个视频做 100 次。
Remotion：1 个模板 + 100 次 API 调用 = 100 个视频。
```

### 第 4 步：快速开始（3 步上手）

**这是文章最重要的部分**——读者看完这部分能动手。

**标准 3 步结构**：

```
## 三、上手：3 步出第一个 [产品]

### 第 1 步：脚手架 / 装环境

[一行命令]

[显示生成的目录结构]

### 第 2 步：写第一个 Hello World

[完整可复制的代码]

### 第 3 步：[渲染 / 运行 / 部署]

[一行命令]
[显示输出]

**恭喜，你的第一个 [产品] 出来了！**
```

**关键**：
- 代码要**完整可复制**（不要 `// ... 省略`）
- 命令要**带前缀**（`$` 或 `npm` 等，让人知道在哪跑）
- 每步**不超过 5 个动作**

### 第 5 步：核心规则 / API 速查（表格化）

用**表格**展示关键规则——让 AI 也能查得到。

**模板**：
```
## 五、核心 API 速查

| API | 干什么 |
|---|---|
| `useCurrentFrame()` | 拿当前帧数 |
| `interpolate(...)` | 帧数 → 任意值的线性映射 |
| ... | ... |
```

或者：

```
## 五、三条核心规则

不管用 AI 还是手动，记住这三条：

| 元素 | 必需属性 |
|---|---|
| **根元素** | `data-composition-id`、`data-width`、`data-height` |
| **时间片段** | `data-start`、`data-duration`、`class="clip"` |
| **GSAP 时间轴** | `{ paused: true }` + 注册到 `window.__timelines` |

漏一个，渲染会报错或视频错位。
```

### 第 6 步：实战场景（让读者意识到能干嘛）

**多场景 + 真实案例链接**：

```
## 七、实战场景

| 场景 | 怎么做 | 📺 真实案例 |
|---|---|---|
| 📊 数据可视化 | [简短描述] | [真实案例链接] |
| 📱 个性化营销 | [简短描述] | [真实案例链接] |
| ... | ... | ... |
```

**关键**：每个场景**必须有一个真实案例链接**——光说"能做"没用，让用户**点开看**。

### 第 7 步：决策对比 + FAQ + 总结 + 链接

#### 7.1 决策树 / 对比表

```
## 八、决策树：怎么选？

```
你的需求是什么？
├─ 想做 X → ✅ 用 XXX
├─ 想做 Y → ✅ 用 YYY
└─ 想做 Z → ✅ 用 ZZZ
```
```

#### 7.2 常见问题（4-5 个）

```
## 十、常见问题

### Q: [新手最常问的]
[直接回答]

### Q: [关于性价比的]
[直接回答]
```

#### 7.3 总结（重申核心价值）

```
## 总结

XXX = **[一句话定位]**。

- 想做 A？**[怎么做]**
- 想做 B？**[怎么做]**

不是"剪映替代品"，是"**视频创作的新姿势**"。

**科技不高冷，AI 很好用。**
我是晚枫，关注我，带你一起玩 AI！

💬 **来评论区聊聊**

[1-2 个互动问题]
```

#### 7.4 快速链接（公众号友好格式）

**严格用这种格式**——让 URL 显式可见，公众号能复制：

```
## 🔗 快速链接

- 📖 官方文档：https://example.com
- 💻 GitHub：https://github.com/owner/repo
- ⚡ 安装命令：`npm install xxx`
- 📚 进阶资源：https://example.com/advanced
```

**或者**（带描述的链接，用内嵌 URL 格式）：

```
- 📖 [新手入门：https://example.com/quickstart](https://example.com/quickstart)
- 💻 [GitHub 仓库：https://github.com/owner/repo](https://github.com/owner/repo)
```

**避免**：
- ❌ `[官方文档](URL)` —— 公众号上 URL 看不到，没法复制
- ✅ `[官方文档：URL](URL)` —— URL 直接显示

---

## 四、🎨 写作风格指南（晚枫风格）

### 1. 句子要短

**改前**：
> Remotion 是一个使用 React 框架来制作视频的工具，它通过将视频抽象为 React 组件，让开发者可以利用熟悉的开发体验来生产视频内容。

**改后**：
> Remotion = 用 React 写视频。
>
> 写组件 → 渲染 MP4。

### 2. 多用对比

不说"很强"——说"比 X 强 10 倍"：

| 维度 | A | B |
|---|---|---|
| 速度 | 1 小时 | 5 分钟 |
| 价格 | $100 | $5 |
| 学习 | 1 个月 | 1 天 |

### 3. 多用 emoji 标识符

| Emoji | 含义 |
|---|---|
| 📊 | 数据 |
| 📺 | 视频 |
| 📖 | 文档 |
| 💻 | 代码/GitHub |
| ⚡ | 快速 |
| 🎓 | 课程 |
| 🔗 | 链接 |
| 🌐 | 网站 |
| ⚠️ | 注意 |
| ✅/✓ | 推荐 |
| ❌/✗ | 不推荐 |

### 4. 关键概念用粗体

```
**HTML → MP4** 不是魔法，是 React 渲染。

**核心逻辑**：写组件，得视频。
```

### 5. 引用块（marker）

```
> **重要观察**：这就是为什么 X。
```

### 6. 章节命名风格

| ✅ 推荐 | ❌ 避免 |
|---|---|
| `三、上手：3 步出第一个视频` | `安装方式` |
| `五、核心 API 速查` | `API 列表` |
| `📺 看真实视频` | `示例视频` |

每个章节都让读者知道**能拿走什么**。

### 7. 段落节奏

短段落 + 长段落交替，避免连续 10 行字墙：

```
[一句话短段落]

[3-4 行展开]

[一句话短段落（强调）]
```

---

## 五、📁 文件命名规范

### 文件名格式

```
20260615-插件名-tutorial.md
20260615-插件名-quickstart.md
20260615-插件名-templates-and-styles.md
20260615-插件名-react-video-framework.md
```

**原则**：
- 日期前缀（YYYYMMDD）
- 全英文小写
- 用 `-` 连接
- 包含**插件名**（让 URL 自解释）
- 主题词放后面（quickstart / tutorial / overview / templates）

### Front-matter 模板

```yaml
---
title: [一句话标题，不超过 30 字]
date: 2026-06-15 23:30:00
tags: [插件名, 类别, AI Skills, 程序员晚枫]
categories: [AI Skills, 平台攻略]
cover: https://images.unsplash.com/photo-XXX?q=80&w=1200&auto=format&fit=crop
---
```

**字段说明**：

| 字段 | 必填 | 内容 |
|---|---|---|
| title | ✓ | 一句话标题，含数字/对比/反常识 |
| date | ✓ | **必须用真实当前时间，精确到秒**：`YYYY-MM-DD HH:MM:SS`（用 `date '+%Y-%m-%d %H:%M:%S'` 命令获取，**禁止编 / 估**）|
| tags | ✓ | 4-8 个，含"程序员晚枫"作为作者标签 |
| categories | ✓ | 2 层：[一级分类, 二级分类] |
| cover | ✓ | Unsplash 图，1200×400 或 1200×800 |

> ⚠️ **特别强调 date 字段**：
> - **不要凭感觉写**（比如"差不多 23:50"）
> - **不要复用旧文章的时间**
> - **必须运行 `date '+%Y-%m-%d %H:%M:%S'` 拿到真实时间再填**
> - 这是 hexo 的排序依据，错了就错位

---

## 六、🔗 链接策略

### 内链（指向自己其他文章）

```
📖 [文章标题：完整 URL](完整 URL)
```

**例**：
```
📖 [HyperFrames 入门指南：https://www.python4office.cn/.../quickstart/](https://www.python4office.cn/.../quickstart/)
```

### 外链（指向官方/第三方）

```
- 📖 官方文档：https://example.com
- 💻 GitHub：https://github.com/owner/repo
```

或：
```
[文字描述：完整 URL](完整 URL)
```

### 总原则

**所有链接都要让 URL 显式可见**——避免在公众号等平台复制不了链接。

---

## 七、📺 配图与视频引用

### Cover 图

- 用 [Unsplash](https://unsplash.com)
- 1200×400（横）或 1200×800（高）
- URL 格式：`?q=80&w=1200&auto=format&fit=crop`
- 主题相关（科技、电脑、视频等）

### 文中插图（可选）

- ![描述](URL) 用 Unsplash
- 一篇文章 1-2 张图就够，不要堆砌

### 视频引用

```
📺 [描述：完整 URL](完整 URL)
```

不要嵌入 iframe（hexo + 公众号都不友好）。

---

## 八、📚 课程推广 section（可选）

放在"总结"前，作为文章的最后一个推广点：

```markdown
## 📚 想系统学习 [主题]？

如果你看完这篇文章，想要：

- ✓ 从 0 到 1 系统学
- ✓ 跟着实战案例做
- ✓ 掌握组合用法
- ✓ 学会完整工作流

欢迎加入我的 **AI 课程**：

🎓 [程序员晚枫 · AI 课程（B 站）：https://pan.quark.cn/s/8f7886f79569](https://pan.quark.cn/s/8f7886f79569)
```

---

## 九、✅ 文章质量自查清单

发布前过一遍：

- [ ] **date 字段用真实当前时间**（运行 `date '+%Y-%m-%d %H:%M:%S'` 取，不要估）
- [ ] 标题不超过 30 字，含数字/对比/反常识
- [ ] 开头 30 秒内说清"是什么 + 为什么读"
- [ ] 第一个代码块在前 1/3 位置出现
- [ ] 至少 1 个对比表
- [ ] 至少 1 个决策树或选型指南
- [ ] 至少 1 个真实案例链接（不是官方文档）
- [ ] 实战场景列表 ≥ 5 个
- [ ] FAQ ≥ 3 个
- [ ] 所有链接都用"内嵌 URL 格式"
- [ ] 结尾有"评论区聊聊"互动
- [ ] 结尾有 🔗 快速链接 section
- [ ] front-matter 完整（title/date/tags/categories/cover）
- [ ] 字数 4000-10000（短了不够深，长了没人读）

---

## 十、📋 常见错误

| 错误 | 应该这样 |
|---|---|
| **date 凭感觉写**（比如随便填一个时间） | **跑 `date '+%Y-%m-%d %H:%M:%S'` 拿真实时间** |
| 把官方文档翻译一遍 | 提炼 + 重组 + 加自己理解 |
| 列一堆特性 | 选 3-5 个最关键的展开 |
| 全文只说"它能干 X" | 加场景 + 对比 + 案例 |
| `[xxx](URL)` | `[xxx：URL](URL)`（让 URL 可见）|
| 章节叫"安装" | 章节叫"3 步上手"（动作 + 结果）|
| 没有 FAQ | 至少 3-5 个常见问题 |
| 没有总结 | 用"X = [一句话]"格式重申 |
| 字数 2000 以下 | 至少 4000 字（给读者足够价值）|
| 只有内链 | 至少 5 个外链（官方文档、GitHub、案例）|

---

## 十一、🚀 完整文章结构模板

复制这个结构，写新文章只需填空：

```markdown
---
title: [一句话标题]
date: YYYY-MM-DD HH:MM:SS
tags: [插件名, 类别, AI Skills, 程序员晚枫]
categories: [AI Skills, 平台攻略]
cover: https://images.unsplash.com/photo-XXX?q=80&w=1200&auto=format&fit=crop
---


大家好，我是程序员晚枫。

[钩子 + 一句话定位]

> **[最有冲击力的一句话]**

[1-2 句过渡]

---

## 一、[插件] 是什么？

**一句话**：[最简单描述]。

跟传统的对比表

[本质上的描述]

---

## 二、为什么用？

### 1. [痛点 1]
### 2. [痛点 2]
### 3. [痛点 3]

---

## 三、上手：3 步出第一个 [产品]

### 第 1 步：脚手架
### 第 2 步：写第一个组件
### 第 3 步：渲染输出

---

## 四、核心 API 速查 / 三条规则

[表格]

---

## 五、实战场景

| 场景 | 怎么做 | 📺 真实案例 |

---

## 六、决策树：怎么选？

[对比 / 决策树]

---

## 七、常见问题

### Q1
### Q2
### Q3

---

## 📚 想系统学习？

[课程推广]

---

## 总结

[X = 一句话定位]

[3-5 个 bullet 点重申价值]

**科技不高冷，AI 很好用。**
我是晚枫，关注我，带你一起玩 AI！

💬 **来评论区聊聊**

[1-2 个互动问题]

---

## 🔗 快速链接

- 📖 官方文档：https://example.com
- 💻 GitHub：https://github.com/owner/repo
- ⚡ 安装：`npm install xxx`
- 📺 [看真实效果：URL](URL)

---

*本文基于 [项目] 官方文档（YYYY-MM）整理。*
```

---

## 十二、💡 案例参考

参考这 6 篇按本指南写的文章：

- 📖 [HyperFrames 入门指南：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-quickstart/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-quickstart/)
- 📖 [HyperFrames 9 大模板详解：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-templates-and-styles/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-hyperframes-templates-and-styles/)
- 📖 [Remotion 入门指南：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-remotion-react-video-framework/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-remotion-react-video-framework/)
- 📖 [videocut-skills 入门指南：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-videocut-skills-tutorial/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-videocut-skills-tutorial/)
- 📖 [video-use 入门指南：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-video-use-ai-editor/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-video-use-ai-editor/)
- 📖 [Codex 5 大视频插件全攻略：https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-codex-video-plugins-overview/](https://www.python4office.cn/course/AI/ai-skills/video-editing-skills/20260615-codex-video-plugins-overview/)

每篇都是按本指南的 7 步框架写的——可以打开对照学习。

---

## 总结

写 Skill 文章 = **结构化拆解 + 真实案例 + 上手即用**。

**7 步框架**：
1. 钩子 → 2. 是什么 → 3. 为什么 → 4. 上手 → 5. 速查 → 6. 实战 → 7. 决策

**最重要的 3 件事**：
- ✓ 第一个代码块出现得早（前 1/3）
- ✓ 每个场景配真实案例链接
- ✓ 链接用"内嵌 URL 格式"（公众号友好）

跟着这个 SOP 走，每篇文章都不会偏。

**最后一条铁律**：**写完之后，自己复制全文到公众号编辑器预览**——看一眼"非作者"读起来是什么感觉。

---

*本指南基于 2026-06 创作经验整理。后续如有新发现，更新 [此文档](https://www.python4office.cn/course/AI/ai-skills/20260615-skill-article-writing-guide/)。*

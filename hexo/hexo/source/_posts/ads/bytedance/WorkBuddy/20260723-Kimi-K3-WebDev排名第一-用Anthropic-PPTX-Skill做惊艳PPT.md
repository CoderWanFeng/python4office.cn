---
title: Kimi K3 WebDev 排名第一，用 Anthropic PPTX Skill 做惊艳 PPT
date: 2026-07-23 19:30:00
tags:
  - Kimi K3
  - Moonshot
  - 月之暗面
  - Web开发
  - PPT
  - PPTX skill
  - Anthropic
  - WorkBuddy
  - AI工具
  - 排行榜
categories: AI设计
cover: https://images.unsplash.com/photo-1677442136019-23781d854236?q=80&w=1200&auto=format&fit=crop
---

兄弟们，今天的 AI 圈又有大新闻——Kimi K3 登顶了 arena.ai 的 Code Arena WebDev 排行榜，直接把 Claude Fable 5 和 GPT 5.6 踩在了脚下。

先说结论：

**Kimi K3 = 1678 分，Code Arena WebDev 榜全球第一。**
**配合 WorkBuddy 的 PPTX Skill，5 分钟出一份专业级 PPT。**

下面一个个讲。

---

## 一、Kimi K3 登顶意味着什么？

先看数据——7 月 21 日的 arena.ai 榜单数据：

| 排名 | 模型 | 厂商 | 得分 |
|------|------|------|
| 1 | **kimi-k3** | **月之暗面 Moonshot** | **1678** |
| 2 | claude-fable-5 | Anthropic | 1634 |
| 3 | gpt-5.6-sol-xhigh (codex-harness) | OpenAI | 1630 |
| 4 | glm-5.2 (max) | 智谱 | 1592 |
| 5 | claude-opus-4-8-thinking | Anthropic | 1565 |

**这几个数字的意义：**

1. **Kimi K3 比第二名 Claude Fable 5 高出 44 分**——在 50 万+投票数的榜上，44 分的差距是不小的领先
2. **Kimi K3 比 GPT 5.6 高 48 分**——说明在 WebDev 这个维度，国产模型已经追上并超越
3. 排名第 4 的 GLM-5.2 也是国产，前 5 里占 2 席

**先说明一下：**

这个排行榜是 **WebDev（网页开发）** 专项榜，重点评估的是 AI 做网页开发的能力，包括：
- 复杂任务的 Agentic 多步推理
- 工具调用的准确性
- 产出代码的质量和可用度
- 实际网页渲染效果

所以，Kimi 拿到第一，说明它在 **网页开发相关的 Agentic 工作流上表现很出色**。

而这些能力，天然可以平移到制作 PPT 上——结构化内容、多步推理、视觉呈现，本质上是同一套 Agentic 工作流。

---

## 二、用 Kimi K3 + PPTX Skill 做 PPT，5 分钟搞定

这是我今天重点要讲的实操部分。

**流程是：**
1. Kimi K3 生成结构化的 PPT 内容
2. WorkBuddy 的 PPTX Skill 生成 .pptx 文件
3. 打开微调，搞定

### 2.1 PPTX Skill 是什么？

PPTX Skill 是 [Anthropic Skills 仓库](https://github.com/anthropics/skills/tree/main/skills/pptx) 里的 PPT 生成技能。

它可以：
- ✅ 接受 Markdown 格式的大纲
- ✅ 自动应用专业设计模板
- ✅ 生成高质量的图表和示意图
- ✅ 支持自定义配色方案
- ✅ 生成可编辑的 `.pptx` 文件

**核心价值：** 不是在 AI 里"画" PPT 截图，而是**生成真正的可编辑 PowerPoint 文件**。

### 2.2 实操 1：用 Kimi K3 出 PPT 内容大纲

**让 Kimi 生成一份「AI Agent 产品发布会 PPT 大纲」**：

```
请为我生成一份 20 页的 AI Agent 产品发布会 PPT 大纲，要求：

【结构要求】
1. 开场 / 痛点（3 页）
2. 产品介绍（5 页）
3. 核心能力（5 页）
4. 客户案例（4 页）
5. 定价与购买（1 页）
6. 结束与行动召唤（2 页）

【格式要求】
- 每页一个标题，3-5 个要点
- 用 Markdown 格式
- 语言简洁有力，适合 PPT 呈现
- 总字数控制在 1000-1500 字
```

**Kimi 的回复质量，你懂的——全球第一的 WebDev 能力，生成的内容不会差。**

### 2.3 实操 2：用 PPTX Skill 生成 PPT 文件

把上面的 Markdown 大纲直接丢到 WorkBuddy，调用 PPTX Skill：

```
用 PPTX Skill 将下面的 PPT 大纲生成一份专业的 PowerPoint 演示文稿。

要求：
1. 主题色：蓝白科技风
2. 字体：思源黑体（标题用粗体）
3. 每页的要点用项目符号呈现
4. 自动添加封面和结束页
5. 自动添加过渡页（每一部分之间）

【PPT 大纲】
（这里粘贴上一步的大纲内容）
```

**5 分钟后，你就能得到一份专业的 `.pptx` 文件**。

### 2.4 最后的微调

拿到 PPT 文件后，只需要做几件事：
1. ✅ 替换公司 Logo
2. ✅ 调整个别图片
3. ✅ 统一一下字体
4. ✅ 演讲者备注页补齐详细内容

**全程不需要手动排版，真正的 0 基础做 PPT。**

---

## 三、这个组合的厉害之处

### 3.1 Kimi K3 的优势

**Kimi K3 生成的内容，比普通 AI 强在哪里？**

- **1M 上下文**——可以一次性理解完整的产品文档
- **结构化输出**——生成的 PPT 大纲结构清晰，层级分明
- **WebDev 第一的能力**——意味着对前端设计的审美和逻辑天然在线
- **中文能力拉满**——国产模型，中文表达自然流畅

### 3.2 PPTX Skill 的优势

- ✅ **原生 PowerPoint 格式**——不是截图，不是 PDF，是真的 .pptx
- ✅ **Skill 机制**——集成在 WorkBuddy，无需额外工具
- ✅ **自动化排版**——配色、字体、布局，Skill 自动处理
- ✅ **可编辑**——拿到文件后想怎么改就怎么改

### 3.3 WorkBuddy 的优势

- ✅ **Skill 生态**——PPTX 只是其中之一，还有更多技能
- ✅ **企业级**——WorkBuddy 有完整的商业版本和组织协作
- ✅ **多模型调度**——不仅 Kimi，也能切 Claude / 豆包 / 其他模型
- ✅ **文件系统深度集成**——生成的文件直接存到本地

---

## 四、3 个进阶技巧

### 4.1 自定义配色方案

**直接在 prompt 里写：**

```
使用自定义配色：
主色：#1890FF（蚂蚁蓝）
辅色：#52C41A（科技绿）
强调色：#F5222D（警示红）
背景色：#FFFFFF
```

### 4.2 生成带图表的 PPT

**让 Kimi 先生成数据结构，再让 Skill 渲染图表：**

```
生成 3 页包含饼图 / 柱状图 / 折线图的 PPT：
- 第一页：市场份额（饼图）
- 第二页：月度增长趋势（折线图）
- 第三页：功能使用率排行（柱状图）
```

### 4.3 多风格模板切换

PPTX Skill 支持内置模板：
- 商务蓝
- 简约灰
- 科技风
- 教育风
- 创业风

**prompt 里直接指定即可。**

---

## 五、适用场景

| 场景 | 为什么适合？ |
|------|------------|
| **职场汇报** | 5 分钟出一份专业级 |
| **产品发布会** | Kimi 懂产品逻辑 + Skill 懂设计 |
| **培训课件** | 批量生成标准化课件 |
| **学术答辩** | 结构清晰 + 专业排版 |
| **创业融资** | 快速出 BP 初稿 |
| **工作总结** | 把零散文字变成专业 PPT |

**一句话：**
**所有你需要做 PPT 的时候，这个组合都能帮你省至少 2 小时。**

---

## 六、写在最后

**Kimi K3 WebDev 第一，有什么意义？**

这不是普通的刷榜——这代表国产模型在 **Agentic Workflow**（智能体工作流）上，已经达到了全球顶尖水平。

**从 Code 到 PPT 到文档，AI 正在把专业能力封装成一个个 Skill。**

**Kimi K3 = 顶级内容理解能力**
**PPTX Skill = 顶级设计排版能力**
**WorkBuddy = 顶级执行调度能力**

**三个加起来，就是 "创意 → 内容 → 交付" 的完整链路。**

**未来的竞争，不再是单个模型的跑分，而是模型+Skill+平台的生态之战。**

---

**评论区告诉我——你最想让 AI 帮你做什么类型的 PPT？**

---

我是晚枫，祝你玩得开心。

---

## 附录 · 关键链接

- 🏆 [arena.ai Code Arena WebDev 排行榜](https://arena.ai/leaderboard/code)
- 🧠 [Kimi K3 官方文档](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart)
- 📊 [Anthropic PPTX Skill 仓库](https://github.com/anthropics/skills/tree/main/skills/pptx)
- 🤖 [WorkBuddy 官网](https://workbuddy.ai)

---
title: AI 读文档又慢又贵又错？这个 Skill 让它快 10 倍、准 10 倍、省一半 token
date: 2026-07-21 10:00:00
tags:
  - markitdown
  - skill
  - ai办公
  - 文档速读
  - pdf阅读
  - token优化
categories: AI工具评测
cover: https://images.unsplash.com/photo-1456324504439-367cee3b3c32?q=80&w=1200&auto=format&fit=crop
---

> **30 秒版本**：

我发布了一个文档速读 Skill：
把 PDF / Word / PPT / Excel 等 **15+ 种格式**一键转成AI能快速读懂的格式（Markdown）。

它解决 AI 读文档的三个痛点：

- ⚡ **AI 读得更快**：不用反复调用工具解析文档，Markdown 一次性喂给 AI，秒级出结果
- 🎯 **AI 读得更准**：标题/表格/章节结构完整保留，不会把页眉页脚当正文、不会表格串行
- 💰 **token 省一半**：Markdown 比原始文档干净 40-60%，AI 处理成本直接砍半

> 📦 GitHub：[wanfeng-skills/skills/doc-speedreader](https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/doc-speedreader)

灵感来自微软的开源项目：markitdown

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260721202237599.png)

---

## 一、AI 读文档的三个毛病

不管 PDF / Word / PPT / Excel，AI "原生"都读不好。具体来说，三个毛病：

### 毛病 1：慢

AI 不能直接读懂 PDF / Word / PPT——它要先调工具提取文本，再调工具识别表格，再自己拼接上下文。一份 80 页 PDF，AI 来回折腾好几轮才能搞清结构。Word / PPT / Excel 也一样，每个格式都是一堵墙，AI 每次都要翻墙。

### 毛病 2：错

- **PDF**：把页眉页脚当正文、双栏串行、表格行列错位
- **Word**：标题层级丢、列表乱套、批注混入正文
- **PPT**：每页之间的逻辑断掉、备注和正文混、图表说明错位
- **Excel**：表头认错、合并单元格炸裂、公式当成数据

你问它"第 3 章讲什么"，它给你总结页脚。

### 毛病 3：贵

PDF / Word / PPT 里的格式噪音（页码 / 页眉 / 水印 / 排版符号）全被当 token 算钱：

- 80 页 PDF ≈ **50,000 tokens**
- 同样内容转 Markdown ≈ **25,000 tokens**
- **一半 token 是浪费的**

---

> doc-speedreader 就是来治这三个病的——**不管什么格式，统一转成干净的 Markdown，让 AI 读得更快、更准、更省 token。**

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260721202333945.png)

---

## 二、doc-speedreader 是什么？

一句话：

> **doc-speedreader = MarkItDown（格式转换）+ 3 轮强制对话流（任务规约）**

架构很简单：

```
用户丢文件/URL
    ↓
scripts/convert.sh  ← 调 MarkItDown 转 Markdown
    ↓
AI 按 SKILL.md 定义的 3 轮对话流，给你 3 种产物选一
    ↓
TL;DR（10 秒）/ 结构化摘要（30 秒）/ 完整 Markdown 副本
```

**核心设计决策**：

- 支持 **15+ 格式**：PDF / Word / PPT / Excel / 图片 / 音频 / HTML / CSV / ZIP / EPUB / YouTube URL 等
- 3 类产物，**默认走 A（TL;DR）**——你不说话，AI 就给你最省时间、最省 token 的版本
- **完全独立**：不联动其他 skill，不做下游推荐，干完活就走

---

## 三、安装（2 分钟）

直接复制下面这句话，让你的AI安装 doc-speedreader：

```bash
全局安装这个skill：https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/doc-speedreader
```

---

## 四、最小可运行示例（30 秒跑通）


### ：AI 对话里用（推荐）

在装了 doc-speedreader 的 AI 客户端（Claude / 其他 AI 客户端）里说一句：

> 帮我速读这份 PDF `/Users/wanfeng/Downloads/report.pdf`

AI 会自动完成：调 `doc-speedreader` → 给你 文档的内容。

---

## 五、核心机制：3 轮强制对话流

这是 doc-speedreader 跟"裸用 MarkItDown"最大的区别。SKILL.md 里定义了一套**强制 3 轮对话**，确保 AI 不会自说自话把整份文档糊你脸上：

| 轮次 | AI 做什么 | 用户做什么 |
|---|---|---|
| **第 1 轮** | 开场 + 收文件路径 / URL | 拖文件 / 给路径 / 给 URL |
| **第 2 轮** | 给出 3 个产物选项（A / B / C） | 选 A / B / C，或自定义 |
| **第 3 轮** | 交付产物 | 拿走用 |
| 第 4 轮（可选） | 回答追问 | 问细节 / 收工 |

**关键设计：默认走 A**

第 2 轮 AI 会明确告诉你：

```
已转成 Markdown（共 N 字 / M 个章节 / 格式：PDF）。
你接下来想要哪一种？

A. ⭐ TL;DR（一句话总结 + 3 个关键点，10 秒看完）
B. 结构化摘要（标题 + 每章要点 + 数据点 + 行动项，30 秒看完）
C. 完整 Markdown（保存到本地路径）
D. 别的（你说）

默认走 A——你要 A 吗？
```

你要是不回答、或者说"默认"，AI 就直接给 TL;DR。这就是"10 秒看完一份报告"这个体验的来源——**不是靠 AI 快，是靠默认选项把决策成本压到 0**。

---

## 六、为什么 AI 用了它，更快、更准、更省？

3 层机制，对应 3 个卖点：

### 机制 1：更快 —— 默认 + 分段策略

SKILL.md 里写死的硬规则：

- **文件 > 5000 字** → AI 在对话里**分段贴关键段**，不一次贴爆上下文窗口
- **文件 < 5000 字** → 全文回灌到对话里
- **用户不主动选 C** → AI 默认只给 TL;DR 摘要，不读全文

AI 拿到的是干净 Markdown + 明确的任务指令，不用自己猜结构、不用反复调工具，一次搞定。

### 机制 2：更准 —— Markdown 保留文档结构

| 维度 | 原始文档直接喂 AI | 转 Markdown 后喂 AI |
|---|---|---|
| **标题层级** | 丢失或错乱 | `#`/`##`/`###` 清晰保留 |
| **表格** | 行列错位、串行 | 干净的 Markdown 表格 |
| **列表** | 混入正文 | `-` / `1.` 结构完整 |
| **页眉页脚** | 当正文读 | 被过滤掉 |

AI 不用猜结构，直接按 Markdown 标题定位章节，按表格读数据，准确率拉满。

### 机制 3：更省 token —— Markdown 比 PDF 干净 40-60%

- PDF / Word / PPT 的格式噪音（页码 / 水印 / 排版符号）全被当 token 算钱
- Markdown 只保留纯内容和结构标记，没有废话
- **摘要用 200 字讲清 80 页报告**，token 消耗是原文的 1/250

3 层机制叠加，token 能省到原来的 **5-10%**。

---

## 七、支持的 15+ 格式

| 类别 | 格式 | 推荐度 | 备注 |
|---|---|---|---|
| 办公文档 | PDF / DOCX / PPTX / XLSX | ⭐⭐⭐⭐⭐ | 主力场景 |
| 网页 | HTML / YouTube URL | ⭐⭐⭐⭐ | 自动抓正文 |
| 电子书 | EPUB | ⭐⭐⭐⭐ | 保留章节结构 |
| 多媒体 | 图片 / 音频 | ⭐⭐⭐ | 默认不开 LLM 图描 |
| 数据 | CSV / ZIP | ⭐⭐⭐ | ZIP 自动解包 |

完整支持矩阵见仓库的 [reference/formats.md](https://github.com/CoderWanFeng/wanfeng-skills/blob/main/skills/doc-speedreader/reference/formats.md)。

---

## 八、相关链接

- **Skill 仓库**：[https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/doc-speedreader](https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/doc-speedreader)
- **MarkItDown 官方**：[https://github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)

---

## 结尾

不是资料太多，是 AI 以前缺一个能让它**读得快、读得准、不浪费 token** 的加速器。

---
name: ai-hot
description: 抓取 AIHOT（卡兹克维护的 AI 热点监控平台）每日精选与日报，按 Python 办公自动化 / AI 工具 / 教程创作 的相关性过滤整理。当用户想"今天 AI 圈有什么新东西"、"最近 Python AI 有什么动态"、"帮我写篇 AI 教程选题"、"AI 日报"等场景时使用。
version: 1.0.0
author: python4office.cn
tags: [ai-news, content-creation, ai-tools, python-automation]
---

# AI Hotspot Tracker（python4office.cn 定制版）

> 基于卡兹克的 AIHOT 公开 API，针对 **Python 办公自动化 / AI 工具 / 教程创作** 场景做了相关性过滤与输出模板优化。
>
> 跟官方 AIHOT Skill 的区别：
> - **相关性过滤**：自动剔除纯融资 PR、纯娱乐八卦，只保留跟 Python/AI 教程可写相关的条目
> - **选题建议**：每条热点附带"是否适合写成 python4office.cn 教程"判断 + 选题角度建议
> - **公众号风格输出**：直接按"标题党 + 痛点 + 干货"模板排版，缩短从"看到热点"到"发文章"的时间

---

## 何时触发这个 Skill

| 用户说的话 | 调用哪个端点 |
|---|---|
| "今天 AI 圈有什么新东西" | `/api/public/items?mode=selected`（默认精选） |
| "看一下 AI 日报" / "今天的日报" | `/api/public/daily` |
| "5 月 6 号的日报" / "昨天的日报" | `/api/public/daily/{date}` |
| "最近一周的 AI 论文" | `/api/public/items?mode=selected&category=论文&since=...` |
| "最近 3 天 AI 模型发布" | `/api/public/items?mode=selected&category=模型&since=...` |
| "OpenAI 最近发了啥" | `/api/public/items?q=OpenAI` |
| "Python 办公自动化的 AI 新工具" | `/api/public/items?q=Python+自动化` |
| "帮我找 AI 教程选题" | 拉精选 + 应用相关性过滤 + 选题建议模板 |

---

## API 基础信息

- **Base URL**：`https://aihot.virxact.com`
- **认证**：❌ 不需要 API Key，公开匿名
- **限流**：默认足够日常使用，正式生产请先观察稳定性
- **时区**：所有时间戳为 UTC，输出给用户时需转 `Asia/Shanghai`
- **必需 Header**：浏览器 User-Agent（否则 nginx 直接 403），脚本已内置

### 主要端点

```http
GET /api/public/items?mode=selected&since=2026-06-17T00:00:00Z&category=ai-models
GET /api/public/items?mode=all&q=Python+AI
GET /api/public/daily
GET /api/public/daily/{YYYY-MM-DD}
GET /api/public/dailies?take=30
```

| 参数 | 必填 | 说明 |
|---|---|---|
| `mode` | 否 | `selected`（精选，默认）/ `all`（全量） |
| `since` | 否 | ISO-8601 时间戳，过滤该时间之后 |
| `category` | 否 | **英文枚举**：`ai-models` / `ai-products` / `industry` / `paper` / `tip` |
| `q` | 否 | 关键词搜索（空格用 `+`，服务端 ILIKE） |
| `cursor` | 否 | 分页 cursor（从上次响应的 `nextCursor` 拿） |
| `take` | 否 | `/dailies` 专用，返回最近 N 天日报列表 |

---

## 工作流

### 第一步：判断意图 → 选择端点

用一句话映射到上面"何时触发"的表格。

### 第二步：调用 API → 拿原始 JSON

直接 `curl` 或 `python -c "import requests; ..."`，无需鉴权。

如果脚本调用，使用本 Skill 自带的 [`scripts/fetch_aihot.py`](scripts/fetch_aihot.py)：

```bash
# 今日日报
python3 scripts/fetch_aihot.py daily

# 精选条目（最近 24h）
python3 scripts/fetch_aihot.py items --mode selected --since 24h

# 按分类
python3 scripts/fetch_aihot.py items --category 模型 --since 7d

# 关键词搜索
python3 scripts/fetch_aihot.py items --q "Python 自动化"
```

### 第三步：相关性过滤

**保留**（python4office.cn 教程相关）：
- ✅ Python / 自动化 / 办公 / 表格 / 文档 / PDF / 爬虫
- ✅ AI 编程助手 / Agent / LLM API / RAG / Prompt 工程
- ✅ 开源 AI 工具发布（特别是 Python 生态）
- ✅ 国产模型 / 国产 Agent 平台更新
- ✅ 公众号 / 短视频 AI 工具

**降权**（仅在用户明确说要看全量时才保留）：
- ⚠️ 纯融资 PR / 估值消息
- ⚠️ 海外纯学术论文（除非有开源代码）
- ⚠️ 跟 Python 生态无关的硬件 / 芯片

**过滤掉**：
- ❌ 名人八卦 / 纯营销内容
- ❌ 重复 / 转载（除非有独特视角）

### 第四步：套用输出模板

按"**公众号选题简报**"模板输出，详见 [`references/output-template.md`](references/output-template.md)。

核心要素：
1. **标题候选**：3 个不同角度的标题（数字型 / 痛点型 / 反常识型）
2. **痛点钩子**：1 句话点出读者会遇到的痛
3. **核心干货**：3-5 条可写成教程的知识点
4. **代码示例方向**：建议用什么库 / API 演示
5. **选题判断**：🟢 必写 / 🟡 可写 / 🔴 不建议（附理由）

---

## 输出示例

> **用户问**："今天 AI 圈有啥适合写 python4office.cn 教程的？"

> **Skill 输出**：
>
> ### 🔥 今日 AI 热点选题简报（2026-06-18）
>
> 共筛选 12 条，**3 条强烈推荐写教程**：
>
> ---
>
> #### 🟢 推荐 1：Anthropic 发布 Claude Code SDK 2.0
> - **原文**：https://...
> - **摘要**：Claude Code 开放 Python SDK，可一键集成进脚本
> - **教程角度**：写一篇《用 Claude Code SDK 批量处理 Excel》
> - **代码方向**：`claude-code-sdk` + `openpyxl` 自动化办公
> - **建议标题**：
>   1. 「Claude Code 能直接调 Excel 了？我用它处理了 200 个表格」
>   2. 「AI 办公神器：Claude Code 2.0 SDK 实战教程」
>   3. 「告别重复劳动：Claude Code + Python 自动化办公指南」
>
> ---
>
> （更多条目...）

---

## 注意事项

1. **原文为准**：摘要由 LLM 生成，引用前请回原文核对（用返回的 `url` 字段）
2. **测试版 API**：AIHOT 处于测试阶段，可能临时下线，生产业务请勿强依赖
3. **时区转换**：API 返回 UTC，输出给用户前转 `Asia/Shanghai (UTC+8)`
4. **分类大小写**：分类参数中文（`模型`），不要传英文
5. **频率控制**：单次会话最多拉 3 次，避免给 AIHOT 造成压力

---

## 相关文件

- [`scripts/fetch_aihot.py`](scripts/fetch_aihot.py)：命令行调用脚本（Python 3.8+，零依赖只用标准库）
- [`references/api-reference.md`](references/api-reference.md)：API 字段详细说明
- [`references/output-template.md`](references/output-template.md)：公众号选题简报输出模板
- [`README.md`](README.md)：安装与快速上手

---

## 跟官方 AIHOT Skill 的区别

| 维度 | 官方 AIHOT Skill | 本 Skill（python4office.cn 定制） |
|---|---|---|
| 数据源 | AIHOT | AIHOT |
| 输出风格 | 通用中文简报 | 公众号选题简报 |
| 相关性过滤 | 无 | ✅ Python 办公 / AI 工具向 |
| 选题建议 | 无 | ✅ 每条带"是否值得写教程"判断 |
| 标题生成 | 无 | ✅ 每条 3 个候选标题 |
| 限流 | 默认 | 3 次/会话（更保守） |

---

**科技不高冷，AI 很好用。** —— 程序员晚枫
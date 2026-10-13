---
title: 模块 3 · LLM 生产化工程（第 5-7 周，核心长模块）
date: 2026-10-14 10:00:00
tags: [FDE, Residency, LLM, RAG, Agent, Prompt工程, 评估]
categories: [AI 课程, FDE 实战课]
cover: https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1200&auto=format&fit=crop
---



![模块 3 · LLM 生产化工程](https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&h=400&fit=crop)


# 模块 3 · LLM 生产化工程（第 5-7 周，核心长模块）

> **💡 一句话总结**：3 周时间，把模块 2 定下的架构图变成 1 个能跑 50 个真实问题的生产级 LLM 系统。

---

## 🎯 本模块三大特点

> **📚 系统**：模块 3 是整个 Residency 的 **核心长模块**——前两个模块做铺垫，后面 4 个模块做集成，3 周时间全压在这里
>
> **🔧 实战**：本模块产出 1 个 RAG + Agent 系统 + 1 套评估体系 + 1 份 trace 看板
>
> **⚡ 不啰嗦**：跳过所有"原理讲解"，直接给生产可用的最小代码

---

## 📖 学习导航

| 上一模块 | 本模块位置 | 下一模块 |
|---|---|---|
| [模块 2 · 解决方案设计](./06-residency-module2-solution-design) | **模块 3 / 共 8 模块（第 5-7 周）** | [模块 4 · 企业系统集成](./08-residency-module4-enterprise-integration) |

---

## 📅 三周时间表

| 周 | 主题 | 产出 |
|---|---|---|
| **第 5 周** | Prompt 工程化 + RAG 全套 | 1 个 RAG 系统（准确率 ≥85%） |
| **第 6 周** | Agent 工程 + 工具调用 | 1 个 Agent 系统（3 个工具调用成功） |
| **第 7 周** | 评估体系 + Trace 追踪 | 1 套 Ragas 评估 + LangSmith 看板 |

---

## 🚀 直接开始：3 周实战任务

### 第 5 周 · RAG 全套

#### 任务 1：分块策略实验（周一）

**目标**：选 1 种分块策略并验证效果
**难度**：⭐⭐

```python
# 对比 4 种分块策略
from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    MarkdownTextSplitter,
)
from langchain_experimental.text_splitter import SemanticChunker

splitters = {
    "fixed_500": CharacterTextSplitter(chunk_size=500, chunk_overlap=50),
    "recursive_500": RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50),
    "markdown": MarkdownTextSplitter(chunk_size=500),
    "semantic": SemanticChunker(OpenAIEmbeddings()),
}

for name, splitter in splitters.items():
    chunks = splitter.split_documents(docs)
    # 跑评估（用任务 3 的 Ragas）
    metrics = run_ragas(chunks, test_set)
    print(f"{name}: recall={metrics['context_recall']:.2f}, precision={metrics['context_precision']:.2f}")
```

**决策原则**：技术文档用 Markdown，PDF 表格用 SemanticChunker，普通文本用 RecursiveCharacterTextSplitter。

---

#### 任务 2：Hybrid 检索 + 重排（周二-周四）

```python
# BM25 + 向量混合检索 + bge-reranker 重排
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from langchain_community.cross_encoders import HuggingFaceCrossEncoder

# 1. BM25 + 向量
bm25 = BM25Retriever.from_documents(chunks)
bm25.k = 5

vector = vectorstore.as_retriever(search_kwargs={"k": 5})

ensemble = EnsembleRetriever(
    retrievers=[bm25, vector],
    weights=[0.4, 0.6],
)

# 2. 重排
reranker = HuggingFaceCrossEncoder(model_name="BAAI/bge-reranker-v2-m3")

def rerank(query, docs, top_k=4):
    scores = reranker.score([(query, d.page_content) for d in docs])
    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    return [d for d, s in ranked[:top_k]]

# 3. 完整 RAG 流程
def hybrid_rag(query):
    initial_docs = ensemble.invoke(query)
    reranked_docs = rerank(query, initial_docs)
    return reranked_docs
```

---

#### 任务 3：50 题评估集（周五）

**目标**：准备 1 个 50 题测试集，跑量化指标

```python
# 用 Ragas 跑全量评估
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_recall, context_precision

test_set = [
    {
        "question": "...",
        "ground_truth": "...",
        "contexts": [...],
    },
    # 共 50 题，分布：
    # - 简单事实查询 20 题
    # - 多跳推理 15 题
    # - 表格 / 数字问题 10 题
    # - 边界 / 长尾问题 5 题
]

results = evaluate(Dataset.from_list(test_set), metrics=[...])
print(f"Recall: {results['context_recall']:.2%}")  # 目标 ≥0.85
print(f"Precision: {results['context_precision']:.2%}")  # 目标 ≥0.85
print(f"Faithfulness: {results['faithfulness']:.2%}")  # 目标 ≥0.90
print(f"Relevancy: {results['answer_relevancy']:.2%}")  # 目标 ≥0.85
```

---

### 第 6 周 · Agent 工程

#### 任务 4：单 Agent + 多工具（周一-周三）

**目标**：基于 RAG 加 3 个外部工具

```python
# 用 Claude / GPT 的 Tool Use
import anthropic

client = anthropic.Anthropic()

tools = [
    {"name": "search_docs", "description": "从知识库检索相关文档", "input_schema": {...}},
    {"name": "send_email", "description": "发邮件", "input_schema": {...}},
    {"name": "create_ticket", "description": "提交工单", "input_schema": {...}},
    {"name": "query_database", "description": "查询业务数据库", "input_schema": {...}},
]

def run_agent(query, max_iter=10):
    messages = [{"role": "user", "content": query}]
    for _ in range(max_iter):
        response = client.messages.create(
            model="claude-sonnet-4-5",
            tools=tools,
            messages=messages,
            max_tokens=4096,
        )
        if response.stop_reason != "tool_use":
            return response.content[0].text
        # 执行工具调用
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = execute_tool(block.name, block.input)
                tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": json.dumps(result)})
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})
```

---

#### 任务 5：多 Agent 编排（周四-周五）

**典型多 Agent 模式：**

```
        ┌────────────────┐
        │  Orchestrator  │  ← 接收任务，分派给子 Agent
        └────────────────┘
          ↓      ↓      ↓
    ┌─────┐ ┌─────┐ ┌─────┐
    │ RAG │ │ SQL │ │ API │   ← 子 Agent 各司其职
    │Agent│ │Agent│ │Agent│
    └─────┘ └─────┘ └─────┘
```

**推荐框架**：LangGraph（推荐）或 AutoGen。

---

### 第 7 周 · 评估 + Trace

#### 任务 6：跑 1 轮完整评估（周一-周二）

**评估 4 大指标：**
- `faithfulness`：答案是否忠于检索内容（无幻觉）
- `answer_relevancy`：答案是否切题
- `context_recall`：检索召回率
- `context_precision`：检索精度

---

#### 任务 7：接 LangSmith / LangFuse（周三-周四）

```python
# LangSmith 一行配置
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "lsv2_xxx"
os.environ["LANGCHAIN_PROJECT"] = "客户项目名"

# 自动追踪所有 LLM 调用
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o")
# 后续所有调用自动在 LangSmith 看板可视化
```

---

#### 任务 8：写《LLM 系统评估报告 v1.0》（周五）

**模板：**

```markdown
# LLM 系统评估报告 v1.0

## 1. 系统架构图（贴）
## 2. 评估集规模
- 总题数：50
- 分布：简单 20 / 多跳 15 / 表格 10 / 长尾 5

## 3. 核心指标
| 指标 | 当前 | 目标 | 通过 |
|---|---|---|---|
| Faithfulness | 92% | ≥90% | ✅ |
| Answer Relevancy | 88% | ≥85% | ✅ |
| Context Recall | 86% | ≥85% | ✅ |
| Context Precision | 90% | ≥85% | ✅ |

## 4. 失败 case 分析（至少 5 个）
1. [case 1] —— 原因 + 改进方案
2. [case 2] —— ...

## 5. 成本分析
- 单次响应平均成本：¥0.012
- 月预估成本（100 万次）：¥12,000

## 6. 下一步
- [ ] 优化分块策略
- [ ] 增加 100 题长尾测试
- [ ] 接入 LangSmith 生产监控
```

---

## 📚 系统学习：核心概念

### 概念 1：RAG 全套的 5 个关键决策

已在 Day 3 详细讲过，此处补充 **生产级** vs **Demo 级** 的差异：

| 决策点 | Demo 级 | 生产级 |
|---|---|---|
| 分块 | RecursiveCharacterTextSplitter | 按文档类型定制 + 评估验证 |
| Embedding | OpenAI text-embedding-3 | 按语言 / 行业选（如 bge 中文） |
| 检索 | 纯向量 | Hybrid（BM25 + 向量） |
| 重排 | 无 | 必有（bge-reranker） |
| 评估 | 凭感觉 | 必有（Ragas + 50 题测试集） |

---

### 概念 2：Agent 的 3 类典型模式

| 模式 | 适用场景 | 代表框架 |
|---|---|---|
| **ReAct** | 工具调用步骤清晰 | LangChain、Claude Tool Use |
| **Plan-and-Execute** | 复杂多步任务 | LangGraph、AutoGen |
| **Multi-Agent** | 跨领域任务 | AutoGen、CrewAI、LangGraph |

**FDE 实战建议**：单 Agent + 多工具覆盖 80% 场景，需要多步规划才上 Multi-Agent。

---

### 概念 3：LLM 评估的 4 个层次

| 层次 | 评估什么 | 工具 |
|---|---|---|
| **模型层** | 模型本身能力 | OpenAI Evals、Anthropic Evals |
| **RAG 层** | 检索 + 生成质量 | Ragas、DeepEval、TruLens |
| **Agent 层** | 工具调用成功率 | LangSmith、LangFuse |
| **业务层** | 真实用户感受 | 人工评估、A/B 测试 |

**FDE 实战建议**：4 层都要有，但 RAG 层 + 业务层最关键。

---

## ⚡ 避坑指南：常见错误

| 错误类型 | 错误做法 | 正确做法 | 为什么 |
|---|---|---|---|
| 不做分块实验 | "RecursiveCharacterTextSplitter 就行" | 至少对比 3 种策略 | 不同文档类型最优分块差很多 |
| 没重排 | 检索 Top-5 直接给 LLM | 必须重排 | 不重排前 5 个里经常有 4 个错的 |
| 测试集太少 | 跑 5 个用例就算成功 | 至少 50 题 + 分层 | 5 题准确率 100% 没意义 |
| Agent 多步执行 | 一次 prompt 让模型做完所有步骤 | 每步独立 + 状态管理 | 多步容易中途跑偏 |
| 没 trace | 黑盒调试 | 接 LangSmith / LangFuse | 没 trace = 出问题不知道错在哪 |

---

## 🎯 模块 3 总结

### 你学到了什么
- ✅ RAG 5 个关键决策的"生产级"标准
- ✅ Hybrid 检索 + bge-reranker 重排的完整代码
- ✅ 50 题评估集的搭建方法 + Ragas 4 大指标
- ✅ 单 Agent + 多工具的 Claude / GPT 实现
- ✅ LangSmith / LangFuse 的接入方式

### 模块交付物 Checklist
- [ ] 1 个 RAG 系统（评估通过）
- [ ] 1 个 Agent 系统（3 个工具调用成功）
- [ ] 50 题评估集 + 评估报告 v1.0
- [ ] LangSmith / LangFuse 看板接入
- [ ] mentor 1v1 review 通过（第 7 周末）

### 下一步行动
1. [ ] 进入 [模块 4 · 企业系统集成（第 8 周）](./08-residency-module4-enterprise-integration)
2. [ ] 把 RAG + Agent 接到客户的 OA / CRM / 飞书
3. [ ] 处理客户的数据合规要求

---

## ➡️ 下模块预告

**模块 4 · 企业系统集成（第 8 周）**
- 你将学到：Webhook / 中间表 / iPaaS 三种对接模式 + SSO / SAML 集成
- 实战任务：跑通 1 次端到端集成（客户系统 → AI 服务）

👉 [继续阅读模块 4](./08-residency-module4-enterprise-integration)

---

---

## 📞 联系作者

| 联系方式 | 入口 |
|---|---|
| 📱 微信 | `aiwf365`（扫码加好友，备注"FDE"） |
| 🌐 个人网站 | https://python4office.cn/ |

<p align="center">
  <img src="https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/wx-aifw365.png" width="200" alt="程序员晚枫微信二维码"/>
</p>

> 加入 AI 编程交流群，第一时间获取 FDE 课程更新 + AI 落地实战案例。

*💡 记住：模块 3 的产出是后面所有模块的基础——花 3 周把 LLM 系统打磨扎实，比赶进度更划算。*
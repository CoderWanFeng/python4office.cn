---
title: Day 3 · Agent 系统构建实战
date: 2026-10-14 10:00:00
tags: [FDE, Bootcamp, Agent, RAG, Prompt工程]
categories: [AI 课程, FDE 实战课]
cover: https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1200&auto=format&fit=crop
---



![Day 3 · Agent 系统构建实战](https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&h=400&fit=crop)


# Day 3 · Agent 系统构建实战

> **💡 一句话总结**：用 1 个限定时间的挑战，把 Prompt 工程、RAG、Agent 工具调用、评估 4 大能力一次性打通。

---

## 🎯 本节三大特点

> **📚 系统**：Day 3 在 4 天 Bootcamp 中的定位是 **技术核心**——前面学业务、选模型，这天全部用来"做出来"
>
> **🔧 实战**：本节只有一个大挑战——**4 小时内从 0 到 1 搭出 1 个可用 Agent**
>
> **⚡ 不啰嗦**：上来就干，规则都在注释里

---

## 📖 学习导航

| 上一节 | 本节位置 | 下一节 |
|---|---|---|
| [Day 2 · 模型与部署形态](./02-bootcamp-day2-model-selection) | **Day 3 / 共 4 天** | [Day 4 · 安全与红队演练](./04-bootcamp-day4-security-review) |

---

## 🚀 直接开始：4 小时挑战任务

### 🎯 任务总目标

**4 小时内搭出 1 个能用的"企业内部 AI 助手" Agent**，能回答基于公司文档的问题，并能调用 3 个外部工具完成指定任务。

**评分维度**：

| 维度 | 权重 | 通过线 |
|---|---|---|
| 能跑通 | 30% | Demo 可演示，无报错 |
| RAG 准确率 | 25% | 50 题答对 ≥ 85% |
| 工具调用成功率 | 25% | 3 个工具各至少 1 次成功调用 |
| 评估报告完整 | 20% | 有指标、有对比、有问题分析 |

---

### 任务 1：搭一个最小可用的 RAG（90 分钟）

**目标**：用一个 50 页 PDF 知识库，搭一个能准确回答的 RAG
**难度**：⭐⭐⭐

```python
# 最小 RAG 示例：基于 LangChain + Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# 1. 加载 + 分块
loader = PyPDFLoader("company-handbook.pdf")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 2. 向量化 + 存储
vectorstore = Chroma.from_documents(
    chunks,
    embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
    persist_directory="./chroma"
)

# 3. 检索 + 生成
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_template("""
你是企业内部 AI 助手。请仅基于以下上下文回答问题，不要编造信息。
如果不知道答案，请回答"我不知道"。

上下文：{context}

问题：{question}
""")

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# 4. 测试
answer = rag_chain.invoke("公司年假是几天？")
print(answer.content)
```

**执行结果：**
- 一个能基于 PDF 回答问题的 RAG
- 50 题测试集准确率 ≥85%

---

### 任务 2：给 RAG 加评估体系（45 分钟）

**目标**：用 LangSmith / LangFuse / Ragas 任何一个工具，搭一套评估看板
**难度**：⭐⭐⭐

```python
# 用 Ragas 做 RAG 评估
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_recall,
    context_precision,
)
from datasets import Dataset

# 1. 准备评估集（50 题 + 标准答案）
test_set = [
    {"question": "公司年假是几天？", "ground_truth": "10 天", "contexts": [...]},
    {"question": "差旅报销标准？", "ground_truth": "一线城市 800 元/天", "contexts": [...]},
    # ... 共 50 题
]

# 2. 跑评估
dataset = Dataset.from_list(test_set)
results = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevancy, context_recall, context_precision],
)

# 3. 产出报告
print(results)
# {'faithfulness': 0.92, 'answer_relevancy': 0.88, 'context_recall': 0.85, 'context_precision': 0.90}
```

**执行结果：**
- 1 份评估报告（4 个核心指标）
- 至少 5 个失败 case 的分析（哪里错了、为什么、怎么改）

---

### 任务 3：让 Agent 能调 3 个外部工具（90 分钟）

**目标**：基于任务 1 的 RAG，加 3 个工具调用：发邮件 / 查日历 / 提交工单
**难度**：⭐⭐⭐⭐

```python
# 用 Claude / GPT 的 Tool Use 机制
import anthropic
import json

client = anthropic.Anthropic()

# 1. 定义 3 个工具
tools = [
    {
        "name": "send_email",
        "description": "发送邮件给指定收件人",
        "input_schema": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "收件人邮箱"},
                "subject": {"type": "string"},
                "body": {"type": "string"},
            },
            "required": ["to", "subject", "body"],
        },
    },
    {
        "name": "check_calendar",
        "description": "查询指定日期的日历安排",
        "input_schema": {
            "type": "object",
            "properties": {
                "date": {"type": "string", "description": "YYYY-MM-DD"},
            },
            "required": ["date"],
        },
    },
    {
        "name": "create_ticket",
        "description": "提交工单到 IT 系统",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"},
                "priority": {"type": "string", "enum": ["low", "medium", "high"]},
            },
            "required": ["title", "description"],
        },
    },
]

# 2. Agent 主循环
def run_agent(user_query: str):
    messages = [{"role": "user", "content": user_query}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4096,
            tools=tools,
            messages=messages,
        )

        # 检查是否要调用工具
        if response.stop_reason == "tool_use":
            for block in response.content:
                if block.type == "tool_use":
                    # 真实调用工具（这里用 mock）
                    tool_result = mock_tool_call(block.name, block.input)

                    messages.append({"role": "assistant", "content": response.content})
                    messages.append({
                        "role": "user",
                        "content": [{
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": json.dumps(tool_result, ensure_ascii=False),
                        }],
                    })
        else:
            # 模型给出最终回答
            return response.content[0].text


def mock_tool_call(name, input):
    if name == "send_email":
        return {"status": "sent", "message_id": "msg_123"}
    if name == "check_calendar":
        return {"events": [{"time": "10:00", "title": "周会"}]}
    if name == "create_ticket":
        return {"ticket_id": "T-456", "status": "open"}
    return {"error": "unknown tool"}


# 3. 测试 3 个端到端任务
print(run_agent("帮我查一下明天的日程，然后发邮件给老板汇报"))
print(run_agent("我电脑坏了，提交一个高优先级工单"))
print(run_agent("查日历、发邮件、提交工单三件事一起做：先看周三日程，再给客户发邀请，最后建一个会议工单"))
```

**执行结果：**
- 3 个工具各至少 1 次成功调用
- Agent 能自主规划多步任务（不是写死的流程）

---

### 任务 4：写 1 份《Agent 评估报告》（45 分钟）

**目标**：把任务 1-3 的产出整理成 1 份给 mentor review 的文档
**难度**：⭐⭐

```markdown
# Agent 评估报告

## 1. 系统架构图
[贴架构图]

## 2. 核心指标
| 指标 | 数值 | 通过线 |
|---|---|---|
| RAG 准确率 | 87% | ≥ 85% ✅ |
| 工具调用成功率 | 100% | ≥ 80% ✅ |
| P95 响应时长 | 2.3s | ≤ 5s ✅ |
| 单次成本 | ¥0.012 | ≤ ¥0.05 ✅ |

## 3. 测试用例覆盖
- RAG 类问题：25 题
- 工具调用问题：15 题
- 多步规划问题：10 题

## 4. 失败 case 分析
1. [问题 1] —— 原因：分块策略导致跨段信息丢失 —— 改进：换 SemanticChunker
2. [问题 2] —— 原因：工具描述不够清晰，模型选错工具 —— 改进：补充 tool description 示例

## 5. 下一步
- [ ] 优化分块策略
- [ ] 补充 50 题测试集
- [ ] 接入 LangSmith 做 trace 追踪
```

---

## 📚 系统学习：核心概念

### 概念 1：什么是 Agent

**一句话解释**：能用工具（Tools）自主决策和执行步骤的 LLM 程序——和只回答问题的 Chatbot 区别在于**能"做事"**。

**Agent 的 4 个核心能力：**
1. **规划（Planning）**：把复杂任务拆成可执行步骤
2. **工具调用（Tool Use）**：调用外部 API 完成具体动作
3. **记忆（Memory）**：保留上下文（短期 + 长期）
4. **反思（Reflection）**：检查自己做的事对不对，错了重试

**Agent vs RAG vs Chatbot 对比：**

| 形态 | 能力 | 适用场景 |
|---|---|---|
| Chatbot | 仅问答 | 客服、闲聊 |
| RAG | 基于知识库问答 | 文档问答、客服增强 |
| Agent | 能自主规划+调工具 | 复杂任务、自动化操作 |

---

### 概念 2：RAG 的 5 个关键决策

**为什么重要**：RAG 看起来简单，但每个环节选错都会让准确率掉 10-20 个百分点。

| 决策点 | 主流选择 | 坑 |
|---|---|---|
| 分块策略 | 按段落 / 按语义 / 按结构 | 太粗召回不准，太细上下文丢失 |
| Embedding | text-embedding-3 / bge / m3e | 中文场景一定要用中文 embedding |
| 检索方式 | 向量 / BM25 / Hybrid | 纯向量在专有名词场景差 |
| 重排 | bge-reranker / cohere-rerank | 不做重排，前 5 个结果经常答非所问 |
| 评估 | Ragas / LangSmith / TruLens | 没评估 = 不知道 RAG 好不好 |

---

### 概念 3：Tool Use 的设计模式

**为什么重要**：Tool description 写不好，模型就调错工具——这是 80% 的 Agent 失败原因。

**3 个关键设计原则：**
1. **Description 要具体**：不要说"查询天气"，要说"查询指定城市的当前天气，输入城市名，返回温度、湿度、天气状况"
2. **Schema 要严格**：用 JSON Schema 明确必填字段和类型
3. **提供示例**：复杂工具在 description 里给 1 个 input 示例

---

## ⚡ 避坑指南：常见错误

| 错误类型 | 错误做法 | 正确做法 | 为什么 |
|---|---|---|---|
| 分块一刀切 | 全用 chunk_size=500 | 不同文档类型用不同策略 | PDF 表格和纯文本分块方式完全不同 |
| 不做评估 | 凭感觉说"效果不错" | 用 Ragas 跑量化指标 | 没指标的 RAG 永远上不了生产 |
| Tool 描述含糊 | "发邮件" | "发邮件给指定收件人，输入 to/subject/body，返回 message_id" | 描述不清 = 模型选错工具 |
| Agent 没规划 | 让模型一次输出所有工具调用 | 用 ReAct / ReWOO 模式分步执行 | 多步任务一次输出容易中途出错 |
| 没 trace | 失败不知道错在哪 | 接 LangSmith / LangFuse | 没 trace = 黑盒调试 |

---

## 🎯 本节总结

### 你学到了什么
- ✅ RAG 的最小可用实现 + 5 个关键决策点
- ✅ Ragas 评估 4 大指标：faithfulness / answer_relevancy / context_recall / context_precision
- ✅ Agent 的 Tool Use 实现（Claude / GPT 双兼容）
- ✅ 1 份完整的 Agent 评估报告怎么写

### 下一步行动
1. [ ] 用任务 1-4 的模板搭 1 个自己的 Agent Demo
2. [ ] 跑 1 次 Ragas 评估，记录失败 case
3. [ ] 把 Agent 接入 LangSmith，看 trace
4. [ ] 进入 [Day 4 · 安全与红队演练](./04-bootcamp-day4-security-review)

---

## ➡️ 下节预告

**Day 4 · 安全、合规与红队演练**
- 你将学到：提示词注入防护、数据脱敏、Guardrails、红队测试
- 实战任务：对 Day 3 的 Agent 做 1 次完整安全自审 + 红队演练

👉 [继续阅读 Day 4](./04-bootcamp-day4-security-review)

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

*💡 记住：4 小时挑战的目的不是搭出"完美系统"，是搭出"能跑、可评估、有失败分析"的最小闭环——这是 Bootcamp 区别于一般教程的核心。*
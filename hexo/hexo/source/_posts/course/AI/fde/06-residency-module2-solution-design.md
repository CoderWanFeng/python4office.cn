---
title: 模块 2 · 解决方案设计与 ADR（第 3-4 周）
date: 2026-10-14 10:00:00
tags: [FDE, Residency, 架构设计, C4, 解决方案]
categories: [AI 课程, FDE 实战课]
cover: https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=1200&auto=format&fit=crop
---


<p align="center" id='FDE-读者群-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/P_o6azd0AwuraLkQQg6t2Q'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%" alt="加入AI学习交流群，第一时间获取FDE课程更新"/>
    </a>   
</p>


![模块 2 · 解决方案设计与 ADR](https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&h=400&fit=crop)


# 模块 2 · 解决方案设计与 ADR（第 3-4 周）

> **💡 一句话总结**：把模块 1 的业务翻译，落到 1 套架构图 + 1 份 ADR——让客户的 CTO 看完就能拍板"做"。

---

## 🎯 本模块三大特点

> **📚 系统**：模块 2 在 12 周 Residency 中的定位是 **决策关口**——技术方向定下来，后面 8 周不再回头
>
> **🔧 实战**：本模块产出 4 张 C4 视图 + 1 份 ADR v1.0 + 1 个 5 页技术方案 PPT
>
> **⚡ 不啰嗦**：直接套模板，不纠结画图工具

---

## 📖 学习导航

| 上一模块 | 本模块位置 | 下一模块 |
|---|---|---|
| [模块 1 · 客户嵌入](./05-residency-module1-customer-embedding) | **模块 2 / 共 8 模块（第 3-4 周）** | [模块 3 · LLM 生产化工程](./07-residency-module3-llm-engineering) |

---

## 📅 两周时间表

| 时间 | 任务 | 产出 |
|---|---|---|
| **第 3 周 Day 1-3** | 画 C4 Model 4 张视图（Context / Container / Component / Code） | 4 张架构图 |
| **第 3 周 Day 4-5** | 写 1 份 ADR 核心决策 | ADR v1.0 |
| **第 4 周 Day 1-3** | 准备 5 页技术方案 PPT | 5 页 PPT |
| **第 4 周 Day 4-5** | 给客户决策人 + CTO 汇报，收集反馈 | 汇报纪要 + v2.0 |

---

## 🚀 直接开始：3 个核心实战任务

### 任务 1：用 C4 Model 画 4 张架构图（推荐工具：draw.io / Structurizr / Mermaid）

**目标**：让客户 CTO 5 分钟看懂系统全貌
**难度**：⭐⭐⭐
**时间**：2 天

#### Level 1 · Context 图（系统上下文）

```
┌─────────────────────────────────────────────────┐
│                                                   │
│  [客户业务人员] ─→ [AI 助手] ←─ [客户 IT 运维]      │
│       ↑               ↓                            │
│       │         [客户业务系统]                      │
│       │               ↓                            │
│       │         [客户文档库 / DB]                  │
│       │                                           │
│  [客户决策人] ←── [周报 / 报表]                    │
│                                                   │
└─────────────────────────────────────────────────┘
```

#### Level 2 · Container 图（容器视图）

```
[Web UI (React)]  [API Gateway (FastAPI)]  [后台管理 (Admin)]
         ↓                  ↓                    ↓
[AI Service (Python)] ←→ [向量库 (Milvus)]   [PostgreSQL]
         ↓                  ↓
[LLM API (Qwen3-72B)] [对象存储 (MinIO)]
```

#### Level 3 · Component 图（组件视图）

```
[AI Service]
├─ [Prompt Manager]
├─ [RAG Pipeline]
│   ├─ [Chunker]
│   ├─ [Embedder]
│   ├─ [Retriever]
│   └─ [Reranker]
├─ [Agent Orchestrator]
├─ [Tool Registry]
├─ [Guardrails Layer]
└─ [Tracing (LangSmith)]
```

#### Level 4 · Code 图（关键类图）

```
略（视项目复杂度决定是否需要）
```

---

### 任务 2：写 1 份 ADR v1.0

**目标**：把"为什么选这个、不选那个"写到 1 页文档里
**难度**：⭐⭐
**时间**：1 天

**模板（已在 Day 2 用过）：**

```markdown
# ADR-001：[决策标题]

## 状态
2026-XX-XX 提议中 / 已通过 / 已废弃

## 背景
[业务约束 + 模块 1 业务画像摘要]

## 决策
[最终选了什么]

## 备选方案
1. [备选 1]：[为什么没选]
2. [备选 2]：[为什么没选]
3. [备选 3]：[为什么没选]

## 后果
### 正面
- [好处 1]
- [好处 2]

### 负面
- [代价 1] + [缓解方案]
- [代价 2] + [缓解方案]

## 验证方法
- [指标 1] 目标 ≥ X
- [指标 2] 目标 ≤ Y
- [评估周期]
```

**典型 FDE ADR 主题：**
- ADR-001：模型选型
- ADR-002：私有化 vs API
- ADR-003：RAG vs Fine-tune
- ADR-004：前端技术栈
- ADR-005：可观测性方案

---

### 任务 3：5 页技术方案 PPT

**目标**：用 5 张幻灯片说服客户决策层
**难度**：⭐⭐
**时间**：1 天

**模板：**

```
PPT-1 · 业务问题
  - 客户的 3 个核心痛点（来自业务画像）
  - 不解决会怎样

PPT-2 · 解决方案全景
  - 系统如何工作（一句话 + 1 张图）
  - 与客户已有系统的集成关系

PPT-3 · 关键技术决策
  - 3 个核心 ADR 的结论
  - 为什么这样选

PPT-4 · 落地计划
  - 12 周时间表
  - 关键里程碑

PPT-5 · 投入产出
  - 客户投入：人 / 钱 / 时间
  - 客户产出：业务指标提升
  - 风险与缓解
```

---

## 📚 系统学习：核心概念

### 概念 1：C4 Model 4 层视图

**一句话解释**：C4 Model 是 Simon Brown 提出的轻量级架构描述标准，从外到内分 4 个层级。

| 层级 | 看的人 | 关心什么 | 用什么画 |
|---|---|---|---|
| **Context** | 业务方、决策人 | 系统与人的关系 | 简单方框 + 箭头 |
| **Container** | IT 主管、应用架构师 | 系统由哪些容器组成 | 容器 + 技术栈标签 |
| **Component** | 开发人员 | 容器内部的组件 | 类图 / 模块图 |
| **Code** | 代码维护者 | 类与方法 | UML 类图（通常省掉） |

**FDE 实战建议**：只画前 3 层就够用，第 4 层省掉。

---

### 概念 2：ADR vs 设计文档

| 维度 | ADR | 设计文档 |
|---|---|---|
| 目的 | 记录"为什么这样选" | 描述"系统长什么样" |
| 时机 | 决策前写 | 决策后 |
| 长度 | 1 页 | 10-50 页 |
| 更新 | 不更新（废弃就写新 ADR） | 持续更新 |

**FDE 实战建议**：用 ADR 锁住 3-5 个核心决策，其他细节用设计文档补充。

---

### 概念 3：怎么跟客户 CTO 沟通技术方案

**FDE 跟 CTO 沟通的 3 个原则：**
1. **结论先行**：先说"我们建议 X，因为 Y"，再展开论证
2. **承认取舍**：每个方案都有取舍，别避而不谈
3. **给退路**：留 1-2 个备选，让 CTO 觉得有控制感

---

## ⚡ 避坑指南：常见错误

| 错误类型 | 错误做法 | 正确做法 | 为什么 |
|---|---|---|---|
| 一上来就画 Component 图 | 想给 CTO 看组件图 | 先画 Context / Container | CTO 只关心"长什么样"，不关心类 |
| ADR 太长 | 写成 5 页 | 严格 1 页 | ADR 是给未来人看的，太长 = 没人看 |
| 技术 PPT 用太多术语 | "我们用 RAG + Hybrid Search + bge-reranker" | 翻译成业务语言 | CTO 不是要懂技术，是要拍板 |
| 没和决策人对齐就定稿 | 直接找 IT 对齐 | 决策人先点头，再技术细化 | 决策人没点头 = 项目可能胎死腹中 |
| 文档不存稿 | 评审完 PPT 没人存档 | 写完发邮件 + 进版本库 | 没存稿 = 后续争议无据可查 |

---

## 🎯 模块 2 总结

### 你学到了什么
- ✅ C4 Model 4 层视图的画法与受众
- ✅ ADR 的 6 个标准章节与典型 FDE ADR 主题
- ✅ 5 页技术方案 PPT 的标准结构
- ✅ 跟客户 CTO 沟通技术方案的 3 个原则

### 模块交付物 Checklist
- [ ] 4 张 C4 视图（Context / Container / Component + 视情况 Code）
- [ ] ADR v1.0（至少 1 份核心决策）
- [ ] 5 页技术方案 PPT
- [ ] CTO 评审通过 + 决策人确认方向

### 下一步行动
1. [ ] 进入 [模块 3 · LLM 生产化工程（第 5-7 周）](./07-residency-module3-llm-engineering)
2. [ ] 启动 RAG / Agent 的实际开发
3. [ ] 准备 50 题测试集

---

## ➡️ 下模块预告

**模块 3 · LLM 生产化工程（第 5-7 周）**——本课程的核心长模块
- 你将学到：Prompt 工程化、RAG 全套、Agent 工程、评估体系
- 实战任务：1 个可演示的 RAG + Agent 系统（覆盖 50 个真实问题）

👉 [继续阅读模块 3](./07-residency-module3-llm-engineering)

---

---

## 📞 联系作者

| 联系方式 | 入口 |
|---|---|
| 📱 微信 | `aiwf365`（扫码加好友，备注"FDE"） |
| 💬 **AI 学习交流群** | [点我扫码加入 →](https://mp.weixin.qq.com/s/P_o6azd0AwuraLkQQg6t2Q) |
| 🌐 个人网站 | https://python4office.cn/ |

<p align="center">
  <img src="https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/wx-aifw365.png" width="200" alt="程序员晚枫微信二维码"/>
</p>

> 加入 AI 编程交流群，第一时间获取 FDE 课程更新 + AI 落地实战案例。

*💡 记住：架构图不是给自己看的，是给"非技术人员也能 5 分钟看懂"——能用方框不用类图。*
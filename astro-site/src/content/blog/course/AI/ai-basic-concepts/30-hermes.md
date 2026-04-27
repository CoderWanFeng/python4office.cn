---

title: Hermes是什么？和龙虾有啥区别？一个会"长大"的AI助手
date: 2026-04-22 17:58:00
author: 程序员晚枫
categories:
- AI
- 基础概念
tags: [Python, AI编程]
- Hermes
- AI Agent
- OpenClaw
order: 30
description: Hermes最近全网爆火！它和龙虾（OpenClaw）到底有啥区别？程序员晚枫用大白话告诉你：一个让AI"活"了，一个让AI"长大"了。

---


> **作者：程序员晚枫**

Hermes最近全网爆火！GitHub两个月破4.7万星，朋友圈都在讨论。它和龙虾（OpenClaw）到底有啥区别？今天咱们用大白话彻底讲清楚。

---

## 👋 先问个扎心的问题

你有没有遇到过这种情况：
- 用AI助手帮写代码，第二天它又忘了你的项目结构
- 每次都要重新告诉AI你的工作习惯、代码风格
- 明明昨天教过AI怎么做某件事，今天它又不会了

**问题出在哪？** AI记不住。用完就忘，像条金鱼。

Hermes说：我能记住。而且越用越聪明。

---

## 🎯 一句话先说清楚

::: tip 核心结论
**Hermes = 会自己变聪明的AI助手**

完成任务后自动提炼技能、积累记忆，用得越久越好用。OpenClaw（龙虾）解决的是"AI怎么活"的问题，Hermes解决的是"AI能不能长大"的问题。
:::

---

## 🤔 Hermes是什么？

### 官方定位

**Hermes Agent** 是 Nous Research 开源的一个AI智能体框架（MIT协议）。

**核心卖点：**
- 🧠 **三层记忆系统**：会话级记忆 + 持久化画像 + 可复用Skill
- 🔧 **自动技能沉淀**：完成任务后自动提炼经验，形成可复用能力
- 🔄 **自我进化**：用得越久，系统越智能

### GitHub数据（2026年4月）

| 指标 | Hermes | OpenClaw（龙虾） |
|------|--------|------------------|
| GitHub Stars | 89k+（53天达成） | 358k+（6个月积累） |
| 开源协议 | MIT | MIT |
| 主语言 | Python | TypeScript |
| 发布时间 | 2026年2月 | 2025年底 |

---

## ⚔️ Hermes vs 龙虾：核心区别

### 设计哲学：两条完全不同的路

| 维度 | OpenClaw（龙虾） | Hermes |
|------|------------------|--------|
| **核心问题** | AI助手怎么"活"？ | AI助手能不能"长大"？ |
| **设计哲学** | 网关平台 + 生态驱动 | 自进化代理 + 学习闭环 |
| **记忆机制** | 静态Markdown文件，用户手动维护 | 三层记忆系统，AI自主管理 |
| **技能来源** | 人工预定义Skills库 | Agent自动创建技能文件 |
| **适合人群** | 企业生产环境、需要稳定可靠 | 个人/小团队、愿意长期投入 |

### 记忆系统对比

#### OpenClaw的记忆

```
记忆存储：memory.md 文件
维护方式：用户手动编辑
特点：
  - 简单可控
  - 容易丢失（文件损坏、崩溃）
  - 不会自动进化
```

#### Hermes的三层记忆

```
第一层：快照层（冻结注入）
  ├─ 常驻记忆：高频稳定信息（你是谁、做什么工作）
  └─ 位置：~/.hermes/memories/

第二层：会话层（按需召回）
  ├─ SQLite FTS5 全文搜索
  ├─ 辅助模型自动摘要
  └─ 位置：~/.hermes/sessions/

第三层：技能层（能力沉淀）
  ├─ 自动提炼的Skill文件
  ├─ YAML frontmatter + Markdown格式
  └─ 位置：~/.hermes/skills/
```

**效果对比：**

| 场景 | OpenClaw | Hermes |
|------|----------|--------|
| 告诉AI"我是Python工程师" | 写进memory.md，下次还在 | 写入常驻记忆，永久记住 |
| AI帮你完成一个复杂任务 | 任务结束，经验丢失 | 自动提炼Skill，下次直接用 |
| 用了3个月后 | 记忆文件可能变大、变乱 | 形成专属技能库，越用越快 |

---

## 🛠️ 功能特性详细对比

### 平台接入能力

| 平台 | OpenClaw | Hermes |
|------|----------|--------|
| Telegram | ✅ | ✅ |
| Discord | ✅ | ✅ |
| Slack | ✅ | ✅ |
| WhatsApp | ✅ | ✅ |
| 微信 | ✅ | ❌ |
| 飞书 | ✅ | ❌ |
| 企业微信 | ✅ | ❌ |
| **平台总数** | **50+** | **6个主流平台** |

### 模型支持

| 维度 | OpenClaw | Hermes |
|------|----------|--------|
| 模型数量 | 主要依赖Anthropic | **400+** |
| Claude | ✅ | ✅ |
| GPT系列 | ✅ | ✅ |
| DeepSeek | ✅ | ✅ |
| 通义千问 | ✅ | ✅ |
| 本地模型 | ✅（Ollama） | ✅ |
| OpenRouter | ✅ | ✅ |

### 技能生态

| 维度 | OpenClaw | Hermes |
|------|----------|--------|
| 技能来源 | ClawHub社区市场 | 动态自生成 + HermesHub |
| 技能数量 | 13000+ | 社区40+（快速增长） |
| 技能创建 | 人工编写 | **AI自动提炼** |
| 技能格式 | OpenClaw自定义 | agentskills.io开放标准 |

### 安全机制

| 维度 | OpenClaw | Hermes |
|------|----------|--------|
| 执行环境 | Docker沙箱 + SSH远程 | 6种后端（含无服务器） |
| 安全模块 | **10+** 安全模块 | 智能审批（辅助模型判断） |
| 审批机制 | 显式审批 | 智能审批 |
| CVE记录 | 139条（3 Critical） | 供应链审计，记录较少 |

---

## 🎯 实战：Hermes适合谁？

### ✅ 适合用Hermes的人

1. **长期主义者**：愿意把AI当基础设施来运营
2. **重复性工作者**：经常做类似的研究、写作、代码审查任务
3. **个人开发者**：不需要复杂的企业级功能
4. **爱折腾的人**：愿意花时间调教AI，让它越来越懂你

**典型场景：**
- 每天都要写技术文章，希望AI记住你的写作风格
- 经常做竞品分析，希望AI积累分析框架
- 长期维护一个项目，希望AI记住代码结构

### ✅ 适合用OpenClaw（龙虾）的人

1. **企业用户**：需要稳定可靠、合规审计
2. **多平台运营者**：需要接入微信、飞书等国内平台
3. **开箱即用党**：不想折腾，直接用现成的技能
4. **安全敏感者**：需要多层审批、完整日志

**典型场景：**
- 公司内部部署，需要对接飞书、企业微信
- 客服场景，需要稳定可靠
- 需要审计每一笔操作记录

---

## 💰 部署成本对比

### Hermes部署

| 方案 | 成本 | 说明 |
|------|------|------|
| 本地/VPS | $5/月起 | 4核4G即可运行 |
| Modal无服务器 | 按调用付费 | 适合低频使用 |
| 腾讯云 | **推荐** | [一键部署](https://curl.qcloud.com/VfVDRptU) |

### OpenClaw部署

| 方案 | 成本 | 说明 |
|------|------|------|
| Docker自托管 | 免费 | 一行命令启动 |
| 云服务 | $59/月起 | 官方托管版 |

---

## 📈 2025年发展趋势

### 1. 融合趋势：两条路正在靠近

**OpenClaw在学Hermes：**
- 正在开发自动技能提取功能
- 记忆系统正在升级

**Hermes在学OpenClaw：**
- 平台接入正在扩展
- 安全机制正在加强

### 2. 云端化：MaxHermes已上线

2026年4月，MiniMax发布 **MaxHermes** —— 全球首个云端沙箱Hermes。

**特点：**
- 无需本地部署
- 自动学习闭环
- Skills云端同步

### 3. 生态竞争：技能标准之争

| 标准 | 推动者 | 特点 |
|------|--------|------|
| ClawHub | OpenClaw | 成熟、丰富、审核严格 |
| agentskills.io | Hermes | 开放、可移植、AI生成 |

---

## 🔧 快速上手：部署你的第一个Hermes

### 方案一：腾讯云一键部署（推荐新手）

👉 **[点击这里一键部署](https://curl.qcloud.com/VfVDRptU)**

腾讯云提供了Hermes的一键部署方案，适合不想折腾的用户。

### 方案二：本地部署

```bash
# 1. 克隆仓库
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置模型（支持OpenAI兼容接口）
export OPENAI_API_KEY="你的API Key"

# 4. 启动
python main.py
```

### 方案三：Ubuntu完整安装

详见这篇教程：[Ubuntu 22.04 零基础安装 Hermes 完整入门指南](https://blog.csdn.net/fysuccess/article/details/160256590)

---

## ⚠️ 常见误区避坑

### 误区1：Hermes比OpenClaw先进

**真相：** 两者解决的是不同问题。

- OpenClaw解决"AI怎么接入各种平台"
- Hermes解决"AI怎么积累经验"

就像问"汽车和房子哪个先进"——没有可比性，用途不同。

### 误区2：Hermes的记忆不会丢

**真相：** 依然会丢，只是概率更低。

- 数据库比文件更可靠
- 但硬件故障、误操作依然会导致数据丢失
- **建议：** 定期备份 ~/.hermes/ 目录

### 误区3：Hermes开箱即用

**真相：** Hermes需要"调教"。

- 刚部署的Hermes和普通AI没区别
- 需要用一段时间，让它积累技能
- **至少用2-4周** 才能感受到差异

### 误区4：Hermes能替代OpenClaw

**真相：** 看场景。

- 需要接入微信、飞书？OpenClaw不可替代
- 需要企业级安全审计？OpenClaw更合适
- 个人使用、追求长期进化？Hermes更香

---

## 💬 互动时间

看完这篇文章，你更想用Hermes还是龙虾？

**留言告诉我：**
1. 你现在用的是哪个AI助手？
2. 你最希望AI记住什么？（代码风格？写作习惯？项目结构？）

---

## 📚 延伸阅读

- [Hermes 三层记忆机制彻底拆解](https://blog.csdn.net/RickyIT/article/details/160347751)
- [OpenClaw vs Hermes: 一文深入拆解两大Agent框架](https://www.huxiu.com/article/4851954.html)
- [Hermes Agent 技术架构全解](https://blog.csdn.net/musicml/article/details/159999949)
- [Ubuntu 22.04 零基础安装 Hermes 完整入门指南](https://blog.csdn.net/fysuccess/article/details/160256590)

---

## 🙏 致谢

本文参考了以下开源项目的官方文档和社区贡献：
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - Nous Research
- [OpenClaw](https://github.com/openclaw/openclaw) - OpenClaw Team

---

> **一句话总结：** OpenClaw让AI助手"活"了，Hermes让AI助手开始"长大"。两个都很强，看你更在意"眼下能用"还是"长期进化"。


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



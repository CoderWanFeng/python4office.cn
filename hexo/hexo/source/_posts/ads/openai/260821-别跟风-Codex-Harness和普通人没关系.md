---
title: 别跟风，Codex Harness 和普通人没关系
date: 2026-08-21 11:00:00
tags:
  - 公众号文章
  - OpenAI
  - Codex
  - AI 智能体
  - 程序员晚枫
categories:
  - 公众号文章
description: Codex Harness 开源了，但它是给开发者用的"代码层基建"。普通用户用 ChatGPT 桌面版就够了，没必要去折腾。
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/codex-harness-cover.jpg
---

<!-- more -->



大家好，我是程序员晚枫。

最近 OpenAI 又扔了一篇博客 **《Codex as a platform: build on the open agent harness》**，GitHub 仓库 [openai/codex](https://github.com/openai/codex) 也摆在明面上。

一时间，"Codex Harness 开源、智能体可被嵌入任何 App"的说法满天飞。

但**这篇博客和 99% 的普通人，没有半毛钱关系**。今天我就把这句话拆开讲清楚。

先说结论，别被标题唬住：

> **Codex Harness 是 OpenAI 官方开源的"智能体运行时底座"——说白了，是给程序员和集成商用的底层基建。**
> 普通人会用 ChatGPT 桌面版、Codex App，就够了。
> 没必要去纠结什么 Harness、SDK、app-server。

我知道为什么大家会迷糊——

上周 OpenAI 在内部分享里，已经把"95% 员工都在用 Codex 干非编程的活"的故事讲得人尽皆知；

这周紧跟着又发了一篇博客，告诉你"Codex 是可被集成进任何产品的平台"。

听起来像是：**"快看，连你家的产品经理都能用 Codex 搭一个智能体。"**

**不是的。**

这篇博客的目标读者，从头到尾只有一类人：**开发者**。

它的受众是：要用 Codex 做产品集成的工程师、要做内网 Agent 平台的技术 leader、要给客户演示"我们接了 OpenAI 智能体"的乙方公司。

不是坐在办公室想"怎么让 AI 帮我写周报"的你。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/codex-harness-cover.jpg)


---

## 这次到底开源了什么？

和上次DeepSeek开源了**DeepSeek Harness**一样，这次**OpenAI 把 Codex 背后的"智能体执行框架"开源了，让开发者可以直接把 Codex 集成进自己的产品里。**

注意几个关键词：

- **开源**：`github.com/openai/codex` 仓库，Apache 2.0，可以随便看、随便改、随便用
- **Harness（执行框架）**：智能体背后驱动模型、调度工具、管理权限、保持上下文的"幕后系统"
- **集成进应用**：不是让你用 Codex App，而是让开发者把 Codex 嵌进自己的产品里

![OpenAI Codex 平台架构图：产品拥有上下文、业务规则和工具，Codex app-server 提供智能体循环和沙箱执行](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/codex-platform-agent-stack.png)

*图片来源：[OpenAI 官方博客《Codex as a platform》](https://developers.openai.com/blog/codex-as-a-platform)*

这张图，就是开发者最兴奋的地方。

它回答了一个问题：**以后每个产品里，都可能内置一个 AI 智能体。**

官方博客给了一组数据：

- 同样的 GPT-5.6 Sol 模型（OpenAI 的一款推理模型），换一个好的 harness（保留推理 + 压缩上下文），在一个高难度推理测试 ARC-AGI-3 里得分从 **13.3% 涨到 38.3%**，输出 token 还省了 6 倍。
- GitHub、JetBrains、Cisco 已经开始把它集成进自己的工具链。
- Thrive Holdings 用它做税务代理，试点处理了 **7000 份申报**，准备时间减少了约三分之一。

**这就是 Codex Harness 真正的意义：它不是又一个聊天机器人，而是让“AI 智能体”变成产品底层能力的基建。**

可惜，这个基建是程序员和集成商看的，不是给你我看的。

OpenAI 自己举了个例子——Relay。

一个虚构的"货运运营仪表盘"，Codex 嵌在右边，物流运营人员点一下"Compare recovery"，智能体自动调用后台 MCP 工具分析数据，**关键操作必须人工审批**。

![OpenAI 官方 Relay 示例：Codex 嵌入货运运营仪表盘，关键操作需人工审批](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/codex-platform-relay-operations.png)

*图片来源：[OpenAI 官方博客《Codex as a platform》](https://developers.openai.com/blog/codex-as-a-platform)*

听起来很酷对吧？

但**这个酷的体验，是给开发者照着抄的样板房**。

你作为终端用户，会在 Cisco Cloud Control、GitHub、JetBrains IDE、税务工作流里，**以"嵌入式智能体"的形式碰到 Codex**。

但你不会亲手去读那篇博客，不会自己跑 `codex exec`，更不会上手去配 Codex SDK。

---

## 开源项目里的 5 个关键词

下面这些词是从博客里抠出来的，你大概率会在各类二创文章里看到。

我帮你翻译一下，**顺便告诉你"用不用管"**。

| 关键词 | 真实含义 | 普通人要不要管 |
|--------|----------|----------------|
| **Harness** | 智能体运行时（管理上下文、调用工具、申请审批） | ❌ 不用管，是开发者的事 |
| **Codex app-server** | 一个本地 Codex 进程，开发者用 gRPC 客户端连进来 | ❌ 不用管，是开发者的事 |
| **Codex SDK** | 官方发布的编程 SDK，TypeScript / Python 都有 | ❌ 不用管，是开发者的事 |
| **`codex exec`** | 非交互模式，CI 脚本里跑一次 Codex 任务 | ❌ 不用管，是开发者的事 |
| **MCP（Model Context Protocol）** | 应用给智能体"喂"工具和数据源的协议 | ❌ 不用管，是开发者的事 |

你看，整篇博客的关键词，**没有一个是终端用户要操作的**。

普通用户会用到的，只有一行：

```
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

——装个 Codex CLI，然后跟它聊天。

或者直接打开 ChatGPT 桌面版，里面的 Codex App 也能用。

**到这里就够了。**

---

## 三、为什么非要强调"和普通人没关系"？

因为我已经看到太多文章，开头是"重磅！Codex Harness 开源了"，结尾是"普通用户也能用上 AI 智能体"。

这种说法不准确，会带来三个实际后果：

### 1. 让你以为"又来一个新东西要学"

没有。

跟上次的 ChatGPT Work、Codex for OSS、Codex App 一样，**你只要会打开 ChatGPT 桌面版，就已经在用 Codex 体系了**。

不需要再学 Harness、不需要重新配置、不需要"切换工作流"。

### 2. 让你去装不必要的东西

有人看到"Codex 是开源的、智能体可被集成"，就跑回去 `git clone` 那个仓库。

然后发现自己根本编译不动——Rust 96.4%，Bazel 构建系统，Hermetic Windows SDK，pnpm monorepo……

**这不是给一个普通用户准备的项目。**

你能用到的，仍然是官网装好的 Codex CLI、桌面 App、IDE 插件。

### 3. 让你被"Agent 元年"忽悠买课

这篇博客的真正重点，是给 OpenAI 圈定"开发者生态"——以后你们公司里跑的智能体，都有可能跑在 Codex Harness 上。

它和"普通用户能不能用 AI"，没有直接关系。

如果你看到的文章把"智能体元年"、"Harness 革命"、"AI 操作系统"挂嘴边，多半是**在收割你的焦虑**。


Codex Harness 是 OpenAI 给开发者做的"智能体基础设施"。

它重要的不是"普通人今天有没有用上"，而是"以后你用的产品里，会不会更普遍地嵌入 AI 智能体"。

作为普通用户，**你真正应该关注的三件事**：

### 1. 你已经在用的 ChatGPT Work

7 月份上线的 ChatGPT Work，把 Codex 的能力从"写代码"扩展到"跨应用协作"。

你不用关心它跑在什么 Harness 上，开箱即用。

### 2. Codex App / 桌面端

如果你 ChatGPT 套餐里包含 Codex，直接在桌面 App 里用就行。

不需要安装什么 Harness，不需要配置什么 SDK。

### 3. Skills（技能）

这是 OpenAI 内部分享里反复强调的：**"把团队的隐性知识写成技能"**。

你公司里周报怎么写、客户跟进流程怎么走、行业汇报模板是什么样——都可以做成一个 Skill，让 Codex 帮你复用。

这个能力，**在 ChatGPT 桌面版里已经能用**。

---

## 面向开发者

你们才是OpenAI这篇博客的目标读者。

简单来说，OpenAI 在告诉你：

- **代码全在 `github.com/openai/codex`**，Apache 2.0 协议，可商用
- **可以用 `codex exec`** 跑非交互任务，适合 CI 脚本
- **可以用 Codex SDK** 做应用级别的集成
- **可以用 Codex app-server** 把 Codex 嵌进自己的产品里，处理多轮会话、审批、工具调用
- **示例项目 Relay** 已经放在那里，可以直接 fork

剩下的玩法，看你们自己的产品需求。

---

## 写在最后

技术圈的话术一直在变。

从 LLM，到 Agent，到 Harness，到 Platform，到 Ecosystem——

每个新词出来，都有人告诉你"这是普通人的机会、你必须跟上"。

**但你要做的，是分清楚：**

- **哪些是给你用的工具**（ChatGPT、Codex App、桌面端）—— 用就完了
- **哪些是给开发者用的底座**（Harness、SDK、app-server）—— 看个热闹就行
- **哪些是给老板画饼的 PPT**（"AI 操作系统"、"Agent 元年"）—— 笑笑就好

**Codex Harness 开源，是个对开发者极大利好的事。**

**但它和你能不能用上 AI，没有一丁点关系。**

你每天用 ChatGPT 写点东西、生成个图、回个邮件，**就已经是 AI 时代的受益者**。

别再被"又来新概念"吓到了。

省下来的时间，去干点别的。

---

**科技不高冷，AI 很好用。**

我是晚枫，关注我，带你一起玩 AI！

---

### 参考链接

- [OpenAI Codex GitHub 仓库：https://github.com/openai/codex](https://github.com/openai/codex)
- [Codex as a platform 官方博客：https://developers.openai.com/blog/codex-as-a-platform](https://developers.openai.com/blog/codex-as-a-platform)
- [Codex 官方文档：https://developers.openai.com/codex](https://developers.openai.com/codex)
- [Codex SDK 文档：https://learn.chatgpt.com/docs/codex-sdk](https://learn.chatgpt.com/docs/codex-sdk)
- [ChatGPT Work 介绍（上一篇文章）：不会写代码的人用 AI 搭了个网站](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)

---

## 相关阅读

- [不会写代码的人用 AI 搭了个网站：OpenAI 内部 95% 员工都在用智能体干非编程的活](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)
- [OpenAI 开源 gpt-oss，16G 内存就能跑](https://mp.weixin.qq.com/s/uPAJewJ-YeRnESEAAwLlkw)
- [OpenAI 突然发福利：6 个月 Pro 限时 0 元！开源人申请攻略](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [AI 圈公开的秘密：DeepSeek V4 Flash 可以免费用](https://mp.weixin.qq.com/s/KNTw9mCUcTMzcPIwNkgPVg)

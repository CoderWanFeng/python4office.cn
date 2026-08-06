---
title: OpenAI联合微软、亚马逊等5家大厂联手发布Agent Plugins：AI插件终于要统一了
date: 2026-08-07 00:45:00
tags:
  - 公众号文章
  - Agent Plugins
  - OpenAI
  - AI智能体
  - MCP
categories:
  - 公众号文章
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/agent-plugins-og.png
---

大家好，我是程序员晚枫。

昨晚睡前，我顺手打开一个OpenAI的Y2B主页看看有没有更新。

没有新模型，没有跑分，没有“再见了某某行业”。页面只说了一件事：给 AI 智能体的插件，规定一种大家都能看懂的包装方式。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/e6b968502347b01b8164c6253c0c388d.png)

但我把参与名单看完，还是愣了一下。

**Amazon、Cursor、Microsoft、OpenAI 和 Vercel 的维护者，正在一起推动 Agent Plugins 这套开放标准。**

> **如果它真的被广泛采用，未来一个插件可能不必为 Codex、Cursor、GitHub Copilot 各做一遍。AI 插件正在等自己的“USB-C 接口”。**

![Agent Plugins 官网封面](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/agent-plugins-og.png)

*图片来源：[Agent Plugins 官方网站](https://agent-plugins.org/)*

---

## 这不是插件商店，而是一张通用说明书

事情是这样的。

现在每家 AI 智能体都有自己的插件体系。Codex、Cursor、GitHub Copilot、Kiro，看起来都能安装技能、连接外部服务，但目录放哪里、配置怎么写、哪些部分能被识别，并不完全相同。

对普通人来说，这种区别很像买了五台电器，结果收到五种插头。

东西都能用，但换一台设备，就要重新找转接头。最忙的不是 AI，而是那个四处复制文件的人。

Agent Plugins 想做的事情很克制：**先规定一个插件最小应该长什么样。**

每个插件都要有一张“身份证”，告诉客户端它叫什么、采用哪个版本；里面可以放教 AI 怎么做事的技能，也可以放连接外部工具和数据的 MCP 服务。某一家产品想增加自己的独有能力，也可以放进单独的扩展区，其他产品看不懂就忽略，不影响公共部分。

官网把这叫作“可移植的最低标准”。我觉得这个词特别准确。

它没有要求所有产品长得一样，也不管每家商店怎么安装、怎么收费、怎么弹权限提醒。它只负责让大家收到同一个包裹时，至少知道标签在哪、说明书在哪、工具放在哪。

| 过去的插件 | Agent Plugins 希望做到 |
| --- | --- |
| 每个平台一套格式 | 公共部分只打包一次 |
| 换工具要重新适配 | 兼容客户端直接识别 |
| 技能和工具分散配置 | 一个插件统一携带 |
| 厂商能力互不相认 | 私有扩展互不干扰 |

目前公开的是 **Agent Plugins 1.0.0**。官网把规范状态标为 **Working Draft，也就是工作草案**。

所以它已经是一份可以实现的正式版本，但还不是刻在石头上的行业终局。坦率地讲，现在就喊“所有 AI 插件彻底统一”，跟装修刚打完地基就开始收婚礼份子钱差不多，气氛到了，房子还没封顶。

---

## 真正值钱的，是让AI能力跟着人走

很多朋友可能不知道，一个 AI 智能体能不能干好活，不只取决于它背后的模型。

我一直觉得，模型更像一个聪明的大脑。但只有大脑，没有工作方法，也没有可以动手的工具，它最多是坐在会议室里给建议。

这里顺手把三个容易混在一起的概念讲明白。

### Skill教它怎么做，MCP让它真的能做

**Skill，也就是技能，像一份经过验证的工作手册。**

它会告诉 AI，什么时候应该使用这项能力，要按什么步骤做，有哪些坑不能踩。像公众号写作规范、合同检查流程、公司内部发布清单，都可以被整理成技能。

**MCP 更像一套通用工具接口。**

它让 AI 可以在得到授权后读取资料、查询系统或者执行操作。一个负责教方法，一个负责把手伸到真实世界里干活。

而 Plugin，就是把这些东西装进同一个行李箱，再贴上一张统一托运标签。

这个设计的“啊哈时刻”就在这里：**标准没有试图统一所有 AI 的大脑，它先统一大脑随身携带的经验和工具。**

模型今天用 Codex，明天换 Cursor，后天团队决定使用 GitHub Copilot。如果技能和工具可以跟着走，用户积累下来的就不再只是某个平台里的几段聊天记录，而是一套能搬家的工作能力。

说真的，这比“某个榜单又高了两分”更值得关注。

### 首批兼容名单，已经不是小圈子实验

我把官网的兼容客户端逐项看了一遍，目前公开列出的有 5 类：

| 兼容客户端 | 已列出的公共能力 |
| --- | --- |
| VS Code | Skills、三种 MCP 连接方式 |
| Cursor | Skills、三种 MCP 连接方式 |
| GitHub Copilot | Skills、三种 MCP 连接方式 |
| ChatGPT 与 Codex | Skills、两种主流 MCP 连接方式 |
| Kiro | Skills、三种 MCP 连接方式 |

再看项目治理名单，也很有意思。

最初的技术指导委员会共有 5 位核心维护者，分别来自 Amazon、Cursor、Microsoft、OpenAI 和 Vercel。章程还特意规定，任何单一厂商都不能控制多数核心维护席位，技术讨论和提案要公开进行。

这话听着有点像委员会文件，但背后的信号很现实：**大家都想做自己的 AI 入口，却也发现插件生态继续各修各的路，最后谁都要多交一遍维护费。**

对插件作者来说，统一格式可以减少重复打包。对公司来说，一套内部流程更容易同时分发给不同工具。对普通用户来说，最直接的好处是少一点平台绑定。

你喜欢哪个 AI，可以继续用哪个。你的能力包，不必被一起扣在里面。

---

## 先别急着喊大一统，它还缺最难的一半

看到这里，可能有小伙伴纳闷：以后是不是随便下载一个插件，Codex、Cursor、Copilot 都能安全使用？

还真不能这么理解。

Agent Plugins 1.0.0 目前只统一两类公共组件：Skills 和 MCP 服务。插件的分发、安装、更新、权限提示、用户界面，仍然由各家客户端自己决定。

更重要的是，官方的“未来考虑”文件非常坦诚，v1.0.0 还没有统一下面这些问题：

- 插件需要哪些文件、网络和工具权限；
- 用户安装时应该看到怎样的授权提醒；
- 如何验证插件来自谁、有没有被篡改；
- 密钥和敏感信息应该怎样安全保存；
- 企业如何统一审核、放行、禁用和审计插件。

这几件事可不是边角料。

插件既能教 AI 做事，又可能让它连接文件、账号和外部服务。一个来路不明的插件，危险的地方不在于“回答错一道题”，而在于它可能拿着你给的钥匙，认真执行了一份有问题的说明书。

所以我自己的判断是：**Agent Plugins 解决了可移植性问题，但还没有替用户解决信任问题。**

这也是为什么它现在更像 USB-C 的接口标准，而不是一个已经审核好所有应用的手机商店。接口统一之后，劣质充电器仍然是劣质充电器。能插进去，不代表应该插进去。

我自己也还在摸索这套规范，但有三件事已经可以提前做：

1. 选择插件时，优先看官方来源和公开仓库；
2. 安装前确认它会连接什么服务、需要什么权限；
3. 涉及公司资料和重要账号时，不要因为“兼容标准”四个字就放弃审核。

回到 Agent Plugins 这块，我是真的觉得它会火。

不是因为今天多了一个新名词，而是 AI 智能体终于开始面对一个成熟生态迟早要回答的问题：**我们积累的能力，到底属于某个平台，还是应该属于我们自己？**

过去大家争的是谁的模型更聪明。下一阶段，大家还会争谁能让用户带着自己的技能、工具和工作方法自由迁移。

接口只是第一步。

但很多真正改变行业的事情，最开始看起来，也只是一张很无聊的接口说明书。

关于 AI 插件要不要统一这件事，你更期待“一个插件到处用”，还是更担心插件权限失控？评论区站个队。

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！

![AI 实战课](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

## 相关阅读

- [Codex入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [OpenAI内部分享：不懂技术怎么用好AI？附Codex官方教程](https://mp.weixin.qq.com/s/x8dvcdf1aUIGhuI_YvzlpA)
- [别再把Codex当聊天机器人了：OpenAI官方9条最佳实践](/ai/ai-tools/codex/01-best-practices-zh-中文翻译/)

## 参考链接

- [Agent Plugins官方网站](https://agent-plugins.org/)
- [Agent Plugins 1.0.0完整规范](https://agent-plugins.org/specification)
- [Agent Plugins兼容客户端名单](https://agent-plugins.org/compatible-clients)
- [Agent Plugins项目治理章程](https://github.com/agentplugins/agent-plugins-spec/blob/main/GOVERNANCE.md)
- [Agent Plugins未来考虑事项](https://github.com/agentplugins/agent-plugins-spec/blob/main/FUTURE_CONSIDERATIONS.md)
- [Agent Plugins规范源码仓库](https://github.com/agentplugins/agent-plugins-spec)

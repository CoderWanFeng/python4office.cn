---
title: AMD 又送了：中国站 15 款模型免费调，不用绑卡，Claude Code 能直接接
date: 2026-11-01 21:00:00
tags:
  - 公众号文章
  - 免费大模型
  - 免费AI
  - 大模型
  - AMD
categories:
  - 免费大模型系列
---

> 都说天下没有免费午餐，大模型第一个不服。
> 今天带大家免费用的是——**AMD 中国站的 Token Factory**。

<!-- more -->

这个系列薅了两年，我有个判断标准越来越清晰：

**看它要不要你绑卡。**

要绑卡的，多半是试用；不要绑卡的，才是真免费。

AMD 这次这个口子，全程不让你填卡，手机号或邮箱收个验证码就给 Key。而且有个别人没有的东西——**它原生支持 Anthropic 协议，Claude Code 换个地址就能接。**

## 一、这不是我上次写的那个 AMD

先说清楚，避免混淆。

我 8 月写过 [AMD 送你 100 美元 GPU 算力](260812-免费用大模型-AMD送你100美元GPU算力.md)，那是**全球站**的 GPU 云：给你 100 美元信用值，有效期 30 天，自己上去开实例跑模型。

这次是**中国站**的 **Token Factory**，完全是另一回事：

| | 全球站 Radeon Cloud | 中国站 Token Factory |
|---|---|---|
| 给你什么 | GPU 算力（自己部署） | **现成的模型 API** |
| 门槛 | 加入开发者计划、申请额度 | 注册登录即得 |
| 有效期 | 100 美元 / 30 天 | 每日额度，**北京时间 00:00 重置** |
| 要不要绑卡 | 否 | **否** |

官方一句话讲得很明白：**Token Factory is on the China site only**——只有中国站有。而且两站的账号、credits、Key、实例**互不通用**，一个站的 Key 拿到另一个站调不通，代码里的 base URL 必须对应你注册的站。

所以别去全球站找这个入口，找不到的。

## 二、三步拿到 Key

**第一步**：打开 `developer.amd.com.cn/radeon/tokenfactory`，登录。手机号、邮箱验证码都行，也支持 GitHub 账号。**全程没出现填卡的页面。**

**第二步**：页面顶部有张 **Your API key** 卡片，里面就是 Base URL 和你的 Key。Key 默认隐藏，点 Show key 或 Copy。

Key 长这样：`rc-` 开头。**一个 Key 通调所有模型**，不用每个模型单独申请。

**第三步**：改 base_url 就能调。

```bash
export RADEON_API_KEY=rc-...

curl https://developer.amd.com.cn/radeon/api/v1/chat/completions \
  -H "Authorization: Bearer $RADEON_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"DeepSeek-V4-Flash","messages":[{"role":"user","content":"你好"}]}'
```

Python 也一样，换 base_url 就行：

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://developer.amd.com.cn/radeon/api/v1",
    api_key="rc-...",
)
resp = client.chat.completions.create(
    model="DeepSeek-V4-Flash",
    messages=[{"role": "user", "content": "你好"}],
)
```

任何 OpenAI 客户端——curl、官方 SDK、LangChain、Cherry Studio——都能直接接。

不知道自己能调哪些模型？问一句：

```bash
curl https://developer.amd.com.cn/radeon/api/v1/models \
  -H "Authorization: Bearer $RADEON_API_KEY"
```

## 三、真正的杀手锏：Anthropic 协议原生支持

这是我看到最意外的一点。

官方文档原话：**Token Factory also accepts the Anthropic Messages API, for clients such as Claude Code.**

翻译过来就是：**Claude Code 这类工具，换个地址、填个 Key 就能用。**

```bash
curl https://developer.amd.com.cn/radeon/api/v1/messages \
  -H "x-api-key: $RADEON_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"model":"DeepSeek-V4-Flash","max_tokens":1024,
       "messages":[{"role":"user","content":"Hello"}]}'
```

Claude Code 平时是要订阅的，订阅费真不是小钱。你要是不确定值不值，先用这个跑两天再说——**这是我见过最低成本的试错方式。**

补充一句：OpenCode 已经原生集成了这个端点。但据开发者反馈，**ZCode 目前接不上**（握手失败），别白折腾。

## 四、能调哪些模型

官方模型目录目前列了 **16 个端点**，其中标注 Public Free 的大约 15 个（**清单会变，以你打开时看到的为准**）：

| 类型 | 模型 |
|---|---|
| **旗舰文本** | DeepSeek-V4-Flash、DeepSeek-V4.1-Flash、Qwen3.8-Flash-Next、GLM-5.3-Flash、MiMo-V2.6-Flash、Gemma-4-31B-IT |
| **视觉多模态** | DeepSeek-V4-Flash-Vision-Exp、MiniCPM-V-4.7-1B、MiniCPM-V-4.7-35B-A3B |
| **轻量端侧** | MiniCPM5-2B |
| **专用端点** | MinerU2.5-Pro（文档解析）、OmniVoice（语音）等 |

DeepSeek-V4-Flash 给的是 **1M 上下文**（1,048,576 tokens），不截断。

注意两点：

- **专用端点接不了 Claude Code**——语音、文档解析这类只能走 OpenAI 协议单独调。
- 目录里还有 **Dedicated** 那一档，是拿你自己的 credits 部署专属实例的，**不是免费的**，别看混了。

顺带说个有意思的细节：半个月前有人写这个口子时，免费清单还是 4~5 款；现在已经到 15 款。**这个清单是活的，在扩。**

## 五、额度到底够不够用

官方的计量单位叫 **points（pts）**，比如 0.14 pts / 百万 tokens。

**pts 不是钱，也不是 credits**，它只是拿来对你的每日上限做折算的尺子。官方原话：*They aren't money, and they aren't credits.*

规则是这样：

- **每日上限按 pts 算，北京时间 00:00 重置**
- RPM（每分钟请求数）和并发数，**按账号和按 Key 分别限制**
- 撞上限返回 **429**，带 `Retry-After`
- **每个响应的 header 里都带着你的剩余额度**
- 控制台 **Credits & Usage** 页也能看

官方没给统一的额度数字——**每个账号不一样，我只信你自己试出来的数**。第三方实测里见过「每日 1.000000 pts、RPM 20」这种配置，按 0.14 pts/百万 tokens 折算，一天大约 **700 万 tokens**。够不够你造，自己除一下就知道。

还有一条容易被忽略：**Key 泄露 = 别人花你的额度。** 官方文档特意写了一句 *anyone who has it can spend your daily allowance*，所以 Key 别往 GitHub 上提交，需要的话可以去 Authentication 页 rotate。

## 六、按我那套框架，它算哪一档

我前几天写了篇 [免费也分「保质期」](../免费大模型系列/261101-免费也分保质期-白嫖过的渠道按寿命分三档.md)，把白嫖渠道按寿命分了三档。拿它套一下 AMD 这个口子：

- **偏第一档**：不绑卡、无有效期栏、官方定位 free and always on、额度每日自动重置——**没有"到期作废"这个说法**
- **带一点第二档特征**：每日有上限，用完得等第二天；而且是 BETA，清单和额度都可能调整

我的结论是：**可以当长期的日常主力用，但别当唯一依赖。** 每天 700 万 tokens 对写代码、跑 Agent 绰绰有余，跑批量数据集就不够看了。

> 🔗 **【推广位 A】AI 工具 / 编程客户端类推广链接**
> 建议放：Claude Code 替代方案、编程客户端、Agent 工具
> 配套文案示例：「想接进 Claude Code 这类工具的，按上面三步走就行，一条命令的事。」
> ⚠️ 发布前删掉本段（保留上方正文即可）

## 七、三条红线，最后说一遍

这部分最重要，别跳过。

**1. 条款白纸黑字：不是生产服务。**
原文：*Token Factory is a free trial and development service, not for production.* 拿它跑个人项目、做原型验证没问题，**公司的线上业务别往这挂**。

**2. 禁止转售。**
原文：*Reselling access is not allowed.* 别拿这个 Key 去给别人做付费中转。

**3. 别往里贴公司资料。**
免费端点没有数据不出域的承诺。**公司机密、客户名单、内部代码仓库，一律别往里发。** 这条对所有免费 API 都成立，不只是 AMD。

## 八、一句话总结

三句话记住这个口子，再决定值不值得你折腾：

- **15 款模型，OpenAI 和 Anthropic 两套协议都能接，Claude Code 直接可用**
- **不绑卡，每日一档额度，零点重算**
- **条款写的是试用和开发，别上生产**

说白了：**白给的东西，值钱的那部分都写在条款里。**

> 🔗 **【推广位 B】结尾引导位（社群 / 课程 / 星球 / 公众号）**
> 建议放：晚枫 AI 圈、OPC 课程、公众号关注引导
> 配套文案示例：「这类口子我一发现就发在群里，想跟着薅的来找我。」
> ⚠️ 发布前删掉本段（保留上方正文即可）

---

本文信息核实于 2026-11-01，来源为 AMD Radeon Cloud 官方文档（`amd-aim.github.io/radeon-cloud-docs`，最后更新 2026-10-21）及第三方实测。**模型清单、额度、BETA 状态以你打开时的官方页面为准。**

相关阅读：
- [免费也分「保质期」：我把白嫖过的渠道按寿命分成了三档](../免费大模型系列/261101-免费也分保质期-白嫖过的渠道按寿命分三档.md)
- [AMD 送你 100 美元 GPU，大模型随便跑](260812-免费用大模型-AMD送你100美元GPU算力.md)（全球站，另一回事）
- [免费用 DeepSeek-V4-Flash：6 个渠道实测](../deepseek/260805-免费用DeepSeek-V4-Flash-6个渠道实测.md)
- [比白嫖大模型更爽的，是免费用 AI（完整路线图）](../免费大模型系列/260919-比白嫖大模型更爽-免费用AI完整路线图.md)

**科技不高冷，AI很好用。**

关注我，用上免费大模型。

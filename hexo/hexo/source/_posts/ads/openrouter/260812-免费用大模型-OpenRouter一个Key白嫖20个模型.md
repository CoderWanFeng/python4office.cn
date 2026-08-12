---
title: 一个 Key 白嫖 20 个大模型，OpenRouter 太狠了
date: 2026-08-12 23:20:00
tags:
  - 公众号文章
  - 免费大模型
  - OpenRouter
  - 免费AI
  - API
categories:
  - 公众号文章
cover: https://images.unsplash.com/photo-1639762681057-408e52192e55?q=80&w=1200&auto=format&fit=crop
---

<!-- more -->

> 都说天下没有免费午餐，大模型第一个不服。
> 今天带大家免费用的是——OpenRouter，一个 API Key 白嫖 20+ 个旗舰大模型。

大家好，我是程序员晚枫。

之前分享的免费大模型方法，不管是 DeepSeek 还是 GLM，都是一个平台用一个模型。今天这个不一样——**一个平台，20 多个免费模型，一个 API Key 全搞定。**

它叫 OpenRouter。

DeepSeek V4 Flash、Llama 4 Maverick、NVIDIA Nemotron 3 Ultra、Qwen 3.5、Mistral Large……这些分属不同公司的旗舰模型，在 OpenRouter 上全部标了 `:free` 后缀，免费调用，输入输出零成本。

**关键是不用信用卡，Google 或 GitHub 登录就能开始用。**

---

## 20+ 免费模型，到底有哪些

先看清单。截至 2026 年 8 月，OpenRouter 上的免费模型包括：

| 模型 | 上下文 | 亮点 |
|------|-------:|------|
| DeepSeek V4 Flash (free) | 1M | 省钱之王，百万上下文 |
| NVIDIA Nemotron 3 Ultra (free) | 1M | 550B MoE，推理怪兽 |
| NVIDIA Nemotron 3 Super (free) | 262K | 120B MoE，高吞吐 |
| Meta Llama 4 Maverick (free) | 128K | Llama 4 旗舰 |
| Meta Llama 4 Scout (free) | 128K | 轻量版 |
| OpenAI gpt-oss-120b (free) | 128K | OpenAI 开源 120B |
| Qwen 3.5 (free) | 多种 | 通义千问全系列 |
| Mistral Small 3 (free) | 32K | 欧洲开源代表 |
| Cohere North Mini Code (free) | 256K | 专为编程优化 |

还有一个更省心的玩法：用 `openrouter/free` 这个路由模型，你不用手动选，OpenRouter 自动从所有免费模型里帮你挑一个最合适的。

**一个 API Key，调完上面所有模型，不用分别注册 20 个平台。**

免费额度的限制是：免费账户每天 50 次请求，每分钟 20 次。充值 10 美元（一次性，不过期）后，限额提升到每天 1000 次。对个人开发和测试来说，50 次/天基本够用。

---

## 3 步开始用，改一行代码就能切换模型

### 第一步：注册并获取 API Key

打开 [openrouter.ai](https://openrouter.ai/)，用 Google 或 GitHub 登录。进入后台，创建一个 API Key，复制保存。

不需要信用卡，不需要手机验证，登录就能用。

### 第二步：选你要用的免费模型

在 [openrouter.ai/models?max_price=0](https://openrouter.ai/models?max_price=0) 可以看到所有免费模型的完整列表。找到你要用的模型 ID（以 `:free` 结尾），记下来。

比如 DeepSeek V4 Flash 的免费版，模型 ID 就是 `deepseek/deepseek-v4-flash:free`。

### 第三步：用 OpenAI 兼容格式调用

OpenRouter 的 API 完全兼容 OpenAI 格式。你现有的代码，只需要改两个地方：

- `base_url` 改成 `https://openrouter.ai/api/v1`
- `model` 改成带 `:free` 后缀的模型 ID

就这一行改动，你就能从付费的 GPT 切到免费的 DeepSeek、Llama、Nemotron。

**如果你用 Cherry Studio、OpenCode、Cursor 这类工具，直接在设置里填 OpenRouter 的 API Key 和 Base URL 就行，不用写代码。**

---

## API 网关为什么能让你免费

你可能会问：这些模型在各自官方平台都是收费的，为什么 OpenRouter 能免费提供？

**答案是一个词：聚合。**

OpenRouter 的角色类似于「大模型界的携程」。它不自己训练模型，而是把几十个模型提供商的 API 聚合到一个入口。你通过 OpenRouter 调用，它在后台帮你路由到最合适的提供商。

为什么能免费？三个原因：

第一，**模型提供商愿意拿出免费额度**。DeepSeek、NVIDIA、Meta 这些公司希望你用他们的模型而不是竞争对手的，免费是最直接的获客方式。OpenRouter 帮他们做分发，他们提供免费配额。

第二，**免费模型的数据可能被用于训练**。你调免费 API 时，对话内容可能被收集去改进模型。这就是免费的代价——你用数据换 token 钱。

第三，**免费用户是未来的付费用户**。OpenRouter 的商业模式是付费模型抽成 5%。免费用户用着用着，发现需要更高配额、更多模型，自然就充值了。免费层就是他们的获客漏斗。

所以，**免费模型适合开发测试和个人项目，公司代码和客户数据别往上放。** 这不是 OpenRouter 的问题，所有免费 AI 服务都是这个逻辑。

一个值得注意的细节：免费端点的上下文窗口有时比付费版小。长文本任务在付费版能跑通，在免费版可能被截断。用之前先看看模型页面的上下文长度说明。

---

![AI 实战课](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

## 相关阅读

- [别怪我没提醒你：DeepSeek V4 Flash 可以免费用](../deepseek/260805-免费用DeepSeek-V4-Flash-6个渠道实测.md)
- [以前用 GLM-5.2 花钱买，现在每天 100 个名额免费抢](../atomgit/260810-免费用GLM-5.2-AtomCode限时白嫖指南.md)
- [免费大模型系列 · 总索引](../免费大模型系列/免费大模型系列总索引.md)

## 参考链接

- [OpenRouter 官网：https://openrouter.ai/](https://openrouter.ai/)
- [OpenRouter 免费模型列表：https://openrouter.ai/models?max_price=0](https://openrouter.ai/models?max_price=0)
- [OpenRouter 免费模型合集页：https://openrouter.ai/collections/free-models](https://openrouter.ai/collections/free-models)
- [OpenRouter API 文档：https://openrouter.ai/docs](https://openrouter.ai/docs)

---

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！

---
title: GitHub 2万星的开源神器：一个接口薅26家免费额度，但其中88个模型来路不明
date: 2026-08-26 01:05:00
tags: [公众号文章, 免费大模型, FreeLLMAPI, 免费AI, API]
categories: [公众号文章]
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260826-freellmapi-cover.png
---

<!-- more -->

> 都说天下没有免费午餐，大模型第一个不服。
> 今天带大家免费用的是——FreeLLMAPI，一个接口薅尽26家大模型的免费额度。

大家好，我是程序员晚枫。

最近我又挖到一个 GitHub 上很火的开源项目：FreeLLMAPI。它干了一件听起来很魔幻的事——把你散落在 Google、Groq、Cerebras、OpenRouter 等二十几家平台的免费额度，全部缝成一个 OpenAI 兼容的接口。

一家公司的免费额度少？没关系，它自动帮你换另一家。这家用完了，下一家顶上。

听起来像是"白嫖党"的终极武器。但我实际用了几天之后，反而想先给你泼一盆冷水：

**它目录里那些"免费GPT-5、o3、Grok 4"，你最好别当真。**

---

## 免费额度太碎，这个项目帮你拼起来

用过大模型接口的人都知道一个痛点：每家厂商都给你一点免费额度，但规则全不一样。

有的按分钟限流，有的按天限流；有的注册要手机号，有的要绑卡；有的只给 REST 接口，有的文档还全是英文。

你想多薅几家羊毛？可以。但代价是记一堆账号、看十几个后台、写一堆适配。

FreeLLMAPI 的思路很简单：**与其分别去 26 家餐厅排队，不如在家开一个小厨房，把各家外卖接进来。**

![FreeLLMAPI 免费额度堆叠图](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260826-freellmapi-free-tier.png)

*图片来源：[FreeLLMAPI 官网](https://freellmapi.co/)*

你只需要做三件事：

- 在本地或服务器上用 Docker 把它跑起来
- 把各家厂商的接口 Key 填进去
- 拿到一个统一的 `freellmapi-xxx` key

之后，你平时用的 AI 客户端只需要改一行地址，就能调用所有接进来的模型。

截至我写这篇文章的时候，这个项目在 GitHub 上已经拿到了 **20179 个 Star**。官方数据宣称聚合了 **34 家供应商、635 个模型端点、每月约 74 亿 token 的免费额度**。

74 亿 token 是什么概念？大概够你写几百篇长文、跑几千次对话。对个人开发者和重度 AI 用户来说，确实诱人。

可能有读者会问：这和 OpenRouter 有什么区别？

OpenRouter 是云端聚合，你的 key 放在 OpenRouter 的服务器上；FreeLLMAPI 是自托管，key 存在你自己的电脑或服务器里。对隐私敏感、希望数据不出自己机器的人来说，后者更安心。但代价是你要自己维护服务。

| 对比项 | OpenRouter | FreeLLMAPI |
|---|---|---|
| 部署方式 | 云端即用 | 本地/服务器自托管 |
| API Key 存放 | OpenRouter 服务器 | 你自己的机器 |
| 适合人群 | 想快速尝鲜 | 对隐私有要求、想长期用 |
| 免费模型 | 20+ 个 `:free` 模型 | 600+ 个，含官方和第三方 |

---

## 真正厉害的不是省钱，是路由调度

这个项目最让我意外的，不是"免费"，而是它背后的调度逻辑。

你想想，每家免费额度本质上都是一个"限流沙漏"：每分钟只能流这么多，每天总共只能流这么多。单独一个沙漏很小，但把几十个沙漏接在一起，水流就大了。

问题是：怎么让水均匀地流，还不让任何一个沙漏被吸干？

FreeLLMAPI 做了三件事：

**第一，实时记账。** 它给每个 key 都记着每分钟请求数、每天请求数、每分钟 token 数、每天 token 数。哪个 key 快用完了，下次请求就不找它。

**第二，自动切换。** 如果某家返回"额度耗尽"或者超时，路由器会立刻把这个 key 放进"冷却期"，然后重试下一家。最多可以重试 20 次。

**第三，粘性会话。** 多轮对话里，它会在 30 分钟内尽量保持同一个模型。不然聊到一半突然换人，前面的上下文对不上，回答质量会断崖式下跌。

说白了，它就是在做大模型时代的"智能导航"：哪条路不堵，就走哪条；前面堵车，自动换匝道。

这就是免费额度能被"拼起来"的底层原理。不是魔法，是工程。

---

## 但我必须泼冷水：免费GPT-5那部分，别碰

好话说完，该说风险了。

FreeLLMAPI 的网站目录里，有一个叫 NavyAI 的供应商，贡献了 88 个模型。其中包括 GPT-5、o3、Grok 4.3、GPT-5.4 这些顶级模型，全部标着"$0"。

但问题是：OpenAI 和 xAI 官方的免费层里，根本没有这些旗舰模型。

它们是怎么"免费"的？大概率是灰色中转站，也叫"影子 API"——通过非官方渠道把付费接口再分发给用户。外面看起来是 GPT-5，里面跑的是什么，只有 NavyAI 自己知道。

这不是我瞎猜。2026 年 3 月，德国 CISPA 信息安全中心发表了一篇论文，题目就叫《Real Money, Fake Models: Deceptive Model Claims in Shadow APIs》。他们对 17 个影子 API 做了系统审计，发现 **45.83% 的模型指纹测试没有通过身份验证**——也就是说，你调用的可能不是你以为的那个模型。

论文还测了医疗问答场景：Gemini-2.5-flash 官方接口正确率 83.82%，而通过影子 API 掉到了约 37%。

所以我的建议很明确：

- **FreeLLMAPI 的开源路由本身是个好工具**，尤其适合聚合 Google Gemini、Groq、Cerebras、OpenRouter 免费区、智谱、NVIDIA NIM 这些官方免费层。
- **NavyAI 提供的"免费GPT-5/o3/Grok"，离远点。** 不要拿它处理敏感信息，更不要用于正式项目。

那什么样的人适合用 FreeLLMAPI？我总结了两类：

- **想一次接多家官方免费层的人**：省去分别注册、分别适配的麻烦。
- **对数据出域敏感的人**：公司或团队希望接口 key 留在自己的机器里，而不是交给第三方平台。

如果你只是想随便聊聊天，直接去各家官网用免费版更省事。这个项目的价值，在于"聚合"和"可控"，而不是"免费 GPT-5"。

![FreeLLMAPI 后台模型列表](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260826-freellmapi-dashboard.png)

*图片来源：[FreeLLMAPI GitHub 仓库](https://github.com/tashfeenahmed/freellmapi)*

这就好比有人告诉你，公园所有景点都能免费玩。结果进去一看，大部分确实是免费的，但有几个"免费项目"其实是私人在围墙外搭的草台班子，门票收了，设备还是坏的。

---

说到底，免费额度这件事，拼的不是谁找的渠道多，而是谁分得清"真免费"和"假免费"。

FreeLLMAPI 把前者做得非常漂亮：一个接口、自动切换、本地托管、隐私可控。但它目录里那些来路不明的"免费旗舰模型"，恰恰是新手最容易踩的坑。

工具是工具，信任是信任。再香的羊毛，也得先确认羊是谁家的。

**如果让你选：一边是额度更大但来源不透明的渠道，一边是额度有限但官方正规的渠道，你站哪一边？评论区聊聊。**

**科技不高冷，AI很好用。**
我是晚枫，关注我，免费大模型只在这里讲。

---

### 参考链接

- [FreeLLMAPI 官网：https://freellmapi.co/](https://freellmapi.co/)
- [FreeLLMAPI GitHub 开源仓库：https://github.com/tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi)
- [FreeLLMAPI 定价说明：https://freellmapi.co/pricing](https://freellmapi.co/pricing)
- [CISPA：Real Money, Fake Models: Deceptive Model Claims in Shadow APIs：https://arxiv.org/abs/2603.01919](https://arxiv.org/abs/2603.01919)

## 相关阅读

- [AI 圈公开的秘密：DeepSeek V4 Flash 可以免费用](https://mp.weixin.qq.com/s/KNTw9mCUcTMzcPIwNkgPVg)
- [英伟达"掀桌子"了：国产大模型免费用，智谱、MiniMax、LLaMA...](https://mp.weixin.qq.com/s/bD0U2NvMzbSgtaRK2OWAcQ)
- [用上 OpenCode 的5 个免费大模型，省了我 200 刀 ChatGPT 年费](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)

![AI 实战课](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

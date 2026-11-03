---
title: 美团放大招：LongCat 白送 1000 万 Token，5 分钟接进 WorkBuddy
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/longcat-free-workbuddy-cover.jpg
date: 2026-11-02 12:00:00
lastmod: 2026-11-03
tags: [公众号文章, 免费大模型, 美团, LongCat, WorkBuddy, 免费AI, API接入]
categories: [公众号文章]
---

<!-- more -->

> 都说天下没有免费午餐，大模型第一个不服。
> 今天带大家免费用的是——美团 LongCat，注册实名直接送 **1000 万 Token**，走我的邀请链接**你我各得 1000 万**，5 分钟接进 WorkBuddy。

大家好，我是程序员晚枫。

AI 用得越久，账单越厚，这事儿懂的都懂。所以我一直在追各家大厂的免费口子——上一期刚说完智谱每天送 3 亿 Token，这一期轮到美团。

**美团自家的 LongCat 平台**，11 月初刚把 **LongCat-2.5-Preview** 正式推上线，并且给新用户开了一个非常实在的福利：**完成实名认证，系统自动发放 1000 万 Tokens 资源包**。老用户（已实名或买过服务）也有 500 万。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/longcat-25-release.jpg)

而且它是**官方直供的 API**，不是第三方聚合平台转手卖——不需要绑卡，注册完就能用；**从我的邀请链接进来，实名认证之后你我各多拿 1000 万 Tokens**。

我实测跑通了整条链路，压缩成了三步：**领额度 → 生成 Key → 填进 WorkBuddy**。全程零门槛，一分钱不花。

**先看 79 秒视频版，走一遍完整流程 👇**

<iframe src="//player.bilibili.com/player.html?bvid=BV1oc4P6GEL9&page=1&high_quality=1&danmaku=0&autoplay=0" scrolling="no" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="480"></iframe>

---

👉 [点击这里试试美团 LongCat 开放平台： https://longcat.chat/platform/product?inviteCode=SLBOB4YQ](https://longcat.chat/platform/product?inviteCode=SLBOB4YQ)

---

## 一、先说清楚：这次免费的是什么

打开 [开放平台： https://longcat.chat/platform/](https://longcat.chat/platform/)，顶部横幅写得很直白：

> **邀请新用户实名，各得 1000 万 Tokens！拼团返现，最高返 50%！**

点进去是这块：

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/longcat-free-tokens.jpg)

三个关键信息，我替你划重点：

| 项目 | 内容 |
|---|---|
| **实名认证奖励** | 完成认证后，系统**自动发放 1000 万 Tokens 资源包** |
| **老用户奖励** | 已完成实名认证或购买过服务的老用户，发放 **500 万免费 Tokens**，去「用量管理」页查余额 |
| **Cache 命中** | **免费**，且不计入赠送 Token 的消耗 |
| **邀请玩法** | 「活动与权益 → 邀请有礼」，拼团返现最高 50% |
| **邀请奖励** | 从带邀请码的链接注册并完成实名，**邀请双方各得 1000 万 Tokens**，再叠上平台新人礼包合计最高 **2000 万** |

最后一条「Cache 命中免费」是很多人忽略的彩蛋——重复调用时命中缓存的部分不烧额度，等于给免费额度加了一层保险。

**模型本身**是 LongCat-2.5-Preview，美团自研，主打 Agentic 场景，官方文档里标的数据是：**上下文 1M Tokens，最大输出 128K Tokens**。

> 一句话判断：这波是真的给量，不是给 1000 次调用。1000 万 Token 足够你把日常办公那点用量包圆了。

---

## 二、领额度：注册只要 2 分钟

### 第一步：打开平台，扫码登录

直接点上面那条邀请链接（或者访问 `longcat.chat/platform/`），点注册，会跳到**美团 passport** 登录页。邀请码已经带在链接里，**不用手填**。左边是 LongCat-2.5-Preview 的视觉，右边两种登录方式：

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/longcat-register.jpg)

- **美团或微信 APP 扫码登录**（推荐，一步到位）
- 手机号验证码登录

登录成功直接进平台，**不需要绑卡、不需要充值**。

### 第二步：完成实名认证，Token 自动到账

在平台里找到「用量管理」或「活动与权益」，走完实名认证，**1000 万 Tokens 资源包自动发放**。这一步不涉及任何支付。

> 如果你是从上面那条邀请链接进来的，实名认证通过后**邀请奖励会另外自动到账**——你一份，我一份。所以链接别自己删掉换成裸网址，也**不用替我去拉人**，你把自己的额度领到手就算帮上忙了。

> 顺带说一句：横幅上那个「拼团返现最高 50%」是拉人头的玩法，**不参与也不影响你的 1000 万**，别被它劝退——你只要点一下上面的邀请链接、自己实名就够了。

---

## 三、生成 API Key（这一步最关键）

拿到额度后，进左侧菜单的 **API Keys** 页面，点右上角「创建 API Key」。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/longcat-api-keys.jpg)

页面上已经有一条我自己的 Key（名字「程序员晚枫」，创建于 2026-11-01）。

**这一步有两个坑，必须注意：**

1. **Key 只在创建时可见一次。** 官方原话：「API Key 仅在创建时可见，请及时复制并妥善保存，丢失需重新创建。」关掉弹窗就找不回来了，**先存进备忘录**。
2. **不要把 Key 贴到公开仓库、前端代码、截图或日志里。** 泄露了额度就被人白嫖，你只能自己重建。

---

## 四、5 分钟接进 WorkBuddy

LongCat 走的是 **OpenAI 兼容协议**，所以任何支持「自定义模型」的工具都能接。WorkBuddy 的完整配置如下。

### 操作路径

打开 WorkBuddy，在**对话框右下角**点「添加自定义大模型」（也可以从 设置 → 模型 进入），弹出「添加模型」窗口。

### 填三样东西，一样都别漏

| 配置项 | 填什么 | 说明 |
|---|---|---|
| **供应商** | 自定义 | WorkBuddy 这里明确写了「仅支持 OpenAI 兼容协议 API」，LongCat 正好是 |
| **接口地址** | `https://api.longcat.chat/openai` | 官方文档给的 OpenAI 兼容地址 |
| **API Key** | 上一步生成的 `ak_2t...` 那串 | 只在创建时显示一次 |
| **模型名称** | `LongCat-2.5-Preview` | 当前平台开放的模型 ID |

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/longcat-wb-add-model.jpg)

填完点「测试连接」，顶部弹出绿色的 **「连接成功」**，再点「保存」——就通了。

### 高级配置怎么选

弹窗下方「高级配置」有一排开关：**工具调用 / 图片输入 / 思考模式 / 深度思考模式 / 各级关闭思考**。

我的建议：

- **工具调用** ✅ 开 —— 你的 AI 能自己读写文件、跑命令，这才是 Agent 的意义
- **图片输入** ✅ 开 —— LongCat-2.5 是原生多模态，截图、长图都能看懂
- **深度思考模式** ❌ 先关 —— 开了会额外消耗 token 且等待变长，赠送额度不要钱也没必要干等，简单任务用不上

### 保存后在哪儿选模型

保存后回到对话框，模型选择器里就能看到你刚加的 LongCat-2.5-Preview，点一下就能用。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/longcat-wb-in-use.jpg)

---

## 五、三个坑，别踩

### 坑 1：接口地址少了 `/v1`，报 404

官方 SDK 示例里 `base_url` 写的是 `https://api.longcat.chat/openai`，但 REST 完整地址其实是 `https://api.longcat.chat/openai/v1/chat/completions`。不同 SDK 版本拼接路径的方式不一样。

**如果报 404，就把接口地址改成 `https://api.longcat.chat/openai/v1` 再测一次。** 我实测填 `https://api.longcat.chat/openai` 是能直接连上的，工具会自己拼 `/v1/chat/completions`。

### 坑 2：模型名称写成了 `LongCat-2.5`

官方文档正文列的 model id 是 `LongCat-2.5`，但**平台当前实际开放给开发者接入的是 `LongCat-2.5-Preview`**（弹窗和媒体稿都写的是 Preview）。WorkBuddy 里按 `LongCat-2.5-Preview` 填，实测连接成功。

不确定的话，在平台「接口文档」页能查到当前可用的模型列表。

### 坑 3：思考模式默认开着，等半天没反应

默认开启的思考过程本身也在消耗 token。赠送额度虽然不要钱，但**等待时间是实打实的**。简单任务把「深度思考模式」关掉，体验会顺很多。

---

## 六、其他工具同理

因为 LongCat 是 OpenAI 兼容接口，**一个 Key 全工具通用**。[官方文档： https://longcat.chat/platform/docs/zh/](https://longcat.chat/platform/docs/zh/)的侧栏里，直接列出了 WorkBuddy 之外的这些工具配置页：

**Claude Code、Codex、OpenCode、Cline、Kilo Code、Cherry Studio、Chatbox、CodeBuddy、OpenClaw、CatPaw、Hermes Agent、CC Switch**

以 OpenCode / Trae 这类工具为例，改 Base URL + 填 Key + 写模型名，三样搞定；如果工具支持 Anthropic 协议，还能用 `https://api.longcat.chat/anthropic` 这个地址（记得加 `anthropic-version: 2023-06-01` 请求头）。

> 一个小提醒：接口限流触发时返回 HTTP `429`，响应里带 `retry_after`（比如 60 秒）。官方建议客户端实现**指数退避重试**。自己写脚本调用的时候记得处理，不然高并发下容易误判成 Key 失效。

---

## 七、我的实测感受

配完之后，我让它干了几件日常活：写周报、总结一份长文档、把一段 Python 脚本批量改名。

几点真实体感：

- **1M 上下文是真的能装东西。** 我把一整份几十页的技术文档丢进去让它通读并总结，没有出现「前面的内容忘了」这种经典问题。这是 1M 上下文的实用价值。
- **图片输入可用。** 我直接截图丢给它识别排版问题，LongCat-2.5 的原生多模态没掉链子。
- **响应速度属于中规中矩。** 比某些付费轻量模型慢一点，但也没到需要干等的地步。开了深度思考就另说了——那属于它在认真想。
- **免费额度的消耗速度：** 日常问答、文档总结这类任务，1000 万 Token 能用相当长一段时间。**缓存命中的部分还不计数**，等于又省了一截。

**另外一个意外发现：WorkBuddy 里其实已经内置了美团的 Space-Bunny，倍率 0.08x。** 那是目前最便宜的一档，日常用它其实已经挺够。那为什么还要自己接 LongCat-2.5-Preview？

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/longcat-wb-model-list.jpg)

因为 Space-Bunny 是**平台内的低价档位**，有倍率系数和额度约束；而自己接官方 API 拿到的是**完整的 LongCat-2.5-Preview 能力**，1M 上下文、原生多模态、不受倍率折扣影响。**两个不冲突，按场景选就行**——赶时间用 Space-Bunny，要旗舰能力就切到你自己接的 LongCat。

---

## 八、为什么美团愿意送 token

值得说两句，不然大家用着不踏实。

美团的打法很清晰：**LongCat-Flash 从开源起就是「低价甚至免费」的路线**，用极低的价格先把开发者拉进生态。这次 1000 万 Token 的注册礼包，本质是**把获客成本换算成额度**——你用得越多，美团这套 API 的心智渗透得越深。

跟第三方聚合平台（比如 TokenRouter 那种）比，美团这个口子的优势是：

| 维度 | 美团官方直供 | 第三方聚合平台 |
|---|---|---|
| 额度来源 | 官方活动预算 | 平台自己的补贴 |
| 稳定性 | 官方服务，有 SLA | 随时可能改价 |
| 透明性 | 官方文档 + 用量管理可查 | 额度规则常不写清楚 |
| 长期风险 | 赠送是一次性资源包，但 API 本身长期存在 | 平台跑路/停服风险 |

**但也得实话实说：1000 万 Token 是一次性资源包，用完不会自动续。** 后续可以看官方「资源权益包」和「API 按量付费」两块怎么定价。真要自己掏钱充值的话，通过邀请链接注册的新用户**首单还能返实付金额的 5%**，等于变相打了个折。

> 按老规矩提醒一句：免费渠道要看**保质期**。美团这个属于「官方直供型」，长期风险低于第三方聚合，但赠送额度是一次性的——用完记得看一眼官方价格，别等扣费了才发现。

👉 [点击这里试试美团 LongCat 开放平台： https://longcat.chat/platform/product?inviteCode=SLBOB4YQ](https://longcat.chat/platform/product?inviteCode=SLBOB4YQ)

---

## 往期回顾

这个系列到这儿已经第 24 篇了，之前写过：

- 智谱每天送 3 亿 Token、5 亿 Token 程序员节活动
- AMD 中国站 Token Factory，15 款模型免费调
- [GLM 5.3 接入 TokenRouter，5 分钟进 WorkBuddy](https://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247506580&idx=1&sn=aeae8e775067c6cf61056dab21f7538c&chksm=ebf3d88fa34ee2f55aa345b3c061e56cc2c91b079b8014dfb5a79d549c24682cbdc5d12e7656#rd)
- 一个 Key 白嫖 20 个大模型、61 个免费大模型清单
- Qoder 里 0 倍率白拿千问、讯飞星火 X2.5 断网也能用

想看完整列表的，我整理了一份[免费大模型系列总索引](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI2Nzg5MjgyNg==&album_id=4326332444153921538)，全在这。

---

💬 **来评论区聊聊**

你有没有把一个国产大模型接进自己常用的 AI 工具？踩过什么坑，评论区说说你的经历。

如果你也想给自己攒一个「免费额度池」，不妨点下面的链接试试美团 LongCat 开放平台——走我的邀请链接完成实名认证，**你我各得 1000 万 Tokens**，叠上新人礼包最高 2000 万。

一个人，也能有用不完的额度。

👉 [点击这里试试美团 LongCat 开放平台： https://longcat.chat/platform/product?inviteCode=SLBOB4YQ](https://longcat.chat/platform/product?inviteCode=SLBOB4YQ)

---

## 最后

接大模型这件事，门槛已经低到只剩「复制、粘贴、点测试」了。以前总觉得「接 API」是程序员专属操作，实际上整个流程就三步。

**迈出这一步，你的 AI 工具就从「包月套餐」变成了「自助餐」**——想用哪家模型就用哪家，不用被绑死。

美团这一波，额度给得实在，接口也规规矩矩（OpenAI 兼容，文档齐全，还专门列了各家工具的配置入口）。没理由不薅。

**科技不高冷，AI 很好用。**

关注我，用上免费大模型。

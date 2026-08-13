---
title: DeepSeek-V4-Pro今天上线，Qoder送300额度免费用
date: 2026-08-13 02:15:00
tags: [公众号文章, DeepSeek, Qoder, AI大模型]
categories: [公众号文章]
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/deepseek-v4pro-free-cover.jpg
---

<!-- more -->

大家好，我是程序员晚枫。

今天凌晨，DeepSeek 悄悄把 V4-Pro 从预览版转正了。定价页上，模型版本号已经更新为 **DeepSeek-V4-Pro-0813**。

1M 上下文、384K 输出、默认思考模式，参数确实拉满了。但一看价格：输出 token 从 Flash 的 2 元涨到 6 元，整整贵了三倍。

想试试最新版又不想花钱？还真有路子。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/deepseek-v4pro-free-cover.jpg)

> **通过 Qoder CN 注册，直接送 300 credits，等于免费用上 DeepSeek-V4-Pro-0813。**

AI+免费用DeepSeek-V4-Pro：``https://www.aliyun.com/product/lingma?userCode=t6duaoe1``

---

## V4-Pro今天转正，贵是真贵

先说说今天上线的 V4-Pro-0813 到底升级了什么。

最直观的变化是**上下文窗口扩到 1M**。什么概念？你把一整本《三体》塞进去，它还能记住三体人住在哪。对于长文档分析、大型代码库理解这种场景，1M 上下文意味着你不用再来回截断、分段喂给它了。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260813022025661.png)

第二个升级是**最大输出 384K token**。以前的模型回你几百字就截断了，现在能一口气输出十几万字。这对生成长篇报告、批量写代码来说，体验差距非常大。

第三个是**默认开启思考模式**。简单说就是模型在回答之前先"想"一遍，把推理过程走完再给你结果。同时提供了一个非思考模式的接口，处理对速度敏感的任务。

但价格确实不便宜。跟 Flash 拉个对比就清楚了：

| 对比维度 | V4-Pro-0813 | V4-Flash-0731 |
|---------|-------------|---------------|
| 缓存命中输入 | 0.025 元/百万token | 0.02 元/百万token |
| 缓存未命中输入 | 3 元/百万token | 1 元/百万token |
| 输出 | 6 元/百万token | 2 元/百万token |
| 并发上限 | 500 | 2500 |
| 上下文 | 1M | 1M |

输出价格直接翻了三倍，并发还砍到五分之一。说白了，Pro 走的是"贵但强"路线，Flash 走的是"便宜量大"路线。

对于只是想体验一下 V4-Pro 能力的人来说，直接调 API 确实有点心疼。**但如果你通过Qoder用，就是另一回事了。**

---

## Qoder注册送300额度，直接用V4-Pro

Qoder CN是阿里云的 AI 编码助手。重点不是它自己多强，而是它**内置了 DeepSeek、GLM、Kimi 等国产主流大模型，可以自由切换**。

也就是说，DeepSeek-V4-Pro-0813 今天刚上线，你在Qoder里就能直接用，不需要自己折腾 API。

操作特别简单：

**第一步：通过专属链接注册。** 打开下面这个链接，用阿里云账号登录就行。新用户注册后会自动发放 300 credits，不需要手动领取。

AI+免费用DeepSeek-V4-Pro：``https://www.aliyun.com/product/lingma?userCode=t6duaoe1``
![Qoder 个人社区版：免费，首次注册300 Credits](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/qoder-free-plan.png)

*图片来源：[阿里云 Qoder CN 官网](https://www.aliyun.com/product/lingma?userCode=t6duaoe1)*



**第二步：下载 Qoder Desktop。** 这是Qoder的桌面客户端，Mac 和 Windows 都支持。装好之后登录你的账号。

**第三步：选模型，开聊。** 在模型选择里找到 DeepSeek-V4-Pro，输入你的问题就行。写代码、改文档、做分析，300 credits 够你跑不少轮了。

![Qoder 中的 DeepSeek-V4-Pro 模型卡片](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/qoder-deepseek-v4pro.png)

*图片来源：[阿里云 Qoder CN 官网](https://www.aliyun.com/product/lingma?userCode=t6duaoe1)*

还有个隐藏福利：注册后 14 天内，你还可以手动再领 1700 credits。加上初始的 300，总共 2000 credits。按 Pro 版一个月也就 2000 credits 算，**这相当于白送你一个月的会员。**

我昨天用 V4-Pro（预览版）跑了一个长文档分析任务，大概 30 页的中文报告，让它提取关键数据和生成摘要。整个过程一次喂完，不用分段，输出结果逻辑清晰、数据准确。换成 Flash 来跑同样的任务，中间断了一次，还得手动拼接上下文。

**1M 上下文不是噱头，是真的能省事。**

---

## 厂商为什么白送？因为AI编码赛道在抢人

你可能会想：DeepSeek 官方定这么贵，Qoder凭什么送你额度免费用？

**答案很简单：阿里在抢开发者。**

AI 编码工具这个赛道，现在卷得厉害。GitHub Copilot 是老牌选手，Cursor 是新晋网红，字节有 Trae，腾讯有云开发，百度有 Comate。大家都想把开发者圈到自己的生态里。

阿里的策略很明确：**用免费额度换用户习惯。** 你在 Qoder CN 里用惯了 DeepSeek-V4-Pro 的生成效果、GLM 的代码补全、Kimi 的长文本处理，将来需要更多 credits 的时候，自然更愿意付费续订。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260813022213813.png)

这里有个很多人没想明白的知识点：**为什么厂商敢把这么贵的模型免费给你用？**

因为对阿里来说，你用 DeepSeek-V4-Pro 产生的费用，是阿里跟 DeepSeek 之间的批量结算价，远低于官方零售价。就像你去饭店吃饭，菜单上一个菜 38 元，但饭店跟食材供应商结算是按批发价走。你吃的每一口，阿里付出的成本远低于你自己调 API 的价格。

再加上阿里自己的云基础设施（算力、存储、网络都在自家机房），边际成本比第三方平台更低。所以 300 credits 对你来说是"免费用 V4-Pro"，对阿里来说是"花小钱买一个潜在付费用户"。

这笔账，阿里算得过来。

对用户来说，**现在就是最好的窗口期。** 趁注册送 credits，把 V4-Pro 的 1M 上下文和 384K 输出跑一遍，看看它到底值不值三倍的价格。等免费额度用完了，你已经心里有数了。

不过提醒一句：**活动政策随时可能调整。** 300 credits 的发放规则、有效期、可用模型范围，都以注册当天页面显示为准。

---

国产大模型从"能不能用"卷到"好不好用"，现在又开始卷"便不便宜"。DeepSeek-V4-Pro 今天正式上线，能力确实上了一个台阶，但三倍于 Flash 的价格也让不少人犹豫。

Qoder送的 300 credits，相当于给你一个零成本试驾的机会。试完觉得值，再考虑要不要长期用；试完觉得不需要，也没花一分钱。

你觉得 V4-Pro 三倍于 Flash 的定价值不值？评论区聊聊你的看法。

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！

### 参考链接

- [DeepSeek API 官方定价页：https://api-docs.deepseek.com/zh-cn/quick_start/pricing](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)
- [阿里云 Qoder CN 新用户 Credits 领取及邀请奖励活动条款：https://help.aliyun.com/zh/lingma/qoderwork-cn-new-user-credits-claim-and-referral-reward-program-terms-and-conditions](https://help.aliyun.com/zh/lingma/qoderwork-cn-new-user-credits-claim-and-referral-reward-program-terms-and-conditions)
- [阿里云 Qoder CN 计费说明：https://help.aliyun.com/zh/lingma/billing-description](https://help.aliyun.com/zh/lingma/billing-description)
- [钱江晚报：DeepSeek V4 Pro正式版上线，1M超大上下文+384K输出，价格比Flash贵三倍：http://m.toutiao.com/group/7673192239073362438/](http://m.toutiao.com/group/7673192239073362438/)

## 相关阅读

- [AI 圈公开的秘密：DeepSeek V4 Flash 可以免费用](https://mp.weixin.qq.com/s/KNTw9mCUcTMzcPIwNkgPVg)
- [Kimi K3和DeepSeek V4 Flash，价格相差40倍](https://mp.weixin.qq.com/s/Ag_qbhR0TXxrmQOtS9UGPg)
- [以前用 GLM-5.2 花钱买，现在每天 100 个名额免费抢](https://mp.weixin.qq.com/s/H144Ocw5TrNLROG-Ost21A)

![AI 实战课](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

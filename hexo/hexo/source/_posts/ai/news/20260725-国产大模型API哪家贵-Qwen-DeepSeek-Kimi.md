---
title: Kimi K3和DeepSeek V4 Flash，价格相差40倍
date: 2026-07-25 22:00:00
tags: [公众号文章, 国产AI, API价格, Qwen, DeepSeek, Kimi, Token]
categories: [公众号文章]
cover: https://cdn.pixabay.com/photo/2024/09/15/15/13/ai-9027436_1280.jpg
---

大家好，我是程序员晚枫。

最近国内外的大模型，又热闹起来了。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260803150551709.png)

GPT-5.6 Luna的价格降低80%，Kimi K3发布并且登顶子榜的榜一，Qwen、DeepSeek、MiniMax也分别发布了新模型。

我之前没系统聊过，所以今天我把几家大模型最新的 API 定价页都翻了一遍。

不认真看还不知道：**同样写一段 1 万字的代码，Kimi K3 要花的钱，是 DeepSeek V4 Flash 的 40 倍。**

差距这么离谱，到底是能力碾压，还是另有原因？

> 文末有一个白嫖Kimi K3大模型的方法，还没体验过的朋友，可以去试试。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260803145122247.png)

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260803145206853.png)

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260803145255475.png)



---

## 一、价格差距比我想的大得多

我截了 3 张图，分别是 Qwen3.8-Max、DeepSeek V4（Flash 和 Pro 各一个）、Kimi K3 的官方定价页。

光看数字你可能没感觉，我先把它们整理成一张表：

| 模型 | 输入（缓存命中）| 输入（缓存未命中）| 输出 |
|------|----------------|------------------|------|
| Qwen3.8-Max | 1.5 元 | 12 元 | 36 元 |
| DeepSeek V4 Flash | 0.02 元 | 1 元 | 2 元 |
| DeepSeek V4 Pro | 0.025 元 | 3 元 | 6 元 |
| Kimi K3 | 2 元 | 20 元 | 100 元 |

单位：每 1M（百万）tokens。你可以把它理解成"模型每读 100 万字收多少钱"。

我拿最常见的场景举例——写一段 1500 字（≈ 1M token）的代码，**输入和输出都算上**：

- Kimi K3：输入 20 元 + 输出 100 元 = **120 元**
- DeepSeek V4 Flash：输入 1 元 + 输出 2 元 = **3 元**
- Qwen3.8-Max：输入 12 元 + 输出 36 元 = **48 元**

**同样一段代码，Kimi 是 DeepSeek 的 40 倍。**

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260803151042695.png)

按每月 1000 次调用算：

- Kimi K3：**12000 元**
- DeepSeek V4 Flash：**300 元**
- Qwen3.8-Max：**4800 元**

看出来了吗？**差距不是"贵一点"，是贵一个量级。**

---

## 二、怎么用得聪明：3 个坑 + 怎么选 + 缓存原理

价格看完了，但你以为会挑了就完事？**真正贵的不是价格，是你以为"差不多就行"的那几个细节。**

**坑 1：只看输出价，忽略输入价。** 很多人盯着"输出价"看，觉得 Kimi 输出 100 元、DeepSeek 输出 2 元，好像"也就 50 倍"。

但**输入价差距更大**：Kimi 20 元 vs DeepSeek 1 元，**差了 20 倍**。真正贵的不是"输出"，是"上下文"。你喂给模型的资料越多、对话历史越长，输入消耗就越高。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260803150446184.png)

**坑 2：以为"缓存命中"白送的。** 官方页都写着"缓存命中"和"缓存未命中"两个价格，差几十倍。但"缓存命中"是个概率游戏，不是用了就一定便宜。

比如 Kimi K3 缓存命中 2 元、缓存未命中 20 元——如果你场景是"反复润色同一份文档"，命中率高，实际平均价格能降到 5.6 元；但每次问新问题，命中率 0%，那 20 元跑不掉。

**坑 3：以为"上下文 1M = 能白嫖 1M"。** Kimi、DeepSeek 都标着"1M 上下文窗口"。但**能塞 1M token，不代表你该塞 1M token**。

按 DeepSeek V4 Pro 不命中价算，光读 1M token 就 3 元一次。塞太多没必要的历史对话，就是在给厂商送钱。
![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260803151958912.png)


那到底怎么选？我的建议是 **3 步**：

**第 1 步：明确你要做什么。** 不同模型擅长的事不一样，**别拿写代码的模型去写文案**：
- 日常写代码、批量改文件 → DeepSeek V4 Flash（极致便宜）
- 复杂业务逻辑、长难代码 → DeepSeek V4 Pro（性价比最优）
- 需要看图、懂设计、生成长 HTML → Kimi K3（贵但 WebDev 能力第一）
- 中文写作、文档总结 → Qwen3.8-Max（中文理解最地道）

**第 2 步：先做小流量测试。** **别一上来就充 1000 块。** 先用每个模型跑 10 个真实任务，看哪个出活、不返工。便宜的模型如果老出错，修 bug 的时间成本比省钱多。**最终成本 = token 钱 + 你的时间钱。**

**第 3 步：把缓存用起来。** 你可能看价格表时纳闷——"缓存命中"到底是什么，怎么差这么多？

大模型每回答你一个问题，**实际上是把"你之前问的 + 当前问题"全部重新读一遍**。

如果你每次问的问题基本一样（比如反复润色一份文档），那 90% 的内容都是重复的。

聪明的厂商把这部分重复内容**记下来放在服务器**，下次再问，**直接从缓存里读**，不再算输入 token。

**这就是为什么"缓存命中"价格能低 50-100 倍。**

但缓存命中有个前提：**你必须用同一个会话、问相似的问题。** 换一个话题，缓存就失效了。

所以想用便宜价，你得这么做：

- 把同一个任务拆成"长会话"，一次问完
- 别每写一段代码就开新窗口
- 把项目说明、需求文档作为"对话前缀"，所有问题都基于它

---

## 三、说句真心话

价格不是越便宜越好，能力也不是越贵越强。

**真正聪明的做法，是按场景混着用：**

- 写代码 → DeepSeek
- 写文档 → Qwen
- 写"看得过去的视频/页面" → Kimi K3

每个模型做自己最擅长的事，**单月成本能砍掉 80%，效果反而更好。**

这才是"省钱"的真正含义，毕竟不是所有场景都需要顶级模型。

最后附一个通过WorkBuddy免费用K3的方法：

- 下载WorkBuddy，免费领取Token：https://www.workbuddy.cn/events/invite?inviteCode=ic1tpbrj2x
- 选择模型列表里提供的K3，不需要额外充值，消耗免费送的积分就可以。还可以选择完全免费的Hy3。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260803151748844.png)


---

## 相关阅读

- [对标Fable 5，Qwen3.8-Max参数达2.4T](https://mp.weixin.qq.com/s/RwBuZHOCAQhyQN05HYToYg)
- [不要低估了 Kimi K3 生成视频的能力，10分钟做一条视频，成本不到1块钱](https://mp.weixin.qq.com/s/y0O9YUVkYVw8iM2B26aVSw)
- [千问办公正式发布，AI办公迎来最强挑战者](https://mp.weixin.qq.com/s/f05PrU-u8TqxILFPBZ7t6A)

---

> 💬 **聊聊你**
>
> 你平时用国产大模型 API 写什么？最在乎的是价格还是能力？
>
> 评论区聊聊，我下篇专门挑被点最多的模型深扒。

---

**科技不高冷，AI很好用。**
我是晚枫（Wayne Liu），关注我，带你一起玩AI！

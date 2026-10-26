---
title: 一个人就是 Video Factory：在 WorkBuddy 里 3 块钱做一条品牌片
date: 2026-10-26 22:50:00
tags: ["公众号文章", "AI工具", "AI视频", "LibTV", "WorkBuddy"]
categories: ["公众号文章", "Python自动化办公社区"]
keywords: [WorkBuddy, LibTV, AI视频生成, AI做视频, 品牌视频, AI短剧, 定时任务, Video Factory]
description: LibTV 打通 WorkBuddy 的完整实操教程：连好连接器、上传素材、说清四件事，3 块钱做一条品牌片，还能挂定时任务 7×24 持续出片，一个人就是一座 Video Factory。
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/01-banner.png
---

大家好，这里是程序员晚枫。

周末去参加了：[2026腾讯云西部架构师峰会](https://mp.weixin.qq.com/s/ay1riSpDkzuQiqjPjEM3eA)，我除了负责少年游这个会场的主持，还和很多技术大咖交流了最新的 AI 应用。

尤其见世面的一点是，我发现做AI视频的工方式，彻底变了。

以前做一条视频，要在好几个工具之间来回切换：找灵感一个工具、写脚本一个工具、生成画面又一个工具，素材导出导入，光是"搬运"就耗掉一半时间。

现在完全可以在一个软件里点几下就搞定了，可用的软件有很多，那今天就给大家推荐这个最新官宣的消息：**LibTV 和 WorkBuddy 正式打通了**。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/01-banner.png)

*图片来源：LibTV 官方公众号*

大家最近有没有刷到这个李白、杜甫、项羽、刘邦等史前大V 在一起唱歌的视频？这个就是用LibTV做出来的。

你可以在 WorkBuddy 里直接调用 LibTV 的专业创作工具、导演级 Skills，还能参考 LibTV 里的爆款作品。品牌视频、爆款素材、短剧制作，从剧本策划、分镜设计到视频生产，一条工作流走完。

**而你只需要提供一个创意，也可以成为视频创作的起点。**

这篇文章，我就把「用 LibTV 在 WorkBuddy 里做视频」的完整教程写给你。

**全文分两部分——准备工作和实操教程。你只需要先把准备工作做完，再往下按教程一步步操作，就能跑通。**

---

## 01 准备工作：先注册这两个账号

这篇教程要用到两个东西：**LibTV（负责视频创作）和 WorkBuddy（负责理解需求、调度任务）**。

所以在开始之前，请先把这两个账号注册好。**这一步就是全部的准备工作，两个账号都注册完成，再往下看教程，一步一步照着做就行。**

**第一件事：注册 LibTV 账号。**

LibTV 是一个 AI 视频创作平台，集成了多个顶级视频生成模型，从剧本、分镜到成片全流程一个画布搞定，上面还有大量全网爆款作品的制作画布和提示词可以直接参考。

👉 [点击这里注册 LibTV： https://libtv.cgref.cn/s/9omkl4jn4d](https://libtv.cgref.cn/s/9omkl4jn4d)

**第二件事：注册 WorkBuddy 账号。**

WorkBuddy 是一个全能办公 AI 工作台，覆盖日常办公、代码开发、设计创意，听得懂自然语言、会自己拆解任务、调用工具执行。我们这次就是借它的「连接器」来调用 LibTV。

👉 [点击这里注册 WorkBuddy： https://www.workbuddy.cn/events/invite?inviteCode=scnqpwi2yipt](https://www.workbuddy.cn/events/invite?inviteCode=scnqpwi2yipt)

**两个账号都注册好了？恭喜，准备工作到此完成。**

接下来就是纯操作环节，跟着教程一步步做即可。

---

## 02 为什么值得折腾：一个人就是 Video Factory

在动手之前，先花一分钟了解这次打通能干什么，你会更有感觉。

**第一，更低成本出片。**

视频是需要反复尝试的东西，成本直接决定你能试多少次。LibTV 借助 **Wan 3、Seedance 2.0 Fast** 等模型的成本优势，创意可以多试几版，素材可以多做一批。

**3块钱做一支品牌片，5块钱做一集短剧。**

**第二，爆款快速复刻。**

你看过的**《过来人》等现象级爆款视频，都在 LibTV 上发布了**，而且带着制作画布和提示词。让 WorkBuddy 参考这些作品，结合你自己的产品或故事去调用 LibTV 制作，从找灵感到出片的路被大幅缩短。

**第三，7×24 持续出片。**

结合 WorkBuddy 的定时任务，你可以把明确的制作需求设成周期任务，按计划自动调用 LibTV 批量生成视频。新品上架、日常运营、投放测试，都能提前安排生产。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/05-demo.gif)

一句话：**配合定时任务，7×24 持续出片，一个人就是 Video Factory。**

---

## 03 教程第一步：把 LibTV 连进 WorkBuddy

准备工作做完，现在开始实操。

打开 WorkBuddy，点击【+】，在「连接器」中搜索「LibTV」，点击【链接】，按页面提示完成账号授权。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/02-step1.png)

*图片来源：LibTV 官方公众号*

这就是第一步的全部内容：**找到 LibTV，完成连接。**

---

## 04 教程第二步：上传素材，说出需求

连接完成后，回到任务对话，上传产品图或参考素材，然后直接输入需求。

需求不用写得多专业，**尽量说清四件事就行**：

| 要说清的事 | 举例 |
|-----------|------|
| **拍什么** | 一支 30 秒的产品介绍视频 |
| **用在哪里** | 视频号 / 抖音投放 / 官网首页 |
| **想要什么风格** | 科技感 / 温暖治愈 / 快节奏卡点 |
| **哪些内容必须保留** | 产品名、Slogan、核心卖点 |

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/03-step2.png)

*图片来源：LibTV 官方公众号*

WorkBuddy 负责理解与规划，LibTV 随时接手创作，无需重新整理 Brief、反复解释需求或来回切换工具。

到这里，教程就跑通了。

👉 [点击这里注册 LibTV： https://libtv.cgref.cn/s/9omkl4jn4d](https://libtv.cgref.cn/s/9omkl4jn4d)

---

## 05 跑通之后，你可以做的三件事

**第一，做品牌视频。**

产品要上新，把手里的产品 Demo、介绍 Deck 直接丢进对话，让 WorkBuddy 提炼卖点、规划创意，再调用 LibTV 完成脚本分镜和视频生成。

**第二，批量做投放素材。**

围绕一个已经验证有效的创意，让 WorkBuddy 规划不同开头、卖点和场景，调用 LibTV 批量生成 UGC 素材，供运营和投放筛选、测试。

**一个有效创意，批量做出不同版本。**

**第三，连载短剧。**

提供故事梗概，让 WorkBuddy 梳理剧情、拆解制作任务，再调用 LibTV 推进角色与场景设定、分镜设计和连续镜头生成。

**短剧要更新，从故事推进到连续剧情，一个人接得住。**

---

## 最后说句掏心窝子的

工具打通这件事，看着是个小更新，实际改变的是做事的顺序。

以前是"我要做视频，所以去开一堆工具"；现在是"我在干活，顺手就把视频做了"。

注册好 LibTV 和 WorkBuddy 这两个账号，按上面的教程走一遍，十分钟就能跑通你的第一条工作流。

明白的点个赞。

💬 **来评论区聊聊**

你最想先做哪一类视频：品牌片、投放素材，还是短剧？评论区打出来。

如果你也想让视频创作直接长在自己的日常工作流里，不妨点下面的链接，注册好账号就开拍。

一个人，也能是一座 Video Factory。

👉 [点击这里加入LibTV： https://libtv.cgref.cn/s/9omkl4jn4d](https://libtv.cgref.cn/s/9omkl4jn4d)

**科技不高冷，AI很好用。**

我是晚枫（Wayne Liu），关注我，带你一起玩AI！

---

## 相关阅读

- [免费用Seedance2.5做AI短剧，商汤Seko这波白嫖攻略收好](https://mp.weixin.qq.com/s/oEdTeiAcbQSTeu3OP-W1Fw)
- [普通人做 AI 短剧：用这 6 个工具，从写剧本到成片](https://mp.weixin.qq.com/s/6anYB88_FXLswO4T_kvYjQ)
- [我在WorkBuddy 的AI活动上，多次大喊"请说人话"](https://mp.weixin.qq.com/s/MQoI6EaGrIm9nSYeWe7pPg)
- [想靠 AI 短剧赚钱？先把剧本写完：Laper 工作流实测](https://mp.weixin.qq.com/s/1IhE_DTvm20X5tGkwiSbWA)
- [别花钱做视频了：MiniMax 开源 H3](https://mp.weixin.qq.com/s/KT3A2ec3Z2rgJ8vAsGGxgg)

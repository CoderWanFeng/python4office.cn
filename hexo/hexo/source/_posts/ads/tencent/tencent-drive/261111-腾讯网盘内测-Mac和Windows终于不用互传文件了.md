---
title: Mac 和 Windows 不用互传文件了：腾讯网盘给 AI 一颗大脑
date: 2026-11-11 23:33:00
tags: [公众号文章, 腾讯网盘, Mac, Windows, AI工具]
categories: [公众号文章]
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-cover-v2.jpg
---

大家好，我是程序员晚枫。

最近我拿到了腾讯网盘的内测资格，被传统网盘的AI功能气哭了几次以后，我对腾讯网盘这种AI Native的产品特别期待。

> 腾讯网盘，体验地址：https://drive.tencent.com/home

我期待的，不是“又能多存多少文件”，而是：它能不能解决我一个很具体的麻烦——不同设备的不同AI工具之间，比如：家里的电脑和公司的电脑之间、Mac 上的AI和 Windows 上的AI之间，文件总得传来传去的问题。

这次体验后，我觉得它更值得讨论的，已经不只是跨设备传文件。

> **在腾讯网盘是在做一件更面向 AI 原生的事：给 AI 装上了一个统一的存储大脑。**

去年我还为了有一个更大的电脑空间，咬牙、分期升级了一个MacBook Pro。

但有了AI 网盘以后，AI生成的东西一股脑都给网盘就行了。本地空间大不大，已经不重要了。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261112182148978.png)

---

## 我受够了在两台电脑之间搬文件

大家现在用上了 AI，肯定体会过那种项目在家里的电脑上，然后公司的电脑处理不了的痛苦吧？

我更加了一层，我平时还会同时在 Mac 和 Windows 上处理工作。

尤其是像我这种极度依赖创作工具的18线 AI博主，生图、剪辑视频、要在 Mac 上；看项目预览或者是一些比较敏感的软件要在 Windows 上。

同一份资料，可能在 家里的Mac 上整理到一半，接下来又要换到公司的 Windows 上继续。或者家里的Windows做了一个文档，要传到公司的Windows里面。

项目本身没换，电脑换了，文件却得重新搬一次。有时候，文件没传丢，版本先乱了。

过去的流程，我熟得不能再熟：

- 把文件从这台电脑发出去；
- 换到另一台电脑接收、下载；
- 找到保存位置，再继续刚才的工作；
- 如果中间改过内容，还要确认哪一份才是最新版。
- 甚至我把所有的项目，都设为了Git仓库

于是桌面上开始出现**“最终版”“最终版-2”“最终版真的不改了”“最终版去哪了？”**。

看起来一直在推进工作，其实只是在给混乱做版本管理。两台电脑没法互通，协同方式却很像我亲自扮演数据线。

这些动作每一个都只要几分钟，拼在一起，却不断打断任务。

**人换电脑，是为了接着工作，不是为了换台设备，再当一次文件搬运工。**

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261112182218991.png)

哪怕把 Windows 都换成 Mac，这个问题也不会自动消失。系统统一了，文件还是可能散在两台电脑里，互传依旧麻烦。

可能有人会说，Mac 不是有隔空投送和 iCloud 吗？有，但它们解决的不是同一个问题。

隔空投送更像是把文件从这台发到那台，iCloud 更偏向苹果生态里的同步。对我来说，它们对 AI 的支持都不够好：文件到了另一台电脑，不代表 AI 就能围绕同一批资料继续处理任务。

> 我需要的不是再快一点的发送按钮，而是两台电脑和 AI 工具能直接共用同一个工作目录，甚至处理同一份文件。

其实，被这个问题折腾久了，我本来都准备自己用COS服务写一个同步工具了。幸好我没写，腾讯网盘替我做了，**差点又浪费 100 亿 token。**

所以，我对腾讯网盘最感兴趣的地方，不是它能不能把文件存起来，而是它能不能让文件不再跟着某一台电脑走，让不同设备上的 AI 也能围绕同一批资料工作。

---

## Mac 和 Windows 的 AI，开始接力做同一件事

拿到内测资格之后，我真的用它完成了一个商单的创作。

其中 AI 入口软件，我这里搭配的也是腾讯自己家的WorkBuddy。

![从腾讯网盘连接页唤起 WorkBuddy](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-workbuddy-launch.png)

*在连接页选择 WorkBuddy 后，页面会唤起对应的客户端。*

需要跨设备处理的资料直接让 WorkBuddy 自己放进腾讯网盘，在 Mac 的AI上整理到一半，换到 Windows 后，直接让AI连上网盘里的同一份资料继续。完全没有上传下载这个步骤，更不用担心版本混乱了。

这次不是只在概念上“支持多设备”。我的网盘左侧已经同时出现了两台电脑：Mac 显示为“CoderWanFeng的MacBook”，联想 Windows 显示为“ZHAOFENG-LENOVO”。

![Mac 和联想 Windows 下均显示 WorkBuddy](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-dual-workbuddy.png)

*Mac 和联想 Windows 两台设备下都接入了 WorkBuddy。*

我在这台电脑新建一个文件夹，换到另一台电脑，也能看到它，无缝衔接。截图里的**“商单投放”**文件夹，就在这个共用目录里。

![腾讯网盘同时连接 Mac 和联想 Windows](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-dual-computers.png)

*网盘左侧同时列出 Mac 和联想 Windows 两台设备，共用同一套目录。*

两台设备我都是用 WorkBuddy作为入口在创作的，通过这种方式，我可以专注于项目的创作进度，所有的成果都让WorkBody给我同步到网盘里，不用保存在本地，这边上传了，那边马上就能看到，并且进入下一个工作步骤。完全没有了怎么同步文件的心智负担。

**从这个角度看，腾讯网盘也是不同设备之间的 AI 连接器。** 两台电脑上的 AI 并不是简单的共享了记忆，而是可以通过授权接入同一个资料中心，接上同一项工作。

| 对比维度 | 过去的工作方式 | 使用腾讯网盘后 |
|---------|---------------|---------------|
| 文件位置 | 散落在不同电脑 | 放进统一存储中心 |
| 换电脑后 | 先传文件，再找版本 | 围绕同一资料继续 |
| 工作重心 | 先处理文件搬运 | 直接接续原任务 |

以前，我更多是围着设备安排工作：这份文件在哪台电脑，就去哪台电脑处理。

现在，更多是围绕任务选择设备：当前这台电脑适合做什么，就接着做什么，资料不需要再单独跑一趟。

**这才是我理解的不同设备、不同AI 的协同：不是远程控制，也不是把屏幕投来投去，而是它们可以访问同一个文件中枢。**

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261112182257950.png)

---

## AI 原生办公，需要一颗共享的大脑

除了 WorkBuddy ，腾讯网盘还支持：DeepSeek Harness、OpenClaw，以及微云、乐享、ima、百度网盘、Notion、Plaud 等入口。

其实悄悄告诉大家，这里面没列出来的 AI 工具也都可以用，只要支持 MCP 接入的都可以。

![腾讯网盘连接页面](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-connections.png)

*连接页里并列展示文档、Agent 和各类资料服务的入口。*

为什么这件事和 AI 关系很大？

因为 AI 要接着完成任务，光会聊天不够，它还得拿到正确的资料。

文件散在不同电脑、聊天窗口和应用里，AI 每次看到的都可能只是其中一段。人就得重新上传文件、重新解释背景，甚至重新告诉它：之前已经做到哪一步了。

统一存储中心的作用，是给资料一个稳定、统一的来源。经过授权并成功连接后，AI 可以从同一处读取材料，上一台电脑整理的内容，下一台电脑才有机会接着用。

**大模型可以负责思考和生成，统一存储中心则负责保管任务所需的资料与前因后果。两者接起来，AI 办公才算真正有了大脑。**

它不是替 AI 思考，而是让不同设备、不同应用里的 AI，都有机会调用同一份资料，不必每次换设备、换工具，都重新听人讲一遍“前情提要”。

*资料汇成一颗共享的「大脑」，供不同设备上的 AI 调用。*

![WorkBuddy 中添加腾讯网盘连接器](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-workbuddy-connector.png)

*WorkBuddy 中的腾讯网盘连接器入口。*

---


**AI 原生办公真正需要的，不只是更聪明的模型，而是一个让这些模型接上同一项工作的连接中枢。**

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261112182109501.png)

*多台设备接入同一个资料中枢，文件与任务可以在它们之间接续。*

我们常说万物互联。过去，我们更多想到的是设备联网，是电脑、手机和各种终端都能连上网络。

但在 AI 原生办公里，光联网还不够。如果每台设备上的 AI 看到的都是不同资料，接不上同一项任务，它们依然只是一个个聪明的孤岛。

所以，万物通过什么互联呢？也许不只是网络，还需要一个统一承载资料、连接设备，让不同 AI 接续工作的中枢。

**也许，腾讯网盘就是下一个答案。**

你期待不同设备上的 AI 接力完成同一项工作吗？评论区聊聊。

**科技不高冷，AI很好用。**

我是晚枫，关注我，带你一起玩AI！

## 参考链接

- [腾讯网盘官网：https://drive.tencent.com/home](https://drive.tencent.com/home)
- [WorkBuddy 官网：https://www.codebuddy.cn/](https://www.codebuddy.cn/)

## 相关阅读

- [免费领取 WorkBuddy 3万积分，教程来了！](https://mp.weixin.qq.com/s/hNQTFuzF0v34D1n2LvigPg)
- [美团放大招：LongCat 白送 1000 万 Token，5 分钟接进 WorkBuddy](https://mp.weixin.qq.com/s/sUH7QLI1KSFMlnDO6JKddw)
- [OpenAI联合微软、亚马逊等5家大厂联手发布Agent Plugins：AI插件终于要统一了](https://mp.weixin.qq.com/s/halvCFr_nz4zFMnjOCBMKQ)
- [千问办公正式发布，AI办公迎来最强挑战者](https://mp.weixin.qq.com/s/f05PrU-u8TqxILFPBZ7t6A)


![免费用AI](https://atomgit.com/api/v5/repos/python4office/hexo-public/raw/free-ai.jpg)

*微信扫码加入「免费用 AI」知识星球的入口。*

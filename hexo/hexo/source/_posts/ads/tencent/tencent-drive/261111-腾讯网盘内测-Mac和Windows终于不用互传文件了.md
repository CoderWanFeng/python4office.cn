---
title: 腾讯网盘内测：AI 办公，终于有大脑了
date: 2026-11-11 23:33:00
tags: [公众号文章, 腾讯网盘, Mac, Windows, AI工具]
categories: [公众号文章]
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-beta-home.png
---

大家好，我是程序员晚枫。

最近我拿到了腾讯网盘的内测资格。

看到页面上的 BETA 标识时，我第一反应不是“又能多存多少文件”，而是：它能不能解决我一个很具体的麻烦——Mac 和 Windows 之间，文件总得传来传去。

这次体验后，我觉得它更值得讨论的，已经不只是跨设备传文件。

> **在我眼里，腾讯网盘是在做一件更面向 AI 原生的事：给 AI 办公一个统一的资料大脑，也给不同设备上的 AI 一个连接器。**

![腾讯网盘内测版首页](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-beta-home.png)

*腾讯网盘首页，页面上带有 BETA 标识。*

---

## 我受够了在两台电脑之间搬文件

我平时会同时在 Mac 和 Windows 上处理工作。

同一份资料，可能在 Mac 上整理到一半，接下来又要换到 Windows 继续。事情本身没换，电脑换了，文件却得重新搬一次。

过去的流程，我熟得不能再熟：

- 把文件从这台电脑发出去；
- 换到另一台电脑接收、下载；
- 找到保存位置，再继续刚才的工作；
- 如果中间改过内容，还要确认哪一份才是最新版。

有时候，文件没传丢，版本先乱了。

于是桌面上开始出现“最终版”“最终版2”“最终版真的不改了”。看起来一直在推进工作，其实只是在给混乱做版本管理。两台电脑都不便宜，协同方式却很像我亲自扮演数据线。

这些动作每一个都只要几分钟，拼在一起，却不断打断任务。

**人换电脑，是为了接着工作，不是为了换台设备，再当一次文件搬运工。**

哪怕把 Windows 换成另一台 Mac，这个问题也不会自动消失。系统统一了，文件还是可能散在两台电脑里，互传依旧麻烦。与其反复发送，不如让两台电脑共用同一个目录。

其实，被这个问题折腾久了，我本来都准备自己写一个同步工具了。就用对象存储 COS 下面的 Agent Bucket 做统一目录，再让 AI 帮我补齐跨设备同步的功能。

幸好我没写，腾讯网盘替我做了。**差点又浪费 100 亿 token。**

所以，我对腾讯网盘最感兴趣的地方，不是它能不能把文件存起来，而是它能不能让文件不再跟着某一台电脑走，让不同设备上的 AI 也能围绕同一批资料工作。

---

## Mac 和 Windows 的 AI，开始接力做同一件事

现在，我的做法变了。

需要跨设备处理的资料放进腾讯网盘，在 Mac 上整理到一半，换到 Windows 后，围绕同一份资料继续。少掉的不只是发送和下载两个动作，而是“先别干活，把文件找到再说”这一整段准备时间。

这次不是只在概念上“支持多设备”。我的网盘左侧已经同时出现了两台电脑：Mac 显示为“CoderWanFeng的Ma...”，联想 Windows 显示为“ZHAOFENG-LENOVO”。

我在这台电脑新建一个文件夹，换到另一台电脑，也能看到它。截图里的“商单投放”文件夹，就在这套共用目录里。

![腾讯网盘同时连接 Mac 和联想 Windows](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-dual-computers.png)

*网盘左侧同时列出 Mac 和联想 Windows 两台设备，共用同一套目录。*

两台设备下面还分别显示着 WorkBuddy。它们接入的不只是一个同步目录，也是同一个可以让 AI 接着工作的资料入口。

**从这个角度看，腾讯网盘也是不同设备之间的 AI 连接器。** 两台电脑上的 AI 并不是突然共享了记忆，而是可以通过授权接入同一个资料中心，接上同一项工作。

![腾讯网盘连接不同设备上的 AI](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-ai-connector.jpg)

*两台电脑通过同一个网盘中枢连在一起，文件不再跟着某一台设备走。*

![Mac 和联想 Windows 下均显示 WorkBuddy](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-dual-workbuddy.png)

*Mac 和联想 Windows 两台设备下都接入了 WorkBuddy。*

| 对比维度 | 过去的工作方式 | 使用腾讯网盘后 |
|---------|---------------|---------------|
| 文件位置 | 散落在不同电脑 | 放进统一存储中心 |
| 换电脑后 | 先传文件，再找版本 | 围绕同一资料继续 |
| 工作重心 | 先处理文件搬运 | 直接接续原任务 |

以前，我更多是围着设备安排工作：这份文件在哪台电脑，就去哪台电脑处理。

现在，更多是围绕任务选择设备：当前这台电脑适合做什么，就接着做什么，资料不需要再单独跑一趟。

**这才是我理解的两台电脑协同：不是远程控制，也不是把屏幕投来投去，而是它们可以访问同一个文件中枢。**

可能有人会说，Mac 不是有隔空投送和 iCloud 吗？有，但它们解决的不是同一个问题。

隔空投送更像是把文件从这台发到那台，iCloud 更偏向苹果生态里的同步。对我来说，它们对 AI 的支持都不够好：文件到了另一台电脑，不代表 AI 就能围绕同一批资料继续处理任务。

我需要的不是再快一点的发送按钮，而是两台电脑和 AI 工具都能接入同一个工作目录。

这种变化还延伸到了具体的工作界面。

在腾讯网盘的连接页选择 WorkBuddy 后，页面会唤起客户端。这个过程让我看到，网盘开始和实际处理任务的工具发生关系，而不只是一个把文件放进去、再取出来的独立仓库。

![从腾讯网盘连接页唤起 WorkBuddy](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-workbuddy-launch.png)

*在连接页选择 WorkBuddy 后，页面会唤起对应的客户端。*

过去是文件跟着电脑走，现在更像是任务围绕同一个文件中枢往前推进。

---

## AI 原生办公，需要一颗共享的大脑

传统网盘的起点是文件。先保存，再同步，需要时下载。

这次体验后，我觉得腾讯网盘更值得关注的是另一个起点：AI 完成任务需要哪些资料，不同设备、不同应用里的 AI 又如何接续同一件事。

**这就是我理解的 AI 原生，尤其是 AI 办公原生。不是简单给网盘加一个 AI 按钮，而是让网盘直接参与 AI 的工作过程，成为统一的资料层和连接层。** 这次内测界面里的两个细节，让我看到了这种方向。

第一个细节，是“连接”页面。

除了 WorkBuddy 和腾讯文档，界面还展示了 WorkBuddy 桌面端、DeepSeek Harness、OpenClaw，以及微云、乐享、ima、百度网盘、Notion、Plaud 等入口。

![腾讯网盘连接页面](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-connections.png)

*连接页里并列展示文档、Agent 和各类资料服务的入口。*

这些入口说明，它试图连接的不只是设备，还有文档、Agent 和已有的资料服务。

注意，我说的是**界面提供了这些连接入口**，不代表我已经把所有服务都连接成功，更不代表它们在内测阶段都具备完全一致的能力。

第二个细节，是 WorkBuddy 里的腾讯网盘连接器。

WorkBuddy 主界面明确提示，为了读取分享内容，需要连接腾讯网盘。也就是说，文件进入统一存储中心之后，下一步不是停在那里，而是可以被 AI 工作界面继续读取和使用。

![WorkBuddy 提示连接腾讯网盘](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-workbuddy-home.png)

*WorkBuddy 主界面提示：要读取分享内容，需要先连接腾讯网盘。*

为什么这件事和 AI 关系很大？

因为 AI 要接着完成任务，光会聊天不够，它还得拿到正确的资料。

文件散在不同电脑、聊天窗口和应用里，AI 每次看到的都可能只是其中一段。人就得重新上传文件、重新解释背景，甚至重新告诉它：之前已经做到哪一步了。

统一存储中心的作用，是给资料一个稳定、统一的来源。经过授权并成功连接后，AI 可以从同一处读取材料，上一台电脑整理的内容，下一台电脑才有机会接着用。

**大模型可以负责思考和生成，统一存储中心则负责保管任务所需的资料与前因后果。两者接起来，AI 办公才算真正有了大脑。**

它不是替 AI 思考，而是让不同设备、不同应用里的 AI，都有机会调用同一份资料，不必每次换设备、换工具，都重新听人讲一遍“前情提要”。

![腾讯网盘为 AI 办公提供共享资料大脑](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-ai-office-brain.jpg)

*资料汇成一颗共享的「大脑」，供不同设备上的 AI 调用。*

![WorkBuddy 中添加腾讯网盘连接器](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-workbuddy-connector.png)

*WorkBuddy 中的腾讯网盘连接器入口。*

不过，内测边界也要说清楚。

早期连接截图中，腾讯网盘连接器仍显示“正在连接”。随后，我又让 WorkBuddy 做了一次更具体的操作：在网盘根目录新建“商单投放”文件夹。

它返回已完成，网盘页面里也出现了这个文件夹。

![WorkBuddy 在腾讯网盘根目录新建商单投放文件夹](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-workbuddy-create-folder.png)

*WorkBuddy 在网盘根目录新建「商单投放」文件夹，页面里也已出现。*

至少这一次从 AI 到网盘的新建操作已经跑通。它还不能证明所有连接和读取能力都已完整实测，但已经让我看到：统一存储中心不只是理论上的资料入口，AI 确实可以参与其中的文件整理。

目前产品仍处于 BETA 阶段，后续界面、连接方式和功能都可能调整，本文截图也只代表我当前看到的版本。

---

以前，文件跟着电脑走。电脑一换，人就得先把资料搬过去，再给 AI 重新交代背景。

现在，Mac 和 Windows 可以围绕同一个文件中枢接续工作，两台设备上的 AI 也有了共同的资料入口。真正省下来的，不只是几次传输，而是一次次被打断后重新进入状态的成本。

**AI 原生办公真正需要的，不只是更聪明的模型，也是一个让这些模型接上同一项工作的连接中枢。**

我们常说万物互联。过去，我们更多想到的是设备联网，是电脑、手机和各种终端都能连上网络。

但在 AI 原生办公里，光联网还不够。如果每台设备上的 AI 看到的都是不同资料，接不上同一项任务，它们依然只是一个个聪明的孤岛。

所以，万物互联之后，万物通过什么互联呢？也许不只是网络，还需要一个统一承载资料、连接设备，让不同 AI 接续工作的中枢。

![多种设备通过腾讯网盘连接同一个资料中枢](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/tencent-drive-connected-everything.jpg)

*多台设备接入同一个资料中枢，文件与任务可以在它们之间接续。*

**也许，腾讯网盘就是下一个答案。**

你期待不同设备上的 AI 接力完成同一项工作吗？评论区聊聊。

## 参考链接

- [WorkBuddy 官网：https://www.codebuddy.cn/](https://www.codebuddy.cn/)
- [腾讯文档官网：https://docs.qq.com/](https://docs.qq.com/)
- [腾讯微云官网：https://www.weiyun.com/](https://www.weiyun.com/)

## 相关阅读

- [精选6个真实案例，带你玩转腾讯 WorkBuddy！](https://mp.weixin.qq.com/s/ZQVSqnNqi4_EyRofpYBZLA)
- [QClaw 和 WorkBuddy，傻傻分不清楚？一文讲清楚！](https://mp.weixin.qq.com/s/49s4n2_H2gtyE3soqN1I0g)
- [腾讯 CodeBuddy：案例玩法+实操教程合集](https://mp.weixin.qq.com/s/N_4iB45NCeVG2tA3GJGWAg)

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！

![免费用AI](https://atomgit.com/api/v5/repos/python4office/hexo-public/raw/free-ai.jpg)

*微信扫码加入「免费用 AI」知识星球的入口。*

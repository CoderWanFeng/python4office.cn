---
title: Mac 和 Windows 不能隔空投送？9.9 万星的开源软件做到了
date: 2026-11-15 16:20:00
tags: [公众号文章, 效率工具, 开源软件, Mac, Windows]
categories: [公众号文章]
keywords: [LocalSend, LocalSend下载, Mac Windows 传文件, 隔空投送替代, 开源工具, 局域网传文件]
description: LocalSend：一个 9.9 万星的开源软件，装好就能在 Mac 和 Windows 之间互传文件、文件夹和文本，不用注册、不走云端。本文含官网与各平台下载直链。
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/localsend-cover.jpg
---

大家好，我是程序员晚枫。

上周我碰到一件小事：要把一个 1.2GB 的视频，从我的 MacBook 拷到公司的 Windows 台式机。

微信：超过 100MB 根本发不出去。QQ：能发，但压缩完画质糊了。网盘：上传 4 分钟，下载 4 分钟，拷进拷出又是 2 分钟。U 盘：我翻包找了一圈，没找到第二根。

最后我盯着 Mac 的「隔空投送」看了半天——那个按钮，安安静静地灰着。

**苹果的东西，暖不了 Windows 的冷。**

问题来了：跨系统传文件，真的只能靠网盘和 U 盘吗？

---

## 一个不需要账号的「隔空投送」

答案是一个开源软件：**LocalSend**。

它要做的事特别朴素——同一个 Wi-Fi 下，两台设备互相发现，点一下就传文件。听着没什么技术含量，但真香的是它把下面这几件事全做到了：

| 特性 | LocalSend 的做法 |
|------|------|
| 支持平台 | Windows、macOS、Linux、Android、iOS |
| 要不要注册 | **不要**，装好打开就能用 |
| 数据走不走云端 | **不走**，局域网内点对点传输 |
| 安全性 | 全程 HTTPS 加密，还能设 PIN 码 |
| 能传什么 | 文件、文件夹、文本、剪贴板内容 |
| 速度 | 吃满你 Wi-Fi 的带宽，不限速 |

![LocalSend 桌面端界面](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/localsend-desktop.jpg)

*图片来源：[LocalSend 官网](https://localsend.org/zh-CN)*

数字有点吓人：**GitHub 上 9.9 万颗星**（Star 就是 GitHub 上的收藏键，有多少人想留着它），**5674 个 fork**（有人把代码复制下来自己改），Apache 2.0 开源协议；官网自己写着，**全球下载量 3500 万+**，230 多位贡献者，**0 广告、0 跟踪器**。2022 年 12 月立项，到现在还在每周更新，最新版本是 2026 年 8 月发布的 v1.18.2。

一个「让手机和电脑说上话」的小工具，能做到这个体量，靠的从来不是营销。

---

## 它是怎么「凭空」找到你电脑的

这是我最想讲清楚的一段，因为理解了原理，你就明白这东西为什么靠谱。

LocalSend 的通信方式是 **REST API + HTTPS**。听起来很复杂，其实拆开就三步：

1. **发现**：每台开着的 LocalSend，会定时在局域网里广播一嗓子——「我在，我叫 XXX」。这一步走的是 UDP 广播，默认端口 53317。
2. **握手**：对方听到广播，回一句自己的信息，双方就知道「哎，你在这儿」。
3. **传输**：走 HTTPS 加密通道，文件直接从你这台机器，流到对方那台。

关键在第三步：**证书是每台设备现场生成的**。不需要去公共机构申请，也不需要谁来给你发账号密码——机器自己生成一张证书，临时用一下。

> 所以它才能做到「零账号、零服务器、零注册」。没有服务器，就没有账号体系；没有账号体系，就不用登录。

那为什么苹果的隔空投送，Mac 和 Windows 之间就是不行？

因为苹果用的是**蓝牙 + AWDL 这套私有协议**，从发现到传输全是苹果自己定的规矩，只在苹果设备之间互通。这不是技术上做不到跨平台，是**它把这件事做成了生态壁垒，顺便还做成了消费电子的信仰**。

LocalSend 的做法是：把「发现 + 加密传输」这两步用公开标准重新做了一遍，谁都能用。

这才是开源最值钱的地方——**它不是抄了隔空投送的界面，它是把隔空投送背后的门道拆开重装了一遍。**

顺带说个当下更有用的场景：现在很多人爱把文件往云端 AI 里丢，合同、简历、身份证，一上传就等于交出去了。LocalSend 这类工具的意义是——**文件从你手里直接到本地那台跑着模型的电脑上，中间一个第三方都不经过。** 数据不出门，这才是真的在用 AI 之前该想明白的事。

---

## 五步把文件送过去

安装完之后，熟练了其实只要 5 步：

1. Mac 和 Windows **都装上 LocalSend**；
2. 两台设备连**同一个 Wi-Fi**；
3. 都打开 LocalSend，**自动发现**对方；
4. 选好要传的文件或文件夹，**点一下对方的设备名**；
5. 接收端点「接受」，**传完收工**。

Mac 和 Windows 的下载地址，我直接放在这儿，不用去官网翻：

| 平台 | 下载地址 |
|------|------|
| 官网下载页（覆盖全部平台） | https://localsend.org/zh-CN/download |
| Mac（App Store） | https://apps.apple.com/us/app/localsend/id1661733229 |
| Mac（直接下载 dmg） | https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2.dmg |
| Windows（直接下载 exe） | https://github.com/localsend/localsend/releases/download/v1.18.2/LocalSend-1.18.2-windows-x86-64.exe |
| 浏览器就能用（网页版） | https://web.localsend.org/ |

我自己这台 MacBook Air 和公司的 Windows 台式机，中间隔着一张桌子，1.2GB 的视频传完是十几秒的事，传过去能直接双击打开，不用解码不用转码。

**文件大的话更爽。** U 盘那玩意儿现在是生产力灾难——你还得先找到它。

---

### 搜不到对方？先查这四件事

大部分人第一次用都会卡在「列表里看不到对方」。按顺序排查这四条，九成能解决：

1. **确认连的是同一个 Wi-Fi**，而且不是「访客网络」——访客网络会把设备互相隔离；
2. **Windows 防火墙放行 LocalSend**，第一次启动时它会弹窗问你，别一路点「取消」；
3. **Mac 给「本地网络」权限**（系统设置 → 网络 → 本地网络），没给的话它连广播都发不出去；
4. **路由器关掉 AP 隔离 / 客户端隔离**，有些公司网络和公共 Wi-Fi 默认开着。

还有一条现实经验：**有些公司网络和校园网会直接封掉 UDP 广播**，那种环境 LocalSend 天生发现不了对方。这时候最省事的办法是——手机开个热点，两台电脑连上去，一样传。

---

### 什么场景不适合它

工具好用归好用，边界得说清楚：

- **必须同一个局域网**。在公司想给家里的电脑发文件，它做不到，这不是 bug，是设计；
- **不适合当网盘用**。它不能生成链接发给别人，它只负责「这台机器到那台机器」；
- **公共网络要留心**。就算加密了，在不可信的 Wi-Fi 上传敏感文件，也不如在家传踏实。

如果你的场景是「懒得装软件」，还有几个替代方案，各有各的位置：

| 方案 | 适合场景 | 门槛 |
|------|------|------|
| **LocalSend** | 日常互传文件、照片、视频 | 两端各装一个客户端 |
| PairDrop / Snapdrop | 不想装任何软件 | 浏览器打开网页 |
| SMB 共享文件夹 | 经常互传，想在资源管理器里直接访问 | 要配共享和权限 |
| Windows 就近共享 | 只在 Windows 之间传 | Mac 用不了 |

**如果你只是日常互传文件、照片、视频，LocalSend 就是最接近隔空投送体验的那个，也最省事。**

---

最后说一句题外话。

我们这代人，被训练出了「什么都要先上传」的肌肉记忆——发文件先传网盘，存照片先传云盘，聊点私事先发云文档。

结果就是，**你的每一个文件，都要在别人的服务器上留一份底。**

LocalSend 这样的工具真正有意思的地方，不是「传得快」，而是它把选择权还给了你：**这个东西，是留在你自己的网络里，还是寄到别人那儿。**

技术不值钱，位置才值钱。

你平时 Mac 和 Windows 之间怎么传文件？网盘、U 盘，还是硬扛微信压缩？评论区聊聊，我挺好奇有多少人还在用 U 盘。

**科技不高冷，AI 很好用。**
我是晚枫，关注我，带你一起玩 AI！

### 参考链接

- [LocalSend 官网（中文）：https://localsend.org/zh-CN](https://localsend.org/zh-CN)
- [LocalSend 官方下载页：https://localsend.org/zh-CN/download](https://localsend.org/zh-CN/download)
- [LocalSend GitHub 仓库（9.9 万星，Apache 2.0）：https://github.com/localsend/localsend](https://github.com/localsend/localsend)
- [LocalSend 最新版本发布页（v1.18.2）：https://github.com/localsend/localsend/releases/latest](https://github.com/localsend/localsend/releases/latest)
- [LocalSend 通信协议文档：https://github.com/localsend/protocol](https://github.com/localsend/protocol)
- [LocalSend 网页版：https://web.localsend.org/](https://web.localsend.org/)

## 相关阅读

- [2026年最值得装的AI神器：开源免费，连接所有大模型](https://mp.weixin.qq.com/s/e5qz5U-2R14qGy88tMD1DA)
- [我做了个「开源搭子」skill：零基础也能秒推 GitHub，国内自动切镜像](https://mp.weixin.qq.com/s/V1oSvUbruxXgAUN0uuClVQ)
- [在 WorkBuddy 里做视频，简单到 3 步就出片](https://mp.weixin.qq.com/s/lU49BY3FjMLeNVQoJRDu5A)

![免费用AI](https://atomgit.com/api/v5/repos/python4office/hexo-public/raw/free-ai.jpg)

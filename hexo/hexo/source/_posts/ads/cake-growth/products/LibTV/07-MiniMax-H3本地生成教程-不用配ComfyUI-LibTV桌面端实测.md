---
title: "AI 数字人怎么做？小白3 步出片，不露脸不剪辑"
date: 2026-11-09 11:22:00
tags: ["公众号文章", "AI视频", "LibTV", "MiniMax H3", "本地部署"]
categories: ["公众号文章", "Python自动化办公社区"]
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261109-libtv-h3-digital-human-cover-v3-wanfeng.png
---

大家好，我是程序员晚枫（Wayne Liu）。

上周有个读者发来一屏报错截图，只配了一句话：晚枫，H3 不是开源了吗？我装了三个晚上，一条视频都没出来。

这种感受我太熟了。模型是免费的，可装模型的那三个晚上不是。

所以今天不聊 H3 有多强，只聊一件事：**本地跑 H3，怎么从三个晚上缩短到吃顿饭的功夫。**

开头放了一条我用 H3 做的视频，大家先看看效果。不过这条是我写代码调接口做出来的，过程挺折腾。如果你不懂技术，或者压根不想碰开发环境，直接看后面的 LibTV 桌面端就行，不用从写代码开始。

想再省点事，也可以看看 [LibTV 和 WorkBuddy 搭着用的方法](https://mp.weixin.qq.com/s/lU49BY3FjMLeNVQoJRDu5A)，两个工具配合起来，操作更顺手。

---

👉 [点击这里下载 LibTV 桌面端： https://libtv.cgref.cn/s/9omkl4jn4d](https://libtv.cgref.cn/s/9omkl4jn4d)

---

## 一、以前本地跑 H3，难的不是显卡，是拼零件

MiniMax 8 月 3 日把 H3 的权重放了出来，这件事本身挺痛快的。

![MiniMax H3 在 Hugging Face 上的官方模型页](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261109-minimax-h3-huggingface-model-card.png)

*图片来源：[MiniMax H3 官方模型仓库（Hugging Face）](https://huggingface.co/MiniMaxAI/MiniMax-H3)*

可权重能下载，不代表你就能用上，中间还隔着五道关。

| 第几关 | 要干的事 | 最容易卡在哪 |
|---|---|---|
| 1 | 装运行环境 | 版本对不上，装一遍报一遍错 |
| 2 | 拉模型文件 | 40–60GB 起步，完整包约 144GB，国内下载经常断 |
| 3 | 找工作流模板 | 文生、图生、参考生视频各有模板，不知道该用哪个 |
| 4 | 调节点参数 | 步数、分辨率、量化档位，一个不对就白等 |
| 5 | 排查报错 | 缺文件、格式混用、显存溢出，报错还全是英文 |

光是 ComfyUI 官方教程里列出的 H3 模板就有好几个，每个对 ComfyUI 的版本要求还不一样。新手头一回打开，很容易看懵。

![ComfyUI 官方 H3 教程列出的模板工作流和版本要求](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261109-comfyui-minimax-h3-template-workflows.png)

*图片来源：[ComfyUI 官方 MiniMax H3 教程](https://docs.comfy.org/tutorials/video/minimax/minimax-h3)*

最磨人的还是第五关。原因在于，一个能同时出画面和声音的视频模型，不是一个文件，而是一整套零件：读懂提示词的文本编码器，把画面压成数据的图像编解码器，真正干活的主网络，再加上合成声音的音频模块。

拿相机打个比方：机身、镜头、存储卡、麦克风，少一样都按不下快门。开源放出来的是全套零件，可组装得你自己来，装错一个位置，就是满屏报错。

我见过最执着的一位读者，装到第三天，已经不在乎视频了，只想要一个能点「下一步」的按钮。

说实话，这个要求一点都不过分。

---

## 二、LibTV 桌面端把这五关，压成了一次安装

LibTV 是哩布哩布 AI 做的一站式 AI 视频创作平台，网页版本来就接入了 Seedance、可灵、Wan、MiniMax H3 这些模型。新出的桌面端，专门把「本地跑 H3」做成了一个客户端。

![LibTV 官网首页，模型栏里已经有 Minimax H3](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261109-libtv-official-home-models.png)

*图片来源：[LibTV 官网](https://www.liblib.tv/)*

**它最大的好处是：电脑配置够的话，装完就能在本机跑 H3，不用自己配 ComfyUI。**

一共三步：

| 步骤 | 你做什么 | 要注意什么 |
|---|---|---|
| 第 1 步 | 从 LibTV 桌面端官网下载 Windows 客户端并安装 | 安装包只有十几 MB，大模型文件要等第一次运行时才下载，别以为装完就完事了 |
| 第 2 步 | 打开后在模型列表里选 MiniMax H3 | 选的就是本地生成这条路 |
| 第 3 步 | 写一句提示词，点生成 | 第一次要下模型，耐心等；先用低分辨率试，满意了再调高 |

原来要照着教程一条条敲命令的本地部署，到这里就成了装一个软件、点两下鼠标。很多人到处搜「MiniMax H3 本地部署」「一键部署」，要找的其实就是这么个装完能用的东西，而不是又一篇得跟着敲的教程。

我推荐 LibTV 还有一个原因：自己写代码、调接口，试错成本不低。

开头那条 8 秒的视频，我已经挑了比较便宜的模型，视频生成加上语音调试，还是花了 30 多块。效果不满意就得重来，每重来一次都可能接着扣钱。**自己折腾，烧掉的不只是时间，还有真金白银。**

![8 秒视频的模型生成和语音服务扣费记录](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261109-h3-8s-opencode-cost.png)

*图片来源：我的 opencode 后台扣费记录*

30 多块贵不贵，要看这条视频能不能把钱挣回来。

我前段时间在视频号发过一条讲免费大模型的视频，65.2 万播放，创作分成拿了 268.59 元，具体经过写在《[1条视频赚了268元，我找到了中国版YouTube](https://mp.weixin.qq.com/s/yvVsbyPasEqr7DHB6Qq_Zg)》里。如果你的视频也能这样分到钱，那 30 块的生成成本基本可以忽略不计。

可也有另一面：我另一条视频 59 万播放，只分到 85.24 元；而且视频号要有 100 个有效关注才能开通分成。刚起步的时候，大多数视频是挣不到钱的，这时候一条 30 块就是实打实的成本，试十次就是三百。

所以还没靠视频挣到钱之前，先把单条成本压下来。LibTV 桌面端在这一点上很合适：电脑配置够的话，本地生成这一段不按次扣云端积分，多试几次也不心疼。

不过，「配置够」这三个字不是客气话，是硬门槛：

**显存 12GB 起步，推荐 24GB 以上；内存 32GB 起、推荐 64GB；固态硬盘留出 150GB 以上；系统 Windows 10/11。**

这些数字取自 MiniMax 官方开源说明和社区公开的实测，量化版本、显卡驱动不同，实际表现会有出入。达不到这个配置，装上了也跑不动。哪些电脑会卡，我在另一篇《别急着装 LibTV 桌面端》里按显卡档位列了清单，可以对照着看。

![在本地电脑上生成 AI 视频，已经不用自己拼环境了](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261109-libtv-h3-laptop-work.jpg)

还有一点容易被忽略：第一次能不能生成成功，要看模型文件有没有下全。

翻官方和社区的排查记录，最常见的失败就是漏了文本编码器或图像编解码器里的一两个文件，接着就一直报「找不到文件」。所以第一次运行宁可多等一会儿，别断网，也别强行关掉。

---

👉 [点击这里下载 LibTV 桌面端： https://libtv.cgref.cn/s/9omkl4jn4d](https://libtv.cgref.cn/s/9omkl4jn4d)

---

## 三、先把话说清楚：免费的到底是哪一段

我看到不少文章把这件事写成「全功能、完全离线、永久免费」。

这几个说法，其实都不准确。

MiniMax 这次开源的是 **H3-Base**，也就是生成画面和声音的主网络。本地能出的是短边 768p、4–15 秒、24 帧、32kHz 立体声的有声视频，支持 11 种语言。

完整系统里还有两段没开源：

- **H3-Context-IR**：把复杂指令翻译成模型听得懂的话，官方托管，只开放接口
- **H3-Regenerate-2K**：把 768p 的结果重做成 2K，同样只开放接口

![MiniMax H3 系统总览，本地开源的是中间那一段](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260823-minimax-h3-overview.png)

*图片来源：[MiniMax H3 官方开源说明](https://www.minimax.io/news/minimax-h3-open-source)*

所以目前没法在本地直接出 2K。不是你的显卡不够，是这一段根本不在开源包里。

另外，权重受 **MiniMax H3 Community License** 约束：美国、欧盟、英国、韩国不在标准授权范围内；年营收超过 2000 万美元的商业主体需要书面授权；商用界面还要显著标出「MiniMax H3」。所以拿来商用之前，最好先把许可证读一遍。

那 LibTV 桌面端到底免不免费？准确地说：

**客户端可以免费安装，本地生成这一段不按次扣云端积分；但平台上的高级模型、更高额度、2K 增强等功能，仍可能需要在站内付费，具体以应用内当天显示的为准。**

微软商店的 LibTV 页面也是这么写的：应用可免费安装，免费额度可能受每日次数、可用模型、导出能力等限制，部分权益需要另外购买。

![Microsoft Store 上的 LibTV 应用页](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261109-libtv-microsoft-store-page.png)

*图片来源：[Microsoft Store 上的 LibTV](https://apps.microsoft.com/detail/9n7c2h1ld5kq)*

如果你手里有一台高配电脑，LibTV 桌面端就是把 H3 本地这一段免费跑起来最省事的办法。

---

最后说句实在话。

开源给的是零件，桌面端给的是装配线。省下来的主要不是钱，是你不用再花三个晚上，去证明自己会装环境。

把这些时间拿去多改几遍提示词吧。片子好不好，差别在提示词上，不在环境装得多漂亮。

💬 **来评论区聊聊**

你本地跑 H3 卡在第几关？是下载、显存，还是那句看不懂的报错？评论区说说，我挑典型的单独写一篇排查。

### 参考链接

- [MiniMax H3 官方开源说明： https://www.minimax.io/news/minimax-h3-open-source](https://www.minimax.io/news/minimax-h3-open-source)
- [MiniMax H3 官方模型仓库： https://huggingface.co/MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3)
- [ComfyUI 官方 H3 教程： https://docs.comfy.org/tutorials/video/minimax/minimax-h3](https://docs.comfy.org/tutorials/video/minimax/minimax-h3)
- [LibTV 官网： https://www.liblib.tv/](https://www.liblib.tv/)
- [Microsoft Store 上的 LibTV： https://apps.microsoft.com/detail/9n7c2h1ld5kq](https://apps.microsoft.com/detail/9n7c2h1ld5kq)

## 相关阅读

- [别花钱做AI视频了：MiniMax 免费开源 H3，人人可用](https://mp.weixin.qq.com/s/cupxgLQVY5PdNBAYuPhJxA)
- [你的电脑就能跑AI，不用花一分钱](https://mp.weixin.qq.com/s/m0sldnGPyMXh5KKZLZOZYA)
- [别花钱做视频了：MiniMax 开源 H3](https://mp.weixin.qq.com/s/KT3A2ec3Z2rgJ8vAsGGxgg)

💬 **再聊一句**

如果你也不想在本地生成这一步上折腾，可以点下面的链接，试试 LibTV 桌面端。

一个人，也能把一条片子从头做到尾。

👉 [点击这里下载 LibTV 桌面端： https://libtv.cgref.cn/s/9omkl4jn4d](https://libtv.cgref.cn/s/9omkl4jn4d)

---

**科技不高冷，AI很好用。**
我是晚枫（Wayne Liu），关注我，带你一起玩AI！

![免费用AI](https://atomgit.com/api/v5/repos/python4office/hexo-public/raw/free-ai.jpg)

<!-- 编辑备注（不显示给读者）：2026-11-09 新增 4 张官方截图——Hugging Face MiniMaxAI/MiniMax-H3 模型页、ComfyUI 官方 H3 教程模板区、LibTV 官网首页模型栏、Microsoft Store LibTV 应用页（描述原文："本应用可免费安装……免费使用可能受到每日 credits、生成次数、可用模型、导出能力、视频质量或其他功能限制的影响"）。ComfyUI 教程列出 5 个 video_minimax_h3_* 模板，T2V/I2V/R2V 需 ComfyUI 0.30.0+，Multiframe Reference 需 0.34.0+。封面 v3：背景 AI 生成（无品牌元素），屏幕人物为作者本人形象（参考 ai-digital-human/persona/demo4/reference），Logo 取自 liblib.tv 页面 SVG 与 minimax.io 官方白色横版 Logo；封面不写"不扣积分" -->

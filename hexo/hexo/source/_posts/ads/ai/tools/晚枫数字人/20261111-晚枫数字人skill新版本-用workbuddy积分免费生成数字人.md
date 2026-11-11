---
title: 「晚枫数字人 Skill」发布新版本：用 WorkBuddy 积分免费生成数字人
date: 2026-11-11 10:55:00
tags:
  - 数字人
  - skill
  - SkillHub
  - WorkBuddy
  - MiniMax
  - AI配音
  - 零基础
categories: AI工具评测
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/cover-%E5%85%AC%E4%BC%97%E5%8F%B7%E5%B0%81%E9%9D%A2-%E6%95%B0%E5%AD%97%E4%BA%BA-v2.jpg
---

大家好，我是程序员晚枫。

上次把「晚枫数字人」这个 Skill 发出来之后，这是那篇文章：

[我做了个「晚枫数字人」Skill：不会剪辑，也能做自己的数字人视频](https://mp.weixin.qq.com/s/IyhSEzVvIMRC164h-wD0Iw)

发出去之后，评论区问得最多的就一句话：**想试一下，是不是必须先充值？**

答案是「是」。老版本只有一条路：MiniMax，克隆音色、生成画面，都按量付费，第一次做一条得先准备 12 块。

说白了，掏十几块去试一个 AI 工具，对大多数人真不算小数目。评论区里排前面的回复是「太贵了，等涨工资再说」。

**大家都是靠薅免费额过日子的穷人，懂你。**

所以我把它更新了一版。**新版本多了一条完全免费的路：用 WorkBuddy 自己的积分生成，一分钱不花。**

代价我先摊开说，不藏着：**这条免费路只能出画面，出不了你的声音，效果也不如 MiniMax 那条。**


![确认 WorkBuddy 不能根据声音生成一段新的音频](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/wanfeng-digital-human-no-voice-clone.png)

成片里会有模型自己念的一句台词，那是通用音色，不是你的声音；你输入的那句文字，也不能拿来做配音。

想用自己的声音说话，还是得走 MiniMax 那条付费路。

**免费又好用的东西，目前PDD都做不到。** 积分这条的意义，是让你不用先掏钱就能看到自己出现在镜头里；真要好看，还是得走 MiniMax 那条付费路。

两条我都留着：想先试水走积分，想直接出好片走 MiniMax。

站内那篇更长的完整介绍，我留在文末的「相关阅读」里。

<!-- more -->

---

## 它到底能帮你做什么

你给它的东西还是很简单：

- 一段你自己的视频，或者一张正脸照片；
- 一句想说的话，40 字以内；
- 走 MiniMax 的话，素材里没声音再补一段 15–20 秒的录音；走积分路线不用录音。

出来的是一条 **4–10 秒的数字人短片**：画面里是你，说的是你写的那句话。

两条路线，差别就这几处：

| | WorkBuddy 积分 | MiniMax |
| --- | --- | --- |
| 画面 | 768P / 2K 两档 | 480P / 1080P |
| 声音 | 模型自带通用音色 | 你的克隆音色 |
| 字幕 | 没有 | 有 |
| 花费 | 不花钱，只消耗 WorkBuddy 积分 | 按量计费，以实际消耗为准 |
| 前置条件 | 装客户端 + 注册账号 | 开账号、实名、充值、开 Key |

一句话：**想先试试水，走积分；想用自己的声音说话，走 MiniMax。**

录一段自我介绍、讲一个知识点、发一条节日祝福，或者给账号做一条短口播，都可以从它开始。

---

## 安装只要三步

**第一步：找到技能。** 电脑打开 WorkBuddy，点击左侧「专家·技能·连接器」，切换到「技能」，搜索「晚枫数字人」。

![在 WorkBuddy 技能页面搜索晚枫数字人](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/wanfeng-digital-human-search.png)

*WorkBuddy 技能页搜索「晚枫数字人」，认准这个名字。*

**第二步：点击安装。** 进入详情页，能看到它的用途、需要配置的 API Key，以及具体的执行说明。确认后点击「安装」。

![晚枫数字人 Skill 详情页和安装按钮](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/wanfeng-digital-human-install.png)

*技能详情里已经写明用途和费用，不用先研究技术文档。走积分路线的话，这次的 API Key 用不上。*

**第三步：点击「去试试」。** 安装完成后，会弹出提示。点一下，就能进入带有这个技能的对话页面。

![晚枫数字人安装完成后点击去试试](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/wanfeng-digital-human-try.png)

*安装完成后，直接进入对话，不需要手动配置运行环境。*

懒得找技能页也行：直接在对话里说「帮我装晚枫数字人技能」，它会自己到市场里找、等你确认再装。

---

## 开工第一步：先选一条路

进入对话页面，输入：**@晚枫数字人 帮我生成数字人**。

装好技能后，它不会闷头开工，而是先问你一个关键问题：这次的数字人走哪条路生成？

![Skill 询问这次的数字人走哪条路生成：WorkBuddy 积分生成 或 MiniMax 生成](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/wanfeng-digital-human-credits-route-choice.png)

*开工第一件事就是选路：上面是 WorkBuddy 积分生成，下面是 MiniMax 生成。*

两个选项的意思：

- **WorkBuddy 积分生成** —— 不花钱，只消耗你账号里已有的 WorkBuddy 积分。注册就有，按周期发放，不用实名、不用充值、不用 API Key；
- **MiniMax 生成** —— 克隆你的音色，费用按 MiniMax 平台的实际消耗结算。

### 免费这条路的代价：出不了你的声音，效果也差一截

这一点我不想让你踩坑，所以单独摊开讲。

积分路线走的是 WorkBuddy 内置的视频生成能力，画面是你的，但声音是模型自己念的一句——通用音色，不是你的。更关键的是，**它不能根据输入的文字生成配音**，台词也控制不了。

效果上我自己对比下来，MiniMax 那条出来的画面和动作更自然一点，积分路线属于「能看，但差点意思」。

所以两条路的分工很明确：

- **积分路线**：画面是你的，模型替你念一句，零花费，成片比 MiniMax 那条糙一些。适合先看看效果，判断自己要不要往下做；
- **MiniMax 路线**：画面更自然一点，声音是你的，字幕也有，按量付费。

想用自己的声音说话，只能走 MiniMax。积分路线做不到的事，我也不会绕着说。

---

## 第一次使用，按路线准备

**走 WorkBuddy 积分：** 什么都不用额外准备。装好客户端、注册登录、装上技能，就有积分可用。积分够不够、消耗明细，个人中心就能看到。

用邀请链接注册，你和邀请人都能多拿一些积分：

[WorkBuddy 邀请注册（邀请码 b1m7bevc9r7ma52y）](https://www.workbuddy.cn/events/invite?inviteCode=b1m7bevc9r7ma52y)

积分全部用完时，WorkBuddy 的 AI 能力会暂停，下个发放周期自动恢复。

**走 MiniMax：** 四件事缺一不可。

1. **注册账号**（免费）：[platform.minimaxi.com](https://platform.minimaxi.com)，手机号注册并登录；
2. **实名认证**：账户管理 → 实名认证，身份证加人脸。个人认证当场就过，不用等审核；
3. **充值余额**：账户管理 → 余额 → 充值，先充一笔够做两三条的；
4. **创建 API Key**：账户管理 → 接口密钥 → 创建新的 API Key，复制出来。

两个坑提前避开：

- **Key 有两种，别拿错。** 要用「按量付费」的 Key；订阅套餐那种（`sk-cp-` 开头）调不通，一路报鉴权错误；
- **Key 只显示一次。** 创建完当场复制，关掉页面就看不到了。

四步做完大概五六分钟。前三步只能你自己去平台上点，我帮不了；四步都做完，剩下的就是我的事。

**两条路都要用的两样：**

**1. 一段合格的形象素材。** 最好用 10 秒以上的本人视频。正脸看镜头、光线均匀、背景干净，画面里只出现一个人。

照片也能用，但表情和头部动作会少一些。视频不足 10 秒，走 MiniMax 的话要补一段 15–20 秒、没有背景音乐和回声的自然说话录音。

**2. 一句真正想说的话。** 建议 40 字以内，最好控制在 36 字左右。一句话只讲一个意思，不要加「镜头拉近」「旁白」这类说明，它们可能会被一起念出来。

> 请只使用本人或已经获得明确授权的形象与声音。API Key 不要发到公开群，也不要写进公开文档。

---

## 费用和边界，提前说清楚

**走 WorkBuddy 积分：不花钱。** 生成只消耗账号里已有的积分，不产生任何额外费用。代价是声音只能用模型自带的音色，台词控制不了，也没有字幕。

**走 MiniMax：声音和视频分开收费。**

| 项目 | 参考费用 | 说明 |
| --- | --- | --- |
| 克隆自己的声音 | 约 1 元 | 一次性，之后可以复用 |
| 合成一句台词 | 约 0.02 元 | 按实际内容计算 |
| 生成数字人画面 | 约 1.1–1.8 元 | 每条收一次，越长、分辨率越高越贵 |

第一次完整做一条，通常按**约 12 元**准备；音色克隆完成后，再做一条通常约 2 元。具体费用会随时长、清晰度和平台价格变化，技能显示的是预估，不是最终账单。

有一个设计我特意保留了：**先只做声音，试听满意后再生成画面。** 音色克隆一次，后面继续复用，不会每做一条都重新付一遍。每次真正调用付费接口前，也需要你明确确认。

它也有清楚的边界：

- 适合做 4–10 秒的单条短片，不做 30 秒以上的长视频和多段拼接；
- 口型能做到大致同步，不承诺逐帧对齐；
- 背景、衣服和整体质感主要由你的素材决定，不是任意换装、换场景工具。

如果你要做更长的口播、多段数字人和 B-roll 规划，可以再看「晚枫数字人 Pro」。普通版负责让第一次尝试足够简单。

---

## 官方评测 4.8 分，数据安全也说清楚

这个 Skill 是我开发的，但「好用」和「可信」不只由我自己说了算。

它已经在 SkillHub 平台跑完了官方 TRACE 评测，**综合得分 4.8 / 5，综合评级「优秀」**，测评时间是 2026 年 11 月 10 日。其中，**可信任度拿到了 5.0 分**。

可信还有很重要的一层：虽然这个 Skill 是我开发的，但数字人生成默认全程调用 **MiniMax 官方接口**，我没有搭建接收用户素材的后台。

你的照片、视频和录音不会经过我的服务器，我也不会因为发布这个 Skill 就能获得查看或收集它们的入口；API Key 配置后保存在你的本机。

走积分路线则完全不碰 MiniMax，素材只在你本机和 WorkBuddy 之间走。

也要把数据边界如实说清楚：生成所需的形象和音频素材会发送给 MiniMax 官方接口，并不是所有素材始终只留在本机。

WorkBuddy 与 MiniMax 对数据的处理，仍以各自平台的隐私政策和安全机制为准。**我能保证的是，素材不经过作者服务器，我也没有获取你数据的入口。**

TRACE 是 SkillHub 用来判断一个 Skill 到底好不好用的五维体系，基于平台长期运营实践和腾讯新闻团队的内容生产经验沉淀而成。

![SkillHub TRACE 评测五维度得分：可信任度 5.0、可靠性 4.7、适用性 5.0、规范性 4.8、有效性 4.6](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/wanfeng-digital-human-trace.png)

*SkillHub 官方评测报告，数据来自平台评测页面。*

五个维度的具体得分：

| 维度 | 得分 | 评测说明 |
| --- | --- | --- |
| T · 可信任度 Trust | 5.0 | 双实验室交叉验证，无 P0/P1 级安全风险 |
| R · 可靠性 Reliability | 4.7 | 正常情况能顺利生成并说清费用，失败时也会指出原因 |
| A · 适用性 Adaptability | 5.0 | 用途和限制交代清楚，费用说明基本无歧义 |
| C · 规范性 Convention | 4.8 | 说明层次清楚，主要步骤容易照做 |
| E · 有效性 Effectiveness | 4.6 | 流程清楚、报价透明，先试听再生成能减少误花 |

几个被打了满分的子项，值得单独说一句：

- **国内适配性 5.0** —— 说明和错误提示全是中文，所需账号和接口在国内直接开通就能用；
- **能力边界定义 5.0** —— 能做什么、不能做什么写得很明确，有效避免用户提出做不到的需求；
- **触发方式 5.0** —— 可以用自己的日常说法发起请求，不需要记固定名称或复杂指令；
- **反模式与 FAQ 5.0** —— 常见错误、失败原因和替代办法都写得很具体，遇到问题能直接按步骤排查修正；
- **渐进式披露 5.0** —— 入门信息排前面，复杂细节和排错方法放后层，需要时再查。

评测报告的原话是：整体完成度较好，收费前说明清楚，会先确认声音效果，也能减少重复付费，素材要求、费用和常见问题都有较细致的指引。

它也点出了不足：少量说明前后不一致，个别操作指引不够清楚。

> 这几条我认。费用数字在不同文件里确实有几处对不上，接下来的版本会把价格表收敛到一处，顺手补一个完整的示例配置文件。

评测报告（作者本人可见）：[SkillHub 评测报告页](https://skillhub.cn/dashboard/evaluation/wanfeng-digital-human?namespace=user_bf8c5b73)

---

## 现在，做出你的第一条

如果你一直想试数字人，又不想先研究一整套复杂工具，现在可以打开 WorkBuddy，在技能页搜索「晚枫数字人」。

安装后，发一句「@晚枫数字人 帮我生成数字人」，跟着提示往下走就行。**想零成本试水，第一步就选 WorkBuddy 积分生成。**

出来的片子满意了，再决定要不要花钱走 MiniMax 那条，把它做到你真正想要的样子。

> **先别追求完美。拍一段正脸视频，写一句真心想说的话，把第一条做出来。**

也可以直接访问 [「晚枫数字人」SkillHub 发布页](https://skillhub.cn/skills/user_bf8c5b73/wanfeng-digital-human) 了解详情。

想查看源码或了解具体实现，可以访问「晚枫数字人」GitHub 开源仓库：

https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/wanfeng-digital-human

---

## 最后，再推荐一个财务办公 Skill

如果你经常处理报销、进项核对或税务台账，可以试试我做的另一个 Skill——「晚枫票据管家」。

它能把增值税发票照片、扫描件和 PDF 批量整理成固定表头的 Excel 台账，减少手工誊抄。

👉 [晚枫票据管家 SkillHub 发布页](https://skillhub.cn/skills/user_bf8c5b73/poocr-vatinvoice2excel)

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20261110-poocr-vatinvoice2excel-卡片拼接.png)

发布页目前显示 **SkillHub AI 评分 4.7 / 5.0、下载量约 1300 次**，科恩实验室和云鼎实验室的安全结果均为「安全，无风险」。想体验的财务朋友，把下面这句直接发给 WorkBuddy：

**请根据 `https://skillhub.cn/install/skillhub.md`，安装 @user_bf8c5b73/poocr-vatinvoice2excel。**

识别使用腾讯云专用 OCR 接口，需配置 API Key，调用额度与费用以腾讯云页面为准。

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！

---

### 参考链接

- [晚枫数字人 SkillHub 发布页：https://skillhub.cn/skills/user_bf8c5b73/wanfeng-digital-human](https://skillhub.cn/skills/user_bf8c5b73/wanfeng-digital-human)
- [晚枫数字人 SkillHub 评测报告：https://skillhub.cn/dashboard/evaluation/wanfeng-digital-human?namespace=user_bf8c5b73](https://skillhub.cn/dashboard/evaluation/wanfeng-digital-human?namespace=user_bf8c5b73)
- [WorkBuddy 官网：https://www.workbuddy.cn](https://www.workbuddy.cn)
- [MiniMax 开放平台：https://platform.minimaxi.com](https://platform.minimaxi.com)
- [MiniMax 视频生成文档：https://platform.minimaxi.com/docs/guides/video-generation](https://platform.minimaxi.com/docs/guides/video-generation)

## 相关阅读

- [我做了个「晚枫数字人」Skill：不会剪辑，也能做自己的数字人视频](https://mp.weixin.qq.com/s/IyhSEzVvIMRC164h-wD0Iw)
- [别花钱做AI视频了：MiniMax 免费开源 H3，人人可用](https://mp.weixin.qq.com/s/cupxgLQVY5PdNBAYuPhJxA)
- [在 WorkBuddy 里做视频，简单到 3 步就出片](https://mp.weixin.qq.com/s/lU49BY3FjMLeNVQoJRDu5A)

---

![免费用AI](https://atomgit.com/api/v5/repos/python4office/hexo-public/raw/free-ai.jpg)

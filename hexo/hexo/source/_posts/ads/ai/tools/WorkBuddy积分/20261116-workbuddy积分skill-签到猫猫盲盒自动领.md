---
title: 我做了个「WorkBuddy 每日积分」Skill：签到、派猫猫、开盲盒，一条命令
date: 2026-11-16 23:00:00
tags:
  - Skill
  - WorkBuddy
  - 积分
  - 自动化
  - Python
categories: AI工具评测
cover: https://images.unsplash.com/photo-1616077168079-7f09c6775b1e?q=80&w=1200&auto=format&fit=crop
---

> **一句话总结**：WorkBuddy 成长中心那三件每天必做的事——签到、派猫猫、开盲盒——**一条命令全包**，还能让它自己定时跑。

大家好，我是程序员晚枫。

先说个真实场景。

WorkBuddy 客户端里有个「成长中心」，每天有三件事能做：

- **Buddy 加油站签到** —— 每天 100 积分；
- **派猫猫去旅行** —— 派出去，猫在外面走 1–4 小时，回来能领奖励；
- **开盲盒** —— 消耗能量，开出什么随缘。

**积分是干嘛的？** 免费用 AI 的时候能省不少事。所以这事儿看着小，其实每天都要惦记。

但你得记住：
- 早上打开客户端，签到；
- 点猫，派它出门；
- 4 小时后再点回来，领奖励；
- 能量够了再开几个盲盒。

**一天点四五次，两周之后就忘了。** 忘了就断签，断签损失比积分本身更大。

所以我写了「WorkBuddy 每日积分（workbuddy-daily-credits）」：**一条命令跑完三件事，一条命令可以设成定时任务。**

**SkillHub 发布页**：[WorkBuddy 每日积分：https://skillhub.cn/skills/user_bf8c5b73/wanfeng-workbuddy-daily-credits](https://skillhub.cn/skills/user_bf8c5b73/wanfeng-workbuddy-daily-credits)
<!-- more -->

## 一、它凭什么不用手点

这里有个判断，我觉得是这个 Skill 最值钱的地方。

**成长中心本质上就是个网页。** WorkBuddy 客户端只是用带登录态的 webview 打开它而已。

那就有两条路：

| 方案 | 做法 | 问题 |
|---|---|---|
| **模拟点击** | 脚本控制鼠标去点按钮 | 页面一改版就全挂；还要处理分辨率、坐标、动画 |
| **直接调接口** | 读本机登录态，直接请求官方接口 | 稳 |

**它选了第二条。**

理由很简单：**界面是给人看的，接口才是给机器用的。** 页面改版改的是布局，不会改接口。

而且省下来的不只是稳定，还有心理负担——**你不用盯着那个猫到底旅行回来没有。**

## 二、三件事，三条接口

| # | 做什么 | 背后的接口 | 幂等性 |
|---|---|---|---|
| ① | Buddy 加油站签到（每日本 100 积分） | `POST /v2/billing/meter/daily-checkin` | ✅ 幂等，当天已签返回「已签到」，**不重复发** |
| ② | 派猫猫（Buddy）旅行 | 先 `POST .../travel/claim` 领，再 `POST .../travel/depart` 派 | ✅ 到达奖励一直挂着，**不会被扣掉** |
| ③ | 开盲盒 | `GET /activity/growth/energy` → `POST /activity/growth/buddy/open` | ✅ 能量不足**直接不发请求** |

**「幂等」这三个字很重要。**

它意味着：**你今天跑了 3 遍、跑了 10 遍，积分也只签一次，猫也只派一次。** 不存在「手滑多跑一次，多扣你积分」这种事。

所以你可以放心地把它扔进定时任务，不用担心任务重复触发。

## 三、怎么用

### 第 1 步：确认能跑

```bash
# 预览模式：只查询，不提交任何写请求
python3 scripts/wb_credits.py --dry-run
```

**第一次一定先跑这个。** 它只读不写，能让你先看清状态。

### 第 2 步：真跑

```bash
python3 scripts/wb_credits.py
```

输出长这样：

```
== WorkBuddy 每日积分 ==
① 签到：今日已签到，无需重复打卡
② 猫猫：状态 idle｜今日派遣次数已用完，跳过派遣
③ 盲盒：能量 5 / 每次 10，不够开一次，未开箱
----------------------------------------
积分余额：1800｜连续登录：18 天｜今日已签到：True
```

**能量不够时它就明说「不够开一次，未开箱」，不硬开。**

### 常用参数

| 参数 | 作用 |
|---|---|
| `--dry-run` | 预览：只查询，不提交任何写请求 |
| `--no-box` | 跳过盲盒（只做签到 + 猫猫） |
| `--max-box N` | 本次最多开 N 个盲盒 |
| `--channel auto\|local\|web` | 登录态通道，默认 auto |
| `--config <路径>` | 指定配置文件 |
| `--json` | 输出 JSON（给定时任务 / 二次开发用） |

## 四、前置条件只有两条

**1. WorkBuddy 客户端已经登录。** 装了、用着就行，**脚本自己去找登录态文件**，不用你导出 cookie。

**2. Python 3.8+。**

- macOS / Linux：系统自带 `python3`，什么都不用装；
- Windows：用 WorkBuddy 自带的 Python，路径形如：
  ```powershell
  & "$env:USERPROFILE\.workbuddy\binaries\python\versions\3.13.12\python.exe" scripts\wb_credits.py
  ```

**注意：Windows 上要把 `python3` 换成那个完整路径**，直接敲 `python3` 是跑不起来的（Windows 默认命令是 `python`）。这是新手最常卡住的地方。

## 五、让它自己每天跑

用宿主（WorkBuddy / CodeBuddy）的**定时任务**功能，设两条：

- **早上 8:30** —— 签到 + 派猫猫出门；
- **晚上 18:30** —— 领回已到达的旅行奖励。

**为什么必须分两次？** 因为**猫在路 1–4 小时**。早上跑一次只能派出去，领不回来；单次跑是跑不到「领取」这一步的。

给自动化写这么一句话就够了（路径按实际改）：

> 每天 8:30 和 18:30，执行 `python3 <技能目录>/scripts/wb_credits.py`，然后用中文简报：积分余额、签到结果、连续登录天数、猫猫状态、能量、盲盒结果。报错就如实说原因，不要编造数字。

最后那句「**不要编造数字**」是特意加的。**自动化最怕的不是失败，是失败之后编一个漂亮的数字糊弄过去。**

> **两条任务共用同一条命令是安全的**：签到幂等，旅行「到达未领」会一直等你下次来领。

## 六、安全边界：四条

| 边界 | 说明 |
|---|---|
| **只读登录态** | 读本机的 `workbuddy-desktop.info`（macOS 需解密），**绝不打印、绝不上传 token** |
| **写操作只有那几个接口** | 签到、旅行领取、旅行派出、开盲盒。**不碰兑换、抽奖、支付** |
| **能量护栏** | 能量 < 单次成本时直接返回，**不发送任何开箱请求**。单次开箱上限默认 2 个 |
| **不修改任何文件** | 不写注册表，不留后台进程 |

**「绝不打印、绝不上传 token」这条是底线。** 一个要读你登录态的工具，**如果你不确定它会不会把 token 打出来，就别用。**

## 七、已知限制，我直说

1. **开箱收益无法预先保证** —— 能开出什么由服务端决定，脚本只负责「点」。
2. **成长计划里的任务不能代做** —— 体验某专家、关注公众号、用模板这些**没有对应接口**，只能人工点。
3. **断签要靠对话** —— 官方规则是「当天完成过一次对话才算记录一天」，脚本只负责签到那 100 分，**不代聊**。
4. **收益规则随时可能被官方调整** —— 字段做了容错，取不到就如实报错，**不会编造**。
5. **仅作用于你自己的账号** —— 不含批量、多账号能力。

**第 3 条我特别想强调一下：它不能帮你保住「连续登录天数」。** 那条记录靠的是「当天跟 WorkBuddy 聊过天」，是产品的设计，不是脚本能绕过的。

**能签到的 100 分它给你签到，连续记录它替不了。** 边界说清楚，才不会有人以为买了个自动续杯神器。

## 八、怎么装

**方式一：从 GitHub 拉源码（本地用）**

```bash
git clone https://github.com/CoderWanFeng/wanfeng-skills.git
cd wanfeng-skills/skills/workbuddy-daily-credits
```

**纯 Python 标准库**，不装任何第三方包，Windows / macOS / Linux 都能跑。

**方式二：从 SkillHub 一键安装（其他支持 Skill 的 AI 工具）**

打开发布页：

> [WorkBuddy 每日积分：https://skillhub.cn/skills/user_bf8c5b73/wanfeng-workbuddy-daily-credits](https://skillhub.cn/skills/user_bf8c5b73/wanfeng-workbuddy-daily-credits)

在支持 Skill 安装的 AI 工具里，可以直接发送下面这句话：

```text
请根据 https://skillhub.cn/install/skillhub.md，安装 @user_bf8c5b73/wanfeng-workbuddy-daily-credits。
```

也可以在发布页下载 Zip 包手动安装。

**源码在这**：

> **GitHub**：[workbuddy-daily-credits：https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/workbuddy-daily-credits](https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/workbuddy-daily-credits)

> **整个仓库**：[wanfeng-skills 仓库首页：https://github.com/CoderWanFeng/wanfeng-skills](https://github.com/CoderWanFeng/wanfeng-skills)

最后要特别致谢：这个 Skill 的登录态解密和接口封装，来自开源技能 **WorkBuddy积分助手**（作者 totorosir，MIT-0 许可），我在它基础上加了统一的盲盒入口和跨平台说明。

**如果你也是 WorkBuddy 用户**，可以试试：**把每天那四五次点按，换成一条命令。** 别小看「少点几下」——**少一件要惦记的事，比多 100 积分值钱。**

用的时候有问题，欢迎到 GitHub 提 Issue，也可以在文章下面留言。

科技不高冷，AI 很好用。我是晚枫，关注我，一起把 AI 真正用起来。

---

### 参考链接

- [workbuddy-daily-credits Skill 源码：https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/workbuddy-daily-credits](https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/workbuddy-daily-credits)
- [WorkBuddy 每日积分 SkillHub 发布页：https://skillhub.cn/skills/user_bf8c5b73/wanfeng-workbuddy-daily-credits](https://skillhub.cn/skills/user_bf8c5b73/wanfeng-workbuddy-daily-credits)
- [SkillHub 安装说明：https://skillhub.cn/install/skillhub.md](https://skillhub.cn/install/skillhub.md)
- [wanfeng-skills 仓库首页：https://github.com/CoderWanFeng/wanfeng-skills](https://github.com/CoderWanFeng/wanfeng-skills)
- [WorkBuddy 官方邀请注册：https://www.workbuddy.cn/events/invite?inviteCode=b1m7bevc9r7ma52y](https://www.workbuddy.cn/events/invite?inviteCode=b1m7bevc9r7ma52y)
- [WorkBuddy积分助手（totorosir-workbuddy-score）：https://github.com/totorosir-workbuddy-score](https://github.com/totorosir-workbuddy-score)

## 相关阅读

- [免费领取 WorkBuddy 3万积分，教程来了！](https://mp.weixin.qq.com/s/hNQTFuzF0v34D1n2LvigPg)
- [开学季羊毛：WorkBuddy 免费送 1000 积分](https://mp.weixin.qq.com/s/K7KTGzhoo8dZOXJTBt7yZg)
- [在 WorkBuddy 里做视频，简单到 3 步就出片](https://mp.weixin.qq.com/s/lU49BY3FjMLeNVQoJRDu5A)
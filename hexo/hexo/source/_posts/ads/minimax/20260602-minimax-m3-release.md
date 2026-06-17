---
title: MiniMax M3 发布！1M上下文+原生多模态，这才是真正的Coding神器
date: 2026-06-02 00:15:00
tags: ["MiniMax", "大模型", "M3", "Token Plan", "编程"]
categories: ["AI工具"]
cover: https://images.unsplash.com/photo-1677442136019-4526a9c9373a?q=80&w=1200&auto=format&fit=crop
---

<!-- more -->

大家好，我是程序员晚枫。

今天有个大消息要跟你们分享——**MiniMax M3 正式发布了！**

如果你一直在找一款既能写代码、又能看图片、还能理解长文档的AI模型，那M3可能就是你要等的那个。

---

## 一、M3 到底强在哪？

先说结论：**这是 MiniMax 目前最强的语言模型，没有之一。**

### 1. 1M 上下文窗口

M3 的上下文窗口达到了 **100万 Token**。

什么概念？之前的 M2.7 是 20万 Token，M3 直接翻了 **5倍**。

这意味着什么？

- 你可以把**整整一本书**扔给它分析
- 你可以把**几百页的需求文档**一次性喂进去
- 你可以把**整个代码仓库**的上下文都带上

我测试了一下，丢了一个 **80万字的技术文档** 进去，M3 不仅没崩，还能准确回答第50万字附近的细节问题。

**这才是真正的长上下文。**

---

### 2. 原生多模态

M3 不是"勉强支持"图片和视频，而是**原生多模态**。

- **图片输入**：支持 JPEG、PNG、GIF、WEBP，最大 10MB
- **视频输入**：支持 MP4、AVI、MOV、MKV，最大 50MB
- **文字输入**：这个不用说了，基础操作

举个例子，你可以：

> 扔一张**手抄的代码截图**给它 → 它帮你转成可运行的代码  
> 扔一段**操作视频**给它 → 它帮你写出操作文档  
> 扔一张**报错截图**给它 → 它直接告诉你哪里错了

**这对于写代码的人来说，简直是开挂。**

---

### 3. Agent 推理能力

M3 在 **Agent 工作流** 上的表现，比我预想的强太多。

它有原生支持的 **thinking** 模块——就是模型会在回答之前"先想想"。

不是装样子那种"我在思考..."，而是真的会：

- 分解复杂任务
- 规划执行步骤
- 调用工具（函数调用）
- 根据返回结果调整策略

我让它"帮我写一个爬虫，把某网站的所有文章标题抓下来，然后分析哪些是关于AI的"。

M3 的回答是：

1. 先分析网站结构（让我提供URL）
2. 写爬虫代码
3. 运行测试
4. 处理反爬措施
5. 输出分析结果

**一步一步来，不像某些模型，上来就给你一堆跑不通的代码。**

---

### 4. 兼容 Anthropic API

这个对于开发者来说，是个大好事。

M3 支持 **Anthropic API 格式**，也就是说：

- 你之前用 Claude 的代码，改个 `base_url` 和 `api_key` 就能用 M3
- 不用重新学一套 SDK
- 迁移成本几乎为零

```python
import anthropic

client = anthropic.Anthropic(
    base_url="https://api.minimaxi.com/anthropic",
    api_key="your_api_key"
)

message = client.messages.create(
    model="MiniMax-M3",
    max_tokens=1000,
    messages=[{"role": "user", "content": "帮我写一个快排"}]
)
```

**5分钟迁移完成，体验提升一个档次。**

---

## 二、Token Plan 新增了什么？

说到这，你们肯定要问：**"晚枫，M3 这么强，用起来贵不贵？"**

贵不贵先不说，我先告诉你，**MiniMax 的 Token Plan 这次新增了一堆权益**：

### ✅ 原有权益
- 高速稳定的 API 访问
- 按量计费，用多少付多少
- 新用户优惠

### 🆕 新增权益（这次的重点）

1. **语音生成权益**  
   用 M3 不仅能写，还能"说"。Text-to-Speech，支持多种情绪和语气。

2. **音乐生成权益**  
   是的，你没看错。MiniMax 现在支持 AI 音乐生成了。

3. **视频生成权益**  
   Hailuo 2.3 视频模型，图生视频、文生视频都能搞。

4. **图片生成权益**  
   配图不用再开 Midjourney 了，M3 生态全搞定。

**一句话：买 Token Plan，送你一整套 AI 创作工具。**

---

## 三、邀请好友，双重好礼

这次 Token Plan 上线，还有一个**邀请奖励活动**。

### 你邀请好友，双方都有好处：

**你的好友获得：**
- 🎁 **9折专属优惠**（用我的链接注册）
- 🎁 **Builder 权益**（更多功能和权限）

**你获得：**
- 💰 **返利**（好友消费，你拿佣金）
- 🏆 **社区特权**（专属身份标识）

---

## 四、怎么参与？

很简单，两步搞定：

### 第一步：注册 MiniMax

👉 **点击这个链接注册**：  
[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

（这是我的**专属邀请链接**，用这个注册，你享9折，我拿返利，双赢～）

### 第二步：选择 Token Plan

进去之后，选一个适合你的套餐：

- **轻度使用**：选按量计费，先充个50块试试水
- **重度使用**：选包月套餐，性价比更高

### 第三步：开始用 M3

注册完，拿到 API Key，就可以开始玩 M3 了。

**支持多种方式调用：**
- 直接调 MiniMax API
- 用 Anthropic SDK（改个 base_url 就行）
- 接入 Cursor / Claude Code / OpenClaw（我都测试过，能用）

---

## 五、我的一些使用建议

M3 很强，但要用好它，有几个建议：

### 1. 长文档分析用 M3，短对话用 M2.5

M3 的 1M 上下文很强，但**价格也比 M2.5 贵一些**。

我的用法是：
- 分析长文档、写复杂代码 → 用 M3
- 日常聊天、简单问答 → 用 M2.5（性价比更高）

### 2. 多模态别浪费

M3 支持图片和视频输入，但很多人不知道怎么用。

**几个实用场景：**
- 把报错截图发给他 → 比复制报错文字更准确
- 把手写笔记拍照发给他 → 帮你整理成 Markdown
- 把操作录屏发给他 → 帮你写操作手册

### 3. 邀请链接记得用

如果你身边有朋友也在用 AI 写代码，**把我的链接发给他**。

他省10%，你拿返利，何乐而不为？

---

## 六、最后说两句

MiniMax M3 的发布，让我看到了国产大模型的**真正实力**。

1M 上下文、原生多模态、强大的 Agent 能力，这些都是**实打实的功能**，不是PPT上的宣传语。

如果你还没试过 MiniMax，现在正是好时机：

- Token Plan 有新用户优惠
- 邀请活动正在进行（你9折，我拿返利）
- M3 的 API 已经稳定可用


---

## 相关阅读

- [刘润开始劝大家学AI编程，但我已经放弃了](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)
- [人在曼谷旅游，AI在帮我赚钱](https://mp.weixin.qq.com/s/KLXXEoxMu9uayJTLXStIzw)
- [最全AI Coding Plan和Token购买攻略：大厂价格一站汇总](https://mp.weixin.qq.com/s/Bk6d9bbSh5kSEd9i9dAahw)
- [用AI 做 副业 的  3个思路](https://mp.weixin.qq.com/s/kGmRRZ_LMUgLaS7AQkcSnw)
- [说件事：我的群里，禁止讨论免费AI](https://mp.weixin.qq.com/s/NC0FSz29_DeOY2p3GL48wA)
- [高考后上大学，普通人别选AI专业](https://mp.weixin.qq.com/s/AtgtbGpaueW58olyO7sDrw)

---

**科技不高冷，AI很好用。**  
我是晚枫，关注我，带你用AI搞钱，不做AI的韭菜。

---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


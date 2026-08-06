---
title: 别怪我没提醒你：DeepSeek V4 Flash 可以免费用
date: 2026-08-05 20:00:00
tags: [deepseek, deepseek-v4-flash, opencode, 免费ai, 大模型, ai编程工具]
categories: [AI工具评测]
keywords: [DeepSeek V4 Flash, 免费大模型, OpenCode, 免费AI编程, DeepSeek模型, 薅羊毛, 视频号教程]
description: 用 OpenCode 的 /models 命令，3 步免费用上 DeepSeek V4 Flash。技术圈人人知道、圈外人不知道的方法，安全合规，国内外都能用；视频号播放 12w+ 的薅羊毛教程文档补充版。
cover: https://images.unsplash.com/photo-1518186285589-2f7649de83e0?q=80&w=1200&auto=format&fit=crop
---

<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="https://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>

<!-- more -->

> **科技不高冷，AI很好用** | 我是程序员晚枫，全网 40 万+ 粉丝


大家好，我是晚枫。

昨天发了一条DeepSeek最新模型免费用的视频教程，创造了视频号有史以来的最高播放：12w+。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260805223032193.png)

真没想到，圈子内外，用AI的信息差这么大。

其实这个薅羊毛的方法，对于技术圈子里的人来说不是什么秘密，十有八九都知道，而且**安全、合规**，国内外都能用。

今天我再把这个教程写成文档的形式，给大家补充使用。

> 大家还有哪些想免费用的大模型？可以在评论区留言，我后面继续给大家分享更多方法。


## 3 步用 OpenCode 免费跑 DeepSeek-V4-Flash


下面是 3 步上手流程：

### 第 1 步：安装 OpenCode

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/iShot_2026-08-04_19.41.29.png)

官网：https://opencode.ai/

```bash
# macOS / Linux
curl -fsSL https://opencode.ai/install | bash

# 或者用包管理器
brew install opencode       # macOS
npm install -g opencode-ai  # Node 用户
```

装完在终端里输入 `opencode` 启动。

### 第 2 步：用 `/models` 选 DeepSeek V4 Flash Free

进入 OpenCode 后，输入：

```bash
/models
```

会弹出当前可用的模型列表。**找到 `opencode/deepseek-v4-flash-free`**（注意带 `-free` 后缀的就是免费版），回车确认。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/iShot_2026-08-04_19.45.34.png)

从此你让 OpenCode 写代码、做 Agent 任务，它就自动调用 DeepSeek V4 Flash 来回答。

除了DS，还有下图列出的free模型，都可以免费用。
![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/iShot_2026-08-04_19.42.38.png)

### 第 3 步：直接用

回到主界面，用自然语言跟 OpenCode 聊就行。比如：

```
帮我写一个 Python 爬虫，爬豆瓣电影 Top 250
或者
请介绍一下程序员晚枫
```

OpenCode 会自动调用 DeepSeek V4 Flash 生成代码、跑命令、读你项目里的文件 or 帮你从网上搜索程序员晚枫的信息🔍，不用切窗口去网页版。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/iShot_2026-08-04_19.42.13.png)

---

## 一个不能忽视的细节

OpenCode 文档里有一句很坦诚的话：

> **DeepSeek V4 Flash Free**: During its free period, collected data may be used to improve the model.

翻译过来就是：免费期间，**你的对话数据可能被用来训练 DeepSeek 的下一版模型**。

所以：

- ✅ 个人项目、学习代码、写开源工具 → 放心用，免费是真实的
- ❌ 公司内部代码、客户数据、未公开的产品逻辑 → 别用，走官方 API（5 厘一次）

**这才是「免费」二字背后真正的代价：你用 token 钱换的是你的数据。**

---

## 相关阅读

- [OpenCode 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/RoqlepeGRzDNOiDJkg7jKw)
- [Codex 换皮肤攻略，0 基础 3 分钟搞定](https://mp.weixin.qq.com/s/G598Htnb4k2cVyLnWGQPSw)
- [千问办公正式发布，AI办公迎来最强挑战者](https://mp.weixin.qq.com/s/f05PrU-u8TqxILFPBZ7t6A)


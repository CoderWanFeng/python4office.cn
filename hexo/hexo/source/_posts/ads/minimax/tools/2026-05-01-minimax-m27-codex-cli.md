---
title: 在 Codex CLI 里使用 MiniMax M2.7
date: 2026-05-01 17:22:00
tags:
  - Codex CLI
  - MiniMax
  - M2.7
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1618477388954-7852f32655ec?q=80&w=1200&auto=format&fit=crop
---

Codex CLI 是 OpenAI 官方推出的命令行工具，接入 MiniMax M2.7 可以获得更强的中文编程支持和多模态能力补充。

今天教大家怎么在 Codex CLI 里配置 MiniMax。

<!-- more -->

---

## 一、配置步骤

### Step 1：获取 API Key

👉 **专属9折优惠通道**：[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

---

### Step 2：在 Codex CLI 中配置

Codex CLI 支持 OpenAI 兼容接口，可以通过环境变量配置 MiniMax：

```bash
export MINIMAX_API_KEY="你的API Key"
export MINIMAX_API_BASE="https://api.minimaxi.com/v1"
```

或者使用 mmx-cli 作为插件：

```bash
npm install -g mmx-cli
mmx auth login --api-key 你的API Key
```

---

### Step 3：测试调用

```
用MiniMax帮我解释这段代码的作用，并标注出潜在的性能问题
```

---

## 二、专属优惠

👉 **点击获取 MiniMax 专属9折**：[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

**好友立享9折专属优惠 + Builder权益，你赢返利 + 社区特权**

---

**作者：程序员晚枫**

全网同名，专注AI工具测评与Python自动化办公教学。

---


<p align="center" id='进群-banner-AI'>
 <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
 <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
 </a>
</p>

**相关阅读：**

- [我用AI开发软件，老板问我是不是偷偷招了个程序员](https://mp.weixin.qq.com/s/59_OV_bJUcQ_-82eXg2IYw)
- [国产AI最大的优点：问什么都是标准答案](https://mp.weixin.qq.com/s/Ni9ZN0bpDEygDZmOAkr-tQ)
- [设计师花3天做的图，我用 AI 15分钟搞定了](https://mp.weixin.qq.com/s/BQZUEFVCWhx8lLDaQsbRTg)
- [我求你别碰 Claude Code](https://mp.weixin.qq.com/s/yshOWQYjQSjdUiqH2VuPDg)
- [HR看简历只花6秒，我用AI让我的简历过了第一关](https://mp.weixin.qq.com/s/XD8bk9Wf6p47HEoP8h84RQ)
- [我用AI做数字人播报，老板问"你什么时候请的主播？"](https://mp.weixin.qq.com/s/7vngGHvX-HxIsUsQHGp1Dw)
---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://r7up9.xetslk.com/s/1uP5YW)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)
- 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://r7up9.xetslk.com/s/1uP5YW)

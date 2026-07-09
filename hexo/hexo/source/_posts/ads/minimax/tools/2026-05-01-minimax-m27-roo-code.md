---
title: 在 Roo Code 里使用 MiniMax M2.7
date: 2026-05-01 17:18:00
tags:
  - Roo Code
  - MiniMax
  - M2.7
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1618477388954-7852f32655ec?q=80&w=1200&auto=format&fit=crop
---

Roo Code 是一个专注于代码审查和优化的AI工具，接入 MiniMax M2.7 可以获得更强的中文注释和多模态分析能力。

今天教大家怎么在 Roo Code 里配置 MiniMax。

<!-- more -->

---

## 一、配置步骤

### Step 1：获取 API Key

👉 **专属9折优惠通道**：[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

---

### Step 2：在 Roo Code 中配置

1. 打开 Roo Code 设置 → AI Providers
2. 选择"Custom"或"OpenAI Compatible"
3. 填写以下信息：

| 字段 | 内容 |
|------|------|
| API URL | `https://api.minimaxi.com/v1` |
| API Key | 你的 MiniMax API Key |
| Model | `MiniMax-Text-01` 或 `m2.7-pro` |

4. 保存并测试

---

### Step 3：安装 mmx-cli（可选）

如果你需要多模态能力（图片、视频、语音）：

```bash
npm install -g mmx-cli
mmx auth login --api-key 你的API Key
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

- [学AI编程别瞎忙！3步走，从零基础到能做实战项目](https://mp.weixin.qq.com/s/VXmJjQwsQlY-2IHjA3OAYA)
- [我的建站搭子skill，入职腾讯QClaw了！动动嘴就能建网站](https://mp.weixin.qq.com/s/XEe9yMpseRvMizhWcbnEoA)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [用上 OpenCode 的5 个免费大模型，省了我 200 刀 ChatGPT 年费](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)
- [日入 1000 后，我把个人网站开源了：拿走代码，你也能跑](https://mp.weixin.qq.com/s/imuuUYYFopkrRlEABUl1IA)
- [PPT 制作神器！Claude Code 审美直接封神](https://mp.weixin.qq.com/s/obGJ2cSLieX2K7ryOdMFpw)
---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《50讲 · AI编程训练营》](https://mp.weixin.qq.com/s/VXmJjQwsQlY-2IHjA3OAYA)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲，先看看适不适合自己](https://pan.quark.cn/s/8f7886f79569)
- 👉 - 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://r7up9.xetslk.com/s/3978Ig)

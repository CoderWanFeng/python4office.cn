---
title: 在 TRAE 里使用 MiniMax M2.7
date: 2026-05-01 17:08:00
tags:
  - TRAE
  - MiniMax
  - M2.7
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1618477388954-7852f32655ec?q=80&w=1200&auto=format&fit=crop
---

TRAE 是一个新兴的AI编程工具，接入 MiniMax M2.7 后可以解锁更多本土化能力。

今天教大家怎么在 TRAE 里配置 MiniMax。

<!-- more -->

---

## 一、TRAE + MiniMax 能做什么？

| 能力 | TRAE 原有 | + MiniMax M2.7 |
|------|----------|----------------|
| 代码补全 | ✅ | ✅ |
| 代码生成 | ✅ | ✅ |
| 中文理解 | ⚠️ 一般 | ✅ 强 |
| 图片理解 | ❌ | ✅ |
| 语音合成 | ❌ | ✅ |

---

## 二、配置步骤

### Step 1：获取 API Key

👉 **专属9折优惠通道**：[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

---

### Step 2：在 TRAE 中配置

1. 打开 TRAE 设置 → AI Providers
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

如果你需要多模态能力：

```bash
npm install -g mmx-cli
mmx auth login --api-key 你的API Key
```

安装后，在 TRAE 的 AI 对话中直接调用：

```
用MiniMax帮我生成一张前端架构图
```

---

## 三、专属优惠

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

- [学会AI编程，人人都是六边形战士](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)
- [我开通了Google广告，把申请到收款的全流程教给你](https://mp.weixin.qq.com/s/scAleVOwH6kDLPuQT4BNlA)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [我开通了Google广告，把申请到收款的全流程教给你](https://mp.weixin.qq.com/s/scAleVOwH6kDLPuQT4BNlA)
- [用上 OpenCode 的5 个免费大模型，省了我 200 刀 ChatGPT Plus 年费](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)
---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《50讲 · AI编程训练营》](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲，先看看适不适合自己](https://pan.quark.cn/s/8f7886f79569)
- 👉 - 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://r7up9.xetslk.com/s/3978Ig)

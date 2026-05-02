---
title: 在 Zed 里使用 MiniMax M2.7
date: 2026-05-01 17:26:00
tags:
  - Zed
  - MiniMax
  - M2.7
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1618477388954-7852f32655ec?q=80&w=1200&auto=format&fit=crop
---

Zed 是一个高性能的代码编辑器，接入 MiniMax M2.7 可以获得更强的中文编程支持和多模态能力。

今天教大家怎么在 Zed 里配置 MiniMax。

<!-- more -->

---

## 一、配置步骤

### Step 1：获取 API Key

👉 **专属9折优惠通道**：[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

---

### Step 2：在 Zed 中配置

1. 打开 Zed 设置 → AI Providers
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

**相关阅读：**

- [刘润开始劝大家学AI编程，但我已经放弃了](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)
- [人在曼谷旅游，AI在帮我赚钱](https://mp.weixin.qq.com/s/KLXXEoxMu9uayJTLXStIzw)
- [最全AI Coding Plan和Token购买攻略：大厂价格一站汇总](https://mp.weixin.qq.com/s/Bk6d9bbSh5kSEd9i9dAahw)
- [用AI 做 副业 的  3个思路](https://mp.weixin.qq.com/s/kGmRRZ_LMUgLaS7AQkcSnw)
- [说件事：我的群里，禁止讨论免费AI](https://mp.weixin.qq.com/s/NC0FSz29_DeOY2p3GL48wA)
- [高考后上大学，普通人别选AI专业](https://mp.weixin.qq.com/s/AtgtbGpaueW58olyO7sDrw)
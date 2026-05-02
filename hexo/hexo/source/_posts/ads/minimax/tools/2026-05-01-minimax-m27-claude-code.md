---
title: 在 Claude Code 里使用 MiniMax M2.7
date: 2026-05-01 17:02:00
tags:
  - Claude Code
  - MiniMax
  - M2.7
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1618477388954-7852f32655ec?q=80&w=1200&auto=format&fit=crop
---

Claude Code 是开发者的热门选择，但如果能加上 MiniMax M2.7 的多模态能力，会更加如虎添翼。

今天教大家怎么在 Claude Code 里接入 MiniMax。

<!-- more -->

---

## 一、Claude Code + MiniMax 能做什么？

| 能力 | Claude Code 原有 | + MiniMax M2.7 |
|------|-----------------|----------------|
| 代码生成 | ✅ | ✅ |
| 中文理解 | ⚠️ 一般 | ✅ 强 |
| 图片理解 | ❌ | ✅ |
| 语音合成 | ❌ | ✅ |
| 视频生成 | ❌ | ✅ |
| 音乐生成 | ❌ | ✅ |

**一句话：Claude Code 的编程能力 + MiniMax 的多模态全家桶 = 全能AI编程助手。**

---

## 二、配置步骤

### Step 1：获取 MiniMax API Key

如果你还没有 MiniMax Token Plan，先去获取：

👉 **专属9折优惠通道**：[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

开通后，在后台复制你的 API Key。

---

### Step 2：在 Claude Code 中配置 MiniMax

Claude Code 支持 OpenAI 兼容接口，MiniMax 提供的正是这种接口。

**方法一：安装 mmx-cli（推荐）**

```bash
npm install -g mmx-cli
mmx auth login --api-key 你的MiniMax API Key
```

安装后，告诉 Claude Code：

```
帮我安装 MiniMax CLI：https://github.com/MiniMax-AI/cli
我的密钥是 sk-cp-xxxxx
```

Claude Code 会自动引导你完成配置。

**方法二：手动配置**

在 Claude Code 的环境变量中设置：

```bash
export MINIMAX_API_KEY="你的API Key"
export MINIMAX_API_BASE="https://api.minimaxi.com/v1"
```

---

### Step 3：验证配置

发送测试消息：

```
请用中文自我介绍，并说明你能调用哪些MiniMax能力
```

如果 Claude Code 能正常调用 MiniMax，说明配置成功。

---

## 三、M2.7 的编程能力

MiniMax M2.7 在编程方面做了专门优化：

### 代码生成

```python
# 试试让M2.7写代码
"""
写一个Python函数，接受一个文件路径列表，
返回每个文件的大小（KB为单位）
"""
```

### 代码审查

```
帮我审查这段代码的问题，并给出优化建议：
[粘贴你的代码]
```

### 中文注释

M2.7 对中文语境理解很深，可以帮你写中文注释、中文文档。

---

## 四、调用多模态能力

配置完成后，在 Claude Code 中可以直接用自然语言调用 MiniMax 的多模态能力：

### 🖼️ 生成图片

```
帮我用MiniMax生成一张科技感海报，蓝色调，适合技术博客
```

### 🎙️ 语音合成

```
帮我用MiniMax生成一段语音：欢迎使用AI编程工具，集成MiniMax多模态能力
```

### 🎬 生成视频

```
帮我用MiniMax生成一段视频：夕阳下程序员在写代码的剪影
```

---

## 五、常见问题

### Q：Claude Code 原生支持 MiniMax 吗？

**A：不完全原生，但可以通过 mmx-cli 或 API 配置接入。**

### Q：会不会和 Claude 的能力冲突？

**A：不会。**

你可以把 MiniMax 作为 Claude Code 的补充，用 Claude 做编程主力，用 MiniMax 做多模态补充。

---

## 六、专属优惠

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
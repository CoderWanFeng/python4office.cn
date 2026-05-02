---
title: "在 Grok CLI 里使用智谱 GLM Coding Plan"
date: 2026-05-02 22:54:00
tags:
  - Grok CLI
  - 智谱
  - GLM
  - Coding Plan
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1516116216624-53e697fedbea?q=80&w=1200&auto=format&fit=crop
---

Grok CLI 是 xAI 推出的命令行工具，接入智谱 GLM 可以获得国产大模型的优质能力，中文理解出色。

今天教大家怎么在 Grok CLI 里接入智谱 GLM 大模型。

<!-- more -->

---

## 一、为什么要在 Grok CLI 里用智谱 GLM Coding Plan？

### Grok CLI 是什么？

Grok CLI 是 xAI 推出的命令行 AI 助手，支持代码生成和技术问答。

### 接入智谱 GLM 有什么好处？

| 优势 | 说明 |
|------|------|
| 🇨🇳 中文优化 | 智谱 GLM 中文理解能力强 |
| ⚡ 响应速度快 | 国产节点，延迟低 |
| 💰 价格实惠 | 智谱定价低，性价比高 |
| 🔧 配置简单 | OpenAI兼容接口，5分钟搞定 |
| 📚 上下文强 | 支持长上下文窗口 |

---

## 二、配置步骤

### Step 1：开通智谱 GLM 服务

👉 **专属优惠通道**：[https://open.bigmodel.cn/](https://open.bigmodel.cn/)

注册并开通智谱 GLM 服务，获取你的 API Key。

---

### Step 2：在 Grok CLI 中配置智谱 GLM

Grok CLI 支持通过环境变量配置：

```bash
export GROK_API_KEY="你的智谱 API Key"
export GROK_API_BASE="https://open.bigmodel.cn/api/paas/v4"
```

或者在配置文件中设置：

```json
{
  "provider": "智谱-glm",
  "api_key": "你的智谱 API Key",
  "base_url": "https://open.bigmodel.cn/api/paas/v4",
  "model": "glm-4-flash"
}
```

---

### Step 3：测试调用

```
用GLM帮我解释这段代码的作用
```

---

## 三、常见问题

### Q：需要付费吗？

**A：需要。**

智谱 GLM 按量计费，价格实惠，用多少付多少。

👉 **专属优惠通道**：[https://open.bigmodel.cn/](https://open.bigmodel.cn/)

---

## 四、总结

| 内容 | 说明 |
|------|------|
| 适合人群 | 喜欢 Grok CLI 的开发者 |
| 配置难度 | ⭐⭐（简单，5分钟搞定） |
| 主要优势 | 中文优化、价格实惠、响应快 |
| 专属优惠 | 专属链接开卡更划算 |

---

*免责声明：本文含推广链接，通过链接购买不会增加你的费用，但可能为我带来推荐收益。*

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
---

## 🤖 MiniMax Token Plan 推荐

🚀 **MiniMax Token Plan 惊喜上线！** 新增语音、音乐、视频和图片生成权益。邀请好友享双重好礼，助力开发体验！

好友立享 **9折** 专属优惠 + Builder 权益，你赢返利 + 社区特权！

👉 **立即参与**：https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link

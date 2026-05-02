---
title: "在 Grok CLI 里使用 DeepSeek Coding Plan"
date: 2026-05-02 19:51:00
tags:
  - Grok CLI
  - DeepSeek
  - Coding Plan
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---

Grok CLI 是 xAI 推出的命令行工具，接入 DeepSeek 可以获得更强的中文编程支持。

今天教大家怎么在 Grok CLI 里接入 DeepSeek 大模型。

<!-- more -->

---

## 一、为什么要在 Grok CLI 里用 DeepSeek Coding Plan？

### Grok CLI 是什么？

Grok CLI 是 xAI 推出的命令行 AI 助手，支持代码生成和技术问答。

### 接入 DeepSeek 有什么好处？

| 优势 | 说明 |
|------|------|
| 🧠 推理能力强 | DeepSeek 数学和代码推理能力业界领先 |
| 💰 按量计费 | 用多少付多少，不浪费 |
| 🔧 配置简单 | OpenAI兼容接口，5分钟搞定 |
| 🌏 国产优先 | 国内节点，响应速度快 |
| 🤝 专属优惠 | 用我的专属链接更划算 |

---

## 二、配置步骤

### Step 1：开通 DeepSeek Coding Plan

👉 **专属优惠通道**：[https://platform.deepseek.com/](https://platform.deepseek.com/)

开通后，获取你的 API Key。

---

### Step 2：在 Grok CLI 中配置 DeepSeek

Grok CLI 支持通过环境变量配置：

```bash
export GROK_API_KEY="你的DeepSeek API Key"
export GROK_API_BASE="https://api.deepseek.com/v1"
```

或者在配置文件中设置：

```json
{
  "provider": "deepseek",
  "api_key": "你的DeepSeek API Key",
  "base_url": "https://api.deepseek.com/v1",
  "model": "deepseek-chat"
}
```

---

### Step 3：测试调用

```
用DeepSeek帮我解释这段代码的作用
```

---

## 三、常见问题

### Q：需要付费吗？

**A：需要。**

DeepSeek Coding Plan 按量计费，用多少付多少。

👉 **专属优惠通道**：[https://platform.deepseek.com/](https://platform.deepseek.com/)

---

## 四、总结

| 内容 | 说明 |
|------|------|
| 适合人群 | 喜欢 Grok CLI 的开发者 |
| 配置难度 | ⭐⭐（简单，5分钟搞定） |
| 主要优势 | 推理强、国产、按量计费 |
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
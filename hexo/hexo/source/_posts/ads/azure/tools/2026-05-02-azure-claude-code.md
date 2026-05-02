---
title: "在 Claude Code 里使用 Azure OpenAI Coding Plan"
date: 2026-05-02 22:32:00
tags:
  - Claude Code
  - Azure
  - OpenAI
  - Coding Plan
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---

Claude Code 是 Anthropic 推出的命令行编程工具，接入 Azure OpenAI 可以获得 GPT-4 的强大能力，同时享受 Azure 企业级安全保障。

今天教大家怎么在 Claude Code 里接入 Azure OpenAI 大模型。

<!-- more -->

---

## 一、为什么要在 Claude Code 里用 Azure OpenAI Coding Plan？

### Claude Code 是什么？

Claude Code 是 Anthropic 官方推出的 AI 编程助手，支持代码生成、修改和项目理解。

### 接入 Azure OpenAI 有什么好处？

| 优势 | 说明 |
|------|------|
| 🤖 GPT-4 加持 | OpenAI 最强模型，代码生成质量高 |
| 🏢 企业级安全 | Azure 安全合规，数据不外泄 |
| 🔧 配置简单 | OpenAI兼容接口，5分钟搞定 |
| 🌏 国内节点 | Azure 中国区，响应速度快 |
| 💰 按量计费 | 用多少付多少，不浪费 |

---

## 二、配置步骤

### Step 1：开通 Azure OpenAI 服务

👉 **专属优惠通道**：[https://ai.azure.com](https://ai.azure.com)

开通 Azure OpenAI 服务后，在 Azure 门户中创建一个 OpenAI 资源，获取你的 API Key 和端点地址。

---

### Step 2：在 Claude Code 中配置 Azure OpenAI

Claude Code 支持通过环境变量配置：

```bash
export ANTHROPIC_BASE_URL="https://<你的资源名>.openai.azure.com/v1"
export ANTHROPIC_API_KEY="你的Azure OpenAI API Key"
```

或者修改配置文件：

```json
{
  "provider": "azure-openai",
  "api_key": "你的Azure OpenAI API Key",
  "base_url": "https://<你的资源名>.openai.azure.com/v1",
  "model": "gpt-4"
}
```

---

### Step 3：测试调用

```
用GPT-4帮我解释这段代码的作用
```

---

## 三、常见问题

### Q：需要付费吗？

**A：需要。**

Azure OpenAI 按量计费，用多少付多少。

👉 **专属优惠通道**：[https://ai.azure.com](https://ai.azure.com)

---

## 四、总结

| 内容 | 说明 |
|------|------|
| 适合人群 | 喜欢 Claude Code 的开发者 |
| 配置难度 | ⭐⭐（简单，5分钟搞定） |
| 主要优势 | GPT-4、企业级安全、按量计费 |
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

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)

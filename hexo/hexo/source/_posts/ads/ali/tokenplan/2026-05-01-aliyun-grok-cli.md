---
title: 在 Grok CLI 里使用阿里云百炼 Coding Plan
date: 2026-05-01 17:48:00
tags:
  - Grok CLI
  - 阿里云
  - 百炼
  - 通义千问
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1618477388954-7852f32655ec?q=80&w=1200&auto=format&fit=crop
---

Grok CLI 是 xAI 推出的命令行工具，接入阿里云百炼可以获得更强的中文编程支持。

今天教大家怎么在 Grok CLI 里接入阿里云百炼通义千问。

<!-- more -->

---

## 一、为什么要在 Grok CLI 里用阿里云百炼？

### Grok CLI 是什么？

Grok CLI 是 xAI 推出的命令行 AI 助手，支持代码生成和技术问答。

### 接入通义千问有什么好处？

| 优势 | 说明 |
|------|------|
| 🌏 国产优先 | 阿里云国内节点，响应速度快 |
| 💰 价格实惠 | Coding Plan 29元/月起，按量计费 |
| 🧠 中文理解强 | 通义千问对中文语境理解更准确 |
| 🔧 配置简单 | OpenAI兼容接口，5分钟搞定 |
| 🤝 专属优惠 | 用我的专属链接开卡更划算 |

---

## 二、配置步骤

### Step 1：获取阿里云百炼 API Key

👉 **专属9折优惠通道**：[https://www.aliyun.com/benefit/scene/codingplan?userCode=t6duaoe1](https://www.aliyun.com/benefit/scene/codingplan?userCode=t6duaoe1)

开通后，在百炼控制台复制你的 API Key。

---

### Step 2：在 Grok CLI 中配置阿里云百炼

Grok CLI 支持通过环境变量配置：

```bash
export GROK_API_KEY="你的阿里云百炼API Key"
export GROK_API_BASE="https://dashscope.aliyuncs.com/compatible-mode/v1"
```

或者在配置文件中设置：

```json
{
  "provider": "aliyun",
  "api_key": "你的API Key",
  "model": "qwen-turbo"
}
```

---

### Step 3：测试调用

```
用通义千问帮我解释这段代码的作用
```

---

## 三、常见问题

### Q：需要付费吗？

**A：需要。**

阿里云百炼 Coding Plan 按量计费，29元/月起，用多少付多少。

👉 **专属9折优惠**：[https://www.aliyun.com/benefit/scene/codingplan?userCode=t6duaoe1](https://www.aliyun.com/benefit/scene/codingplan?userCode=t6duaoe1)

---

## 四、总结

| 内容 | 说明 |
|------|------|
| 适合人群 | 喜欢 Grok CLI 的开发者 |
| 配置难度 | ⭐⭐（简单，5分钟搞定） |
| 主要优势 | 国产、中文理解强、价格实惠 |
| 专属优惠 | 专属链接开卡更划算 |

---

**作者：程序员晚枫**

全网同名，专注AI工具测评与Python自动化办公教学。

---

**相关阅读：**

- [2026年AI大模型API价格对比](https://www.python-office.com/)
- [如何选择适合自己的 Coding Plan](https://www.python-office.com/)
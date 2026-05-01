---
title: "在 Codex CLI 里使用 MiniMax M2.7"
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

**相关阅读：**

- [2026年AI大模型API价格对比](https://www.python-office.com/)
- [如何选择适合自己的Token Plan](https://www.python-office.com/)
---
title: 在 Cursor 里使用 MiniMax M2.7
date: 2026-05-01 17:05:00
tags:
  - Cursor
  - MiniMax
  - M2.7
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1618477388954-7852f32655ec?q=80&w=1200&auto=format&fit=crop
---

Cursor 是很多开发者的日常编辑器，接入 MiniMax M2.7 后，可以解锁更多国产AI能力。

今天教大家怎么在 Cursor 里配置 MiniMax。

<!-- more -->

---

## 一、为什么 Cursor 需要 MiniMax？

Cursor 内置了多个AI模型，但如果你需要：

- 更强的中文代码注释
- 图片理解能力（看截图改bug）
- 语音合成（生成代码解说）
- 更便宜的调用成本

**MiniMax M2.7 是个好选择。**

---

## 二、配置步骤

### Step 1：获取 API Key

👉 **专属9折优惠通道**：[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

---

### Step 2：在 Cursor 中配置

1. 打开 Cursor 设置 → AI Providers
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

如果你需要多模态能力（图片、视频、语音），安装 mmx-cli：

```bash
npm install -g mmx-cli
mmx auth login --api-key 你的API Key
```

安装后，在 Cursor 的 AI 对话中直接调用：

```
用MiniMax帮我生成一张代码流程图
```

---

## 三、使用场景

### 🐛 看图改bug

截一张报错截图给 Cursor，Cursor 会调用 MiniMax 的视觉理解能力，分析问题并给出修复建议。

### 📝 中文代码注释

```
给这段代码加上中文注释，风格通俗易懂
```

### 🎙️ 生成代码解说

```
把这段Python代码用语音读出来，方便我通勤时听
```

---

## 四、专属优惠

👉 **点击获取 MiniMax 专属9折**：[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

**好友立享9折专属优惠 + Builder权益，你赢返利 + 社区特权**

---

**作者：程序员晚枫**

全网同名，专注AI工具测评与Python自动化办公教学。

---

**相关阅读：**

- [2026年AI大模型API价格对比](https://www.python-office.com/)
- [如何选择适合自己的Token Plan](https://www.python-office.com/)
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

👉 **专属优惠通道**：[https://cloud.siliconflow.cn/i/ciS03HX7](https://cloud.siliconflow.cn/i/ciS03HX7)

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

👉 **专属优惠通道**：[https://cloud.siliconflow.cn/i/ciS03HX7](https://cloud.siliconflow.cn/i/ciS03HX7)

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


<p align="center" id='进群-banner-AI'>
 <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
 <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
 </a>
</p>

**相关阅读：**

- [2026 年学习编程，你需要的不是更多教程](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)
- [我用AI做PPT，同事说你是PPT设计师吗](https://mp.weixin.qq.com/s/aLo7mW3BLnglwhSZCKoOow)
- [设计师花3天做的图，我用 AI 15分钟搞定了](https://mp.weixin.qq.com/s/BQZUEFVCWhx8lLDaQsbRTg)
- [我求你别碰 Claude Code](https://mp.weixin.qq.com/s/yshOWQYjQSjdUiqH2VuPDg)
- [HR看简历只花6秒，我用AI让我的简历过了第一关](https://mp.weixin.qq.com/s/XD8bk9Wf6p47HEoP8h84RQ)
- [我用AI做数字人播报，老板问"你什么时候请的主播？"](https://mp.weixin.qq.com/s/7vngGHvX-HxIsUsQHGp1Dw)
---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)
- 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)

---
title: '在 Grok CLI 里使用 Kimi Coding Plan'
date: 2026-05-02 23:24:00
tags:
  - Grok CLI
  - Kimi
  - Moonshot
  - 月之暗面
  - Coding Plan
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---

Grok CLI 是 xAI 推出的命令行工具，接入 Kimi 可以获得超长上下文能力，128K token 处理大型项目无压力。

今天教大家怎么在 Grok CLI 里接入 Kimi 大模型。

<!-- more -->

---

## 一、为什么要在 Grok CLI 里用 Kimi Coding Plan？

### Grok CLI 是什么？

Grok CLI 是 xAI 推出的命令行 AI 助手，支持代码生成和技术问答。

### 接入 Kimi 有什么好处？

| 优势 | 说明 |
|------|------|
| 📚 超长上下文 | 128K token，适合大项目分析 |
| 🇨🇳 中文优化 | Kimi 中文理解能力强 |
| ⚡ 响应速度快 | 国产节点，延迟低 |
| 💰 价格实惠 | 按量计费，用多少付多少 |
| 🔧 配置简单 | OpenAI兼容接口，5分钟搞定 |

---

## 二、配置步骤

### Step 1：开通 Kimi 服务

👉 **专属优惠通道**：[https://platform.moonshot.cn/](https://platform.moonshot.cn/)

注册并开通 Kimi 服务，获取你的 API Key。

---

### Step 2：在 Grok CLI 中配置 Kimi

Grok CLI 支持通过环境变量配置：

```bash
export GROK_API_KEY="你的 Kimi API Key"
export GROK_API_BASE="https://api.moonshot.cn/v1"
```

或者在配置文件中设置：

```json
{
  "provider": "Kimi",
  "api_key": "你的 Kimi API Key",
  "base_url": "https://api.moonshot.cn/v1",
  "model": "moonshot-v1-8k"
}
```

---

### Step 3：测试调用

```
用Kimi帮我解释这段代码的作用
```

---

## 三、常见问题

### Q：需要付费吗？

**A：需要。**

Kimi 按量计费，价格实惠，用多少付多少。

👉 **专属优惠通道**：[https://platform.moonshot.cn/](https://platform.moonshot.cn/)

---

## 四、总结

| 内容 | 说明 |
|------|------|
| 适合人群 | 大型项目开发者、中文编程场景 |
| 配置难度 | ⭐⭐（简单，5分钟搞定） |
| 主要优势 | 128K超长上下文、中文理解好、价格实惠 |
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
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [HR看简历只花6秒，我用AI让我的简历过了第一关](https://mp.weixin.qq.com/s/XD8bk9Wf6p47HEoP8h84RQ)
- [我用AI做数字人播报，老板问"你什么时候请的主播？"](https://mp.weixin.qq.com/s/7vngGHvX-HxIsUsQHGp1Dw)
---

## 🤖 MiniMax Token Plan 推荐

🚀 **MiniMax Token Plan 惊喜上线！** 新增语音、音乐、视频和图片生成权益。邀请好友享双重好礼，助力开发体验！

好友立享 **9折** 专属优惠 + Builder 权益，你赢返利 + 社区特权！

👉 **立即参与**：https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link
---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲，先看看适不适合自己](https://pan.quark.cn/s/8f7886f79569)
- 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)

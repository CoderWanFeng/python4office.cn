---
title: '在 Claude Code 里使用 Kimi Coding Plan'
date: 2026-05-02 23:16:00
tags:
  - Claude Code
  - Kimi
  - Moonshot
  - 月之暗面
  - Coding Plan
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---

Claude Code 是 Anthropic 推出的命令行编程工具，接入 Kimi 可以获得超长上下文能力，128K token 处理大型项目无压力。

今天教大家怎么在 Claude Code 里接入 Kimi 大模型。

<!-- more -->

---

## 一、为什么要在 Claude Code 里用 Kimi Coding Plan？

### Claude Code 是什么？

Claude Code 是 Anthropic 官方推出的 AI 编程助手，支持代码生成、修改和项目理解。

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

### Step 2：在 Claude Code 中配置 Kimi

Claude Code 支持通过环境变量配置：

```bash
export ANTHROPIC_BASE_URL="https://api.moonshot.cn/v1"
export ANTHROPIC_API_KEY="你的 Kimi API Key"
```

或者修改配置文件：

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

- [学会AI编程，人人都是六边形战士](https://mp.weixin.qq.com/s/VXmJjQwsQlY-2IHjA3OAYA)
- [我开通了Google广告，把申请到收款的全流程教给你](https://mp.weixin.qq.com/s/scAleVOwH6kDLPuQT4BNlA)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [我开通了Google广告，把申请到收款的全流程教给你](https://mp.weixin.qq.com/s/scAleVOwH6kDLPuQT4BNlA)
- [用上 OpenCode 的5 个免费大模型，省了我 200 刀 ChatGPT Plus 年费](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)
---

## 🤖 MiniMax Token Plan 推荐

🚀 **MiniMax Token Plan 惊喜上线！** 新增语音、音乐、视频和图片生成权益。邀请好友享双重好礼，助力开发体验！

好友立享 **9折** 专属优惠 + Builder 权益，你赢返利 + 社区特权！

👉 **立即参与**：https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link
---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《50讲 · AI编程训练营》](https://mp.weixin.qq.com/s/VXmJjQwsQlY-2IHjA3OAYA)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲，先看看适不适合自己](https://pan.quark.cn/s/8f7886f79569)
- 👉 - 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://r7up9.xetslk.com/s/3978Ig)

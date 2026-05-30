---
title: "在 Claude Code 里使用智谱 GLM Coding Plan"
date: 2026-05-02 22:46:00
tags:
  - Claude Code
  - 智谱
  - GLM
  - Coding Plan
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1516116216624-53e697fedbea?q=80&w=1200&auto=format&fit=crop
---

Claude Code 是 Anthropic 推出的命令行编程工具，接入智谱 GLM 可以获得国产大模型的优质能力，中文理解出色。

今天教大家怎么在 Claude Code 里接入智谱 GLM 大模型。

<!-- more -->

---

## 一、为什么要在 Claude Code 里用智谱 GLM Coding Plan？

### Claude Code 是什么？

Claude Code 是 Anthropic 官方推出的 AI 编程助手，支持代码生成、修改和项目理解。

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

### Step 2：在 Claude Code 中配置智谱 GLM

Claude Code 支持通过环境变量配置：

```bash
export ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/paas/v4"
export ANTHROPIC_API_KEY="你的智谱 API Key"
```

或者修改配置文件：

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
| 适合人群 | 喜欢 Claude Code 的开发者 |
| 配置难度 | ⭐⭐（简单，5分钟搞定） |
| 主要优势 | 中文优化、价格实惠、响应快 |
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

- [我用AI开发软件，老板问我是不是偷偷招了个程序员](https://mp.weixin.qq.com/s/59_OV_bJUcQ_-82eXg2IYw)
- [我用AI做PPT，同事说你是PPT设计师吗](https://mp.weixin.qq.com/s/aLo7mW3BLnglwhSZCKoOow)
- [设计师花3天做的图，我用 AI 15分钟搞定了](https://mp.weixin.qq.com/s/BQZUEFVCWhx8lLDaQsbRTg)
- [我求你别碰 Claude Code](https://mp.weixin.qq.com/s/yshOWQYjQSjdUiqH2VuPDg)
- [HR看简历只花6秒，我用AI让我的简历过了第一关](https://mp.weixin.qq.com/s/XD8bk9Wf6p47HEoP8h84RQ)
- [我用AI做数字人播报，老板问"你什么时候请的主播？"](https://mp.weixin.qq.com/s/7vngGHvX-HxIsUsQHGp1Dw)
---

## 🤖 MiniMax Token Plan 推荐

🚀 **MiniMax Token Plan 惊喜上线！** 新增语音、音乐、视频和图片生成权益。邀请好友享双重好礼，助力开发体验！

好友立享 **9折** 专属优惠 + Builder 权益，你赢返利 + 社区特权！

👉 **立即参与**：https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link
---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://r7up9.xetslk.com/s/1uP5YW)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)
- 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://r7up9.xetslk.com/s/1uP5YW)

---
title: 在 MonkeyCode 里使用腾讯云 Token Plan
date: 2026-05-01 17:54:00
tags:
  - MonkeyCode
  - 腾讯云
  - Token Plan
  - 混元大模型
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---

MonkeyCode 是一个专注于轻量级代码生成的 AI 工具，接入腾讯云 Token Plan 可以获得更强的中文支持。

今天教大家怎么在 MonkeyCode 里接入腾讯云混元大模型。

<!-- more -->

---

## 一、为什么要在 MonkeyCode 里用腾讯云 Token Plan？

### MonkeyCode 是什么？

MonkeyCode 是一个专注于轻量级代码生成的 AI 工具，帮助开发者快速完成编程任务。

### 接入腾讯云有什么好处？

| 优势 | 说明 |
|------|------|
| 🌏 国产优先 | 腾讯云国内节点，响应速度快 |
| 💰 按量计费 | 39元/月起，用多少付多少，不浪费 |
| 🧠 混元加持 | 腾讯混元大模型，代码能力有保障 |
| 🔧 配置简单 | OpenAI兼容接口，5分钟搞定 |
| 🤝 专属优惠 | 用我的专属链接开卡更划算 |

---

## 二、配置步骤

### Step 1：开通腾讯云 Token Plan

👉 **专属优惠通道**：[https://curl.qcloud.com/Z9TkzRuj](https://curl.qcloud.com/Z9TkzRuj)

开通后，在腾讯云控制台获取你的 SecretId 和 SecretKey。

---

### Step 2：在 MonkeyCode 中配置腾讯云 Token Plan

1. 打开 MonkeyCode 设置 → AI Providers
2. 选择"Custom"或"OpenAI Compatible"
3. 填写以下信息：

| 字段 | 内容 |
|------|------|
| API URL | `https://api.tokenplan.tencentcloudapi.com/v1` |
| API Key | 你的 SecretId:SecretKey |
| 模型名称 | `hunyuan` 或 `hunyuan-pro` |

4. 保存并设置为默认模型

---

### Step 3：开始使用

配置成功后，在 MonkeyCode 中直接使用 AI 功能。

---

## 三、常见问题

### Q：需要付费吗？

**A：需要。**

腾讯云 Token Plan 按量计费，39元/月起，用多少付多少。

👉 **专属优惠通道**：[https://curl.qcloud.com/Z9TkzRuj](https://curl.qcloud.com/Z9TkzRuj)

---

## 四、总结

| 内容 | 说明 |
|------|------|
| 适合人群 | 喜欢 MonkeyCode 的开发者 |
| 配置难度 | ⭐⭐（简单，5分钟搞定） |
| 主要优势 | 国产、混元大模型、按量计费 |
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

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)
- 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)

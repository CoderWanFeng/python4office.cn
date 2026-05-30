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

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://r7up9.xetslk.com/s/1uP5YW)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)
- 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://r7up9.xetslk.com/s/1uP5YW)

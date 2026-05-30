---
title: 在 Claude Code 里使用 MiniMax M2.7
date: 2026-05-01 17:02:00
tags:
  - Claude Code
  - MiniMax
  - M2.7
  - AI编程
categories: AI编程工具配置
cover: https://images.unsplash.com/photo-1618477388954-7852f32655ec?q=80&w=1200&auto=format&fit=crop
---

Claude Code 是开发者的热门选择，但如果能加上 MiniMax M2.7 的多模态能力，会更加如虎添翼。

今天教大家怎么在 Claude Code 里接入 MiniMax。

<!-- more -->

---

## 一、Claude Code + MiniMax 能做什么？

| 能力 | Claude Code 原有 | + MiniMax M2.7 |
|------|-----------------|----------------|
| 代码生成 | ✅ | ✅ |
| 中文理解 | ⚠️ 一般 | ✅ 强 |
| 图片理解 | ❌ | ✅ |
| 语音合成 | ❌ | ✅ |
| 视频生成 | ❌ | ✅ |
| 音乐生成 | ❌ | ✅ |

**一句话：Claude Code 的编程能力 + MiniMax 的多模态全家桶 = 全能AI编程助手。**

---

## 二、配置步骤

### Step 1：获取 MiniMax API Key

如果你还没有 MiniMax Token Plan，先去获取：

👉 **专属9折优惠通道**：[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

开通后，在后台复制你的 API Key。

---

### Step 2：在 Claude Code 中配置 MiniMax

Claude Code 支持 OpenAI 兼容接口，MiniMax 提供的正是这种接口。

**方法一：安装 mmx-cli（推荐）**

```bash
npm install -g mmx-cli
mmx auth login --api-key 你的MiniMax API Key
```

安装后，告诉 Claude Code：

```
帮我安装 MiniMax CLI：https://github.com/MiniMax-AI/cli
我的密钥是 sk-cp-xxxxx
```

Claude Code 会自动引导你完成配置。

**方法二：手动配置**

在 Claude Code 的环境变量中设置：

```bash
export MINIMAX_API_KEY="你的API Key"
export MINIMAX_API_BASE="https://api.minimaxi.com/v1"
```

---

### Step 3：验证配置

发送测试消息：

```
请用中文自我介绍，并说明你能调用哪些MiniMax能力
```

如果 Claude Code 能正常调用 MiniMax，说明配置成功。

---

## 三、M2.7 的编程能力

MiniMax M2.7 在编程方面做了专门优化：

### 代码生成

```python
# 试试让M2.7写代码
"""
写一个Python函数，接受一个文件路径列表，
返回每个文件的大小（KB为单位）
"""
```

### 代码审查

```
帮我审查这段代码的问题，并给出优化建议：
[粘贴你的代码]
```

### 中文注释

M2.7 对中文语境理解很深，可以帮你写中文注释、中文文档。

---

## 四、调用多模态能力

配置完成后，在 Claude Code 中可以直接用自然语言调用 MiniMax 的多模态能力：

### 🖼️ 生成图片

```
帮我用MiniMax生成一张科技感海报，蓝色调，适合技术博客
```

### 🎙️ 语音合成

```
帮我用MiniMax生成一段语音：欢迎使用AI编程工具，集成MiniMax多模态能力
```

### 🎬 生成视频

```
帮我用MiniMax生成一段视频：夕阳下程序员在写代码的剪影
```

---

## 五、常见问题

### Q：Claude Code 原生支持 MiniMax 吗？

**A：不完全原生，但可以通过 mmx-cli 或 API 配置接入。**

### Q：会不会和 Claude 的能力冲突？

**A：不会。**

你可以把 MiniMax 作为 Claude Code 的补充，用 Claude 做编程主力，用 MiniMax 做多模态补充。

---

## 六、专属优惠

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

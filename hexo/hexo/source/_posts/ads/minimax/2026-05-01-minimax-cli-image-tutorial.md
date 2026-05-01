---
title: "一行命令搞定图片生成！MiniMax CLI保姆级教程"
date: 2026-05-01 16:55:00
tags:
  - MiniMax
  - CLI
  - 图片生成
  - AI工具
  - 教程
categories: AI工具教程
cover: https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1200&auto=format&fit=crop
---

你们有没有遇到过这种情况：

> 想生成一张图，但懒得打开网页、注册账号、复制粘贴……

今天教你一个更爽的方法：**一行命令，直接生成图片**。

MiniMax刚刚上线的CLI工具，就是来解决这个问题的。

<!-- more -->

---

## 一、MiniMax CLI是什么？

MiniMax CLI（命令：`mmx`）是MiniMax推出的命令行工具，让你在终端里直接调用MiniMax的全部多模态能力：

| 能力 | 命令 | 说明 |
|------|------|------|
| 🖼️ 图片生成 | `mmx image` | 文生图，支持比例和批量 |
| 🎬 视频生成 | `mmx video generate` | 文生视频，异步生成 |
| 🎙️ 语音合成 | `mmx speech synthesize` | 文字转语音，多音色 |
| 🎵 音乐生成 | `mmx music generate` | AI作曲，文生音乐 |
| 📝 文本对话 | `mmx text chat` | 多轮对话，流式输出 |
| 👁️ 图像理解 | `mmx visual` | 看图说话 |

**一句话：一套CLI，全部搞定。**

---

## 二、安装只需2步

### Step 1：安装CLI

打开终端，运行：

```bash
npm install -g mmx-cli
```

> 如果你没有安装Node.js，需要先装一下：[nodejs.org](https://nodejs.org)

---

### Step 2：登录API Key

```bash
mmx auth login --api-key sk-xxxxx
```

把你的API Key替换进去就行。

**API Key在哪找？** 去MiniMax Token Plan后台：

👉 **专属9折通道获取Key**：[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

---

## 三、重点来了：怎么用CLI生成图片？

安装完成后，生成图片只需要一行命令：

```bash
mmx image "赛博朋克风格的城市夜景，16:9"
```

这就是生成一张图片的命令。

**完整语法：**

```bash
mmx image "你的图片描述" --aspect-ratio 16:9
```

### 参数说明

| 参数 | 说明 | 示例 |
|------|------|------|
| 图片描述 | 必填，你想生成什么 | "夕阳下的海边" |
| `--aspect-ratio` | 图片比例 | `16:9` / `1:1` / `9:16` |

### 支持的比例

| 比例 | 说明 | 适合场景 |
|------|------|----------|
| `16:9` | 宽屏 | 电脑壁纸、PPT背景 |
| `1:1` | 正方形 | 社交媒体封面、头像 |
| `9:16` | 竖版 | 手机壁纸、小红书封面 |
| `4:3` | 标准 | 博客配图、文档插图 |

---

## 四、实用示例：生成不同风格的图片

### 示例1：科技感海报

```bash
mmx image "科技感海报，蓝色调，有机器人元素，适合用在演讲PPT里，16:9"
```

生成结果示例：
![科技感海报示例](https://filecdn.minimax.chat/public/94db816d-016e-4fc5-8913-b1a6a4935aad.jpeg)

---

### 示例2：可爱插画

```bash
mmx image "一只橘猫坐在咖啡馆窗边，阳光透过窗户洒进来，温暖治愈风格，1:1"
```

---

### 示例3：产品展示图

```bash
mmx image "极简风格的产品摄影照，主体是一个白色的无线耳机，背景是浅灰色，8K画质，1:1"
```

---

### 示例4：社交媒体配图

```bash
mmx image "小红书风格的读书分享配图，暖色调，桌面上放着一本书和一杯咖啡，旁边有绿植，9:16"
```

---

### 示例5：批量生成

```bash
mmx image "不同色调的日落海边，第一张橙色调，第二张粉色调，第三张蓝紫色调，16:9"
```

---

## 五、生成结果在哪里？

所有生成的文件会保存在当前目录下的 `minimax-output/` 文件夹中。

```bash
ls minimax-output/
```

可以看到你生成的所有图片和音视频文件。

---

## 六、除了图片，还能做什么？

### 🎙️ 语音合成

```bash
mmx speech synthesize --text "欢迎收听程序员晚枫的AI工具测评" --out intro.mp3
```

生成一段语音，可以用于：
- 视频配音
- 有声书朗读
- 播客内容

---

### 🎵 AI音乐生成

```bash
mmx music generate --prompt "轻快的钢琴曲，适合写作时听" --out writing-music.mp3
```

生成专属背景音乐，没有版权问题。

---

### 🎬 视频生成

```bash
mmx video generate --prompt "夕阳下，一只猫坐在窗边望向远方"
```

生成AI视频，适合做：
- 短视频素材
- 产品展示
- 内容创意

---

## 七、用CLI面板查看用量

输入以下命令，可以查看CLI面板和剩余额度：

```bash
mmx
```

面板显示：
- **resources**：当前可用的调用资源类型
- **flags**：支持在命令后加的参数/选项
- **用量信息**：剩余额度与配额概览
- **帮助入口**：使用方法说明

---

## 八、进阶技巧

### 技巧1：用自然语言指挥AI Agent

如果你用OpenClaw、Claude Code等AI助手，直接发指令就行：

```
帮我用MiniMax生成一张赛博朋克风格的城市夜景，16:9比例
```

AI会自动调用CLI完成操作，你甚至不需要记住命令。

---

### 技巧2：结合脚本批量生成

写一个简单的Shell脚本，批量生成多张图片：

```bash
#!/bin/bash
mmx image "科技蓝的PPT背景，16:9" --out slide-bg-1.jpg
mmx image "温暖橙色的PPT背景，16:9" --out slide-bg-2.jpg
mmx image "简约白的PPT背景，16:9" --out slide-bg-3.jpg
```

---

### 技巧3：输出到指定目录

```bash
mmx image "程序员晚枫风格的技术博客配图" --out ~/blog/cover.jpg
```

---

## 九、专属优惠：怎么获取API Key？

说了这么多，怎么开通？

👉 **点击这里获取专属9折通道**：[https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

开通后获得API Key，配合CLI使用，全部能力都能调用。

**好友立享9折专属优惠 + Builder权益，你赢返利 + 社区特权**

---

## 十、总结

| 内容 | 说明 |
|------|------|
| 安装命令 | `npm install -g mmx-cli` |
| 登录命令 | `mmx auth login --api-key sk-xxxxx` |
| 生成图片 | `mmx image "描述" --aspect-ratio 16:9` |
| 输出目录 | `minimax-output/` |
| 开通入口 | [https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link) |

---

**一句话：命令行生成图片，爽到停不下来。**

快去试试吧！

---

**作者：程序员晚枫**

全网同名，专注AI工具测评与Python自动化办公教学。

---

**相关阅读：**

- [2026年AI大模型API价格对比](https://www.python-office.com/)
- [如何选择适合自己的Token Plan](https://www.python-office.com/)
---
title: VS Code + 火山方舟Coding Plan配置教程：免费插件方案
keywords: 程序员晚枫, 火山方舟Coding Plan VS Code, VS Code AI编程, Continue插件配置, 免费AI编程
description: 程序员晚枫教程：VS Code + 火山方舟Coding Plan配置教程，免费插件方案，5分钟搭建AI编程环境。
date: 2026-04-10 00:07:00
tags: [火山方舟Coding Plan VS Code, VS Code AI编程, Continue插件, 火山引擎VS Code, 免费AI编程, 程序员晚枫]
categories: [AI编程, 教程]
---

> **本文作者：程序员晚枫 | AI编程布道者 | 专注AI工具测评与教学**
> 
> 全网40万+粉丝，6年Python开发经验，开源项目python-office作者

> 📢 **先上链接**：👉 **[点击订阅火山方舟Coding Plan](https://volcengine.com/L/a6sqe8YHzWo/)**
> 
> 邀请码：**GF2QJX3V**
> 
> 💡 **想系统学习AI编程？** 👉 **[点击了解AI编程训练营](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

大家好，这里是程序员晚枫。

不想花钱Cursor？VS Code + 火山方舟Coding Plan是最佳免费方案。

今天手把手教你配置。

<!-- more -->

## 方案优势

| 方案 | 费用 | 特点 |
|------|------|------|
| Cursor Pro | $20/月 | 开箱即用 |
| VS Code + Coding Plan | 36元/月 | 更便宜，更灵活 |

**省下的钱：** 约100元/月

## 配置步骤

### 第一步：安装Continue插件

1. 打开VS Code
2. 进入扩展商店（Cmd/Ctrl + Shift + X）
3. 搜索 "Continue"
4. 点击安装

### 第二步：订阅火山方舟Coding Plan

👉 **[点击订阅](https://volcengine.com/L/a6sqe8YHzWo/)**

获取API Key。

### 第三步：配置Continue

1. 点击左侧Continue图标
2. 点击设置（齿轮图标）
3. 选择 "config.json"
4. 添加以下配置：

```json
{
  "models": [
    {
      "title": "火山方舟 Doubao",
      "provider": "openai",
      "model": "doubao-pro-32k",
      "apiKey": "你的API Key",
      "apiBase": "https://ark.cn-beijing.volces.com/api/v3"
    },
    {
      "title": "火山方舟 DeepSeek",
      "provider": "openai",
      "model": "deepseek-v3",
      "apiKey": "你的API Key",
      "apiBase": "https://ark.cn-beijing.volces.com/api/v3"
    }
  ]
}
```

### 第四步：开始使用

- 选中代码，右键选择 "Explain" 解释代码
- 选中代码，右键选择 "Edit" 让AI修改
- 在侧边栏和AI对话

## 常用功能

### 1. 代码解释

选中代码 → 右键 → Explain

AI会解释这段代码的工作原理。

### 2. 代码生成

在侧边栏输入需求，AI生成代码。

### 3. 代码重构

选中代码 → 右键 → Edit → 输入修改要求

### 4. 自动补全

输入代码时，按Tab接受AI建议。

## 快捷键

| 快捷键 | 功能 |
|--------|------|
| Cmd/Ctrl + L | 打开侧边栏 |
| Cmd/Ctrl + Shift + L | 新对话 |
| Tab | 接受建议 |
| Esc | 取消生成 |

## 模型切换

在侧边栏顶部可以切换模型：
- 日常开发 → Doubao
- 复杂问题 → DeepSeek-V3
- 写文档 → GLM-4

## 写在最后

VS Code + 火山方舟Coding Plan，是目前性价比最高的AI编程方案。

36元/月，享受接近Cursor的体验。

👉 **[点击订阅](https://volcengine.com/L/a6sqe8YHzWo/)**

---

## 📚 想系统学习AI编程？

👉 **[点击了解AI编程训练营](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

**《30讲 · AI编程训练营》** —— VS Code AI编程最佳实践。

---

程序员晚枫，专注AI编程培训，开源项目 [python-office](https://www.python-office.com/) 作者。

---

## 相关阅读

- [我用AI卖了600本书，单日收入2400+](https://mp.weixin.qq.com/s/iyzIiPyiL1t-5s93E9sw4A)
- [人在曼谷旅游，AI在帮我赚钱](https://mp.weixin.qq.com/s/KLXXEoxMu9uayJTLXStIzw)
- [别再用人力硬扛任务了！普通人也能落地的全场景 AI 实战营来了](https://mp.weixin.qq.com/s/KuyuljSXInUFavCz7iL5Yw)
- [副业收入是工资的10倍，上班真的耽误赚钱](https://mp.weixin.qq.com/s/tCCOrtxPwn_s_ShBvfS-HQ)
- [学AI编程别瞎忙！3步走，从零基础到能做实战项目](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)
- [小白10分钟搞定！OpenClaw下载和安装教程，无脑点击开通](https://mp.weixin.qq.com/s/mT_MKixwcY6HTMhT_69Imw)

---

## 🤖 开发者效率工具推荐

👉 想体验 **MiniMax Token Plan**？[点击这里享受 9 折优惠](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

💡 **按次计费，非常划算！** 想象成去菜市场买菜——买张门票进去，菜随便拿。按使用次数收费，不限额度，用多少付多少，特别适合开发者！


---
title: DeepSeek Coding Plan 教程：API + 本地部署 2 种玩法，手把手带你跑通
date: 2026-04-22 19:25:00
tags: ["deepseek", "coding plan教程", "api调用", "本地部署", "Ollama", "开源"]
categories: ["DeepSeek实战"]
keywords: [DeepSeek Coding Plan教程, API调用, 本地部署, Ollama, DeepSeek Coder, 开源]
description: DeepSeek Coding Plan 2 种玩法实测：API 调用 5 分钟上手，本地部署 0 API 费用。含可直接复制的 Python 代码和硬件清单。
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="https://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>

<p align="center" name="atomgit">
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>	
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    <a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
</p>

<!-- more -->

> **科技不高冷，AI很好用** | 我是程序员晚枫，全网 40 万+ 粉丝

---

> 📖 **看本文之前，建议先读这篇**：
> 👉 [《大厂 Coding Plan 价格被我扒光了！买贵的人都在偷偷看这个》](https://www.python-office.com/openclaw/coding-plan/)
>
> 想看完整的大厂 AI Coding Plan + Token 价格对比、隐藏购买渠道、避坑提醒？这份持续更新的价格汇总表全整理好了。建议先收藏，再回来按本文 2 种玩法上手。

---

## 一句话结论

**DeepSeek Coding Plan 有 2 种主流玩法，看你需求：**
- 想 5 分钟跑通、懒得折腾：**走 API 调用**，5 步搞定
- 想 0 API 费用、数据私有：**本地部署**，Ollama 一行命令
- 不确定：**先 API，再本地**——80% 的用户其实只需要 API

下面分别讲。

---

## 🚀 玩法一：API 调用（5 分钟上手）

适合：想快速体验、不愿折腾硬件的同学。

### 第一步：获取 API Key（1 分钟）

1. 打开 [DeepSeek 开放平台](https://platform.deepseek.com/)
2. 注册账号（新用户有免费额度，不用先充钱）
3. 进「API Keys」→ 「创建」→ 复制保存（**只显示一次**）

### 第二步：安装依赖（1 分钟）

```bash
pip install openai
```

### 第三步：调用 API（1 行代码）

```python
from openai import OpenAI

client = OpenAI(
    api_key="你的 API Key",
    base_url="https://api.deepseek.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个 Python 专家。"},
        {"role": "user", "content": "帮我写一个 Python 快速排序"}
    ]
)

print(response.choices[0].message.content)
```

### 第四步：接入 IDE（可选）

支持 **VS Code、JetBrains** 等主流 IDE 装 Continue / Cline 插件：
- VS Code：搜「Cline」或「Continue」装上
- JetBrains：搜「Continue」插件

配置 `base_url = https://api.deepseek.com/v1` + 你的 API Key 即可。

### 第五步：成本控制（避坑）

- **先小额测试**：充 10 元，够跑几十万次对话
- **设置月度上限**：后台 → 账户设置 → 限额
- **监控调用量**：Prometheus / 自建脚本都行

> 💡 **V4 Pro 当前 2.5 折**，活动到 5 月 5 日截止。[点我看价格](https://www.python4office.cn/ads/deepseek/20260422-deepseek-money-saving-tips/)

---

## 💻 玩法二：本地部署（0 API 费用）

适合：有显卡、追求数据私有、想长期省钱的同学。

### 核心优势

- ✅ 没有 API 调用费用（电费忽略不计）
- ✅ 数据完全私有（代码不出本机）
- ✅ 可以离线使用（出差 / 飞机上也能用）
- ✅ 商用免费（MIT 协议）

### 硬件要求

| 模型 | 最低显存 | 推荐显卡 | 性能对标 |
|------|----------|----------|----------|
| DeepSeek-Coder 6.7B | 6GB | GTX 1060+ | 比 GPT-3.5 略弱 |
| DeepSeek-Coder 33B | 24GB | RTX 4090 | 对标 GPT-4 |
| DeepSeek-V3 量化版 | 24GB | RTX 4090 | 对标 GPT-4 |
| DeepSeek-V3 满血版 | 80GB+ | 多卡服务器 | GPT-4 Turbo |

> 💡 **没有显卡？** 阿里云 / 腾讯云租 A100，约 8 元/小时，跑完任务关机。

### 部署步骤（4 步）

**Step 1：装 Ollama**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Step 2：拉模型**

```bash
ollama pull deepseek-coder:6.7b
```

**Step 3：跑起来**

```bash
ollama run deepseek-coder:6.7b
```

**Step 4：用 OpenAI 兼容 SDK 调用**

```python
from openai import OpenAI

client = OpenAI(
    api_key="ollama",  # 任意非空字符串
    base_url="http://localhost:11434/v1"
)

response = client.chat.completions.create(
    model="deepseek-coder:6.7b",
    messages=[
        {"role": "user", "content": "写一个 Python 快速排序"}
    ]
)

print(response.choices[0].message.content)
```

---

## 📊 两种方式对比

| 维度 | API 调用 | 本地部署 |
|------|----------|----------|
| 上手难度 | ⭐ 5 分钟 | ⭐⭐⭐ 半天 |
| 费用 | 按 token 付费 | 一次性硬件投入 |
| 初始成本 | 0 元 | 几千-几万元（显卡） |
| 数据安全 | 数据在云端 | 完全私有 |
| 离线可用 | ❌ | ✅ |
| 模型更新 | 自动 | 手动 |
| 性能上限 | 取决于套餐 | 取决于显卡 |
| 适合谁 | 个人 / 中小团队 | 重度 / 隐私敏感 / 团队 |

---

## 🎯 怎么选？一张图说清

| 你的情况 | 推荐 | 理由 |
|---------|------|------|
| 第一次接触 DeepSeek | **API 调用** | 5 分钟跑通，先试再决定 |
| 个人开发者 / 偶尔用 | **API 调用（V4 Pro 2.5 折）** | 性价比最高 |
| 数据敏感 / 金融 / 医疗 | **本地部署** | 数据不出本机 |
| 重度使用 / 月花 500+ 元 | **本地部署** | 一次投入，长期省钱 |
| 团队 / 多人协作 | **API 调用 + 企业版** | 免维护 |
| 喜欢折腾 / 学习用 | **本地部署** | 练手 + 省钱 |

---

## ⚠️ 3 条避坑提醒

1. **API Key 别上传 GitHub** —— 加 `.env` + `.gitignore`
2. **本地部署别硬上 67B** —— 6.7B / 33B 已足够日常使用
3. **出 5xx 错误立刻降级** —— API 失败时切本地，反之亦然

---

## 📚 想深入了解？

- 👉 想看完整大厂 Coding Plan 价格对比？[点这里](https://www.python-office.com/openclaw/coding-plan/)
- 👉 [DeepSeek Coding Plan 全解析：开源 + 1/70 价格](https://www.python4office.cn/ads/deepseek/20260422-deepseek-coding-plan-intro/)
- 👉 [DeepSeek Coding Plan 适合谁用？5 类人闭眼入](https://www.python4office.cn/ads/deepseek/20260422-deepseek-coding-plan-who-should-use/)
- 👉 [DeepSeek API 完整教程：5 步从注册到第一个调用](https://www.python4office.cn/ads/deepseek/20260422-deepseek-api-tutorial/)

---

> 👉 加我微信：**aiwf365**（备注：Coding Plan）
> 或 👉 [加入 AI 编程学习交流群](https://www.python4office.cn/wechat-group/)

---

<p align="center">
	<img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="80%"/>
</p>
## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)
- 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)

---
title: DeepSeek API 全网最细教程！5 步从注册到第一个调用，附 Python 代码
date: 2026-04-22 00:00:00
tags: ["deepseek", "api", "AI编程", "程序员晚枫", "入门教程"]
categories: ["DeepSeek实战"]
keywords: [DeepSeek API, DeepSeek 教程, API注册, API Key, Python调用]
description: DeepSeek API 5 步上手：从注册、获取 Key、Python 调用、价格说明到避坑提醒，附可直接复制的代码。
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
> 想看完整的大厂 AI Coding Plan + Token 价格对比、隐藏购买渠道、避坑提醒？这份持续更新的价格汇总表全整理好了。建议先收藏，再回来按本文 5 步上手 DeepSeek API。

---

## 一句话结论

**DeepSeek API 是目前中文场景下最便宜的 LLM API（GPT-4 价格的 1/70）。**
- 第一次接触 API：**严格按本文 5 步走，30 分钟内跑通第一个调用**
- 已经有 OpenAI 经验：**只看你不熟的部分**（第 2、4 步）
- 想批量 / 团队使用：**先看价格表**，再决定充值策略

下面开始。

---

## 第一步：注册账号（2 分钟）

1. 打开 [DeepSeek 开放平台](https://platform.deepseek.com/)
2. 点击右上角「注册」，用手机号或邮箱
3. 完成验证，登录后台

**避坑 3 条**：
- 新用户有 **免费额度**（通常 1 元起），先别充值
- 国内手机号即可，**不用科学上网**
- 实名认证可以后补，**不认证也能先调用 API**

---

## 第二步：获取 API Key（1 分钟）

登录后 → 左侧菜单「API Keys」→ 「创建新的 API Key」→ 复制保存。

**注意**：
- API Key **只显示一次**，丢了只能重新创建
- 不要提交到 GitHub、不要在公开场合贴
- 建议立刻存到密码管理器（1Password / Bitwarden）

---

## 第三步：Python 调用（10 分钟）

DeepSeek 兼容 OpenAI 协议，**直接用 OpenAI SDK 即可**。

**安装依赖**：

```bash
pip install openai
```

**最小可运行代码**：

```python
from openai import OpenAI

client = OpenAI(
    api_key="你的 API Key",
    base_url="https://api.deepseek.com/v1"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个有用的 AI 助手。"},
        {"role": "user", "content": "你好"}
    ]
)

print(response.choices[0].message.content)
```

**进阶：流式输出**（打字机效果）：

```python
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "用 100 字介绍 DeepSeek"}],
    stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```

---

## 第四步：价格说明（决定你充多少钱）

**DeepSeek V4 Pro 当前 2.5 折，活动到 5 月 5 日截止。**

| 模型 | 原价输入 | 2.5 折输入 | 原价输出 | 2.5 折输出 |
|------|----------|-----------|----------|-----------|
| V4 Pro（缓存命中） | 1 元 | **0.25 元** | 24 元 | **6 元** |
| V4 Pro（缓存未命中） | 12 元 | **3 元** | 24 元 | **6 元** |
| V3 / V3.2 | 1-2 元 | —— | 2-3 元 | —— |

**单位：元 / 百万 tokens**（1M tokens ≈ 75 万字中文）

**对比参考**：
- GPT-4：约 200 元/百万 tokens（输入）
- Claude Sonnet 4.6：约 21 元/百万 tokens（输入）
- **DeepSeek V4 Pro 打折后：3 元/百万 tokens**

**充值建议**：
- 个人玩玩：**先充 10 元**，能跑几十万次对话
- 团队 / 项目：**先充 100 元 + 设月度限额**
- 重度使用：**联系商务谈批量价**

---

## 第五步：实战场景（直接抄作业）

| 场景 | 推荐模型 | 关键参数 |
|------|----------|----------|
| 代码补全 / 生成 | `deepseek-coder` | temperature=0.2 |
| 长文总结 / 翻译 | `deepseek-chat` | max_tokens=2000 |
| Agent / 工具调用 | `deepseek-chat` | tools=[...] |
| 长上下文（>32K） | `deepseek-chat` | 支持 128K |
| 复杂推理 | `deepseek-reasoner` | 多走几步思考 |

---

## ⚠️ 6 条避坑提醒

1. **API Key 一定别上传 GitHub** —— 加进 `.env` + `.gitignore`
2. **先小额测试** —— 新模型 / 新 Prompt，先用 1 元跑通再放量
3. **设置使用限额** —— 后台 → 账户设置 → 月度上限
4. **监控调用量** —— Prometheus / Grafana / 自建脚本都行
5. **不要在前端暴露 Key** —— 所有调用走后端
6. **出 5xx 错误立刻降级** —— 配 OpenAI 兼容的备用模型（Qwen / GLM）

---

## 📚 想深入了解？

- 👉 想看完整大厂 Coding Plan 价格对比？[点这里](https://www.python-office.com/openclaw/coding-plan/)
- 👉 [DeepSeek 一年省几千的 5 个狠招](https://www.python4office.cn/ads/deepseek/20260422-deepseek-money-saving-tips/)
- 👉 [DeepSeek Coding Plan 完整教程](https://www.python4office.cn/ads/deepseek/20260422-deepseek-coding-plan-tutorial/)
- 👉 [DeepSeek 办公自动化 10 大狠招](https://www.python4office.cn/ads/deepseek/20260422-deepseek-office-automation/)

---

> 👉 加我微信：**aiwf365**（备注：API）
> 或 👉 [加入 AI 编程学习交流群](https://www.python4office.cn/wechat-group/)

---

<p align="center">
	<img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="80%"/>
</p>
## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)
- 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)

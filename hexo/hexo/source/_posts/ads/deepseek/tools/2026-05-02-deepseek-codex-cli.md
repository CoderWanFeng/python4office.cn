---
title: Codex CLI 接入 DeepSeek Coding Plan 实战：5 分钟配置，AI 编程成本砍半
date: 2026-05-02 19:52:00
tags: ["Codex CLI", "DeepSeek", "Coding Plan", "命令行", "AI编程", "程序员晚枫"]
categories: ["AI编程工具配置"]
keywords: [Codex CLI, DeepSeek Coding Plan, OpenAI替代, 命令行AI, 终端编程]
description: 在 Codex CLI（OpenAI 出的命令行 AI 助手）里接入 DeepSeek Coding Plan 完整教程：5 分钟配置步骤 + 4 个常见问题。
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
> 想看完整的大厂 AI Coding Plan + Token 价格对比、隐藏购买渠道、避坑提醒？这份持续更新的价格汇总表全整理好了。建议先收藏，再回来按本文 5 分钟配好 Codex CLI + DeepSeek。

---

## 一句话结论

**在 Codex CLI（OpenAI 出的命令行 AI 助手）里接入 DeepSeek Coding Plan，5 分钟搞定，AI 编程成本砍掉 50%+。**
- 已经是 Codex CLI 用户：**按本文 3 步配置**，换底层模型
- 不想订阅 ChatGPT Plus：**首选 Codex CLI + DeepSeek**
- 担心配置出问题：**先看第 4 节 4 个常见问题**

下面开始。

---

Codex CLI 是 OpenAI 官方推出的命令行 AI 助手，支持代码生成和技术问答，**默认绑定 OpenAI 模型，国内访问困难，按 token 收费偏贵**。

**接入 DeepSeek Coding Plan 之后**：
- ✅ OpenAI 兼容接口，**配置几乎零成本**
- ✅ 国内节点直连，响应稳定
- ✅ API 1 元/百万 tokens 起，**比 OpenAI API 便宜 90%+**
- ✅ 仍用熟悉的 `codex` 命令行交互

---

## 一、Codex CLI 接入 DeepSeek 的 4 大优势

| 优势 | 说明 |
|------|------|
| 🧠 推理能力强 | DeepSeek 数学和代码推理能力业界领先 |
| 💰 按量计费 | 用多少付多少，1 元/百万 tokens 起 |
| 🔧 配置简单 | OpenAI 兼容接口，2 行环境变量搞定 |
| 🌏 国产节点 | 国内服务器，响应速度快 |
| 🤝 专属优惠 | 用晚枫的专属链接开卡更划算 |

---

## 二、5 分钟配置步骤

### Step 1：开通 DeepSeek Coding Plan

👉 **专属优惠通道**：[cloud.siliconflow.cn/i/ciS03HX7](https://cloud.siliconflow.cn/i/ciS03HX7)

开通后，进入控制台 → API Keys → 创建并保存你的 Key。
**注意：API Key 只显示一次，丢失需重新创建。**

---

### Step 2：在 Codex CLI 中配置 DeepSeek（环境变量方式）

**临时生效**（当前终端）：

```bash
export OPENAI_API_KEY="你的DeepSeek API Key"
export OPENAI_API_BASE="https://api.deepseek.com/v1"
```

**永久生效**（推荐，写入 `~/.bashrc` 或 `~/.zshrc`）：

```bash
echo 'export OPENAI_API_KEY="你的DeepSeek API Key"' >> ~/.zshrc
echo 'export OPENAI_API_BASE="https://api.deepseek.com/v1"' >> ~/.zshrc
source ~/.zshrc
```

> 💡 Codex CLI 默认读 `OPENAI_API_KEY` / `OPENAI_API_BASE`，**DeepSeek 完美兼容**，零代码改动。

---

### Step 3：验证 + 开始使用

1. 终端输入 `codex`
2. 提问测试：`用Python写一个快速排序`
3. 看到 AI 正常回复 = 配置成功

> 💡 **进阶**：想用更强的 V4 Pro（代码推理更好），可在调用时传参 `--model deepseek-reasoner` 或 `deepseek-coder`。

---

## 三、成本对比：Codex CLI + OpenAI vs Codex CLI + DeepSeek

**假设每天 100 次 AI 编程对话，每次 2000 tokens（输入 + 输出）：**

| 方案 | 月调用量 | 月成本 | 年成本 |
|------|----------|--------|--------|
| Codex CLI + GPT-4 | 60 万 tokens | **~120 元** | ~1440 元 |
| Codex CLI + DeepSeek V3.2 | 60 万 tokens | **~1 元** | ~12 元 |
| Codex CLI + DeepSeek V4 Pro（2.5 折）| 60 万 tokens | **~3 元** | ~36 元 |

**结论：换 DeepSeek 后，月成本从 120 元降到 1-3 元，**省 95% 以上****。

> 📌 **DeepSeek V4 Pro 当前 2.5 折，活动到 5 月 5 日截止**——这是 V4 上市以来最低价。

---

## 四、4 个常见问题

### Q1：Codex CLI 的所有功能都能用 DeepSeek 吗？

**A：能用。** Codex CLI 是 OpenAI 兼容的 CLI 工具，**所有功能照常用**，只是底层模型换成 DeepSeek。

### Q2：会不会比 OpenAI 模型弱？

**A：分场景。**

| 任务 | DeepSeek V4 Pro | GPT-4 | 选谁 |
|------|----------------|-------|------|
| 中文代码生成 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | DeepSeek |
| 算法题 / 推理 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | DeepSeek 略胜 |
| 复杂业务逻辑 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | GPT-4 |
| 多文件 Agent | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | GPT-4 |
| 文档 / 注释 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | DeepSeek |

**结论**：日常编码任务 DeepSeek 完全够用，复杂业务逻辑再考虑 GPT-4。

### Q3：环境变量配完不生效怎么办？

**A：3 步排查**：
1. **重启终端**：环境变量修改后必须重启终端
2. **检查变量名**：必须是 `OPENAI_API_KEY` 和 `OPENAI_API_BASE`（不是 `DEEPSEEK_API_KEY`）
3. **检查 URL 末尾**：必须是 `https://api.deepseek.com/v1`（带 `/v1`）

### Q4：能同时用 OpenAI 和 DeepSeek 吗？

**A：能。** 通过切换环境变量或写脚本包装即可：

```bash
# 切到 OpenAI
export OPENAI_API_BASE="https://api.openai.com/v1"
export OPENAI_API_KEY="你的OpenAI Key"

# 切到 DeepSeek
export OPENAI_API_BASE="https://api.deepseek.com/v1"
export OPENAI_API_KEY="你的DeepSeek Key"
```

---

## 五、Codex CLI vs 其他编辑器 + DeepSeek

| 编辑器 | 配置 DeepSeek 难度 | 是否推荐 | 适合谁 |
|--------|-------------------|----------|--------|
| Cursor | ⭐⭐ 简单 | ⭐⭐⭐⭐ | 想要 AI-first IDE 的开发者 |
| Claude Code | ⭐⭐ 简单 | ⭐⭐⭐⭐⭐ | 命令行党 |
| Cline | ⭐⭐ 简单 | ⭐⭐⭐⭐⭐ | VS Code 用户 / 开源党 |
| **Codex CLI** | ⭐⭐ 简单 | ⭐⭐⭐⭐ | **OpenAI 习惯用户** |
| JetBrains + Continue | ⭐⭐ 中等 | ⭐⭐⭐⭐ | 用 IDEA 体系的 Java 开发者 |
| Zed | ⭐⭐⭐ 中等 | ⭐⭐⭐ | 追求速度的极客 |
| OpenCode | ⭐⭐ 简单 | ⭐⭐⭐⭐⭐ | 命令行党 |

> 📌 想看**完整的编辑器 + 模型选型表**？[点这里看持续更新的版本](https://www.python-office.com/openclaw/coding-plan/)

---

## 六、总结

| 维度 | 配置情况 |
|------|----------|
| 配置时间 | **5 分钟** |
| 配置难度 | ⭐⭐（简单） |
| 适合人群 | OpenAI 习惯用户 / 命令行党 |
| 月成本 | **从 120 元降到 1-3 元** |
| 中文支持 | 显著优于 GPT-4 |
| 国内速度 | 节点直连，秒级响应 |

**一句话：在 Codex CLI 里用 DeepSeek，配置 5 分钟，省钱 95%，中文还更好。**

---

## 📚 相关阅读

- 👉 [各大厂 Coding Plan 价格一站对比](https://www.python-office.com/openclaw/coding-plan/)
- 👉 [DeepSeek Coding Plan 全解析：开源 + 1/70 价格](https://www.python4office.cn/ads/deepseek/20260422-deepseek-coding-plan-intro/)
- 👉 [DeepSeek Coding Plan 教程：API + 本地部署 2 种玩法](https://www.python4office.cn/ads/deepseek/20260422-deepseek-coding-plan-tutorial/)
- 👉 [DeepSeek Coding Plan 适合谁？5 类人闭眼入](https://www.python4office.cn/ads/deepseek/20260422-deepseek-coding-plan-who-should-use/)
- 👉 [DeepSeek API 完整教程：5 步从注册到第一个调用](https://www.python4office.cn/ads/deepseek/20260422-deepseek-api-tutorial/)
- 👉 [DeepSeek 一年省几千的 5 个狠招](https://www.python4office.cn/ads/deepseek/20260422-deepseek-money-saving-tips/)

---

*免责声明：本文含推广链接（cloud.siliconflow.cn），通过链接购买不会增加你的费用，但可能为晚枫带来推荐收益。*

---

> 👉 加我微信：**aiwf365**（备注：Codex CLI）
> 或 👉 [加入 AI 编程学习交流群](https://www.python4office.cn/wechat-group/)

---

<p align="center">
	<img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="80%"/>
</p>
## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲，先看看适不适合自己](https://pan.quark.cn/s/8f7886f79569)
- 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)

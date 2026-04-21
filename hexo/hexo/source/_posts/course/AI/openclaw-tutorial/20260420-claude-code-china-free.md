---
title: Claude Code现在可以免费用！还可以接入便宜的国产大模型
date: 2026-04-20 19:08:00
tags: [AI编程, openclaw, claude-code]
---



<p align="center" id='扫码查看AI编程训练营'>
    <a target="_blank" href='https://www.bilibili.com/cheese/play/ss982042944'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
    </a>   
</p>




<p align="center" name="atomgit">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>	
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
<a href="https://www.bilibili.com/cheese/play/ss982042944">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>

<!-- more -->

大家好，这里是程序员晚枫。

最近在[AI编程交流群](https://www.python4office.cn/wechat-group/)里，有个问题被反复问到：

> **"晚枫，Claude Code我想用，但是在大陆用不了怎么办？"**

我每次都要解释一遍，干脆写篇文章，一次说清楚。

---

## 一、先搞清楚一件事：Claude Code ≠ Claude大模型

很多人把这两个东西搞混了，这是理解问题的关键。

**Claude大模型**（claude.ai）：
- Anthropic公司的AI大模型服务
- 在大陆**确实无法直接访问**
- 需要特殊网络环境才能使用

**Claude Code**（编程工具）：
- 一个**开源的AI编程框架/工具**
- 本质上是一个可以调用任意大模型的**终端编程助手**
- 在大陆**完全可以正常安装和使用** ✅

> 💡 打个比方：Claude Code就像一辆车的"车身"，Claude大模型只是其中一款"发动机"。车身你可以随便用，只是原装发动机在大陆买不到——但你完全可以换一个国产发动机！

---

## 二、Claude Code本身是免费的

Claude Code是开源项目，**安装和使用本身完全免费**。

你需要付费的，只是你接入的**大模型API调用费用**。

而这个费用，完全可以通过接入国产便宜大模型来大幅降低。

---

## 三、怎么在大陆用Claude Code？

### 第一步：安装Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

安装完成后，在终端输入 `claude` 就可以启动。

### 第二步：接入便宜的国产大模型

这一步是关键。Claude Code支持通过环境变量配置任意兼容OpenAI格式的API。

国内可以用的便宜大模型（每百万Token价格参考）：

| 模型 | 输入价格 | 输出价格 | 平台 |
|------|----------|----------|------|
| **DeepSeek V3** | ~2元 | ~3元 | DeepSeek官方 |
| **千问 Qwen3-Flash** | 1.2元 | 7.2元 | 阿里百炼 |
| **豆包** | ~0.8元 | ~2元 | 火山引擎 |
| **GLM-4** | ~1元 | ~5元 | 智谱AI |

配置方式（以DeepSeek为例）：

```bash
export ANTHROPIC_BASE_URL=https://api.deepseek.com
export ANTHROPIC_API_KEY=你的DeepSeek_API_Key
claude
```

### 第三步：开始编程

配置完成后，Claude Code就可以正常使用了。你可以：

- 让它帮你读懂整个项目代码
- 直接用自然语言描述需求，让它写代码
- 让它帮你debug、重构、写测试

---

## 四、更多接入方案

如果你想了解更多便宜大模型的接入方式，以及如何搭建自己的AI编程环境，可以看我整理的这个教程：

👉 **[https://python-office.com/openclaw](https://python-office.com/openclaw)**

里面包含了：
- ✅ 各大厂Token价格对比
- ✅ 国内大模型接入教程
- ✅ OpenClaw完整使用指南
- ✅ AI编程实战案例

---

## 总结

| 问题 | 答案 |
|------|------|
| Claude大模型在大陆能用吗？ | ❌ 直接访问受限 |
| Claude Code在大陆能用吗？ | ✅ 完全可以 |
| Claude Code免费吗？ | ✅ 工具本身免费 |
| 大陆用户怎么用？ | 接入国产便宜大模型即可 |
| 去哪里看详细教程？ | [python-office.com/openclaw](https://python-office.com/openclaw) |

**一句话总结：Claude Code是工具，大模型是燃料。工具免费，燃料换国产的，又便宜又好用。**

---

## 相关阅读

- [2026年最全AI Coding Plan和Token购买攻略](https://www.python4office.cn/course/AI/openclaw-tutorial/20260419-AI-coding-plan-token-price-guide/)
- [给小白的AI编程训练营](https://www.bilibili.com/cheese/play/ss982042944)
- [OpenClaw完整教程](https://python-office.com/openclaw)


<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

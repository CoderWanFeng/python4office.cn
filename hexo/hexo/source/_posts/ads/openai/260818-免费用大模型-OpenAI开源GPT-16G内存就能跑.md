---
title: 别花钱买大模型了！OpenAI 开源了 gpt-oss，16G 内存就能跑
date: 2026-08-18 00:18:00
tags:
  - 公众号文章
  - 免费大模型
  - OpenAI
  - gpt-oss
  - 开源模型
categories:
  - 公众号文章
cover: https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/gpt-oss-free-cover.jpg
---

<!-- more -->

> 都说天下没有免费午餐，大模型第一个不服。

> 今天带大家免费用的是——OpenAI 自己开源的 gpt-oss。

大家好，我是程序员晚枫。

很多人不知道，OpenAI 开源了一款新模型——gpt-oss。虽然比不上 GPT-5，但作为开源模型，它具备完整推理能力、支持函数调用，能力接近 OpenAI 自家的 o4-mini。Apache 2.0 协议，能商用，能下载到自己电脑上跑。

**16G 内存的笔记本就能跑起来，一分钱不花。**

我知道国内有不少朋友，对 GPT 模型一直挺感兴趣，但用起来总有不少麻烦——要么网络不畅，要么注册流程繁琐，要么用着用着就断了。现在有个新选择：**把模型下载到自己电脑上运行，不依赖任何在线服务，一次下载，永久可用。**

**视频版讲解**：B 站《GPT 可以免费用》（1 分钟）

<iframe src="//player.bilibili.com/player.html?bvid=BV1CH8n6CEmp&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="480"> </iframe>

视频链接：[https://www.bilibili.com/video/BV1CH8n6CEmp/](https://www.bilibili.com/video/BV1CH8n6CEmp/?spm_id_from=333.1387.homepage.video_card.click)

***

## OpenAI 开源的 GPT，到底有哪几个

先说结论：目前能下载部署的，一共就两个——**gpt-oss-120b** 和 **gpt-oss-20b**。

这两个模型是 2025 年 8 月发布的，是 OpenAI 自 2019 年开源 GPT-2 以来，时隔 6 年第一次重新开源。消息出来那天凌晨，GitHub star 5 小时破 2 万，全球开发者都炸了。
![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260819231624271.png)

| 模型               | 参数量    | 硬件门槛                   | 适合谁          |
| ---------------- | ------ | ---------------------- | ------------ |
| **gpt-oss-20b**  | 210 亿  | 16G 内存                 | 笔记本、手机，个人本地跑 |
| **gpt-oss-120b** | 1170 亿 | 单张 80G 显卡（H100/MI300X） | 服务器、生产级部署    |

两个模型都支持完整思维链输出、函数调用、结构化输出，推理能力接近 OpenAI 的 o4-mini。**而且都是 Apache 2.0 协议，商用免费，没有版权风险。**

还有一个容易混淆的点。很多人一听说"OpenAI 开源"，就以为 GPT-3、GPT-4、GPT-4o、GPT-5 都能下载了——**想多了，这些全是闭源的，只能调 API，下载不到。**

OpenAI 确实开源了不少项目，但能称为"语言模型"的，就 gpt-oss 这两个，外加 2019 年的 GPT-2（现在看来已经过时了，只有学习价值）。其他几个经常被误认为是 GPT 的开源项目，其实做的是完全不同的事：

| 开源项目 | 干什么 | 是语言模型吗 |
|---------|--------|------------|
| **Whisper** | 语音转文字 | 不是 |
| **CLIP** | 判断图片和文字有多相关 | 不是 |
| **tts** | 文字转语音 | 不是 |

简单说：OpenAI 开源的"能跟你聊天的 GPT"，就 gpt-oss-20b 和 gpt-oss-120b 这两个，没有别的了。

所以别被网上那些"卖 GPT 模型"的忽悠了——**OpenAI 自己都免费开源了，你花钱买的所谓"GPT 本地版"，大概率就是帮你下载了一个免费的东西。**

***

## 16G 内存就能跑，3 种方式下载部署

### 方式一：Ollama 一行命令（最简单，推荐国内用户首选）

如果你不想折腾环境，装个 [Ollama](https://ollama.com/)，然后终端输入一行命令：

```bash
ollama run gpt-oss:20b
```

等它下载完（大约 13G），直接就能聊天了。不用写代码，不用配显卡驱动，Mac、Windows、Linux 都支持。

**下载完之后断网都能用。** 模型文件存在你本地硬盘上，跑起来不依赖任何在线服务，不上传你的对话内容。之前为远程访问 GPT 折腾过的朋友，这条方案值得试试——下载一次，永久免费，离线可用。

**16G 内存的电脑就能跑，2020 年以后的笔记本基本都达标。**

![OpenAI gpt-oss-20b 官方图](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/gpt-oss-20b-banner.png)

*图片来源：[OpenAI gpt-oss 官方仓库](https://github.com/openai/gpt-oss)*

### 方式二：HuggingFace 下载 + Transformers

如果你想用 Python 代码跑，从 HuggingFace 下载模型权重：

```bash
git lfs install
git clone https://huggingface.co/openai/gpt-oss-20b
```

然后几行 Python 就能调用：

```python
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="openai/gpt-oss-20b",
    torch_dtype="auto",
    device_map="auto",
)
messages = [{"role": "user", "content": "介绍一下你自己"}]
outputs = pipe(messages, max_new_tokens=256)
print(outputs[0]["generated_text"][-1])
```

### 方式三：在线试玩，不下载

如果你只是想体验一下，不想下载十几个 G 的文件，打开 [gpt-oss.com](https://www.gpt-oss.com/)，网页上直接聊。

**三种方式的下载地址我都放在文末参考链接里了。**

***

## 1200 亿参数，为什么 16G 内存就够跑

![OpenAI gpt-oss-120b 官方图](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/gpt-oss-120b-banner.png)

*图片来源：[OpenAI gpt-oss 官方仓库](https://github.com/openai/gpt-oss)*

这里有个很多人想不通的问题：gpt-oss-120b 有 1170 亿参数，按照"1 个参数约 2 字节"的常识，光模型文件就要 200 多 G，怎么塞进 16G 内存的电脑？

**答案是三个字：混合专家（MoE）。**

传统大模型比如 GPT-3，1750 亿参数，每次生成一个字，1750 亿参数全部参与计算。就像一个 1750 人的公司，每写一封信，全员都得加班。

但 gpt-oss 用的是 MoE 架构——把参数分成很多个"专家小组"，每次只激活其中一小部分。gpt-oss-120b 虽然总参数 1170 亿，但每次推理只激活 **51 亿**参数。

打个比方：一家医院有 1000 个医生，你看感冒的时候，只需要挂一个耳鼻喉科的号，不需要 1000 个医生全到场。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260819231811289.png)

这意味着两件事：

第一，**推理时占用的内存大幅降低**。120b 模型用 MXFP4 量化后，文件大约 60G，但运行时不需要把所有参数同时加载到显存。配合量化技术，20b 版本 16G 内存就能跑。

第二，**速度更快**。因为每次只激活 5% 的参数，计算量远小于同等参数量的稠密模型。这就是为什么 gpt-oss-20b 在手机上都能流畅运行。

这也是整个开源大模型领域的趋势——DeepSeek V4、Qwen 3.5、Llama 4，旗舰模型几乎全在用 MoE。**大模型不再拼"谁参数多"，而是拼"谁在同等参数下激活得更少"。**

所以你看到 OpenAI 开源 1170 亿参数的模型，别被数字吓到。它实际跑起来，比很多 200 亿参数的稠密模型还轻快。

而对于国内朋友来说，这可能是目前最优雅的 GPT 使用方案：**不用梯子，不用抢号，不依赖网络，下载一次，永久免费，离线可用。** 之前为了用 GPT 折腾的那些功夫，从今天起可以省了。

想看本地部署教程的，评论区告诉我，下期手把手教你怎么在笔记本上跑 gpt-oss。

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！

### 参考链接

- [OpenAI 官方：gpt-oss 模型发布博客：https://openai.com/index/introducing-gpt-oss/](https://openai.com/index/introducing-gpt-oss/)
- [OpenAI gpt-oss GitHub 仓库：https://github.com/openai/gpt-oss](https://github.com/openai/gpt-oss)
- [gpt-oss-20b HuggingFace 下载：https://huggingface.co/openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b)
- [gpt-oss-120b HuggingFace 下载：https://huggingface.co/openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b)
- [Ollama 官方：本地运行 gpt-oss 文档：https://ollama.com/library/gpt-oss](https://ollama.com/library/gpt-oss)

## 相关阅读

- [用上 OpenCode 的5 个免费大模型，省了我 200 刀 ChatGPT 年费](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)
- [AI 圈公开的秘密：DeepSeek V4 Flash 可以免费用](https://mp.weixin.qq.com/s/KNTw9mCUcTMzcPIwNkgPVg)
- [别再乱选大模型了！小白也能看懂的「好坏判断指南」，3分钟避坑](https://mp.weixin.qq.com/s/uPAJewJ-YeRnESEAAwLlkw)

![AI 实战课](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/gpt-oss-free-cover.jpg)
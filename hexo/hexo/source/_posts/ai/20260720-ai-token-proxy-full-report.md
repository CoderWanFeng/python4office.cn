---
title: 我查了一圈AI中转站，发现近一半在偷偷换模型
date: 2026-07-20 11:00:00
tags: [ai工具, token中转站, api proxy, openrouter, one-api, 开源项目]
categories: [ai工具]
keywords: [AI Token中转站, API Proxy, One API, New API, LiteLLM, OpenRouter, 大模型API, 中转服务]
description: 一篇德国论文测出45.83%的AI中转站在"掉包"——你付GPT-5的钱，后台悄悄换成廉价小模型。中转站怎么运作、怎么自己搭、为什么能神不知鬼不觉换模型，一次讲清楚。
cover: https://images.unsplash.com/photo-1558494949-ef010cbdcc3b?q=80&w=1200&auto=format&fit=crop
---

<!-- more -->

# 我查了一圈AI中转站，发现近一半在偷偷换模型

大家好，我是程序员晚枫。

最近我看到一篇德国 CISPA 信息安全中心的论文，看完后背发凉。

他们系统性地测了一批 AI 中转站，结果发现：**45.83% 的接口在"掉包"**——你按 GPT-5、Claude 的价格付了钱，后台却悄悄换成了廉价的开源小模型<sup>[4]</sup>。

换句话说：你付了 14.84 美元，实际只拿到 5 块多的服务。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260720174026239.png)

问题来了：**这些帮你"翻Q用 AI"的中转站，到底怎么运作？为什么能神不知鬼不觉地把模型换掉，你还一点都察觉不到？**

> 稳定靠谱的中转站：https://ai.ahzm.top/sign-up?aff=wanfeng

---

## 不是它想火，是你不得不用

先说说中转站为什么突然遍地都是。不是它多厉害，而是普通人想直接用海外 AI，处处是坑：

- **想用 OpenAI**：2024 年 7 月起，大陆 IP 直接被封<sup>[17]</sup>。
- **想付钱**：得要 Visa/Mastercard，还要海外账单地址验证，大多数人卡在这一步。
- **接口乱成一锅粥**：大模型从十几个暴涨到数百个，每家的接口格式、计费方式都不一样。

以前你要一个个注册账号、一个个搞信用卡、一个个适配接口，折腾到崩溃。

现在呢？接入中转站只要改两个参数，代码一行不动：

```python
client = OpenAI(
    api_key="sk-relay-xxx",          # 换成中转站给你的Key
    base_url="http://中转站地址/v1"  # 换成中转站的地址
)
```

需求有多猛？中国日均 Token 调用量，从 2024 年初的 1000 亿，飙到 2026 年 3 月的 140 万亿——涨了 1000 多倍<sup>[3]</sup>。这么大的口子，中转站自然一拥而上。

---

## 想自己搭一个？记住这 3 步

中转站听着神秘，其实用开源项目三步就能搭起来。

### 第 1 步：选一个开源底座

主流就三个，一句话记住区别：

**One API**——国内最早成熟的那个，33.7K Stars，一行 Docker 就跑，512MB 的小机器都扛得住。业内有个说法：80% 以上的商业中转站，底层都是它套了个壳<sup>[9]</sup>。

![One API](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260720140746374.png)

**New API**——One API 的加强版，多了 Midjourney/Suno 这类生成接口、TTS 语音、还有好看的数据看板。国内小团队现在多数优先选它<sup>[13]</sup>。

![New API](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260720154551010.png)

**LiteLLM**——国际上最流行的那个，45.2K Stars，Python 写的，Stripe、Netflix 都在用，成本追踪能力最强，但不太懂国内渠道。

![LiteLLM](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260720154643253.png)

### 第 2 步：一行命令跑起来

以 One API 为例，一条 Docker 命令就启动：

```bash
docker run --name one-api -d --restart always \
  -p 3000:3000 -v ./data:/data \
  justsong/one-api
```

### 第 3 步：加渠道 Key、设模型倍率

打开后台，把你的官方 Key 填进"Key 池"，再给每个模型设一个**倍率**。这个倍率就是你的差价——中转站赚钱，赚的就是这个数。

---

## 真正的坑不是贵，是你不知道喂了什么

自己搭没问题，但如果你是去买别人的中转服务，就得当心了。

中转站真正的风险，从来不是贵一点，而是**你付了钱，却不知道后台到底喂给你哪个模型**。

想想看这几种人的处境：

- **个人开发者**：省了信用卡的麻烦，但可能拿到被掉包的劣质回答，还蒙在鼓里。
- **公司团队**：你的 prompt、代码、商业文件，全都要从它的服务器过一遍。
- **整个行业**：劣币驱逐良币，认真做正规生意的反而活得难。

这不是我吓唬人。医疗问答测试里，Gemini 官方 API 准确率 83.82%，走了某些中转站直接掉到约 37%<sup>[4]</sup>。有安全研究员测了 428 款中转站，其中 9 款存在主动恶意代码注入，1 款甚至直接盗走了以太坊资产<sup>[5]</sup>。

那怎么判断一家靠不靠谱？记三条就够：

1. 有没有企业资质和 ICP 备案；
2. 能不能开正规发票、给 SLA 保障；
3. 别信不合理的超低价。要知道，17 家头部中转站里，有 15 家是个人运营、无企业注册、无备案<sup>[9]</sup>。

---

## 它凭什么能"掉包"还不被你发现？

聊到这，得讲一个背后的原理，你就明白 45.83% 这个数字为什么能长期存在。

这得从中转站怎么"接活"说起。现在几乎所有大模型的接口，都被统一成了"OpenAI 格式"：你发一个标准请求，它返回一个标准结构。

关键就在这——**返回结果里那个标注模型名的字段，是中转站自己填的，不是模型盖章签名的**。

打个比方：你点了一份"和牛套餐"，后厨端上来一盘肉，盒子上贴着"和牛"的标签。可这标签是店家自己打印的，肉到底是不是和牛，你尝不出来。

再加上计费是按 token 算的。AI 不是一个字一个字读，而是把文字切成一个个叫 **token** 的小块，按块收钱。中转站截下返回数据，数一下 token，乘以自己设的倍率，就是你的账单。

换个便宜模型，token 照数、倍率照乘，你从账单上根本看不出差别。所以从技术上讲，用户端确实"看不见"——这才是最麻烦的地方。

---

## 三个开源项目，一张表选完

如果你想动手，这张表帮你 5 秒选定：

| 维度 | One API | New API | LiteLLM |
|------|---------|---------|---------|
| Stars | 33.7K | 33.1K | 45.2K |
| 语言 | Go+JS | Go+JS | Python |
| 国产模型 | 强 | 强 | 一般 |
| 生成接口 | 无 | MJ/Suno/SD | 部分 |
| 部署难度 | 极低 | 低 | 中 |
| 适合谁 | 个人/小团队 | 小团队/代理商 | 中大团队/企业 |

一句话：国内自己玩选 New API，要极致轻量选 One API，Python 团队、要国际模型选 LiteLLM。

风口其实正在过去：Anthropic 在收紧政策，国产模型也从"被中转"变成"主动出海"<sup>[3]</sup>。纯中间商的空间会越来越小，能活下来的是有自研技术、肯合规的那批。

最后留个问题：**你用过 AI 中转站吗？有没有怀疑过自己被"掉包"？评论区聊聊你一个月在 AI 上花多少钱。**

**科技不高冷，AI 很好用。**
我是晚枫，关注我，每天带你玩一个 AI 新工具！

![AI 实战课](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

## 相关阅读

- [学会AI编程，人人都是六边形战士](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)
- [用上 OpenCode 的5 个免费大模型，省了我 200 刀 ChatGPT Plus 年费](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [论文被查出AI率40%？我用AI反降AI率，导师直接过了](https://mp.weixin.qq.com/s/z0y3wByLzfI2JRMxAT2wpQ)
- [我开通了Google广告，把申请到收款的全流程教给你](https://mp.weixin.qq.com/s/scAleVOwH6kDLPuQT4BNlA)
- [最全AI Coding Plan和Token购买攻略：大厂价格一站汇总](https://mp.weixin.qq.com/s/Bk6d9bbSh5kSEd9i9dAahw)

---

## 参考文献

1. 腾讯云开发者社区, 2026, [https://cloud.tencent.com/developer/article/2687320](https://cloud.tencent.com/developer/article/2687320)
2. 36氪, 2026, [https://eu.36kr.com/zh/p/3834566154920194](https://eu.36kr.com/zh/p/3834566154920194)
3. 界面新闻, 2026, [https://www.21jingji.com/article/20260506/herald/2c23c0fba0f85c44e02443e2d91d547.html](https://www.21jingji.com/article/20260506/herald/2c23c0fba0f85c44e02443e2d91d547.html)
4. CISPA亥姆霍兹信息安全中心, 2026, [https://www.agentupdate.ai/news/ai-model-proxy-service-integrity-challenges/](https://www.agentupdate.ai/news/ai-model-proxy-service-integrity-challenges/)
5. 每日经济新闻, 2026, [https://www.cnenergynews.cn/article/4RX6K4Ca9W0](https://www.cnenergynews.cn/article/4RX6K4Ca9W0)
6. 虎嗅, 2026, [https://www.huxiu.com/article/4863469.html](https://www.huxiu.com/article/4863469.html)
7. 百度百科, 2026, [https://baike.baidu.com/item/AI%20API%E4%B8%AD%E8%BD%AC%E7%AB%99/67786705](https://baike.baidu.com/item/AI%20API%E4%B8%AD%E8%BD%AC%E7%AB%99/67786705)
8. 百度百科, 2026, [https://baike.baidu.com/item/New%20API/67751277](https://baike.baidu.com/item/New%20API/67751277)
9. 腾讯新闻, 2026, [https://news.qq.com/rain/a/20260509A0376S00](https://news.qq.com/rain/a/20260509A0376S00)
10. CSDN, 2026, [https://chensishang.blog.csdn.net/article/details/162016761](https://chensishang.blog.csdn.net/article/details/162016761)
11. SegmentFault, 2026, [https://segmentfault.com/a/1190000047683963](https://segmentfault.com/a/1190000047683963)
12. PiStack, 2026, [https://www.pistack.xyz/posts/2026-04-30-litellm-vs-one-api-self-hosted-llm-api-gateway-guide](https://www.pistack.xyz/posts/2026-04-30-litellm-vs-one-api-self-hosted-llm-api-gateway-guide)
13. cnblogs, 2026, [https://www.cnblogs.com/aibi1/p/19655434](https://www.cnblogs.com/aibi1/p/19655434)
14. 云TTS, 2026, [https://www.yuntts.com?p=836/](https://www.yuntts.com?p=836/)
15. CSDN, 2026, [https://blog.csdn.net/lotusxyhf/article/details/162575549](https://blog.csdn.net/lotusxyhf/article/details/162575549)
16. 网易, 2026, [https://www.163.com/game/article/DK3UFFO400318PFH_mobile.html](https://www.163.com/game/article/DK3UFFO400318PFH_mobile.html)
17. 路透社, 2024, [https://www.reuters.com/technology/artificial-intelligence/openai-cut-access-tools-developers-china-other-regions-chinese-state-media-says-2024-06-25/](https://www.reuters.com/technology/artificial-intelligence/openai-cut-access-tools-developers-china-other-regions-chinese-state-media-says-2024-06-25/)

---

> ⚠️ **免责声明**：本文基于公开信息整理，引用来源均来自 2026 年公开报道与学术研究。中转站市场变化极快，文中数据截至 2026 年 7 月，重要决策请经专业人员核验。

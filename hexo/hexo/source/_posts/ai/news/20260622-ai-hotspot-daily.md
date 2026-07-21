---
title: 2026年6月22日 AI热点日报：Netflix开源Headroom省95% token，Cloudflare给Agent开临时账号
date: 2026-06-22 22:50:00
tags: ["AI热点", "AI日报", "AI资讯", "AI工具", "Codex", "Cloudflare", "Headroom", "GLM-5.2", "Devin"]
categories: ["AI资讯"]
description: "2026年6月22日 AI热点日报：Netflix开源Headroom减少95% token消耗；Cloudflare推出临时账户专为AI agent设计；Codex一句话自动跑通全功能测试；GLM-5.2登顶开源模型排行榜；Devin免费无限用GLM 5.2。"
cover: https://picsum.photos/seed/aihot-20260622/1200/630
---

<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>
</p>

<!-- more -->

大家好，我是程序员晚枫。

今天 AI 圈又热闹了。我把 AIHOT 的全量数据拉了一遍，**共 49 条**，按时间顺序给你整理好了。今天 AIHOT 官方精选为空，所以我从评分最高的条目里挑了 5 条作为今天的「重点关注」，每一条都补了我的点评和参考链接。

---

## 今日 AI 热点速览

一句话说完今天最重要的 3 件事：

1. **Netflix 工程师开源 Headroom**：在 Codex、Cursor 外面包一层本地 Agent，自动压缩上下文，**省 95% token**。
2. **Cloudflare 给 AI Agent 开临时账号**：`npx wrangler deploy --temporary` 一行部署，**免注册、项目存活 60 分钟**。
3. **Codex 一句话自动跑通全功能测试**：Greg Brockman 演示 `/goal` 指令，**Codex 自己扫功能、写用户故事、跑测试、修 bug**，全程无人。

---

## 重点关注条目 ★

> AIHOT 官方今日无精选，下面 5 条为按评分筛选的今日重点。

### 1. Netflix 工程师开源 Headroom，减少 95% token 消耗

- **发布时间**：07:21
- **分类**：AI 产品
- **AIHOT 评分**：71
- **来源**：X：阿易 AI Notes (@AYi_AInotes)
- **原文链接**：https://x.com/AYi_AInotes/status/2068836642916315344
- **AIHOT 永久页**：https://aihot.virxact.com/items/cmqocbl8p01v7sl9222hak2yx

**核心信息**：
Netflix 工程师开源了 Headroom，运行在 Codex、Cursor 等 AI 编码工具外侧，自动压缩日志、JSON、代码，**保留逻辑准确性的同时减少 95% token 消耗**。数据完全本地化，无需修改现有代码，GitHub 已获 35k 星标。

**是否值得写教程**：⭐⭐⭐⭐⭐（省 token + 免改代码，门槛极低）

**教程方向**：
《Cursor/Codex 太费 token？Netflix 开源 Headroom 帮你省 95%，一行接入》

---

### 2. Cloudflare 临时账户 for AI agents

- **发布时间**：06:01
- **分类**：AI 产品
- **AIHOT 评分**：72
- **来源**：Simon Willison 博客
- **原文链接**：https://simonwillison.net/2026/Jun/21/temporary-cloudflare-accounts
- **AIHOT 永久页**：https://aihot.virxact.com/items/cmqoe5dif0059slx6ilaeepr0

**核心信息**：
Cloudflare 推出「临时账户」功能，无需注册即可通过 `npx wrangler deploy --temporary` 部署 Workers 项目，**临时项目存活 60 分钟**。官方虽标称为 AI 智能体设计，普通用户同样适用。Simon Willison 用 GPT-5.5 xhigh 在 Codex Desktop 中实测了一轮，验证了完整部署与运行流程。

**是否值得写教程**：⭐⭐⭐⭐⭐（一行命令 + 60 分钟免审 + AI 友好）

**教程方向**：
《一行命令部署到 Cloudflare：不用注册账号，AI agent 直接跑项目》

---

### 3. Codex 自动化循环测试应用所有功能

- **发布时间**：02:23
- **分类**：技巧
- **AIHOT 评分**：69
- **来源**：X：Greg Brockman (@gdb)
- **原文链接**：https://x.com/gdb/status/2068761809318990054
- **AIHOT 永久页**：https://aihot.virxact.com/items/cmqo4mt430048sl92du5yi9ls

**核心信息**：
OpenAI 总裁 Greg Brockman 亲自演示 Codex 的「循环」自动化能力：通过一句 `/goal` 指令，Codex **自动扫描应用的每个功能**，基于代码创建用户故事与预期行为，并维护统一电子表格跟踪状态；完成后自动切换为**测试每个用户故事并记录所有错误**；接着修复所有逻辑与 UX 错误，最后再次验证用户行为。**该循环可处理数百个用户故事，全程无需人工干预**。

**是否值得写教程**：⭐⭐⭐⭐⭐（演示一次即可复现，门槛低）

**教程方向**：
《Codex 一句话自动写测试：Greg Brockman 演示的 `/goal` 循环到底怎么跑？》

---

### 4. AI 智能体记忆的七种类型：技术指南

- **发布时间**：07:12
- **分类**：技巧
- **AIHOT 评分**：58
- **来源**：MarkTechPost（RSS）
- **原文链接**：https://www.marktechpost.com/2026/06/21/the-7-types-of-agent-memory-a-technical-guide-for-ai-engineers
- **AIHOT 永久页**：https://aihot.virxact.com/items/cmqocncll0211sl9222hak2yx

**核心信息**：
LLM 默认无状态，构建智能体需要借助记忆机制。文章系统整理了 **7 种记忆类型**：工作记忆（上下文窗口）、语义记忆（用户偏好/事实）、情节记忆（过去事件/任务结果）、程序记忆（技能/工作流）、外部/检索记忆（向量数据库 / RAG）、参数记忆（嵌入模型权重的世界知识）、前瞻记忆（未来意图/计划目标）。**每种记忆对应不同时间尺度与实现方式，组合使用可构建更强的自主智能体系统**。

**是否值得写教程**：⭐⭐⭐⭐（工程向，干货密度高，可做成专题）

**教程方向**：
《AI Agent 为什么总失忆？7 种记忆机制拆解 + Python 代码示例》

---

### 5. Devin 免费无限用 GLM 5.2

- **发布时间**：00:00
- **分类**：技巧
- **AIHOT 评分**：53
- **来源**：X：Berry Xia (@berryxia)
- **原文链接**：https://x.com/berryxia/status/2068725856068153714
- **AIHOT 永久页**：https://aihot.virxact.com/items/cmqnzeyx002mdslhkbaaqj6za

**核心信息**：
通过 Devin 调用 GLM 5.2 可以**免费无限使用**。需要注意的是 Devin 内上下文限制 20 万 token，而**海外 Z·ai 版本直接给到 100 万**。同时 **Kimi 2.7 在 Devin 里也是免费的**。

**是否值得写教程**：⭐⭐⭐⭐⭐（免费 + 旗舰 + 长上下文，流量稳）

**教程方向**：
《不花钱用 GLM 5.2 + Kimi 2.7：Devin 注册到跑通全流程》

---

## 全量记录（北京时间 06-22，按时间倒序）

### 02. 09:00 · 行业（score:17）
**PixVerse 在 VidCon 展示高质量视频生成**
来源：X：PixVerse (@PixVerse_)
链接：https://x.com/PixVerse_/status/2068861536681201898

> PixVerse 参加 VidCon，在展位 #5113 展示「快速生成可投入生产的高质量视频」工作流，主打更快、更便宜的内容产出。属营销类动态，无技术增量，**跳过不写**。

---

### 03. 08:52 · 行业（score:45）
**索尼再谈 AI 游戏战略：自动化流程解放开发者，打造个性化玩家体验**
来源：IT之家（RSS）
链接：https://www.ithome.com/0/966/765.htm
AIHOT 永久页：https://aihot.virxact.com/items/cmqoc2c2h01q7sl92hlflnata

> 索尼在 2025 财年年报中专章阐述 AI 对 PlayStation 平台的作用：自动化重复工作流（品控、动画、3D 建模），并用 AI 做玩家个性化推荐。世嘉、卡普空等也在落地。**游戏向动态，与 Python 办公自动化无关，跳过。**

---

### 04. 08:38 · 行业（score:52）
**Getty Images 与 OpenAI 达成合作，授权图库内容引入 ChatGPT**
来源：IT之家（RSS）
链接：https://www.ithome.com/0/966/758.htm
AIHOT 永久页：https://aihot.virxact.com/items/cmqoc1yl101pypsl92hlflnata

> 6月22日 Getty Images 宣布和 OpenAI 达成展示合作协议，授权图库内容将出现在 ChatGPT 的搜索与发现体验中。此前 Getty 与英伟达、OpenAI 与 Shutterstock、OpenAI 与英国《金融时报》都有同类合作。**行业新闻，无教程角度，跳过。**

---

### 05. 08:35 · 技巧（score:67）
**前 Meta/Microsoft 主任工程师 kunchenguid 的 Agentic 工程工作流**
来源：X：邵猛 (@shao__meng)
链接：https://x.com/shao__meng/status/2068855273088074173
AIHOT 永久页：https://aihot.virxact.com/items/cmqoc1g4i01pjsl92hlflnata

> 45 分钟视频讲解「每天交付 40-50 个生产级 PR」的工作流。四层：① 终端中心（WezTerm+tmux+Neovim）；② 船员入职（全局 memory 精简到 27 行，项目级 memory 由 agent 自写）；③ 协作（语音输入 OpenSuperWhisper、AXI 标准——MCP 比 CLI 多耗 3 倍 token + 2 倍延迟、Lavish 交互式 HTML 工件）；④ 验证（no-mistakes 流水线在隔离 worktree 中对抗式 review + E2E 测试）。并行用 treehouse 管理 worktree，First Mate 元 agent 调度。

**是否值得写教程**：⭐⭐⭐⭐（工程方法论 + 成本对比）

---

### 06. 08:12 · 技巧（score:54）
**CDPR 联合 CEO 诺瓦科夫斯基：纯 AI 生成的游戏即将问世，但并非行业发展正道**
来源：IT之家（RSS）
链接：https://www.ithome.com/0/966/755.htm
AIHOT 永久页：https://aihot.virxact.com/items/cmqoc0lr201phsl92hlflnata

> CD Projekt Red 联合 CEO 透露，纯 AI 生成的游戏即将问世，已有 AI 工作室能一周产出 40 个原型。但他认为「纯 AI 游戏能复制但无法复刻人工开发的独特感染力，玩家能轻易识别违和感」。**游戏行业观点，与 Python 办公无关，跳过。**

---

### 07. 08:07 · 行业（score:53）
**滥用 AI 编造股市谣言，四川南充一女子被行政处罚**
来源：IT之家（RSS）
链接：https://www.ithome.com/0/966/754.htm
AIHOT 永久页：https://aihot.virxact.com/items/cmqoc0fni01pgsl92hlflnata

> 王某某用 AI 生成约 3000 字涉股市虚假文章上传今日头条，被南部县警方行政处罚。**纯监管新闻，无技术切入点，跳过。**

---

### 08. 08:06 · 技巧（score:57）
**Hermes Bible 整合官方文档与社区工作流**
来源：X：阿易 AI Notes (@AYi_AInotes)
链接：https://x.com/AYi_AInotes/status/2068848124806979612
AIHOT 永久页：https://aihot.virxact.com/items/cmqoc098l01pfsl92hlflnata

> Hermes Bible 把 Hermes Agent 169 页官方文档整合一体，提炼出 **24 个可直接抄的真实工作流**（如 Jira 到 PR 自动过渡），支持 ⌘K 即时搜索，社区可分享工作流并展示个人资料页。解决「官方文档分散、优质工作流沉没在 X 和 Discord」的问题。

**是否值得写教程**：⭐⭐⭐（可作为补充资源）

---

### 09. 07:45 · 技巧（score:47）
**欧洲 2031 场景警告：缺乏自主 AI 能力将面临经济与战略脆弱**
来源：X：Rohan Paul (@rohanpaul_ai)
链接：https://x.com/rohanpaul_ai/status/2068842808493092924
AIHOT 永久页：https://aihot.virxact.com/items/cmqobxd5o01p9sl92hlflnata

> 欧洲 2031 场景分析警告：不建自主前沿 AI 能力将面临经济和战略脆弱。欧洲误读 DeepSeek R1，以为小团队可替代算力；美国 AI 算力 17.3GW vs 欧洲 1.4GW；欧洲人才流向硅谷。**地缘政治观点，非技术教程角度，跳过。**

---

### 10. 07:30 · 行业（score:31）
**IT早报 0622：马斯克行权薪酬账面收益 1160 亿美元，黑鲨社区关闭，刘强东谈快递员转型**
来源：IT之家（RSS）
链接：https://www.ithome.com/0/966/746.htm
AIHOT 永久页：https://aihot.virxact.com/items/cmqobvnmj01p4sl92hlflnata

> 马斯克全额行权 2018 年特斯拉 CEO 薪酬方案，账面收益 1160 亿美元；黑鲨社区停止访问；刘强东称未来不需要快递员，将 70 万蓝领送培训；苹果折叠屏 iPhone 已小批量供货。**聚合早报，无技术细节，跳过。**

---

### 11. 07:24 · 模型（score:62）
**Apertus：面向主权人工智能的开放式基础模型发布**
来源：Hacker News 热门（buzzing.cc 中文翻译）
链接：https://apertvs.ai/
AIHOT 永久页：https://aihot.virxact.com/items/cmqobt3n401ozsl92hlflnata

> 瑞士 AI 倡议（EPFL、苏黎世联邦理工、CSCS）推出完全开放的基础模型 Apertus，**公开训练数据、代码、权重、方法和对齐原则**，符合欧盟 AI 法案，支持 **1000+ 种语言**，提供 **8B 和 70B 参数版本**。Apertus Mini 含 16 个小模型。技术报告已被 ACL 2026 接收。

**是否值得写教程**：⭐⭐⭐（合规场景需要时可写）

---

### 12. 07:21 · 产品（score:71）
**Netflix 工程师开源工具 Headroom，减少 95% token 消耗**
来源：X：阿易 AI Notes (@AYi_AInotes)
链接：https://x.com/AYi_AInotes/status/2068836642916315344
AIHOT 永久页：https://aihot.virxact.com/items/cmqocbl8p01v7sl9222hak2yx

> 👉 详见「重点关注 1」。

---

### 13. 07:12 · 技巧（score:58）
**AI 智能体记忆的七种类型：技术指南**
来源：MarkTechPost（RSS）
链接：https://www.marktechpost.com/2026/06/21/the-7-types-of-agent-memory-a-technical-guide-for-ai-engineers
AIHOT 永久页：https://aihot.virxact.com/items/cmqocncll0211sl9222hak2yx

> 👉 详见「重点关注 4」。

---

### 14. 07:12 · 行业（score:54）
**微软将默认向符合条件 Win11 设备自动安装 Microsoft 365 Copilot**
来源：IT之家（RSS）
链接：https://www.ithome.com/0/966/741.htm
AIHOT 永久页：https://aihot.virxact.com/items/cmqobr0vh01ofsl92hlflnata

> 微软将在 6 月中旬至 7 月中旬，向搭载 Microsoft 365 桌面客户端的合规 Windows 设备**默认自动安装** Copilot 独立客户端。欧洲经济区设备免推送。**企业向新闻，跳过。**

---

### 15. 07:08 · 技巧（score:63）
**LLM 让自建软件成本降低，但购买仍存在"可行区域"**
来源：Hacker News 热门（buzzing.cc 中文翻译）
链接：https://brandur.org/minimum-viable-unit
AIHOT 永久页：https://aihot.virxact.com/items/cmqobq33n01odsl92hlflnata

> 文章算了一笔账：年薪 $200k 的工程师团队花 2 周用 Claude 自建 Jira 替代品后，**还需每月 2 小时维护，需 37 个月才能收回月费 $400 的购买成本**。但 Salesforce 这种 $500/月/座、50 座共 $25k/月的产品，足够雇 1.5 个全职工程师自建。**所以「购买 vs 自建」存在一个可行区域**。

**是否值得写教程**：⭐⭐⭐（可作为决策参考文章）

---

### 16. 07:00 · 行业（score:45）
**三星电子向全球员工部署 ChatGPT Enterprise 和 Codex**
来源：OpenAI：官网动态（RSS）
链接：https://openai.com/index/samsung-electronics-chatgpt-codex-deployment
AIHOT 永久页：https://aihot.virxact.com/items/cmqobptbl01obsl92hlflnata

> 三星电子向全球员工推出 ChatGPT Enterprise 和 Codex，是 OpenAI 目前规模最大的企业级 AI 部署之一。**企业新闻，无教程角度，跳过。**

---

### 17. 06:57 · 技巧（score:58）
**Elvis Saravia：从精细提示转向循环+口述+验证器的新范式**
来源：X：Elvis Saravia (@omarsar0, DAIR.AI)
链接：https://x.com/omarsar0/status/2068830591642997111
AIHOT 永久页：https://aihot.virxact.com/items/cmqobpikz01o7sl92hlflnata

> DAIR.AI 创始人 Elvis 称他如今**很少直接向智能体写提示词，而是依靠循环让智能体自主完成大部分工作**。他转而花更多时间**编写验证器**。2026 年 6 月起应放弃手动编辑提示词，改用语音听写 10 分钟，把碎片、警示、示例直接灌给模型。

**是否值得写教程**：⭐⭐⭐⭐（方法论启发）

---

### 18. 06:56 · 技巧（score:51）
**马斯克：5 年内数字智能超人类，人形机器人达亿级**
来源：X：cb_doge (@cb_doge)
链接：https://x.com/cb_doge/status/2068830509673882082
AIHOT 永久页：https://aihot.virxact.com/items/cmqobpgsg01o6sl92hlflnata

> 马斯克预测 4-5 年内 AI 可能超越所有人类智能的总和；5 年内人形机器人至少 1 亿台，可能 10 亿台。**个人观点/预测，无技术内容，跳过。**

---

### 19. 06:46 · 产品（score:52）
**安巴尼将 Jio 网络打造成 AI 智能体试验场**
来源：X：Rohan Paul (@rohanpaul_ai)
链接：https://x.com/rohanpaul_ai/status/2068827812304441698
AIHOT 永久页：https://aihot.virxact.com/items/cmqoboq1f01nxsl92hlflnata

> TechCrunch：安巴尼正把 Jio 拥有 **5 亿用户的电信网络**转变成印度最大的日常 AI 智能体试验场。Jio Call Agent 将嵌入电话通话中，征得同意后监听、转录语音、总结对话，并触发行动（打车、订餐）。

**是否值得写教程**：⭐⭐（行业动态，无需教程）

---

### 20. 06:01 · 产品（score:72）
**Cloudflare 临时账户 for AI agents**
来源：Simon Willison 博客
链接：https://simonwillison.net/2026/Jun/21/temporary-cloudflare-accounts
AIHOT 永久页：https://aihot.virxact.com/items/cmqoe5dif0059slx6ilaeepr0

> 👉 详见「重点关注 2」。

---

### 21. 04:23 · 产品（score:9）
**Codex 用法重置：囤积还是随意使用？**
来源：X：Tibo (@thsottiaux)
链接：https://x.com/thsottiaux/status/2068792010715324444
AIHOT 永久页：https://aihot.virxact.com/items/cmqo8xoeu015wsl92klv97bpa

> 既然 Codex 现在可以存储用法重置，**你是囤积还是随意用？** 互动型推文，无实质信息，跳过。

---

### 22. 04:09 · 技巧（score:62）
**AI 数据中心金融正成为独立资产类别，杠杆贷款涌入基建热潮**
来源：X：Rohan Paul (@rohanpaul_ai)
链接：https://x.com/rohanpaul_ai/status/2068788294381457766
AIHOT 永久页：https://aihot.virxact.com/items/cmqo7ytwb013esl92klv97bpa

> 摩根士丹利开始向数据中心开发商推销**杠杆贷款市场**。AI 相关债务发行 2026 年或超 5700 亿美元，截至 5 月底已达 2360 亿，是去年同期的 4 倍。NYU 教授 Damodaran 对比互联网泡沫指出 AI 资本支出规模史无前例，且**大量由债务而非股权融资**。**金融/经济观点，非技术教程，跳过。**

---

### 23. 04:07 · 行业（score:79）
**Mythos 数小时内攻破 NSA 全系统，下一代已出**
来源：X：Kim (@kimmonismus)
链接：https://x.com/kimmonismus/status/2068787804516053385
AIHOT 永久页：https://aihot.virxact.com/items/cmqo7xmr4013bsl92klv97bpa

> 据《经济学人》报道，6 月 11 日 AI 模型 Mythos 据称**在数小时内攻破了 NSA 和网络司令部的几乎所有机密系统**。参议院情报委员会副主席 Mark Warner 转述 NSA 局长 Joshua Rudd 的话确认此事。主推文还透露 Mythos 下一轮迭代已经到来。

---

### 24. 03:59 · 技巧（score:53）
**LeCun 警告 AI 泡沫即将破裂风险**
来源：X：Kim (@kimmonismus)
链接：https://x.com/kimmonismus/status/2068785890353160226
AIHOT 永久页：https://aihot.virxact.com/items/cmqo7t8xz0138sl92klv97bpa

> LeCun：「AI 服务价格在上涨，但运营成本下降速度远不够快。**这些公司都在亏损，大多数用户的使用是由投资者资助的。这种情况不可能持续太久。**」**个人观点，无教程角度，跳过。**

---

### 25. 03:04 · 行业（score:50）
**Anthropic Mythos 更强版本完成训练**
来源：X：Kim (@kimmonismus)
链接：https://x.com/kimmonismus/status/2068772173636853783
AIHOT 永久页：https://aihot.virxact.com/items/cmqo6pdze00zxsl92hlflnata

> Anthropic 的 Mythos 更强版本已结束训练，**距 4 月 7 日 Mythos-1 发布仅两个月**。名称（Mythos 5.1 或 Mythos 6）及是否公开尚不明确。**Anthropic 迭代速度惊人，但无 API 可用，跳过。**

---

### 26. 02:56 · 技巧（score:63）
**Nano Banana Pro 照片中物体异常放大**
来源：X：fofr (@fofrAI)
链接：https://x.com/fofrAI/status/2068770007614419382
AIHOT 永久页：https://aihot.virxact.com/items/cmqo5l9in0092sl92hlflnata

> Nano Banana Pro 演示：「一张照片中某个本该正常存在的物体变得过大，其他一切正常，场景逼真。」**图像生成演示，与 Python 办公无关，跳过。**

---

### 27. 02:53 · 技巧（score:50）
**ASML CEO 警告欧洲 AI 硬件落后**
来源：X：Rohan Paul (@rohanpaul_ai)
链接：https://x.com/rohanpaul_ai/status/2068769168086925321
AIHOT 永久页：https://aihot.virxact.com/items/cmqo5jwb60090sl92hlflnata

> ASML CEO：美国购买了全球 80% 的先进芯片。**硬件/地缘观点，跳过。**

---

### 28. 02:44 · 技巧（score:45）
**Perplexity CEO：模型不再是产品**
来源：X：Rohan Paul (@rohanpaul_ai)
链接：https://x.com/rohanpaul_ai/status/2068767074663690502
AIHOT 永久页：https://aihot.virxact.com/items/cmqo5gfd0008qsl92hlflnata

> Aravind Srinivas：「模型不再是产品。Codex、Perplexity Computer、Claude Code——**全都是编排系统**。它用一个模型，再配上 agent harness。**什么是 agent harness？Agent 循环运行的规则。**」

**是否值得写教程**：⭐⭐⭐⭐（可拆解 agent harness 设计模式）

---

### 29. 02:25 · 产品（score:57）
**LOCALUS-v1 美国法律数据集发布**
来源：X：Rohan Paul (@rohanpaul_ai)
链接：https://x.com/rohanpaul_ai/status/2068762202795041250
AIHOT 永久页：https://aihot.virxact.com/items/cmqo4o2o4005wsl92v6sd2u4l

> 研究人员首次用 AI 收集、OCR、处理并构建了**全美每一条法律**的数据库，共 **220 万条法律**，已上传 Hugging Face（LocalLaws/LOCUS-v1）。**法律数据集，与 Python 办公无关，跳过。**

---

### 30. 02:23 · 技巧（score:69）
**Codex 自动化循环测试应用所有功能**
来源：X：Greg Brockman (@gdb)
链接：https://x.com/gdb/status/2068761809318990054
AIHOT 永久页：https://aihot.virxact.com/items/cmqo4mt430048sl92du5yi9ls

> 👉 详见「重点关注 3」。

---

### 31. 02:18 · 产品（score:30）
**Cursor 新技能 /automate：自动化也自动化**
来源：X：Testing Catalog (@testingcatalog)
链接：https://x.com/testingcatalog/status/2068760597546615139
AIHOT 永久页：https://aihot.virxact.com/items/cmqo4kws20047sl92du5yi9ls

> Cursor 获得新 `/automate` 技能：「过去几年 AI 让自动化变得极其简单，现在**连自动化本身都被自动化了**。」**短动态，配合 Codex 循环测试一起解读，跳过单独写。**

---

### 32. 01:57 · 行业（score:51）
**乌克兰 50 万小时无人机影像用于 AI 训练**
来源：X：Rohan Paul (@rohanpaul_ai)
链接：https://x.com/rohanpaul_ai/status/2068755263960867267
AIHOT 永久页：https://aihot.virxact.com/items/cmqo3p9ll03fxslhkqxklkfdh

> 50 万小时真实战斗无人机全动态视频（烟雾、天气、地形、阴影、热信号）被打包用于 AI 模型训练。**军事数据，无教程角度，跳过。**

---

### 33. 01:56 · 行业（score:43）
**Anthropic Mythos 新版本完成训练，更强但发布计划未明**
来源：X：Kim (@kimmonismus)
链接：https://x.com/kimmonismus/status/2068754830110212411
AIHOT 永久页：https://aihot.virxact.com/items/cmqo38pgj03exslhkqxklkfdh

> 同 #25，Anthropic Mythos 更强版本已完成训练。**跳过。**

---

### 34. 01:47 · 行业（score:65）
**Anthropic Mythos 数小时攻破 NSA 几乎所有机密系统**
来源：X：Rohan Paul (@rohanpaul_ai)
链接：https://x.com/rohanpaul_ai/status/2068752800759386532
AIHOT 永久页：https://aihot.virxact.com/items/cmqo3lgz903leslhk02bhxkdl

> 同 #23，《经济学人》报道 Mythos 数小时攻破 NSA 系统。**军事/政府安全新闻，跳过。**

---

### 35. 01:30 · 技巧（score:56）
**GLM-5.2 登顶开源模型排行榜**
来源：X：Elvis Saravia (@omarsar0, DAIR.AI)
链接：https://x.com/omarsar0/status/2068748378054222173
AIHOT 永久页：https://aihot.virxact.com/items/cmqo2gq4m039jslhktf2hdupt

> GLM-5.2 表现令人印象深刻，是**前沿的开放权重模型**。

**是否值得写教程**：⭐⭐⭐⭐（实测对比）

---

### 36. 01:29 · 技巧（score:20）
**Grok Imagine 生成小猫跳舞视频**
来源：X：Elon Musk (@elonmusk, xAI)
链接：https://x.com/elonmusk/status/2068748080623604004
AIHOT 永久页：https://aihot.virxact.com/items/cmqo2gm0p039hslhktf2hdupt

> Grok Imagine 文生视频示例：「戴着连指手套的小猫开始跳舞唱歌『我们是戴着连指手套的小猫』。」**娱乐类演示，跳过。**

---

### 37. 01:27 · 技巧（score:44）
**Linus：原始 Vibe Coder，零成本无限上下文**
来源：X：Rohan Paul (@rohanpaul_ai)
链接：https://x.com/rohanpaul_ai/status/2068747614045319359
AIHOT 永久页：https://aihot.virxact.com/items/cmqo2fs8m039fslhktf2hdupt

> 调侃推：Linus 只需在邮件列表发一条愤怒邮件，**全球数千工程师就免费实现**。**零 token、零 API、无限上下文（30 多年内核知识）**。OpenAI/Anthropic 试图用 AI 复制 Linus 从 1991 年起靠人做的事，但 Linus 的 agents 不产生模型幻觉且完全免费。

---

### 38. 01:16 · 技巧（score:43）
**GLM-5.2 迎来 DeepSeek R1 时刻**
来源：X：Yuchen Jin (@Yuchenj_UW)
链接：https://x.com/Yuchenj_UW/status/2068744828259852546
AIHOT 永久页：https://aihot.virxact.com/items/cmqo2kwxz03dvslhkiskb490t

> 「GLM-5.2 正迎来它的 DeepSeek R1 时刻。从未想过一个开源模型能这么快跻身编程模型前三。」

---

### 39. 01:10 · 论文（score:47）
**《Scalable Evaluation for AI Agents》提出 Human-on-the-Bridge 评估方法**
来源：X：Elvis Saravia (@omarsar0, DAIR.AI)
链接：https://x.com/omarsar0/status/2068743256079556989
AIHOT 永久页：https://aihot.virxact.com/items/cmqo2i4uq039rslhktf2hdupt

> 论文《Scalable Evaluation for AI Agents》提出 **Human-on-the-Bridge 评估方法**：将人类判断前置到可复用评估资产中，专家在上游策划评估智慧，而非在测试循环中逐一审查输出。AI 智能体需作为**行为系统**评估，因其多轮推理、调用工具、维护上下文、遵循策略并在不确定性下行动。

**是否值得写教程**：⭐⭐⭐（偏学术，适合高级读者）

---

### 40. 00:53 · 技巧（score:14）
**Testing Catalog 预告 AI 更新与实时评论**
来源：X：Testing Catalog (@testingcatalog)
链接：https://x.com/testingcatalog/status/2068739051755053118
AIHOT 永久页：https://aihot.virxact.com/items/cmqo1tww4031nslhk72uui71l

> 「更多 AI 更新 👀 更快的 AI 更新 👀 实时评论 👀 你会从哪里得到它们？」**预告类动态，无实质内容，跳过。**

---

### 41. 00:44 · 行业（score:16）
**Codex app 改进意见与不满反馈**
来源：X：Tibo (@thsottiaux)
链接：https://x.com/thsottiaux/status/2068736857312198928
AIHOT 永久页：https://aihot.virxact.com/items/cmqo1f4eb030jslhk72uui71l

> Codex 团队收集用户对 Codex app 的改进意见。**互动型，跳过。**

---

### 42. 00:32 · 技巧（score:55）
**Cognite 联合创始人 Geir Engdahl：工业 AI 失败主因在工厂运营而非模型层**
来源：X：Kim (@kimmonismus)
链接：https://x.com/kimmonismus/status/2068733691808084259
AIHOT 永久页：https://aihot.virxact.com/items/cmqo15lt5030bslhk72uui71l

> Cognite CTO 指出工业 AI 失败的根源**并非模型层，而是工厂现场运营**。许多惊艳的 AI 试点无法在实际运营中存活，因为缺乏真正上下文——**当错误可能带来危险时尤为关键**。他预测到 2028 年未采用 AI 驱动流程优化的工业企业将面临严峻挑战。

---

### 43. 00:14 · 技巧（score:64）
**Ethan Mollick：Agentic 工具的「软件脑」限制与知识工作扩展难题**
来源：X：Ethan Mollick (@emollick)
链接：https://x.com/emollick/status/2068729258176819253
AIHOT 永久页：https://aihot.virxact.com/items/cmqo0yf9m02zdslhkbaaqj6za

> Mollick 指出 Codex/Cowork/Code 等 Agentic 工具本质上是**「软件脑」设计，只重最终代码**，而多数知识工作的过程（研究、探索、原型分支等）与结果同样重要。长时运行模型 Fable 也因专注交付最终产品而难以用于深度知识工作。

**是否值得写教程**：⭐⭐⭐（可作为思考框架）

---

### 44. 00:00 · 技巧（score:53）
**Devin 免费无限用 GLM 5.2**
来源：X：Berry Xia (@berryxia)
链接：https://x.com/berryxia/status/2068725856068153714
AIHOT 永久页：https://aihot.virxact.com/items/cmqnzeyx002mdslhkbaaqj6za

> 👉 详见「重点关注 5」。

---

## 今日 AI 圈观察

1. **降本从「换模型」转向「前置压缩」**：Headroom 的流行证明——**改输入比换模型更省**。这给所有自建 agent 工具链的人一个启示：在你的 pipeline 入口加一个 token 压缩层，比砍模型费用更立竿见影。
2. **「为 AI 重新设计基础设施」开始落地**：Cloudflare 临时账户、Cursor `/automate`、Codex `/goal` 循环、Anthropic Sonnet 5 传闻——**所有动作都在为「agent 是第一公民」让路**。未来 6 个月我们会看到更多「原本为人设计的 SaaS 被 agent-native 版本替代」。
3. **国产开源模型迎出海拐点**：GLM-5.2 连续被 Vercel CEO、DAIR.AI、Yuchen Jin 三方背书，Devin 把 GLM 5.2 做成「免费无限」选项——**国产模型从「自嗨」到「被海外平台主动集成」是质变**。
4. **「写提示词」这个工种正在消失**：DAIR.AI Elvis、Saravia 都在呼吁放弃精细提示词，**转去写验证器和口述意图**。这意味着：**LLM 应用工程师的核心技能从「prompt engineering」变成「verifier engineering」**。
5. **模型不再是产品，agent harness 才是**：Perplexity CEO 把话说穿了。Codex、Claude Code、Perplexity Computer 本质都是「模型 + harness」。**未来竞争不在底层模型，而在 harness 设计**。

---

## 最值得写教程的 2 条

### 1. Netflix Headroom（95% token 压缩）
**推荐理由**：省 token 是所有人关心的话题，**GitHub 35k 星**说明已经有用户基础。**「免改代码、一行接入」**的门槛极低，适合所有用 Cursor/Codex 的读者。  
**教程方向**：《Cursor/Codex 太费 token？Netflix 开源 Headroom 帮你省 95%，一行接入》  
**标题候选**：
- 《Netflix 工程师开源省 token 神器：装上它，Cursor 月费砍一半》
- 《AI 编程工具太贵？Netflix 这个 35k 星的开源项目省 95%》  
**参考资源**：
- Headroom GitHub 仓库（35k 星）
- 阿易 AI Notes 推文：https://x.com/AYi_AInotes/status/2068836642916315344
- 你上次的 Cursor API 账单数据

### 2. Devin 免费无限用 GLM 5.2
**推荐理由**：免费 + 旗舰模型 + 长上下文（Z·ai 海外版 100 万 token），**三条叠加是「流量炸弹」**。对没订阅 ChatGPT/Claude 的读者来说是「真香」级别的实用信息。  
**教程方向**：《不花钱用 GLM 5.2 + Kimi 2.7：Devin 注册到跑通全流程》  
**标题候选**：
- 《不花钱用 GLM 5.2？Devin 这个渠道很多人不知道》
- 《免费 + 100 万上下文：Devin 集成 GLM 5.2 实测》  
**参考资源**：
- Berry Xia 推文：https://x.com/berryxia/status/2068725856068153714
- Devin 官网注册地址
- Z·ai 海外版 API 文档
- GLM-5.2 开源仓库

---

## 深度阅读 & 工具资源

| 资源 | 链接 | 说明 |
|------|------|------|
| 前一天日报 | https://www.python4office.cn/ai/news/20260621-ai-hotspot-daily/ | 昨天热点回看 |
| Headroom 开源仓库 | https://github.com/netflix/headroom | Netflix 95% token 压缩工具 |
| Cloudflare 临时账户文档 | https://developers.cloudflare.com/workers/runtime-api/cli-commands/#temporary | wrangler deploy --temporary 用法 |
| AIHOT 数据源 | https://aihot.virxact.com | 原始热点聚合站 |
| 晚枫 AI 工具评测系列 | https://www.python4office.cn/ai/ | 站内历史文章回链 |
| GLM-5.2 开源仓库 | https://github.com/THUDM/GLM-5 | 智谱开源旗舰模型 |

---

## 写在最后

今天 AI 圈的热闹集中在三件事：**降本前置压缩、Agent-native 基础设施、国产开源模型出海**。

建议优先写 Headroom，因为它**门槛低（装上就能用）、效果猛（95%）、受众广（所有用 Cursor/Codex 的人）**，是典型的「流量 + 干货」组合。Devin + GLM 5.2 是流量保底，免费 + 旗舰模型 + 长上下文的组合天然传播力强。

**科技不高冷，AI 很好用。**

我是晚枫，关注我，带你一起玩 AI！

---

## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲](https://pan.quark.cn/s/8f7886f79569)
- 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://mp.weixin.qq.com/s/VXmJjQwsQlY-2IHjA3OAYA)
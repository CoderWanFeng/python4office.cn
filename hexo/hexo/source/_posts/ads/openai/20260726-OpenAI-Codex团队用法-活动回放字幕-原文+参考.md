---
title: 资料｜OpenAI 活动回放字幕中英双语对照：OpenAI 团队怎么用 Codex 做非编程工作
date: 2026-07-26 22:00:00
tags: [参考资料, OpenAI, Codex, 字幕, 活动回放]
categories: [参考资料]
cover: https://cdn.pixabay.com/photo/2018/09/27/09/22/artificial-intelligence-3706562_1280.jpg
description: 2026-07-14 OpenAI Forum 活动《Inside OpenAI》完整字幕中英对照，作为「不会写代码的人用 AI 搭了个网站」一文的素材底稿。
published: false
---

> **来源**：OpenAI Forum — Event Replay: Inside OpenAI — How OpenAI Teams use Codex to Do More
> **视频链接**：https://forum.openai.com/home/videos/event-replay-inside-openai-how-openai-teams-use-codex-to-do-more-2026-07-14
> **活动日期**：2026-07-14｜**发布日期**：2026-07-15｜**浏览量**：556
> **时长**：约 43 分钟
> **说明**：以下为视频完整字幕（Transcript）的中英双语对照，按时间戳整理。英文为视频原声转录，中文为对照翻译。
> **状态**：本文件作为成品文《不会写代码的人用 AI 搭了个网站》的原始素材，设置 `published: false`，不会生成博文页。

---

## 一、视频简介

这是一场 OpenAI Forum 活动，探讨了**智能体 AI（agentic AI）如何改变编程之外的工作**。OpenAI 首席经济学家 Ronnie Chatterji 和研究员 Drew Johnston 分享了 Codex 采用如何改变工作流的研究发现——让人们能委派更长的任务、并行运行多条工作流、跨越传统岗位边界。随后 OpenAI 各团队现场演示了智能体如何在数据科学、产品设计和销售等真实工作中提供支持：从自动化 KPI 报告、构建交互式原型，到管理周期性市场推广流程。

核心主张：**可复用的 Skills（技能）、连通的工作工具、清晰的组织支持**，能帮助团队把重复工作流变成可扩展的系统。建议观众从一个"雄心勃勃或令人头疼的工作问题"入手，给智能体充分的上下文，再尝试哪些可以被委派或自动化。

---

## 二、演讲者

| 姓名 | 身份 |
|------|------|
| **Drew Johnston** | OpenAI 技术员工（ECON 经济研究团队，哈佛经济学博士） |
| **Ronnie Chatterji** | OpenAI 首席经济学家（首位，杜克大学教授，前白宫 CHIPS 协调员） |
| **Allie Sandza Wood** | OpenAI 执行制片人（主持，前 CBS News 政治流媒体监制） |
| **Ken Claassen** | OpenAI 规模化入站/出站团队负责人（GTM 组织） |
| **Melanie Appleby** | OpenAI 数据科学员工（让智能体更擅长数据工作） |
| **Blaine Billingsley** | OpenAI 设计员工（UX 设计师） |

---

## 三、完整字幕

**[00:00:00]（Allie，主持）**
Hi everyone, thank you so much for joining us. Today's discussion is focused on how agents are transforming work, particularly work that is outside of coding.
> 大家好，非常感谢大家参与。今天的讨论聚焦于智能体如何改变工作，尤其是**编程之外**的工作。

> 周四我们发布了 ChatGPT Work，把 Codex 的智能体能力从编程扩展到跨应用和文件工作。Codex 仍是我们专门的编程智能体，但两者现在都活在 ChatGPT 桌面应用里。

**[00:00:43]（Allie）**
So we're going to start today with OpenAI's Chief Economist, Ronnie Chatterji, and Drew Johnston...
> 我们先请 OpenAI 首席经济学家 Ronnie Chatterji 和经济研究团队的技术员工 Drew Johnston，聊聊智能体如何在 OpenAI 内外部改变工作，然后各团队做简短演示，最后一起回答提问。

**[00:01:13]（Ronnie）**
Thanks so much, Allie, and great to be here with Drew Johnston from the ECON research team. Welcome to OpenAI Forum.
> 谢谢 Allie，很高兴和 ECON 研究团队的 Drew Johnston 一起。欢迎来到 OpenAI Forum。

**[00:01:22]（Drew）**
Hey, Ronnie. Great to be here. I figured I'd start people off just with the origin story. Why did we write this paper?
> 嘿 Ronnie。我想从起源故事讲起——我们为什么写这篇论文？为什么 Codex 和智能体 AI 现在这么有意思？

**[00:01:40]（Ronnie）**
This paper was in part inspired by my own experiences. I came on board at OpenAI back in January, so six months ago... Switching jobs is always a pretty big change... But this was a much bigger change.
> 这篇论文部分受我个人经历启发。我今年 1 月加入 OpenAI，也就是 6 个月前。换工作本来就是大变化，但这次更大——我一边处理医保、401k 这些行政事务，一边经历日常工作组成的彻底转变，因为我从"智能体 AI 不普及"的环境，进入了"非常普及"的环境。

**[00:02:30]（Ronnie）**
Coming onto this job, the composition of what I did changed pretty much overnight. I went from writing and testing all of my own code by hand... to working at OpenAI where agentic tools can help with all of that automatically. In the past couple of months, I haven't written any code by hand.
> 上岗后，我做的事几乎一夜之间变了。我从上一份工作"手写并测试自己的全部代码"，变成在 OpenAI 用智能体工具自动完成这一切。过去几个月，我**一行代码都没手写过**，智能体工具还帮我搭测试、找分析所需的数据。

**[00:03:17]（Drew）**
As researchers we're almost like participant observers... we're actually going through this revolution at work on our own team. You've been on the vanguard within our team in terms of getting us all to use Codex in new ways.
> 作为研究者，我们几乎是"参与式观察者"——亲身经历这场工作革命。你（Ronnie）在团队里带头用新方式使用 Codex。我们也研究 Codex 对经济整体的影响，很多灵感来自每天遇到的用例。

**[00:03:51]（Ronnie）**
I want you to talk about my favorite part of the paper — the different samples we study Codex adoption. It's not just consumers or enterprise. It has a special twist.
> 说说我最喜欢的部分——我们研究 Codex 采用的"不同样本"。不只是消费者或企业，还有个特别的角度。

**[00:04:08]（Drew）**
In the paper, one thing novel is we're able to contrast how people use Codex both inside OpenAI and outside of it. We look at two distinct groups outside OpenAI: organizational users (account supplied by someone else, like a business license) and individual accounts (free or self-purchased Pro plan).
> 论文的新颖之处在于，我们能对比 OpenAI **内部**和**外部**的人如何使用 Codex。外部有两个截然不同的人群：组织用户（账号由公司提供，比如企业许可）和个人账号（免费或自己买的 Pro）。

**[00:04:41]（Drew）**
We look at how Codex usage differs across those three account types. There are pretty profound differences.
> 我们观察 Codex 在这三类账号中的使用差异，差异非常显著。

**[00:05:00]（Drew）**
Within OpenAI, pretty much everybody is already using agentic tooling. More than 95% of people at the company in the past month have used Codex. That includes research and engineering, as well as legal, HR, and comms.
> 在 OpenAI 内部，几乎所有人都已用上智能体工具。过去一个月，**超过 95% 的员工用过 Codex**——包括研发，也包括法务、HR、传播团队。

**[00:05:19]（Drew）**
Within OpenAI, people have really made the transition from conversational AI to much more capable agentic tools. In other populations, this transition is still a lot earlier.
> OpenAI 内部已经从"对话式 AI"真正过渡到能力更强的智能体工具。外部群体还早得多。

**[00:05:30]（Drew）**
The paper was finalized back in early June... only about one in five or one in six people with an organizational account was using Codex in a given month. Most people still interact with AI through traditional conversational harnesses.
> 论文数据截止到 6 月初：外部组织账号中，每月只有约 1/5 到 1/6 的人在用 Codex，大多数人仍通过传统对话式工具接触 AI。

**[00:05:50]（Drew）**
Among individual accounts, this was even less widespread; less than 1% of people were making use of Codex and agentic technologies.
> 个人账号中更不普及——**不到 1%** 的人在用 Codex 和智能体技术。

**[00:06:18]（Drew）**
Why? Within OpenAI there's widespread enthusiasm, team champions promoting usage, leadership encouragement for experimentation, dense community of experts, and spillovers from coworkers talking about workflows.
> 为什么？OpenAI 内部有广泛热情、团队里有"推广者"分享工作流知识、领导鼓励试验、密集的专家社群，以及同事间交流带来的溢出效应。

**[00:07:05]（Ronnie）**
When I look at this chart, I think we're living in the future. Today we hit the 7 million milestone — we're continuing to gain users. What's exciting is watching the ramp in other enterprises.
> 看这张图，我觉得我们活在未来。今天我们达到 700 万（用户）里程碑。令人兴奋的是看其他企业如何爬坡。

**[00:07:32]（Ronnie）**
The non-technical roles chart went viral on Twitter. Research and engineering were saturated by end of last year, but quickly all other functions — finance, recruiting, legal — caught up. This closing of the gap is remarkable; it's basically just one quarter.
> 那张"非技术角色"图表在 Twitter 上疯传。研发岗去年底就饱和了，但财务、招聘、法务等其他职能迅速追上。差距缩小之快令人惊叹——基本就一个季度。

**[00:08:18]（Drew）**
Codex initially was seen as a coding tool... People realized how impactful this can be outside the coding domain. Within later-adopting fields like recruiting or legal, convergence has been faster — in April, entire departments switched from conversational to agentic tooling in two or three weeks.
> Codex 最初被视为编程工具……人们发现它在编程域外同样有冲击力。在招聘、法务等后期采用领域，收敛反而更快——4 月时，整个部门在两三周内从对话式切换到智能体工具。

**[00:09:14]（Drew）**
The functionality has been there for a long time. Once in place, it just takes a champion, willingness, and a team willing to rethink workflows and formalize tacit knowledge. Then things transition rapidly.
> 功能早就具备。一旦到位，只需要一个推广者、意愿，以及团队愿意重思工作流、把隐性知识显性化。之后转变就很快。

**[00:09:47]（Ronnie）**
We've talked about a capability gap for a long time. AI capabilities advance fast. The big question: why aren't more people using them that way? At OpenAI we see our own version of that gap closing — from chatbots to reasoning to agentic work, where it's not just asking for an answer, it's delegating work.
> 我们谈"能力差距"很久了。AI 能力飞快进步，大问题是：为什么更多人没这么用？在 OpenAI，我们亲眼看到这个差距在缩小——从聊天机器人，到推理，到智能体工作：不只是要答案，而是**委派工作**。

**[00:10:53]（Ronnie）**
I wanted to ask about those less technical folks. They can use agentic AI to do things they were already doing, OR to do new things that weren't part of their job. Those are two different forces.
> 我想问非技术人群。他们用智能体做本来就在做的工作，或做原本不属于岗位的新工作——这是两种不同的力量。

**[00:11:24]（Drew）**
Alongside the paper we released statistics about job titles and the prevalent tasks within Codex usage for each. Developers use it most; software engineering is still the biggest workflow. But we see examples blurring job boundaries — people doing things that previously required large cross-company collaboration or were totally outside their skillset.
> 我们发布了各职位的 Codex 使用统计。开发者用得最多，软件工程仍是最大工作流。但我们看到模糊岗位边界的例子——人们做以前需要跨部门大协作、或完全超出技能的事。

**[00:12:21]（Drew）**
A cool example on our team just last week. We put out a call for the "OpenAI Research Exchange" — external researchers come in-house to propose a project. We got ~500 applications, dropped into one enormous spreadsheet. Reading multi-page applications in one spreadsheet cell was painful for our team.
> 上周团队有个酷例子。我们发起"OpenAI 研究交流计划"——外部研究者来内部提案。收到约 500 份申请，全进了一个巨大表格。在表格单元格里读几页长的申请，团队很痛苦。

**[00:13:10]（Drew）**
Our chief of staff — amazing, capable, but not technical, no programming experience — used Codex to turn that spreadsheet into an interactive website. It presents all proposal details inline, links to attached documents, lets people submit comments and ratings via a web form, and populates those back into the spreadsheet.
> 我们的**幕僚长**——很厉害，但非技术、无编程经验——用 Codex 把表格变成**交互式网站**：内联展示所有提案细节、链接附件、让人在网页表单里评论评分，并回填到表格。

**[00:13:43]（Drew）**
This is from someone whose title is Chief of Staff with no programming experience. Normal job boundaries are being blurred, and work that wouldn't have gotten done is getting done.
> 这人官方头衔是幕僚长、毫无编程经验。常规岗位边界正在模糊，以前做不成的工作现在做成了。

**[00:14:25]（Ronnie）**
It's the lump of labor fallacy we've discussed — there isn't an upper limit on the amount of work you can do. She built this website quickly, we sped up review, gave better reviews. Without Codex, creating it wouldn't have been possible.
> 这就是我们聊过的"劳动总量恒定谬误"——你能做的工作没有上限。她快速建了网站，加速评审、提升质量。没有 Codex，这网站根本建不出来。

**[00:14:54]（Drew）**
Websites very quickly, then you run through applications efficiently, people get better reviews, the team moves with pace. When she added "website development" to her task list, it's a window into how AI will be used — expand people's agency, help teams do more.
> 快速建站，高效审申请，评审更好，团队提速。当她把"建网站"加进任务清单，这扇窗让我们看到 AI 将如何被使用——扩展人的能动性，帮团队做更多。

**[00:15:28]（Ronnie）**
One of the most interesting things about agents is parallelization — doing multiple things at once — and building repeated, scalable tasks and automations. We'll see this with the skills feature.
> 智能体最有趣的是**并行化**（同时做多件事）和构建可重复、可扩展的任务与自动化。后面 Skills 功能会体现。

**[00:15:53]（Drew）**
In Codex you can have multiple threads running simultaneously, keeping context contained per thread. Among consumers and organizational users, a good share run multiple threads concurrently in a week. What surprised me: within OpenAI this is supercharged. About 10% of users peak at more than 10 agents running simultaneously in a given week.
> Codex 里可多线并行、各线程上下文隔离。消费者和组织用户中，不少人每周会并发多线。令我惊讶的是 OpenAI 内部被"超频"——约 **10% 的用户某周峰值同时跑超过 10 个智能体**。

**[00:16:52]（Drew）**
This is powerful for me: kick off an agent for data analysis, another to clean up code, another to check my paper for typos — simultaneously. On paper I'm an individual contributor who manages no one, but I often feel like a manager. Thinking like a manager — dividing work across threads — is a valuable skill.
> 这对我很有用：同时启动一个做数据分析、一个清理代码、一个查论文拼写。我头衔是个人贡献者、不管理任何人，但常觉得自己像经理。像经理一样把工作分到各线程，是宝贵技能。

**[00:18:12]（Drew）**
We're interested in how users use Skills within Codex to codify team workflows — share knowledge without formal instruction. E.g., your team has a specific way to format the weekly rollup before sending to executives. Skills give repeatable, shareable instructions to Codex about how to perform a workflow.
> 我们关注用户如何用 Codex 的 **Skills** 把团队工作流"法典化"——无需正式培训就能分享知识。比如团队给高管发周报有特定格式，Skills 给 Codex 可复用、可分享的指令。

**[00:19:01]（Drew）**
Skills document workflows in something shared freely among team members, making work automatic. Huge increase in Skills usage since the beginning of the year, both inside OpenAI and externally.
> Skills 把工作流写成可在成员间自由分享的文档，让工作自动执行。今年以来 Skills 使用量激增，内部外部皆然。

**[00:19:52]（Ronnie）**
Taken together: we're moving to an era where instead of just asking questions, you delegate work — in multiple streams at a time — and increasingly longer tasks. Some lead users delegate more than a workday's worth of agent work. Then you make them routine daily tasks. Working in parallel and systematizing — that's the new operating system for work.
> 综合来看：我们进入一个时代——不只是问问题，而是**委派工作**，且多线并行、任务越来越长。有些领先用户委派的量超过一整个工作日。然后变成日常例行任务。并行 + 系统化，就是工作的新操作系统。

**[00:20:55]（Ronnie）**
What's your favorite way to use Codex? You're the lead author.
> 你最喜欢怎么用 Codex？你是主要作者。

**[00:21:03]（Drew）**
I use Codex to write all of our one-on-ones. Before our weekly meeting, I tell it: scan my calendar, scan my Slack, scan our task tool, and summarize everything I worked on this past week. Then scan the coming week. Doing this by hand was super painful. Having Codex create a one-pager and send it to Ronnie automatically has been a huge boon.
> 我用 Codex 写我们所有的**一对一纪要**。周会前我让它扫描日历、Slack、任务工具，总结上周工作，再总结下周安排。手工做超级痛苦。让 Codex 自动生成一页纸发给 Ronnie，生产力大提升。

**[00:22:34]（Melanie，数据科学）**
I'm a data scientist. I'll demo a core data workflow: a KPI metrics update. Like most data teams, we review important metrics weekly — what changed, why, and what to do next.
> 我是数据科学家。我演示核心数据工作流：KPI 指标更新。像多数数据团队，我们每周复盘重要指标——变了什么、为什么、下一步做什么。

**[00:23:05]（Melanie）**
My basic approach: connect Codex to as much working context as possible. Under the plugins tab I have many plugins installed — data warehouse, BI tool, experimentation platform, Google Drive, Slack. Once Codex has access, I don't start by picking a tool or writing a query. I start with the outcome I want.
> 基本方法：把 Codex 连到尽可能多的工作上下文。插件标签下我装了数据仓库、BI 工具、实验平台、Google Drive、Slack。连上后，我不用先选工具或写查询，而是从**想要的结果**出发。

**[00:23:39]（Melanie）**
Producing a trustworthy KPI update can take a data scientist one or two days. Codex lets me approach it as one end-to-end workflow.
> 出一份可信的 KPI 更新，数据科学家要 1-2 天。Codex 让我把它当作一个端到端工作流。

**[00:24:12]（Melanie）**
I prompted Codex to produce this week's KPI update — a deliberately outcome-level request, asking it to coordinate the workflow, not just help write queries.
> 我让 Codex 产出本周 KPI 更新——刻意用"结果级"请求，让它协调工作流，而不只是帮写查询。

**[00:24:25]（Melanie）**
I used a custom skill called "Northstar KPI Context" our team created. It captures things we shouldn't explain weekly: which metrics matter, how defined, where trusted datasets live, useful dimensions, how the update should be structured. Think of the skill as reusable institutional knowledge.
> 我用了团队创建的自定义技能"Northstar KPI Context"。它固化了不该每周重复解释的东西：哪些指标重要、如何定义、可信数据在哪、有用维度、更新结构。技能就是**可复用的机构知识**。

**[00:24:54]（Melanie）**
I also use the Data Analytics plugin — a recipe for producing a high-quality metrics update: validating data, comparing week-over-week, identifying largest contributors, creating visualizations.
> 还用了数据分析插件——产出高质量指标更新的"配方"：校验数据、周环比对比、找出最大变动贡献者、生成可视化。

**[00:25:27]（Melanie）**
Because experimentation and product contexts are connected, Codex goes beyond saying the metric moved — it answers "why." It used Databricks to query, Google Drive connector to find experiment results, incorporating both.
> 因为连了实验和产品上下文，Codex 不只说指标动了，还回答"为什么"。它用 Databricks 查数、用 Google Drive 连接器找实验结果，并纳入更新。

**[00:25:55]（Melanie）**
The update leads with an executive summary and current state, shows important movements and likely drivers, includes charts and supporting evidence so someone can inspect and go deep.
> 更新以执行摘要和现状开头，展示重要变动和可能驱动因素，含图表和佐证，让人可审查、深挖。

**[00:26:36]（Melanie）**
This isn't putting decisions on autopilot. My role shifted from assembling the update to reviewing and extending it — checking data correctness, whether the explanation matches team knowledge, whether Codex missed context.
> 这不是让决策自动驾驶。我的角色从"组装更新"变成"审查并延展"——检查数据是否正确、解释是否符合团队认知、Codex 是否漏了上下文。

**[00:27:02]（Melanie）**
It flagged European revenue down significantly; I asked it to investigate further using the same context. The first output isn't the end — it's a strong starting point for better follow-up questions.
> 它标出欧洲收入显著下降，我让它用同一上下文深挖。首次输出不是终点，而是更好追问的起点。

**[00:27:23]（Melanie）**
Once working well, I schedule it via automation. Every Thursday morning an automation runs against fresh data, so when I start my day, the first draft of the deck and Slack update is ready, with anomalies flagged. Automation handles repeatable work; I stay responsible for interpretation.
> 跑顺后我把它排成自动化。每周四早自动化跑新鲜数据，我开工时初稿和 Slack 更新已就绪，异常被标记。自动化处理重复工作，我负责解读。

**[00:28:16]（Blaine，设计）**
Hi, I'm Blaine, a UX designer. Designers use Codex daily to get ideas into tangible form faster. We add polish directly into production and submit pull requests. We collect feedback on autopilot with scheduled tasks, generate Sigma mocks in bulk. We recently released a "Product Design" plugin.
> 我是 UX 设计师 Blaine。设计师每天用 Codex 更快把想法变实体。我们直接在生产代码加打磨、提交 PR。用定时任务自动收集反馈、批量生成 mock。最近发布了"产品设计"插件。

**[00:29:02]（Blaine）**
When I have a new idea, I go straight to Codex. I had a vague idea for a calendar experience in ChatGPT, asked Codex to explore a first pass. Under the hood we gave Codex our design system canon and screenshots of every production flow, so it knows what makes ChatGPT feel like ChatGPT.
> 有新想法直接找 Codex。我对 ChatGPT 里的日历功能只有模糊想法，让 Codex 先探一轮。底层我们给了 Codex 设计系统规范和每个生产流程的截图，所以它懂 ChatGPT 的"味"。

**[00:29:32]（Blaine）**
It generated rough mocks — timeline concept, standard calendar, inboxy style. What I love: it inspires other ideas. I ask it to mock more; once happy, prototype it interactive and fully fleshed out, using production code and Figma system.
> 它生成粗略 mock——时间线、标准日历、收件箱风。我喜欢它激发更多想法。满意后让它做成可交互完整原型，用生产代码和 Figma 系统。

**[00:30:34]（Blaine）**
I turn on annotation, add thoughts/critiques directly to the page, fire them into a queue, and Codex fixes in real time. This gets me into the actual work of designing — what I want it to do, what feels good — without worrying about Figma bases or design system lookups.
> 我开注释功能，把想法/批评直接标在页面上，丢进队列，Codex 实时修复。这让我进入真正的设计工作——想要什么、什么感觉好——而不用管 Figma 底版或查设计系统。

**[00:32:24]（Blaine）**
When done, Codex makes sharing easy — publish the website, or make a movie/GIF for Slack. I get feedback fast without the rote design-system management.
> 做完后 Codex 让分享很容易——发布网站，或为 Slack 做视频/GIF。我快速拿到反馈，免去设计系统的机械管理。

**[00:33:11]（Ken，销售/GTM）**
Hey, I'm Ken, I lead our SDR team in go-to-market. I use Codex all the time, especially as a leader. My team is large; typically I'd need a data analyst, systems person, and ops person. For the last year I've basically done it solo because of Codex.
> 我是 Ken，带 GTM 的 SDR 团队。我大量用 Codex，尤其作为leader。团队大，通常我需要数据分析师、系统人员和运维。过去一年我基本 Solo 搞定，靠 Codex。

**[00:33:48]（Ken）**
My Codex has access to all main systems — Salesforce, Outreach, Slack, GONG. Full access makes a huge difference for high-level reporting and data pulling.
> 我的 Codex 能访问所有主系统——Salesforce、Outreach、Slack、GONG。完全访问对高层报告和取数差别巨大。

**[00:34:02]（Ken）**
An automation runs every Monday ~9am — by the time I exit my 9am meetings, a full report awaits with fresh data from Salesforce, GONG, Outreach: team performance at scale, plus anything going wrong or trending weird. It can even dive into troubling things itself.
> 每周一早 9 点左右跑一个自动化——我开完 9 点会，一份完整报告已在等：含 Salesforce/GONG/Outreach 新鲜数据、团队规模化表现、异常或怪趋势。它甚至能自己深挖问题。

**[00:34:46]（Ken）**
Before this era, people like me needed others to support them, relied on Salesforce reports — cumbersome to build, and if underlying data changes you must update the report. My Codex is self-adaptive; it checks latest info and adapts. It generates charts, pie charts — I screenshot them into docs.
> 以前我这类人需要别人支持，靠 Salesforce 报告——难建，底层数据一变就得改。我的 Codex 自适应，查最新信息并调整，还能生成图表，我截图进文档。

**[00:35:28]（Ken）**
This screenshot shows how it connects to my Outreach instance using the Outreach skill. It knows our tone of voice, the nuance of making sequences. My Codex makes a whole sequence from scratch in ~5 minutes that's effectively perfect. Any error, we update the skill so it never happens again.
> 这张图显示它用 Outreach 技能连我的实例。它懂我们的语调和做序列的细微差别。我的 Codex 约 5 分钟从零做出一整套基本完美的邮件序列。出错就更新技能，永不再犯。

**[00:36:05]（Ken）**
Lead assignments: we get signals like job changes (teams adopting Codex, hiring for AI) — those are leads. I use Codex to find latest signals, assign to reps in Salesforce, enroll them in Outreach sequences — manual in the past, now automated.
> 线索分配：我们收到如职位变动（团队采用 Codex、招 AI 岗）等信号——这些是线索。我用 Codex 找最新信号、在 Salesforce 分给销售、纳入 Outreach 序列——过去手动，现在自动化。

**[00:36:42]（Ken）**
Anything I do frequently becomes an automation. "Make this an automation" — it does it perfectly every time. I usually just update the model to the latest, like from 5.5 to 5.6.
> 任何频繁做的事都变成自动化。"做个自动化"——每次都完美。我通常只把模型更新到最新，比如 5.5 换 5.6。

**[00:37:15]（Ken）**
A critical automation for leadership: instead of a newsletter or PowerPoint (slow to generate), Codex uses latest Salesforce data to build a website every week, updating Fridays — an interactive experience. We track who views it and what they interact with most, to adapt. It's the frontier of technology.
> 给领导层的关键自动化：不用通讯稿或 PPT（生成慢），Codex 用最新 Salesforce 数据每周建网站、周五更新——交互体验。我们追踪谁看、互动最多的是什么，据此调整。这是技术前沿。

**[00:37:51]（Ken）**
Auditing: normally manual. Codex looks through 30-50 outbound sequences, balances against our internal standards, recommends which underperform, repeat, or could be optimized.
> 审计：通常手动。Codex 扫 30-50 个外联序列，对照内部标准，建议哪些表现差、重复或可优化。

**[00:38:30]（Ken）**
I'll say: take the best performing sequence, what's good about it, make a skill for this. Now whenever you make a sequence, it knows the characteristics of our best outbound messaging. Every business thing I need to know is a skill. Most I made myself — our BPO function is a 2,400-word skill. Anytime something changes, I update the skill.
> 我会说：拿最佳序列，好在哪，做个技能。以后做序列它就知道最佳外联信息的特征。我业务里要知道的每件事都是个技能。大多我自己写——BPO 职能是个 2400 词的技能。有变化就更新技能。

**[00:39:26]（Allie，主持收尾）**
Thank you all. We're a bit over time, so one question for everyone: what's one idea you hope people leave with today?
> 谢谢各位。超时了，问大家一个问题：希望观众今天带走的一个想法是什么？

**[00:39:49]（Drew）**
These things move fast; the technology for agentic AI to change workflows exists outside OpenAI too. The limiting factor is organizational buy-in and internal effort, not the technology itself. Once the ball rolls, things move fast.
> 这些发展很快；智能体 AI 改变工作流的技术在 OpenAI 之外也存在。限制因素是对组织的认同和内部投入，而非技术本身。一旦启动，就很快。

**[00:40:31]（Melanie）**
If you're not sure what to do or how to start, just ask. Ask the most moonshot question, then find failure points and solve them. Or: what's the most annoying task of your job? Solve it, automate it.
> 不确定怎么做或如何开始，就问。问最"登月"的问题，再找失败点解决。或者：你工作最烦的任务是什么？解决它、自动化它。

**[00:41:03]（Blaine）**
How do I do this thing? I need this solved. How do I make a video of this prototype? Codex can help you figure out how to use Codex. That mindset change was a huge unlock.
> 我怎么做这事？我需要它解决。我怎么给原型做视频？Codex 能帮你搞懂怎么用 Codex。这种心态转变是巨大解锁。

**[00:41:28]（Ronnie）**
The data shows AI is changing how we work. Second, organizations will change how they get work done — build scalable skills, do more at once. That process will lead to big economic changes.
> 数据显示 AI 在改变工作方式。其次，组织将改变做事方式——建可扩展技能、同时做更多。这过程将带来经济大变化。

**[00:41:55]（Ken）**
Codex performs well at base level, and even better the more context you give it — about yourself, your work, what good and bad look like. More info = like a well-onboarded colleague. If you tell a colleague "go, I won't tell you what good looks like," they won't do their best.
> Codex 基础就表现好，给的上下文越多越好——关于你自己、工作、好坏标准。信息越多，越像入职良好的同事。若你只说"去干，我不说好坏标准"，同事也做不好。

**[00:42:22]（Allie）**
Thank you all. Keep an eye out for more forums — we'll announce two events: one on AI and scientific advances, another on how AI helps doctors diagnose rare pediatric diseases. Stay tuned to the forum newsletter and OpenAI Global Affairs LinkedIn.
> 谢谢大家。留意更多论坛——我们将宣布两场：AI 与科学进展、AI 如何帮医生诊断罕见儿科疾病。关注论坛通讯和 LinkedIn。

---

## 四、关键数据速览（来自视频）

| 数据点 | 数值 |
|--------|------|
| OpenAI 内部 Codex 月活 | > 95%（含研发、法务、HR、传播） |
| 外部组织账号月活（2026-06 数据） | 约 1/5 ~ 1/6 |
| 外部个人账号月活 | < 1% |
| OpenAI 内部峰值并发智能体 | 约 10% 用户某周同时跑 > 10 个 |
| ChatGPT 用户里程碑 | 700 万（视频当日宣布） |
| Ken 的 BPO 技能长度 | 2,400 词 |
| 数据科学家传统 KPI 更新耗时 | 1-2 天 → Codex 端到端自动化 |

## 五、可直接用于创作的选题角度

1. **"不会写代码的幕僚长，用 AI 建了个网站"** —— 非技术岗如何用智能体模糊岗位边界（强故事性）
2. **"一个人 = 一个团队"** —— OpenAI 销售 leader 如何用 Codex Solo 搞定分析+运维+运营
3. **Skills 才是护城河** —— 把团队隐性知识"法典化"是可复用的机构资产
4. **并行化 = 新操作系统** —— 同时跑 10 个智能体的"经理思维"
5. **给 AI 上下文 = 带新人入职** —— Ken 的比喻可直接引用
6. **从问答案到委派工作** —— 聊天→推理→智能体的三代演进
7. **能力差距 vs 采用差距** —— 技术已就绪，卡在组织认同（适合做趋势文）

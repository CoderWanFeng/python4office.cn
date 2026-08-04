---
title: OpenAI 官方：Codex 9 个高效习惯，用对才不焦虑
date: 2026-08-04 15:00:00
tags: [公众号文章, Codex, 最佳实践, OpenAI, 官方文档翻译, AI编程, Agent]
categories: [公众号文章, AI工具实战]
cover: https://cdn.pixabay.com/photo/2024/05/19/05/59/ai-generated-8771581_1280.jpg
description: "OpenAI 官方《Codex 最佳实践》中文翻译：把 Codex 当成可长期配置、持续培养的「队友」——从上下文、AGENTS.md、MCP、技能到定时任务的完整实践指南。"
---

# 最佳实践（Best practices）

> 原文：https://learn.chatgpt.com/guides/best-practices
> 适用对象：Codex 及各类编程智能体（coding agent）

如果你刚接触 Codex 或编程智能体，这份指南能帮你更快拿到更好的结果。它覆盖了让 Codex 在 [CLI](https://learn.chatgpt.com/docs/codex/cli)、[IDE 扩展](https://learn.chatgpt.com/docs/codex/ide) 和 [ChatGPT 桌面端](https://learn.chatgpt.com/docs/app) 上更高效的那些核心习惯——从提示词与规划，到验证、MCP、技能（skills）和定时任务。

把 Codex 用好的关键，是别把它当成一次性助手，而是当成一个可以长期配置、持续培养的「队友」。

一个有用的心智模型：先为任务准备好正确的上下文，用 `AGENTS.md` 沉淀长期有效的指引，把 Codex 配置成贴合你工作流的样子，通过 MCP 接入外部系统，把重复性的工作固化成技能，再把稳定的工作流自动化。

## 第一步：上下文与提示词

即便你的提示词不够完美，Codex 本身已经强到能直接派上用场。你常常只需把难题丢给它、几乎不做额外配置，就能拿到不错的结果。清晰的 [提示词（prompting）](https://learn.chatgpt.com/docs/prompting) 不是拿到价值的必要条件，但它确实能让结果更可靠——尤其是在大型代码库或高风险任务里。

如果你在一个庞大或复杂的仓库里工作，最大的提升点就是：给 Codex 提供「针对这个任务的正确上下文」，以及「你希望它做什么」的清晰结构。

一个稳妥的提示词默认应包含四部分：

- **目标（Goal）：** 你打算改动或构建什么？
- **上下文（Context）：** 哪些文件、文件夹、文档、示例或报错与这个任务相关？你可以用 `@` 提及特定文件作为上下文。
- **约束（Constraints）：** Codex 应该遵循哪些标准、架构、安全要求和约定？
- **完成标准（Done when）：** 任务完成前什么必须为真？比如测试通过、行为改变、或某个 bug 不再复现。

这能帮助 Codex 保持范围聚焦、减少假设，产出更易审查的工作成果。

根据任务难度选择推理强度（reasoning level），并测试哪种设置最适合你的工作流。不同用户、不同任务，最优设置各不相同。

- **Low（低）：** 用于更快、范围明确的任务
- **Medium / High（中 / 高）：** 用于更复杂的改动或调试
- **Extra High（超高）：** 用于漫长、自主性强、重度推理的任务

想要更快地提供上下文，可以在 ChatGPT 桌面端里用语音听写功能，直接说出你希望 Codex 做什么，而不是打字。

## 复杂任务先规划

如果任务很复杂、含糊不清，或者很难描述清楚，就让 Codex 在动手写代码之前先规划。

以下几种方式都很好用：

**使用 Plan 模式：** 对大多数用户来说，这是最简单也最有效的方式。Plan 模式让 Codex 先收集上下文、提出澄清问题，并在动手前形成更完善的计划。用 `/plan` 或 `Shift`+`Tab` 切换。

**让 Codex 反过来采访你：** 如果你对想要的东西有一个模糊的概念，但说不清楚，就让 Codex 先向你提问。告诉它去挑战你的假设，在写代码之前把模糊的想法变成具体的方案。

**使用 PLANS.md 模板：** 对于更进阶的工作流，你可以配置 Codex 在执行周期较长或多步骤的任务时，遵循一个 `PLANS.md` 或执行计划模板。详见 [执行计划指南](https://learn.chatgpt.com/cookbook/articles/codex_exec_plans)。

## 用 `AGENTS.md` 让指引可复用

一旦某种提示词模式奏效，下一步就是别再手动重复它。这就是 [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) 的用武之地。

可以把 `AGENTS.md` 理解为给智能体看的开放式 README。它会自动加载进上下文，也是沉淀「你和你团队希望 Codex 在这个仓库里怎么干活」的最佳位置。

一份好的 `AGENTS.md` 应覆盖：

- 仓库布局与重要目录
- 如何运行项目
- 构建、测试和 lint 命令
- 工程规范与 PR 预期
- 约束与「禁止事项」规则
- 「完成」的定义，以及如何验证工作成果

CLI 里的 `/init` 斜杠命令，是在当前目录快速生成一份 `AGENTS.md` 起手的命令。它是很好的起点，但你应当编辑生成的结果，使其贴合你团队真实的构建、测试、审查和发布代码的流程。

你可以在不同层级创建 `AGENTS.md`：放在 `~/.codex` 的全局 `AGENTS.md` 用于个人默认配置，仓库级文件用于共享标准，子目录里更具体的文件用于局部规则。如果存在离当前目录更近的更具体文件，则以该文件的指引为准。

保持实用。一份简短而准确的 `AGENTS.md`，胜过塞满模糊规则的长文件。先从基础开始，只有在发现重复的失误后，才追加新规则。

如果 `AGENTS.md` 开始变得过大，保持主文件精简，把规划、代码审查、架构等任务相关的具体说明，用单独的 markdown 文件来引用。

当 Codex 犯了两次同样的错误时，让它做一次复盘（retrospective），并更新 `AGENTS.md`。指引应始终基于真实痛点、保持实用。

## 配置 Codex 以保持一致性

配置是让 Codex 在不同会话和不同界面上行为更一致的主要手段之一。例如，你可以为模型选择、推理强度、沙箱模式、审批策略、配置文件和 MCP 设置定义默认值。

一个不错的起始模式是：

- 把个人默认值放在 `~/.codex/config.toml`（ChatGPT 桌面端中 **Settings > Configuration > Open config.toml**）
- 把仓库特定的行为放在 `.codex/config.toml`
- 命令行覆盖只用于一次性场景（如果你用 CLI 的话）

[`config.toml`](https://learn.chatgpt.com/docs/config-file/config-basic) 是你定义持久化偏好的地方，比如 MCP 服务器、多智能体设置和功能开关。特定配置文件的覆盖项，存放在独立的 `$CODEX_HOME/profile-name.config.toml` 文件里。

Codex 自带运行级沙箱（operating level sandboxing），有两个关键开关可由你控制。审批模式（approval mode）决定 Codex 何时请求你的许可来运行命令；沙箱模式（sandbox mode）决定 Codex 能否在目录中读写、以及智能体能访问哪些文件。

如果你刚接触编程智能体，请从默认权限起步。默认情况下保持审批和沙箱收紧，只有在需求明确后，才为可信仓库或特定工作流放宽权限。

注意，CLI、IDE 扩展和 ChatGPT 桌面端共享同一套配置层。更多内容见 [示例配置](https://learn.chatgpt.com/docs/config-file/config-sample) 页面。

尽早为你的真实环境配置 Codex。很多「质量问题」其实是「配置问题」——比如工作目录错误、缺少写入权限、模型默认值不对，或缺少工具与连接器。

## 用测试和审查提升可靠性

不要止步于「让 Codex 改个东西」。该让它建测试时就建测试、跑相关的检查、确认结果，并在你接受之前审查工作成果。

Codex 可以帮你跑完这一整套循环——但前提是它知道「好」长什么样。这个指引可以来自提示词，也可以来自 `AGENTS.md`。

它可以包括：

- 为改动编写或更新测试
- 运行正确的测试套件
- 检查 lint、格式化或类型检查
- 确认最终行为符合需求
- 审查 diff，排查 bug、回归和风险模式

在 ChatGPT 桌面端里可以打开 diff 面板，直接在本地 [审查改动](https://learn.chatgpt.com/docs/code-review?surface=app)。点击某一行即可给出反馈，该反馈会作为上下文喂给 Codex 的下一轮。

这里很有用的一个选项是斜杠命令 `/review`，它提供几种审查代码的方式：

- 基于基础分支做 PR 风格的审查
- 审查未提交的改动
- 审查某次提交
- 使用自定义的审查指令

如果你和团队有一份 `code_review.md` 文件，并从 `AGENTS.md` 里引用它，Codex 在审查时也能遵循这份指引。对于希望审查行为跨仓库、跨贡献者保持一致的团队，这是一个很强的模式。

Codex 不该只是生成代码。在正确的指令下，它还能帮你 **测试它、检查它、审查它**。

如果你使用 GitHub Cloud，可以配置 Codex 来为你的 PR 做 [代码审查](https://learn.chatgpt.com/docs/third-party/github)。在 OpenAI 内部，Codex 审查了 100% 的 PR。你可以开启自动审查，或让 Codex 在你 @Codex 时被动响应审查。

## 用 MCP 接入外部上下文

当 Codex 需要的上下文存在于仓库之外时，就用 MCP。它让 Codex 接入你已经在用的工具与系统，你就不用反复把实时信息复制粘贴进提示词。

[模型上下文协议（Model Context Protocol，MCP）](https://learn.chatgpt.com/docs/extend/mcp) 是一个把 Codex 连接到外部工具和系统的开放标准。

在以下情况使用 MCP：

- 所需上下文存在于仓库之外
- 数据频繁变化
- 你希望 Codex 使用某个工具，而不是依赖粘贴的指令
- 你需要在多个用户或项目间建立可复用的集成

Codex 同时支持 STDIO 和 Streamable HTTP 服务器，并支持 OAuth。

在 ChatGPT 桌面端，进入 **Settings > MCP servers** 即可查看自定义和推荐的服务器。很多时候，Codex 可以帮你安装所需的服务器——你只需要开口问。你也可以在 CLI 里用 `codex mcp add` 命令，通过名称、URL 等细节添加你的自定义服务器。

只在工具能打通真实工作流时才添加。不要一开始就接入你使用的每一个工具。先从一两个能明显消除你经常做的人工循环的工具开始，再逐步扩展。

## 把可重复的工作固化成技能

一旦某个工作流变得可重复，就别再依赖长提示词或反复的来回拉扯。用一个 [技能（skill）](https://learn.chatgpt.com/docs/build-skills) 把指令、上下文和支持逻辑打包进一份 `SKILL.md` 文件，让 Codex 始终如一地应用。技能在 CLI、IDE 扩展和 ChatGPT 桌面端都通用。

让每个技能只聚焦于一件事。从 2 到 3 个具体用例起步，定义清晰的输入和输出，并写好描述——说清这个技能做什么、何时使用它，包括用户真正会说的那些触发短语。

不要一开始就试图覆盖所有边界情况。先从一个有代表性的任务做起，把它打磨好，再把这个工作流固化成技能并持续改进。只有当脚本或额外资源确实能提升可靠性时，才把它们包含进来。

一个好经验：如果你一直在复用同一段提示词，或一直在纠正同一个工作流，那它大概就该变成一个技能了。

技能在以下这类重复性工作里尤其有用：

- 日志分流（log triage）
- 发布说明草稿
- 对照清单做 PR 审查
- 迁移规划
- 遥测或事故摘要
- 标准调试流程

`$skill-creator` 技能是搭建第一个技能版本的最佳起点。在迭代期间，先让它保持本地。当准备好广泛分享时，再把它打包成 [插件（plugin）](https://developers.openai.com/plugins/build/plugins)。技能描述是最重要的一部分之一——它应当说清技能做什么、何时使用。

个人技能存放在 `$HOME/.agents/skills`，团队共享技能可以签入仓库内的 `.agents/skills`。这对新成员 onboarding 尤其有帮助。

## 用定时任务处理重复工作

一旦某个工作流稳定了，你就可以让 Codex 在后台替你定时运行它。在 ChatGPT 桌面端，[定时任务（scheduled tasks）](https://learn.chatgpt.com/docs/automations) 让你为周期性工作选择项目、提示词、节奏和执行环境。

从 **Scheduled** 页面创建一个定时任务。选择项目、提示词、节奏，以及任务是在专用的 Git worktree 中运行还是在你的本地环境中运行。提示词可以调用技能。了解更多关于 [Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees) 的内容。

合适的候选任务包括：

- 总结最近的提交
- 扫描可能的 bug
- 起草发布说明
- 检查 CI 失败
- 生成站会（standup）摘要
- 按计划运行可复用的分析工作流

一个有用的原则：技能定义「方法」，定时任务定义「节奏」。如果一个工作流还需要大量人工干预，就先把它变成技能。一旦它变得可预测，再把它排期就能省时间。

把定时任务用于反思和维护，而不只是执行。回顾最近的对话、总结反复出现的痛点，并随着时间持续改进提示词、指令或工作流配置。

## 管理长周期对话

对话会随时间累积上下文、决策和行动，因此管理好它们对质量影响很大。

ChatGPT 桌面端允许你置顶（pin）对话并创建 worktree。如果你用 CLI，这些 [斜杠命令](https://learn.chatgpt.com/docs/developer-commands?surface=cli) 特别有用：

- `/experimental`：切换实验性功能，并写入你的 `config.toml`
- `/resume`：恢复一个已保存的对话
- `/fork`：在保留原始记录的前提下，创建一个新对话
- `/compact`：当对话变长、你想要一份早期上下文的摘要版本时使用。Codex 也会自动压缩对话
- `/agent`：当你在并行运行多个智能体、想在活动线程间切换时使用
- `/theme`：选择语法高亮主题
- `/apps`：在 Codex 里直接使用 ChatGPT 应用
- `/status`：检查当前会话状态

一个连贯的工作单元，对应一个对话。如果工作仍是同一问题的一部分，留在同一个对话里往往更好，因为它保留了推理轨迹。只有当工作真正分叉时，才 fork。

用 Codex 的 [子智能体（subagent）](https://learn.chatgpt.com/docs/agent-configuration/subagents) 工作流，把边界清晰的工作从主线程中卸载出去。让主智能体聚焦核心问题，把探索、测试或分流类任务交给子智能体。

## 常见错误

初次使用 Codex 时，有几个常见错误要避免：

- 把长期有效的规则堆进提示词，而不是移入 `AGENTS.md` 或技能
- 不告诉智能体如何最好地运行构建和测试命令，导致它看不到自己的工作成果
- 在多步骤和复杂任务上跳过规划
- 在还不了解工作流之前，就给 Codex 你电脑的完全权限
- 不使用 Git worktree，就在同一批文件上跑实时任务
- 在任务手动执行还不稳时，就把它排期成定时任务
- 把 Codex 当成需要一步步盯着的东西，而不是让它和你的工作并行
- 整个项目只用一条对话，而不是「一个连贯结果对应一条对话」。这会让上下文臃肿，长期结果变差

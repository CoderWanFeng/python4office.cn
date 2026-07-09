---
title: OpenCode 入门指南，从零基础到实战，看这一篇就够了！
date: 2026-07-09 12:00:00
tags:
  - OpenCode
  - AI编程
  - 入门教程
  - popdf
  - Claude Code
  - 平替
categories: AI工具评测
cover: https://images.unsplash.com/photo-1517694712202-14dd9538aa97?q=80&w=1200&auto=format&fit=crop
---

# OpenCode 入门指南，从零基础到实战，看这一篇就够了！

> 本文以 [popdf](https://github.com/CoderWanFeng/popdf) 作为实战案例贯穿全文，把抽象的 AI 编码代理概念落到一个真实可运行的 Python 项目里。

OpenCode 是一个**开源的 AI 编码代理**。它可以帮你读代码、看懂陌生的仓库、做代码评审、排查问题，并通过 TUI 终端界面、Web 界面、IDE 扩展、CLI、SDK、ACP 协议、以及 GitHub/GitLab Action 这几个入口为你工作。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260709203908424.png)

本文中提到的 OpenCode，指的是当前版本的 [anomalyco/opencode](https://github.com/anomalyco/opencode)。它和许多 AI 编码工具一样都装在本地，但有三点显著不同：

1. **完全开源**：所有代码公开可审计，你拥有所有生成内容的全部权利，没有任何许可限制。
2. **模型无关**：支持 75+ LLM 提供商，包括 Claude、GPT、Gemini、MiniMax、Kimi、GLM、Qwen、DeepSeek、Moonshot 等。
3. **真正本地**：默认不在任何服务器存储你的代码或上下文数据，所有处理在本地完成，或通过直接 API 调用发到你信任的 AI 提供商。

> ⚠️ 唯一需要注意的可选功能是 `/share`（分享对话链接）。如果启用了，对话会被发送到 opencode 的 CDN。**企业用户建议在 `opencode.json` 里把它关掉**：`"share": "disabled"`。

文中截图和终端示例来自 OpenCode 的官方页面或官方 GitHub 仓库，实际界面可能随版本变化。

## 这份指南写给谁

这份指南面向**从未用过 OpenCode 的人**，也包括目前还不太会写代码的读者。你不需要先把所有 AI 智能体相关概念都搞懂，只需要先记住一句话：

> **OpenCode 不只是一个 AI 聊天窗口。它可以进入一个代码项目，读文件、改文件、执行命令，并把改完之后的 diff 呈现给你看。**

正因为 OpenCode 能动到项目里的文件，新手最关键的习惯，不是**一上来就让它帮我做一个完整的项目**，而是先学会：

- 先让它把项目读一遍；
- 让它先给出方案（**Plan 模式**）；
- 一次只改一小处；
- 看 diff；
- 跑测试；
- 提前打好 Git 检查点。

下面开始今天的内容。

---

## 1. OpenCode 是什么？

OpenCode 是一个**可以在代码项目里干活的 AI 编码助手**。

你可以用自然语言描述任务，例如：

> 请帮我解释一下这个项目是做什么的。

> 请找出这个 bug 的原因，并做最小必要的修复。

> 请为这个函数加一个单元测试。

OpenCode 可以读取项目文件、分析代码，必要时修改文件、执行命令或运行测试，然后把结果和 diff 反馈给你。

简单说：**ChatGPT 像是在聊天窗里问问题，而 OpenCode 更像是有人坐在你的项目目录里跟你一起干活。**

### OpenCode 的基本工作流程

1. **读**：扫一遍项目结构，理解目录、入口、依赖。
2. **改**：在得到你授权后修改文件（始终先给你看 diff）。
3. **执行**：跑命令、跑测试、跑 lint。
4. **汇报**：把改动总结、验证结果、风险点列出来。
5. **审阅**：由你决定接受、回滚、还是继续迭代。

其中最关键的是最后一步：**结果仍然由你审阅**。OpenCode 很强，但它不是一个自动上线工具。对新手来说，最安全的心态是：**把它当成一个能力很强、但产出仍需要复核的助手。**

---

## 2. OpenCode 长什么样？

OpenCode 没有官方桌面 GUI 应用（这是和很多同类工具最显著的区别），但提供了 6 类入口：

### ① 终端 TUI（最常用）

在终端运行 `opencode` 进入交互式界面：

```bash
opencode
```

你会看到类似这样的界面：上半屏是历史对话，下半屏是输入框，右下角显示当前模型和代理。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260709205140694.png)

### ② CLI 一次性提问

不想进入 TUI？直接用 `run`：

```bash
opencode run "用中文解释 Python 闭包"
```

适合脚本、CI 流水线、定时任务。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260709205055246.png)

### ③ Web 界面

```bash
opencode web
```

会自动打开浏览器（默认 `http://127.0.0.1:<随机端口>`）。无终端场景下用。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260709204958066.png)

### ④ IDE 扩展

在 VS Code / Cursor / Windsurf / VSCodium 集成终端里运行 `opencode`，扩展会自动安装。常用快捷键：

- `Cmd+Esc`（Mac）/ `Ctrl+Esc`（Win/Linux）：打开 OpenCode
- `Cmd+Shift+Esc`：新建会话
- `Cmd+Option+K`：插入文件引用

### ⑤ ACP 编辑器协议

OpenCode 支持 [Agent Client Protocol](https://agentclientprotocol.com)。在 **Zed、JetBrains IDE、Neovim（Avante.nvim / CodeCompanion.nvim）** 中可以把 OpenCode 当作 ACP 子进程调用：

```bash
opencode acp
```

通过 stdio 的 JSON-RPC 与编辑器通信。

### ⑥ GitHub / GitLab 自动化

- **GitHub**：安装 `opencode-agent` GitHub App，在 Issue 或 PR 评论里写 `/oc` 或 `/opencode` 触发。
- **GitLab**：在 issue 或合并请求评论里 `@opencode` 触发（需要 GitLab Duo Agent Platform）。

### ⑦ SDK 编程控制

```bash
npm install @opencode-ai/sdk
```

构建自己的客户端或集成（详见 [opencode.ai/docs/sdk](https://opencode.ai/docs/sdk)）。

---

## 3. 新手需要知道的五个关键词

| 关键词 | 通俗解释 | 为什么重要 |
|---|---|---|
| **项目文件夹** | 装着你代码的那个文件夹 | OpenCode 需要知道在哪里干活 |
| **`.opencode/`** | 放自定义命令、代理、技能、插件、主题、工具的目录 | 团队协作时提交到 Git，让所有成员共享同一套约定 |
| **Git** | 一种代码版本管理工具 | **`/undo` 命令真的靠 Git 回滚**，所以必须先 `git init` |
| **diff** | 改动前后的差异 | OpenCode 改完后，先看 diff 再决定要不要接受 |
| **权限** | 每个工具可设 `allow`/`ask`/`deny` | 比"沙箱"更细，控制到具体命令模式 |

如果暂时只能记住一个词，记住 **diff**。OpenCode 改完文件之后，不要只看它的总结，要看 diff，因为 diff 才是它真正改了什么。

> 💡 **实战贴士**：popdf 这种 Python 项目里，建议在仓库根创建 `.opencode/AGENTS.md` 而不是 `AGENTS.md`，这是 OpenCode 约定俗成的位置。

---

## 4. 选入口：TUI、CLI、Web、IDE、SDK、ACP 还是 GitHub Action？

| 入口 | 适合人群 | 主要用法 |
|---|---|---|
| **TUI** | 90% 的开发者首选 | 终端内交互式对话，常驻开发流 |
| **CLI（`opencode run`）** | 写脚本、做 CI、做自动化 | 一行命令提问，非交互 |
| **Web** | 不在终端前的临时使用 | 浏览器打开即用 |
| **IDE 扩展** | 已在用 VS Code/Cursor/Windsurf 的人 | 编辑器侧边栏/终端内唤起 |
| **SDK** | 想做自定义客户端或集成 | TypeScript / JS 编程控制 |
| **ACP** | Zed / JetBrains / Neovim 用户 | 编辑器原生集成 |
| **GitHub Action** | 自动化 PR 审查、Issue 处理 | 在评论里 `/oc` 触发 |
| **GitLab** | 用 GitLab 的团队 | 在评论里 `@opencode` 触发 |

我的推荐很简单：**新手先从 TUI 入手**。已经天天住在编辑器里的开发者，用 IDE 扩展。终端用得顺手之后再试 `opencode run`。需要后台任务或自动 PR 的 GitHub/GitLab 项目，用 GitHub Action / GitLab Duo。

---

## 5. 第一次使用：从 TUI 开始（实战 popdf）

下面我用一个**真实的中文 Python 项目**——[popdf](https://github.com/CoderWanFeng/popdf)——带大家走完一遍流程。popdf 是 Python 自动化办公的 PDF 处理库，已有 10 个功能（PDF 转 Word、转图片、加水印、加密、解密、合并等），非常适合作为入门实战。

### 5.1 安装

**macOS / Linux**（推荐）：

```bash
curl -fsSL https://opencode.ai/install | bash
```

**通过 npm / Bun / pnpm / Yarn**：

```bash
npm install -g opencode-ai
# 或
bun install -g opencode-ai
# 或
pnpm install -g opencode-ai
# 或
yarn global add opencode-ai
```

**macOS 用 Homebrew**（推荐用团队 tap）：

```bash
brew install anomalyco/tap/opencode
```

**Windows**：强烈建议用 **WSL**（Windows Subsystem for Linux），性能更好、终端兼容性更佳。

**Docker**：

```bash
docker run -it --rm ghcr.io/anomalyco/opencode
```

安装完成后，终端里跑 `opencode --version` 验证。

### 5.2 登录 + 选模型

第一次进入 TUI 通常会提示登录：

```bash
opencode
```

然后在 TUI 里输入：

```
/connect
```

会列出所有可用提供商，其中有可以免费使用的AI大模型（不同时间，免费的大模型也不同）。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260709205321156.png)

如果想使用付费的，**新手建议选 OpenCode Zen**（团队精选，按量付费，含 Claude/GPT/Gemini/MiniMax 等顶级模型）。如果你想省钱，OpenCode **Go** 是首月 $5、之后 $10 的订阅，包含 13 个开源编程模型。

国内用户的中文项目，**优先选 Zen 里的 MiniMax M3、Kimi K2.7 Code 或 DeepSeek V4 Pro**——中文理解和价格都友好。具体可以查看：https://aiwf365.site/token

选完提供商会进入浏览器登录（或贴入 API Key），凭据存在 `~/.local/share/opencode/auth.json`。

### 5.3 项目初始化

以 popdf 为例：

```bash
git clone https://github.com/CoderWanFeng/popdf
cd popdf
git checkout develop   # popdf 的主分支是 develop
opencode
```

进入 TUI 后，先跑一个**最重要**的命令：

```
/init
```

OpenCode 会分析整个 popdf 项目，在项目根目录生成 `.opencode/AGENTS.md`。建议把它提交到 Git，这样团队成员都能共享。

### 5.4 推荐的第一条提示词

注意 popdf 用了 `uv` 做包管理，不是 pip。这个细节后面会反复用到。

```
请暂时不要修改任何文件，用中文向我解释这个项目：
1. 这个项目大致是做什么的？
2. 主要的目录（popdf/api/ popdf/core/ popdf/lib/ examples/ tests/）分别负责什么？
3. 入口文件可能在哪里？
4. 如果我想跑起来，通常要执行哪些命令？
5. 包管理用的是 uv 还是 pip？
6. 有哪些你不确定的地方？请直接说"不确定"，不要猜。
```

核心思想是：**先读，不急着改。**

---

## 6. 第一条提示词：在动手之前，先让 OpenCode 读

新手最常见的一个坑，是上来就这样问：

> 帮我把整个项目重构一遍。

> 帮我做一个完整的网站。

> 帮我把所有 bug 都修了。

这种任务太宽，你自己也很难判断 OpenCode 做得对不对。

### 6.1 用 Plan 模式先出方案

在 TUI 里按 `Tab` 键切换到 **Plan 模式**（右下角会显示模式指示器）。这个模式下 OpenCode **不会修改任何文件**，只会给你一个"如何实现"的方案。

切到 Plan 模式后，输入：

```
当一个用户删除 PDF 时，我们希望把它移到回收站目录而不是真删除。
请基于 popdf 现有结构（popdf/api/ popdf/core/）给一个最小实现方案，
列出需要改哪些文件、新增哪些函数。不要现在动手改。
```

OpenCode 会输出类似这样的方案：

> 1. 在 `popdf/api/` 新增 `del4pdf_trash.py` 暴露 `move_to_trash()` 接口
> 2. 在 `popdf/core/file_utils.py` 实现移动逻辑（用 send2trash 库或 shutil.move）
> 3. 在 `examples/` 加 `del4pdf_to_trash.py` 演示用法
> 4. 在 `tests/test_code/` 加单元测试

你可以反复迭代这个方案：

```
改一下：不要用 send2trash（多一个依赖），用 shutil.move + .trash/ 目录就行。
另外加个回收站清理命令，超过 30 天的文件自动删除。
```

> 💡 **技巧**：在 TUI 里你可以**直接把图片拖到终端**，OpenCode 会扫描图片并附加到提示词里——这对 UI 类任务非常有用。

满意后按 `Tab` 切回 Build 模式，然后说：

```
听起来不错，开始改吧。
```

### 6.2 用 `@文件` 和 `!命令` 引用上下文

Plan 模式之外，日常对话里两个超好用的符号：

- **`@文件名`**：把文件内容注入到提示词。比如 `请评审 @popdf/core/pdf2docx.py 的错误处理`
- **`!命令`**：把 shell 命令输出注入。比如 `!uv run pytest tests/test_code -v`

输入 `@` 会触发模糊文件搜索；输入 `!` 会被识别为 bash 命令。

---

## 7. 第一次改代码：只改一小处（实战 popdf）

熟悉了 OpenCode 对 popdf 项目的理解之后，让它做一个**非常小**的修改。第一次的好目标是 **README.md**：

```
请只修改 README.md，新增一节叫"🛠️ 开发者入门"。
要求：
- 不要修改任何其他文件
- 不要新增第三方依赖
- 不要改 pyproject.toml 和 uv.lock
- 改完之后告诉我你改了什么
- 如果项目里没有明确写启动命令，请直接说"不确定"，不要凭空编造命令。
```

OpenCode 改完之后，做两件事：

```bash
git status
git diff
```

如果是 TUI 应用，也可以直接在审阅面板里查看。

### 看 diff 时要看什么？

- OpenCode 是否动了你没允许它动的文件？
- 是否引入了你不认识的依赖？
- 是否删除了重要的配置（特别是 `pyproject.toml` / `uv.lock`）？
- 文字或代码内容是否符合你的要求？
- diff 是否真的支撑了它在总结里讲的那些话？

### 不满意怎么办？用 `/undo` 真回滚

OpenCode 的 `/undo` 真的基于 Git：

```
/undo
```

文件改动会被还原，对话回到上一轮。你可以修改提示词再试。

```
/redo   # 还原刚才的撤销
```

**OpenCode 会自动维护一个 Git 暂存区**，让你无需手动 `git stash` 就能回退到任意一轮。所以**强烈建议第一次使用前先 `git init` 或 `git clone` 一个有版本管理的项目**。

### popdf 的提交流程特殊提醒

popdf 用 `develop` 分支 + Pull Request 流程，**不能直接 push 到 develop**。所以改完 README 之后还要：

```bash
git checkout -b docs/dev-getting-started
git add README.md
git commit -m "docs: 新增开发者入门章节"
git push origin docs/dev-getting-started
# 然后去 GitHub 开 PR
```

这一点我们会在第 9 章权限配置里再强化。

---

## 8. 可以直接抄的提示词模板

OpenCode 支持把常用提示词写成 **Markdown 命令文件**，放在 `.opencode/commands/` 或 `~/.config/opencode/commands/`。文件名就是命令名。

下面 5 个模板都围绕 popdf 实战展开，可以直接 `cp` 到你的 `.opencode/commands/` 目录使用。

### 模板结构速览

每个命令文件都长这样：

```markdown
---
description: 命令描述
agent: build        # build / plan / general
model: anthropic/claude-haiku-4-5   # 可选，覆盖默认模型
---

命令提示词正文。
支持 $ARGUMENTS（用户输入的参数）、!`shell 命令`（注入命令输出）、@文件名（引用文件）。
```

### 模板 1：解释项目

`.opencode/commands/explain.md`：

```markdown
---
description: 解释项目结构和入口
agent: plan
model: anthropic/claude-haiku-4-5
---

请暂时不要修改任何文件，先帮我理解这个项目：
1. 这个项目是做什么的？
2. 用的是什么技术栈？包管理是 uv 还是 pip？
3. 入口在哪里？
4. 各个主要目录分别负责什么？
5. 作为新手，应该按什么顺序读代码？
6. 哪些地方你不确定？
```

用法：`/explain`

### 模板 2：修 bug

`.opencode/commands/fix.md`：

```markdown
---
description: 定位并修复 bug
agent: build
---

我遇到了一个 bug，请帮我定位并修复。
现象：$ARGUMENTS
复现步骤：
1. xxx
2. xxx
3. xxx

要求：
- 先讲一下你判断的原因
- 做最小必要的改动
- 不要在没问我之前就加新依赖
- 不要改 pyproject.toml 和 uv.lock
- 修复之后跑相关测试：uv run pytest
- 最后列出改动文件和风险
```

用法：`/fix popdf 加密大文件（>5MB）会卡死超时`

### 模板 3：加新功能

`.opencode/commands/feature.md`：

```markdown
---
description: 给项目加新功能
agent: plan
---

请帮我加一个新功能：$ARGUMENTS

范围：
- 可以改动：popdf/api/、popdf/core/、popdf/lib/、examples/、tests/test_code/
- 不要改动：pyproject.toml、uv.lock、tests/test_files/ 里已有素材、.github/

要求：
- 先给一个简短方案（哪些文件、哪些函数、沿用什么风格）
- 沿用现有代码风格（参考 popdf/core/ 已有模块）
- 如果需要新依赖，请先停下来问我
- 完成后跑 uv run pytest
- 输出：改了哪些文件、如何验证、哪些地方仍需我手工检查
```

用法：`/feature PDF 转 Excel`

### 模板 4：代码评审

`.opencode/commands/review.md`：

```markdown
---
description: 评审当前未提交的改动
agent: plan
---

请评审当前未提交的改动，关注点：
1. 明显的 bug
2. 漏掉的边界情况（空 PDF、加密 PDF、超大文件、特殊字符文件名）
3. 可能造成的回归
4. 是否需要补测试
5. 是否改了 pyproject.toml、uv.lock、.github/ 等敏感文件
6. 是否遵循 popdf 的目录约定

要求：
- 先列高风险问题
- 再列中、低风险建议
- 不要修改任何文件，除非我明确要求
```

用法：`/review`

### 模板 5：补单元测试

`.opencode/commands/test.md`：

```markdown
---
description: 为最近的改动补单元测试
agent: build
---

请为刚才的改动补一个最小测试。

要求：
- 先讲清楚这个测试覆盖了哪些场景（包括边界）
- 沿用 tests/test_code/ 现有风格（参考已有的 test_pdf2docx.py）
- 用 tests/test_files/ 里的小 PDF，不要新增大文件
- 完成后跑 uv run pytest tests/test_code/<新文件>.py -v
```

用法：`/test`

### 模板进阶：参数化命令

使用 `$ARGUMENTS` 接收用户输入，使用 `$1` `$2` `$3` 访问位置参数。

`.opencode/commands/explain-file.md`：

```markdown
---
description: 解释指定文件
agent: plan
---

请不要修改任何文件，向我详细解释 @popdf/$1 这个文件：
1. 它做什么？
2. 关键函数/类有哪些？
3. 与哪些模块有依赖关系？
4. 有没有可以改进的地方（仅指出，不要改）？
```

用法：`/explain-file core/pdf2docx.py`

### 模板进阶：注入 shell 输出

用 `` !`命令` `` 把命令输出注入到提示词：

```markdown
---
description: 分析测试覆盖率
---

当前测试结果：
!`uv run pytest tests/ --tb=short`

基于以上结果，建议如何提升覆盖率。不要直接改代码，先列建议。
```

---

## 9. 安全使用：权限、Policies、AGENTS.md 护栏

OpenCode 能读文件、改文件、跑命令，所以**安全边界**很重要。OpenCode 用了一套比"沙箱"更精细的**权限系统**——每个工具、每条命令都可以单独设置 `allow` / `ask` / `deny`。

### 9.1 三态权限

每条权限规则解析为以下之一：

- `"allow"`：无需审批直接运行
- `"ask"`：每次提示审批
- `"deny"`：直接阻止

**默认值**（不配置时）：

- 大多数权限默认 `"allow"`
- `doom_loop`（同一工具重复 3 次）和 `external_directory`（访问项目外路径）默认 `"ask"`
- `read` 工具默认 `"allow"`，**但 `.env` / `.env.*` 文件默认被拒绝**（`.env.example` 除外）

### 9.2 给 popdf 的权限配置

把下面这份配置写到 popdf 项目的 `.opencode/opencode.jsonc`：

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "edit": {
      "*.py": "allow",
      "*.md": "allow",
      "pyproject.toml": "deny",     // 依赖文件锁死
      "uv.lock": "deny",
      ".github/**": "ask"           // CI 配置改动需确认
    },
    "bash": {
      "*": "ask",
      "git status": "allow",
      "git diff": "allow",
      "git log *": "allow",
      "uv run pytest*": "allow",
      "uv run ruff*": "allow",
      "git add *": "ask",           // 提交前确认
      "git push": "deny"            // 禁止直接 push（必须人工开 PR）
    },
    "webfetch": "allow"
  }
}
```

**规则按"最后匹配优先"**。所以上例的逻辑是：默认 ask，对安全的只读命令和测试命令 allow，对危险命令 deny。

### 9.3 跨目录控制（OpenCode 独有）

想让 OpenCode 能访问工作目录之外的某些路径？用 `external_directory`：

```jsonc
{
  "permission": {
    "external_directory": {
      "~/notes/**": "allow",
      "$HOME/Documents/popdf-mock-files/**": "allow"
    },
    "edit": {
      "~/notes/**": "deny"          // 在外部目录里只读、不写
    }
  }
}
```

`~` 和 `$HOME` 在模式开头会被展开为你的主目录。

### 9.4 提供商级管控（OpenCode 独有：Policies）

**这是 OpenCode 比同类工具更高级的能力**。如果团队只想允许用某几家提供商的模型，可以用 **Policies**（实验性）：

```jsonc
{
  "experimental": {
    "policies": [
      { "effect": "deny",  "action": "provider.use", "resource": "*" },
      { "effect": "allow", "action": "provider.use", "resource": "anthropic" },
      { "effect": "allow", "action": "provider.use", "resource": "minimax" }
    ]
  }
}
```

效果：**即使 OpenCode 通过 `/connect` 拿到了 OpenAI 的 API Key，也会被 Policies 拦截**，模型选择列表里根本不会出现 OpenAI。

规则顺序同样是"最后匹配优先"。并且**全局 Policies 优先于项目 Policies**，防止仓库里有恶意配置重新启用被禁用的提供商。

### 9.5 遇到审批弹窗怎么办

当 OpenCode 请求审批时，界面提供三种选择：

- `once` — 仅批准本次请求
- `always` — 批准与建议模式匹配的后续请求（当前会话有效）
- `reject` — 拒绝请求

下面这些动作要**特别小心**：

```bash
rm -rf             # 删文件
sudo               # 提权
curl ... | sh      # 下载并执行
pip install xxx    # 装不熟悉的包
访问项目外的系统目录
```

不确定时，选范围更窄的那个选项，或者拒绝，然后让 OpenCode 解释为什么需要这条命令。

### 9.6 不要把这些秘密交给 OpenCode

下面这些东西，不要直接粘到提示词里、日志里或截图里：

- API Key、数据库密码、生产环境令牌
- 客户隐私数据、个人敏感信息
- 公司内部不允许外传的资料
- 生产数据库连接串

**报错日志要特别小心**，里面可能藏着令牌、Cookie、URL 参数或数据库连接信息。粘贴之前先扫一眼。

### 9.7 改之前先打 Git 检查点

在项目目录里：

```bash
git status
git add .
git commit -m "checkpoint before opencode task"
```

OpenCode 改完之后再跑：

```bash
git status
git diff
```

万一出问题，Git 给你留了一条退路。**`/undo` 不灵的时候，`git reset --hard HEAD~1` 是终极武器。**

---

## 10. 新手 7 天练习计划（popdf 实战版）

下面 7 天的练习全部围绕 **popdf** 这个真实项目。每天 30 分钟到 1 小时即可。

### 第 1 天：只读 popdf

```
请不要修改任何文件。解释 popdf 是做什么的、目录结构、入口在哪里、怎么运行（用 uv 还是 pip？）。
```

目标：弄清楚 popdf 是个什么项目，有哪些功能模块。

### 第 2 天：让 OpenCode 写项目概览

```
基于你对 popdf 的理解，起草 docs/project-overview.md。
要求：
- 面向新手
- 说明 10 个功能（PDF 转 Word / 转图片 / TXT 转 PDF / 切割 / 加密 / 解密 / 加水印 / 合并 / 删除）各自用哪个函数
- 说明目录约定（popdf/api/ popdf/core/ popdf/lib/）
- 不要修改任何代码文件
```

目标：练习让 OpenCode 生成文档。

### 第 3 天：只改 README

```
请只修改 README.md，加上"🛠️ 开发者入门"章节。
要求：
- 不要修改任何其他文件
- 不要新增第三方依赖
- 不要改 pyproject.toml
```

改完后看 diff，跑 `/undo` 练习回滚。目标：掌握 `diff` 和 `/undo`。

### 第 4 天：修一个假设的加密 bug

假设你接到用户反馈：**popdf 加密超过 5MB 的 PDF 会卡住超时**。

```
我遇到了一个 bug，请帮我定位并修复。
现象：popdf/core/encrypt4pdf.py 处理 5MB 以上的 PDF 会卡住，最终超时
复现步骤：
1. 准备一个 5MB 以上的测试 PDF
2. 调用 popdf.encrypt4pdf(input, output, password='test')
3. 命令卡住不返回，最终报错 timeout

报错：
[粘贴超时堆栈]

要求：
- 先讲你判断的原因（流式处理？内存？锁？）
- 做最小必要改动
- 不要在没问我之前就加新依赖
- 修复之后跑相关测试
- 最后列出改动文件和风险
```

目标：学会描述"现象 + 复现步骤 + 期望行为"。

### 第 5 天：补一个测试

```
请为刚才修的加密 bug 补一个最小测试。
要求：
- 先讲清楚这个测试覆盖了什么（包括边界：刚好 5MB、10MB、空 PDF、加密 PDF）
- 沿用 tests/test_code/ 现有风格（参考 test_encrypt4pdf.py）
- 用 tests/test_files/ 里的小 PDF
- 完成后跑 uv run pytest tests/test_code/test_encrypt4pdf.py -v
```

目标：让 OpenCode 不仅写代码，也去验证代码。

### 第 6 天：让 OpenCode 评审你的改动

```
请评审当前未提交的改动，关注 bug、边界情况、回归风险，以及是否需要补测试。
暂时不要修改文件，只输出评审意见。
```

目标：把 OpenCode 当作多一双眼睛。

### 第 7 天：试一下 Explore 子代理

OpenCode 内置了 3 个子代理：**General**（多步研究）、**Explore**（只读检索）、**Scout**（外部仓库研究）。在消息里用 `@` 提及它们：

```
@explore 帮我搜一下 popdf 里所有处理加密 PDF 的代码位置，
列出文件路径和函数名，按调用关系排序。
```

Explore 会并发读取多个文件并整理一份索引给你。这是 popdf 维护者必备技能——快速熟悉陌生代码。

---

## 11. 进阶：用 AGENTS.md 教 OpenCode 认识你的项目

经常用 OpenCode 之后，可以考虑在项目根目录加一个 **`.opencode/AGENTS.md`** 文件，把它当成一份**写给 AI 智能体看的项目说明书**。OpenCode 在开始工作之前会读这些约定，从而更贴合你们团队的规范。

### 11.1 给 popdf 写的 AGENTS.md 范本

```markdown
# popdf 项目规则

## 目录约定
- popdf/api/：对外接口，新功能在这里暴露函数
- popdf/core/：核心实现
- popdf/lib/：通用工具
- examples/：使用案例，每个功能一个 py 文件
- tests/test_code/：单元测试
- tests/test_files/：测试用 PDF、图片

## 包管理
- 用 uv，不要用 pip
- 新增依赖：`uv add <包>`，会自动更新 pyproject.toml 和 uv.lock
- 不要手动改 pyproject.toml 的 [project.dependencies]

## 提交流程
- 永远走 PR，不要直接 push develop 或 main
- 提交前必须跑 `uv run pytest tests/`
- 提交信息用中文，prefix 用 type: feat/fix/docs/refactor/test/chore
- 一个 commit 只做一件事

## 代码风格
- 用 ruff 格式化（`uv run ruff format .`）
- 函数命名遵循 popdf 现有风格（xxx4pdf、xxx2xxx）
- 不要无端加 type hints，除非必要
- 不要在源码里写 print（用 logging）

## 文档
- 新增功能必须：① popdf/api/ 加接口 ② popdf/core/ 加实现 ③ examples/ 加案例 ④ tests/test_code/ 加测试 ⑤ README.md 更新功能列表
```

把这文件提交到 Git，团队所有成员第一次跑 `opencode` 都会读到。

### 11.2 AGENTS.md 的三个层级

OpenCode 按以下顺序查找规则文件（先匹配先使用）：

1. **本地文件**：从当前目录向上遍历找 `AGENTS.md` / `CLAUDE.md`
2. **全局文件**：`~/.config/opencode/AGENTS.md`
3. **Claude Code 兼容**：`~/.claude/CLAUDE.md`（可关闭）

每个层级第一个匹配的文件优先。比如同时有 `AGENTS.md` 和 `CLAUDE.md`，只读 `AGENTS.md`。

想禁用 Claude Code 兼容：

```bash
export OPENCODE_DISABLE_CLAUDE_CODE=1        # 全部禁用
export OPENCODE_DISABLE_CLAUDE_CODE_PROMPT=1 # 只禁用 ~/.claude/CLAUDE.md
export OPENCODE_DISABLE_CLAUDE_CODE_SKILLS=1 # 只禁用 .claude/skills/
```

### 11.3 引用外部规则文件

如果规则太多，可以用 `opencode.json` 的 `instructions` 字段拆分到多个文件：

```jsonc
{
  "instructions": [
    "docs/development-standards.md",
    "test/testing-guidelines.md",
    "packages/*/AGENTS.md"           // 单仓库多包的子目录 AGENTS.md
  ]
}
```

支持远程 URL（5 秒超时）：

```jsonc
{
  "instructions": [
    "https://raw.githubusercontent.com/python4office/popdf/main/CONTRIBUTING.md"
  ]
}
```

### 11.4 用 Skills 按需加载

OpenCode 的 **Skills** 功能让 AI 按需加载"操作手册"，而不是一股脑全塞进上下文。

创建 `.opencode/skills/release/SKILL.md`：

```markdown
---
name: release
description: 给 popdf 准备发布版本，包括更新版本号、生成 changelog、打 tag
license: MIT
compatibility: opencode
metadata:
  audience: maintainers
  workflow: github
---

## What I do
- bump pyproject.toml 的 version
- 生成 CHANGELOG 条目
- 给出 `git tag` 命令

## When to use me
用在我告诉你"准备发布 popdf"时。先问我目标版本号（遵循 SemVer）。
```

**frontmatter 必填字段**：

- `name`：1-64 字符，正则 `^[a-z0-9]+(-[a-z0-9]+)*$`，与目录名一致
- `description`：1-1024 字符，要具体到让代理能正确选择

**6 个搜索位置**：

| 优先级 | 项目级 | 全局 |
|---|---|---|
| OpenCode 原生 | `.opencode/skills/` | `~/.config/opencode/skills/` |
| Claude 兼容 | `.claude/skills/` | `~/.claude/skills/` |
| 代理通用 | `.agents/skills/` | `~/.agents/skills/` |

**权限控制**：

```jsonc
{
  "permission": {
    "skill": {
      "*": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

### 11.5 用 References 引用外部项目

如果你的 popdf 项目里要参考另一个仓库的代码（比如想知道别人怎么实现 PDF 转 Excel），可以在 `opencode.json` 里加 References：

```jsonc
{
  "references": {
    "design-system": {
      "path": "../design-system",
      "description": "设计系统，UI 组件参考"
    },
    "pdf-lib": {
      "repository": "pypdfium2-team/pypdfium2",
      "branch": "main",
      "description": "PDF 底层库实现参考"
    }
  }
}
```

在 TUI 里输入 `@pdf-lib/` 就能模糊搜索那个外部仓库的文件。Git 引用是异步克隆，第一次用可能需要等一下。

### 11.6 实用判据

> **当你不得不第二次提醒 OpenCode 同一件事时，就该考虑把它写进 AGENTS.md / SKILL.md。**

---

## 12. 常见问题

### Q1：我不会写代码，可以用 OpenCode 吗？

可以，但要从"解释项目""整理文档""看懂这条报错""写学习路线"这类任务开始，不要一上来就让它做大幅重构。

比如面对 popdf：你可以让 OpenCode 帮你在 `examples/` 写一个新案例脚本，你只需要描述"我有一个 PDF 列表，希望批量加水印"，OpenCode 会按 popdf 现有风格写出可运行的代码。

你可以把 OpenCode 当作学习助手，但它改完文件之后，你仍然要看 diff、验证结果。

### Q2：到底用 TUI、CLI、Web 还是 IDE？

新手先用 TUI。如果你已经每天用 VS Code/Cursor/Windsurf，那就用 IDE 扩展。终端用得顺手之后再用 `opencode run`。需要后台任务或建 PR 的 GitHub/GitLab 项目，用 GitHub Action / GitLab Duo。

### Q3：OpenCode 改错了怎么办？

先看 diff。不满意就让它再调整。如果项目已经被改乱，**用 `/undo`**（基于 Git 回滚，比大多数同类工具更可靠）。

如果你还没学 Git，先在练习项目上练，再让 OpenCode 在重要项目里做大改动。终极退路是 `git reset --hard HEAD~1`。

### Q4：OpenCode 让我批准一条命令，要不要同意？

**只批准你能看懂的命令。**

特别留意：删除文件、安装依赖、访问项目之外的目录、从网络下载、执行脚本。

不懂的时候，可以这样问 OpenCode："请解释一下这条命令是做什么的，为什么必要，有没有更安全的做法。"

### Q5：我必须要 API Key 吗？

不一定。OpenCode **Zen** 和 **Go** 走 OpenCode 账号体系（类似订阅），不需要各家提供商的 API Key。

如果要用 OpenAI/Anthropic 原生账号，也可以通过 `/connect` 用 **ChatGPT Plus/Pro** 订阅或 **Claude Pro/Max** 订阅免 Key 登录（OpenCode 在终端帮你走 OAuth）。

### Q6：怎么挑模型？

- **闭源顶配**：OpenCode Zen 上的 Claude Sonnet 4.5 / GPT 5.1 Codex / Gemini 3 Pro
- **中文项目友好**：Zen 上的 **MiniMax M3**（$0.30/$1.20 每 1M tokens）、**DeepSeek V4 Pro**（$1.74/$3.48）
- **省钱首选**：Zen 上的 **DeepSeek V4 Flash**（$0.14/$0.28），或 **OpenCode Go** 订阅（首月 $5，之后 $10，13 个开源模型）
- **完全免费**：Zen 上的 MiMo-V2.5 Free / Big Pickle / North Mini Code Free（限免）

用 `opencode run` 不会启动 TUI，可以快速测试不同模型的响应速度和质量。

### Q7：OpenCode 能直接帮我部署吗？

**不要让 OpenCode 在没有人复核的情况下操作生产环境。**

更安全的流程是：

> 小任务 → 审 diff → 跑测试 → 看风险 → 提交 / PR → 上线前由人确认

### Q8：有没有桌面 GUI 应用？

**没有官方桌面 GUI 应用**。这是 OpenCode 和很多同类工具最显著的区别。

替代方案：

- 不在终端前 → 用 `opencode web`（浏览器）
- 想要原生编辑器体验 → 用 IDE 扩展（VS Code/Cursor/Windsurf/VSCodium）
- 想用 Zed/JetBrains/Neovim → 用 ACP 协议集成

### Q9：怎么启用 Web 搜索？

OpenCode 的 `websearch` 工具默认关闭，需要：

```bash
OPENCODE_ENABLE_EXA=1 opencode
```

或在 `opencode.json` 里配置。底层用 Exa AI，**无需 API Key**。

### Q10：LSP 怎么开启？

LSP 默认关闭。开启方法：

```jsonc
{
  "lsp": true
}
```

开启后 OpenCode 会自动检测项目语言并启动对应 LSP 服务器（typescript、pyright、gopls、rust-analyzer、jdtls 等 30 个）。

**但更建议**：

> 把项目的 lint/test 命令写到 AGENTS.md，让 agent 自己跑命令拿到反馈，而不是依赖 LSP 的诊断信息。

理由：LSP 可能与项目不同步、占内存、某些项目里收益不大。让 agent 跑 `uv run pytest` 同样能拿到错误反馈，还更可控。

---

## 最后

开始用 OpenCode 的正确方式，**不是**一把帮我把整个项目做好。

**而是**：先解释项目 → 给方案 → 改一小处 → 看 diff → 跑测试 → 迭代

任务小一点、权限收紧一点、把验证讲明白，你就可以从第一天起，安全地用 OpenCode 来读代码、改代码、评审代码。

### 三个立刻可以做的事

1. **选 TUI + 写 AGENTS.md** —— 第一次用就在项目里写一份 `.opencode/AGENTS.md`，把团队约定固化下来。
2. **用 Git 检查点** —— 每次大改之前先 `git commit`，出问题时 `/undo` 或 `git reset`。
3. **挑对模型** —— 中文项目优先 MiniMax / Kimi / DeepSeek；顶配用 Claude / GPT；预算紧用 Go 订阅。

### 推荐资源

#### 实战练习项目

- **[popdf](https://github.com/CoderWanFeng/popdf)** —— Python 自动化办公 PDF 库，中文项目，目录约定清晰，有 `api/core/lib/examples/tests` 完整分层。本文 7 天练习计划就是围绕它展开，强烈建议照着跑一遍。
- [python4office/popdf 交流群](https://www.python4office.cn/wechat-group/)

#### 官方资源

- 官网：[opencode.ai](https://opencode.ai)
- 文档：[opencode.ai/docs/zh-cn](https://opencode.ai/docs/zh-cn)
- GitHub：[github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)
- Discord：[opencode.ai/discord](https://opencode.ai/discord)

#### 模型选择

- **OpenCode Zen**（按量付费）：含 Claude Sonnet 4.5、GPT 5.1 Codex、Gemini 3 Pro、**MiniMax M3**、Kimi K2.7 Code、DeepSeek V4 Pro 等
- **OpenCode Go**（订阅）：首月 $5、之后 $10/月，13 个开源编程模型
- **自带 API Key**：Claude Pro/Max、ChatGPT Plus/Pro 订阅可直接登录
- **免费大模型**：无需 API Key，直接在 OpenCode 里用



## 相关阅读

- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
---
title: HyperFrames 入门指南，从零基础到实战，看这一篇就够了！
date: 2026-07-10 03:30:46
tags:
  - HyperFrames
  - AI视频
  - AI编程
  - 视频创作
  - 开源工具
categories: HyperFrames
cover: https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop
description: 一份面向零基础读者的 HyperFrames 入门指南，让 AI Agent 帮你用 HTML 写出可发布的视频。
---



<!-- more -->
<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>
</p>

# HyperFrames 入门指南，从零基础到实战，看这一篇就够了！

一份面向新手的 HyperFrames 入门指南，覆盖"什么是 HyperFrames"、CLI 与 AI Agent 两种入口、第一次跑通、提示词模板、7 天练习计划，以及权限 / 沙箱 / Git 检查点。

如果你读完之后只想记住一句话，那应该是这一句：

**HyperFrames 不是剪辑软件，是"用 HTML 写视频"。AI Agent 是你的剪辑师。**

正因为 HyperFrames 让 Agent 能直接读 HTML、改 HTML、跑命令出 MP4，新手最关键的习惯，不是上来就让它帮你"做个抖音爆款"，而是先学会：

- 先让它把模板读一遍；
- 让它先给出方案；
- 一次只改 `index.html` 的一行；
- 看 diff；
- 跑 `npx hyperframes preview`；
- 跑 `npx hyperframes render` 出片。

下面开始今天的内容。

## 1. HyperFrames 是什么？

HyperFrames 是一个"用 HTML 写视频"的开源框架。它出自 HeyGen（GitHub 33k+ ⭐，npm 包名就叫 `hyperframes`），最新版本 0.7.46。

你可以用自然语言描述任务，例如：

> 请帮我做一个 10 秒的产品介绍视频，标题淡入，背景是深色，配一首轻 BGM。

> 请把这段 CSV 做成一个 45 秒的柱状图竞速视频。

> 请给这个 PR 做一段 30 秒的代码变更解说。

HyperFrames 接到任务后，会读 `index.html`、分析结构、写 GSAP 动画、调用 FFmpeg 编码，最后给你一个 MP4 文件。简单说：

> ChatGPT 像是在聊天窗里问问题，而 HyperFrames 更像是有人坐在你的项目目录里，跟你一起剪视频。

最关键的一步仍然是最后那句：**成片仍由你审阅**。

HyperFrames 很强，但它不是自动上线工具。对新手来说，最安全的心态是：把它当成一个能力很强、但产出仍需要复核的助手。

## 2. HyperFrames 长什么样？

### 图 1：init 命令行输出

第一次跑 `npx hyperframes init my-video`，会看到类似这样的初始化面板：选择模板、是否带入示例媒体、是否启用 AI skills。

> HyperFrames init 初始化界面

### 图 2：脚手架出来的项目结构

跑完 init 之后，会生成这样的项目目录：

```
my-video/
├── meta.json
├── index.html
├── compositions/
│   ├── intro.html
│   └── captions.html
└── assets/
    └── video.mp4
```

> HyperFrames 项目结构

### 图 3：`index.html` 在编辑器中

`index.html` 就是一个普通 HTML 文件。带 `data-*` 属性的元素，就是"时间轴里的一段素材"。

> HyperFrames index.html 编辑器视图

### 图 4：浏览器里的 preview

跑 `npx hyperframes preview`，会启动一个本地 Studio，浏览器自动打开 `http://localhost:3002`。你一边改 `index.html`，浏览器一边自动热更新。

> HyperFrames Studio 预览

### 图 5：GSAP 时间轴

HyperFrames 默认用 GSAP 做动画。你写一个 `paused: true` 的 timeline，注册到 `window.__timelines`，渲染器就能 seek 到任意时间点。

> GSAP timeline 在 HyperFrames 中的位置

### 图 6：Catalog 目录

`npx hyperframes add flash-through-white`、`npx hyperframes add data-chart`，可以把现成的转场、覆盖层、图表装到项目里。

> HyperFrames Catalog

### 图 7：render 输出

跑 `npx hyperframes render`，命令行会逐帧告诉你渲染进度。

> HyperFrames render 控制台输出

### 图 8：生成的 MP4

渲染完成后，你会在项目根目录拿到一个 `output.mp4`。1080p、30fps、时长精确等于你 `data-duration` 的总和。

> HyperFrames render 输出的 MP4

### 图 9：AI Agent 里的 `/hyperframes` 路由

在 Claude Code / Cursor / Gemini CLI / Codex 里装好 skills 之后，输入 `/hyperframes`，会触发一个意图路由器：它会根据你的输入（产品 URL / 普通网站 / GitHub PR / 一段话题 / 一段口播视频）自动选 workflow。

> AI Agent 中的 /hyperframes 路由

### 图 10：从 prompt 到 MP4 的完整流水线

从"用一句话描述想要的视频"，到"拿到 MP4 文件"，HyperFrames 大约会经过这 7 步：**DESIGN → SCRIPT → STORYBOARD → LAYOUT → BUILD → VALIDATE → RENDER**。

> HyperFrames 7 步流水线

## 3. 新手需要知道的五个关键词

| 关键词 | 通俗解释 | 为什么重要 |
|---|---|---|
| `data-*` 属性 | 写在元素上的"时间属性"（开始 / 持续 / 轨道） | HyperFrames 的定时全靠它 |
| GSAP timeline | 一个 `{ paused: true }` 的 JS 时间轴 | 动画的"剧本"，可被 seek |
| `class="clip"` | 标记元素受时间轴管理 | 漏写会变静态元素 |
| render | `npx hyperframes render` 把 HTML 烘成 MP4 | 整个框架的"出片"动作 |
| AGENTS.md | 写在项目根目录的"给 Agent 看的说明书" | 第二次提醒它同一件事时，就该写进去 |

如果暂时只能记住一个词，记住 **`data-*`**。HyperFrames 改完 `index.html` 之后，不要只看预览，要看 diff，因为 diff 才是它真正改了什么。

## 4. 选入口：AI Agent 还是 CLI？

HyperFrames 有两种主流用法。多数新手卡在不知道从哪里开始这一步。

| 入口 | 适合人群 | 主要用法 |
|---|---|---|
| **AI Agent 路线（推荐）** | 新手 / 不想碰代码 / 想"动嘴做视频" | 在 Claude Code / Cursor / Codex 里跑 `/hyperframes`，用中文描述视频 |
| **CLI 手动路线** | 会写 HTML/CSS/JS 的开发者 / 想精确控制每一帧 | 自己写 `index.html`，跑 `init / preview / render` |

我的推荐很简单：

- **新手用 AI Agent 路线**。让 Claude Code 或 Cursor 帮你写 HTML，你负责提需求和审稿。
- **会写代码的开发者用 CLI 手动路线**。`npx hyperframes init my-video && npx hyperframes preview && npx hyperframes render`，一气呵成。

下面这两条都会讲到。

## 5. 第一次使用：先把"家伙"备齐

### 5.1 装 Node.js 22+

HyperFrames 要求 Node.js 22 或更高版本。先检查一下：

```bash
node --version
```

如果低于 v22，去 [nodejs.org](https://nodejs.org) 下载最新 LTS。

### 5.2 装 FFmpeg

FFmpeg 是 HyperFrames 本地渲染的"发动机"，负责把逐帧的截图烘成 MP4。

```bash
# macOS
brew install ffmpeg

# Ubuntu / Debian
sudo apt install ffmpeg

# Windows
winget install Gyan.FFmpeg
```

装完确认一下：

```bash
ffmpeg -version
```

看到 `ffmpeg version 7.x` 就 OK。

### 5.3 装好之后，三选一进入

**路线 A（推荐）：AI Agent 路线**

在 Claude Code / Cursor / Gemini CLI / Codex 里跑：

```bash
npx skills add heygen-com/hyperframes
```

选 **"core set"**（核心 7 个 skill）就够了。装完直接在编辑器里输入 `/hyperframes`，用中文描述你想做的视频。

**路线 B：CLI 手动路线**

```bash
npx hyperframes init my-video
cd my-video
npx hyperframes preview
```

浏览器自动打开 `http://localhost:3002`，你看到的就是 Studio 预览界面。

## 6. 第一条提示词：用 `/hyperframes` 描述想要的视频

新手最常见的坑，是上来就这样问：

> 帮我做个 30 秒的抖音爆款。

> 帮我做一段完整的宣传片。

> 帮我把所有数据都做成可视化。

这种任务太宽，你自己也很难判断 AI 做得对不对。

更安全的顺序是这样——**先用一句话、零约束地试一次**：

```
/hyperframes
帮我做一个 10 秒的产品介绍视频，标题淡入，背景深色，配一首轻 BGM。
```

看到 AI 给出的方案之后，再决定要不要继续。

如果想更稳一点，可以先让它"读模板"：

```
/hyperframes
请先不要修改任何文件。先告诉我 my-video 这个项目的 index.html 是怎么组织的。
如果有不清楚的地方，请直接说"不确定"，不要编。
```

核心思想只有一句：**先读，不急着改**。

## 7. 第一次改代码：只改 `index.html` 的一行

熟悉了 AI 对项目的理解之后，让它做一个非常小的修改。

第一次的好目标是 `index.html` 里那段 `Hello, Hyperframes!`：

```
/hyperframes
请只修改 index.html，把那段文字改成"晚枫出品"，不要动其他任何文件。
```

AI 改完之后，自己做两件事：

```bash
git status
git diff
```

或者直接在编辑器里看 diff 面板。

### 看 diff 时要看什么？

- AI 是否动了你没允许它动的文件？
- 是否新增了你没要的依赖？
- 是否删掉了原本的 GSAP 引用？
- `data-*` 属性的语义对不对？
- diff 是否真的支撑了它在总结里讲的话？

作为新手，不需要马上看懂每一行代码。先学会"看动了哪些文件"，这一招就能避免一大半问题。

## 8. 可以直接抄的提示词模板

### 8.1 通用结构

```
目标：我想要一段什么样的视频？
上下文：参考链接、参考视频、风格样片、目标受众
范围：可以改哪些文件？绝对不能动哪些文件？
约束：不要加新依赖、不要改 GSAP 版本、不要动 compositions/ 目录外的素材
验证：跑 npx hyperframes preview，并对比改前改后
输出：列出改了哪些文件、preview 中的视觉变化、render 后的成片大小
```

这个结构很朴素，但很有用，因为它能减少"猜"的成分。

### 8.2 读模板模板

```
/hyperframes
请暂时不要修改文件。先帮我理解这个项目：
1. 这个项目大致是做什么的？
2. index.html 的结构是什么样的？
3. 用了哪些 GSAP 动画？
4. 如果我想跑起来，要执行哪些命令？
5. 哪些地方你不确定？请直接说"不确定"，不要猜。
```

### 8.3 改一段视频模板

```
/hyperframes
我想在 0:03 处加一段 5 秒的产品介绍文字：
- 位置：屏幕正下方 20%
- 动画：从下方滑入，停留 3 秒，淡出
- 不要改 GSAP 引用
- 不要引入新的 CSS 库
- 改完告诉我你改了什么
```

### 8.4 加效果模板

```
/hyperframes
请加一个转场效果：
- 在两段视频之间，0.5 秒的"闪光淡入"
- 可以从 Catalog 里挑现成的块（npx hyperframes add）
- 不要重复实现已经存在的转场
- 改完跑一下 preview，把过渡帧截图给我看
```

### 8.5 评审模板

```
/hyperframes
请评审当前未提交的改动：
1. data-* 属性是否完整（start / duration / track-index）
2. class="clip" 是否漏写
3. GSAP timeline 是否注册到 window.__timelines
4. 是否有可以换成 Catalog 块的重复实现
5. 输出 5 条以内的高优先级建议，不要修改任何文件
```

### 8.6 截图 / 样片参考模板

HyperFrames 支持图片输入。对于"想抄某个视频风格"的场景，可以把参考样片截图 / 设计稿作为上下文一起提供。

```
/hyperframes
请按附带的截图复刻风格：
- 沿用项目现有技术栈
- 字体、配色、间距尽量贴近截图
- 不要引入新的 UI 库
- 完成后告诉我用哪个命令预览
```

## 9. 安全使用：权限、沙箱、审批与隐私

HyperFrames 能读文件、改文件、跑命令，所以安全边界很重要。

### 9.1 给新手的权限建议

| 模式 | 适合做什么 | 给新手的建议 |
|---|---|---|
| **只读 / 解释** | 解释项目、读模板、写方案 | 先用这个 |
| **小幅修改** | 改 `index.html` 一行、跑 preview | 接受前看 diff |
| **完整访问** | 跨目录、复杂 catalog 调用、批量渲染 | 不要把它当默认起点 |

### 9.2 遇到审批弹窗怎么办

当 AI 请求"要不要跑这条命令"时，先看它到底想干什么。下面这些动作要特别小心：

```bash
rm -rf
sudo
curl ... | sh
npm install 你不认识的包
访问项目以外的目录
```

不确定时，选范围更窄的那个选项，或者拒绝，然后让 AI 解释为什么需要这条命令。

### 9.3 不要把这些秘密交给 HyperFrames

下面这些东西，不要直接粘到项目里、提示词里、日志里或截图里：

- API Key
- 数据库密码
- 生产环境令牌
- 客户隐私数据
- 个人敏感信息
- 公司内部不允许外传的资料
- 生产数据库连接串

报错日志要特别小心，里面可能藏着令牌、Cookie、URL 参数或数据库连接信息。粘贴之前先扫一眼。

### 9.4 改之前先打 Git 检查点

在项目目录里执行：

```bash
git add .
git commit -m "checkpoint before hyperframes task"
```

HyperFrames 改完之后再跑：

```bash
git status
git diff
```

万一出问题，Git 给你留了一条退路。

如果你还不熟悉 Git，记住一句话就够：**在重要的项目里，不要在没有备份的情况下让 AI 做大幅改动**。

## 10. 新手 7 天练习计划

### 第 1 天：跑通 init → preview → render

```bash
npx hyperframes init my-first-video
cd my-first-video
npx hyperframes preview
npx hyperframes render --output first.mp4
```

**目标**：先弄清楚"从 0 到一段 MP4"具体是怎么发生的。

### 第 2 天：让 AI 读模板

```
/hyperframes
请不要修改任何文件。解释这个项目：index.html 怎么组织、GSAP 怎么用、render 走什么流程。
```

**目标**：熟悉 AI 怎么读 HyperFrames 项目。

### 第 3 天：只改一行

```
/hyperframes
请只修改 index.html 中那段 h1 文案，不要动其他任何文件。
```

**目标**：练习审阅 diff。

### 第 4 天：用 Catalog 加一个效果

```bash
npx hyperframes add flash-through-white
```

```
/hyperframes
在两段视频之间加上刚装的 flash-through-white 块。
```

**目标**：学会"装现成块"。

### 第 5 天：换一段 BGM

```
/hyperframes
把 assets/music.wav 换成 assets/calm-piano.mp3，
确保 data-duration 与新音频一致，不要动 GSAP。
```

**目标**：学会"换素材不动代码"。

### 第 6 天：让 AI 评审你的改动

```
/hyperframes
请评审当前未提交的改动，关注 data-* 属性完整性、class="clip" 是否漏写、是否能换 Catalog。
暂时不要修改文件，只输出评审意见。
```

**目标**：把 AI 当作多一双眼睛。

### 第 7 天：试一下完整工作流

```
/hyperframes
我的产品页是 https://example.com，帮我做一段 30 秒的产品宣传片。
```

**目标**：让 AI 自动选 `product-launch-video` 工作流，端到端跑一次。

## 11. 进阶：用 AGENTS.md 让 HyperFrames 认识你的项目

经常用 HyperFrames 之后，可以考虑在项目根目录加一个 `AGENTS.md` 文件。

把它当成一份**写给 AI Agent 看的项目说明书**。AI 在开始工作之前会读这些约定，从而更贴合你们团队的规范。

示例：

```markdown
# AGENTS.md

## 项目约定
- 修改 index.html 后，请运行 npx hyperframes preview 截图对比。
- 在用户确认之前，不要新增 catalog 块以外的依赖。
- 修改 GSAP timeline 时，请同步更新 README 里的"动画清单"。
- 最终总结里，请列出改了哪些文件、preview 截图、render 输出路径。

## 命令约定
- 跑 render 前必须先 npx hyperframes validate。
- 出片统一放 ./output/ 目录。
- 不要直接覆盖历史 output，使用带时间戳的文件名。

## 资源约定
- BGM 统一放 assets/audio/。
- 视频片段统一放 assets/clips/。
- 封面图放 assets/covers/，命名格式 {slug}-cover-{ratio}.png。

## 禁止
- 不要 rm -rf 项目根目录以外的内容。
- 不要 npm install 未确认的包。
```

适合写进 `AGENTS.md` 的内容：

- 启动 / render 命令；
- preview 截图对比规范；
- 命名 / 目录约定；
- 绝对不能动的目录；
- 视频命名与归档规则；
- review 流程；
- 输出分辨率与帧率默认。

一个实用的判据：**当你不得不第二次提醒 AI 同一件事时，就该考虑把它写进 AGENTS.md**。

## 12. 常见问题

### Q1：我不会写代码，可以用 HyperFrames 吗？

可以，但要从"解释项目""读模板""换一行文案""装一个 Catalog 块"这类任务开始。不要一上来就让它做完整宣传片。

把 AI 当学习助手，但它改完 `index.html` 之后，你仍然要看 diff、看 preview、看 render 输出。

### Q2：到底用 AI Agent 路线还是 CLI 手动路线？

新手先用 AI Agent 路线。会写 HTML/CSS/JS 的人用 CLI 手动路线。需要批量 / CI 集成时，直接调 `npx hyperframes render`。

### Q3：AI 改错了怎么办？

先看 diff。不满意就让它再调整。如果项目已经被改乱，用 Git 回滚。

如果你还没学 Git，先在练习项目上练，再在重要项目里做大幅改动。

### Q4：AI 让我批准一条命令，要不要同意？

**只批准你能看懂的命令。**

特别留意这些场景：删除文件、安装依赖、访问项目之外的目录、从网络下载、执行脚本。

不懂的时候，可以这样问 AI："请解释一下这条命令是做什么的，为什么必要，有没有更安全的做法。"

### Q5：一定要 Node 22+ 吗？

是的。低于 Node 22 跑 `npx hyperframes` 会直接报错。

### Q6：能渲染 4K 吗？需要 GPU 吗？

可以。`npx hyperframes render` 支持任意分辨率（在 `data-width` / `data-height` 里指定）。本地不需要 GPU；如果走 Docker 模式可以保证完全可复现。

### Q7：商用 / 版权？

HyperFrames 是 Apache 2.0 开源协议，可商用，无单帧 / 单 render 计费。商用前注意 BGM / 字体 / 视频片段的版权。

## 最后

开始用 HyperFrames 的正确方式，**不是**一把帮我把整个宣传片做好。

**而是**：先 init → 看模板 → 改一行 → 看 diff → 跑 preview → 跑 render → 审片 → 迭代。

任务小一点、权限收紧一点、把验证讲明白，你就可以从第一天起，安全地用 HyperFrames + AI Agent 来做出能发布的视频。

---

用好 HyperFrames 这些书也推荐你看看👇

**《图解 Skill：AI 提效实战指南》**
宝玉｜著

知名 AI 应用专家宝玉结合自身实战经验，撰写了这本技能实操指南，旨在帮助你将个人经验转化为智能体可执行的技能，摆脱"AI 工具人"困境，真正实现工作自动化。作者手把手教你掌握：3 个单技能模板、1 条组合式写作工作流、1 套技能工程方法论、1 次从零开始完整迭代的技能项目实战。本书不绑定平台，扣子、Claude Code、OpenClaw 均可使用。也不要求读者具备编程基础，只要你想用 AI 提效，就可以通过本书学会技能，并立刻投入使用。

---

<p align="center">
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://cos.python-office.com/group%2Ffree-group.jpg" width="60%"/>
    </a>
</p>

扫码上图，直达晚枫 AI 学习群 👇

---

<p align="center" id='30讲自动化办公-banner'>
    <a target="_blank" href='https://www.python-office.com/video/video.html'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg" width="100%"/>
    </a>
</p>
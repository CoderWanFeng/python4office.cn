---
title: Codex 桌面端换皮肤：开源 Codex-Dream-Skin，0 基础 3 分钟搞定
date: 2026-07-15 14:00:00
tags:
  - Codex
  - Codex-Dream-Skin
  - 换皮肤
  - 主题皮肤
  - 桌面美化
  - 开源
  - QClaw
  - 开源管家
  - 零基础
  - 工具教学
categories: AI工具评测
cover: https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1200&auto=format&fit=crop
---

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260716170150990.png)

🎨 **Codex 桌面端终于能换皮肤了！**

今天讲一个**真正解决"办公桌审美疲劳"**的开源项目：[Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)。

获取开源项目的链接，直接在公众号的后台，发送命令：皮肤，24小时自动获取～

- 公众号：晚枫AI学习笔记

它能让你 **Codex 桌面端换皮肤**：6 套官方主题、任意图片背景、自定义配色，**而且不破坏官方安装，签名不变，随时能还原**。

配合 QClaw 「**开源管家**」，**0 基础 3 分钟搞定**。

<!-- more -->

先说结论：

**3 步搞定，全程在 QClaw 里聊天完成：**

1. 找到「开源管家」（QClaw 专家广场）：https://qclaw.qq.com/as/4VlrmxmvAnlV
2. 把 从公众号后台获取的 项目链接发给它
3. 让AI给你装依赖、运行项目，**全程不用懂原理**

下面手把手讲。

---

## 一、Codex-Dream-Skin 是干啥的？一句话讲清

**它是一个开源的 Codex 桌面端换肤工具。**

简单说，就是 **让你 Codex 桌面端的界面变好看、变个性**——还能换图、换配色、换字体。

| 维度 | Codex 默认 | 装了 Dream-Skin |
|------|------------|----------------|
| **背景** | 单色 | 可自定义图片 |
| **主题** | 2 套黑白 | 6+ 套风格主题 |
| **配色** | 跟随系统 | 完全可自定义 |
| **字体** | 默认 | 可换任意字体 |
| **图片** | 无 | 可传任何图（含动漫、风景）|
| **风格** | 死板 | 科幻 / 动漫 / 赛博朋克 / 极
![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260716170212282.png)
### 1.1 它解决什么痛点？

Codex 是 OpenAI 出品的 AI 编程工具，但你打开它会发现——**界面太单调了**。

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260716170241001.png)


如果你想：

- 🎨 给 Codex 换个深色主题
- 🌌 换张好看的背景图
- 🚀 改成 sci-fi 风格、动漫风格、赛博朋克风格
- 🔧 调整字体 / 配色 / 间距

**这些在 Codex 官方设置里都没法做**。

而 [Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin) 就是解决这个问题的——**让你 Codex 从此告别"默认灰"**。

### 1.2 它怎么做到"不破坏官方包"？

README 里写得很清楚：

| 特性 | 说明 |
|------|------|
| **本机回环 CDP 注入** | 用 Chrome DevTools 协议注入样式 |
| **不改官方安装目录** | 不动 `.app` / `app.asar` / WindowsApps |
| **不改代码签名** | 你的 Codex 仍然是官方正版 |
| **可一键还原** | 不想用了随时回到默认 |

**这意味着：用了这个工具，你的 Codex 不会失效，不会变成"黑户"**——它只是穿了件"好看的衣服"。

### 1.3 它支持什么主题？6 套皮肤免费试

仓库自带 **6 套官方主题皮肤**，开箱即用：

| # | 皮肤名 | 风格 | 适合 |
|---|--------|------|------|
| 1 | 🔴 **红白科幻** | 极简 + 暖色调 | 不喜黑白的人 |
| 2 | 🌊 **清透定制** | 清透 + 蓝色系 | 写 Python 的人 |
| 3 | 🌌 **灵感小宇宙** | 渐变 + 太空感 | 夜里写代码的人 |
| 4 | 🟣 **紫夜限定** | 深紫 + 神秘 | 喜欢氛围感的人 |
| 5 | 🎤 **初音未来** | 动漫 | 二次元 |
| 6 | ⚫ **舞台黑金** | 黑金 + 商务 | 正式场合 |

每套皮肤都是 **一张背景图 + 一套配色方案 + 一套字体方案**，**装上就能直接用**。

你也可以：
- 把任意一张图片（自拍 / 宠物 / 风景）当背景
- 调主题主色（适合你的喜好吧）
- 换字体（系统装了就行）

**换皮肤 = 换一种写代码的心情。**

### 1.4 它支持哪些平台？

| 平台 | 入口 | 难度 |
|------|------|------|
| **macOS（Apple Silicon + Intel）** | 双击 `Install Codex Dream Skin.command` | ⭐ |
| **Windows** | PowerShell 脚本 | ⭐⭐ |

如果是懂技术的朋友，现在可以拿到项目去玩起来了！

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260716170315016.png)


直接在公众号的后台，发送命令：皮肤，24小时自动获取～

- 公众号：晚枫AI学习笔记

如果是不懂技术的朋友，下面讲怎么用 QClaw「开源管家」全自动装。

---

## 二、什么是 QClaw「开源管家」？

**「开源管家」** 是 QClaw 里的一个 Skill，专门给"不会用 GitHub 的人"用的：

> 我在QClaw发现一个超好用的「开源管家」:https://qclaw.qq.com/as/4VlrmxmvAnlV

你给它一个 **GitHub 仓库 URL**，它会一步一步带你**克隆、装依赖、运行**——**全程不用懂原理**。

它的本质是：

```
你：把项目链接发我，里面装啥？
开源管家：……
     1. 检查你的 Node.js 版本
     2. git clone 这个仓库
     3. cd 到目录
     4. 装依赖
     5. 启动
     6. 怎么用
```

**你只要复制粘贴命令 + 看着它跑完就行**。

---

## 三、3 步实战：用开源管家给 Codex 换皮肤

### 3.1 第 1 步：找到「开源管家」

打开你的 **QClaw 客户端**（或者微信扫 QClaw 入口），进入"**专家广场**"或"**Skill 库**"，搜索"**开源管家**"，点击添加。

然后在对话窗口里输入：

```
你：帮我跑一下这个 GitHub 项目，我想给 Codex 桌面端换皮肤：公众号后台获取项目链接
```

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260716170442085.png)
### 3.2 第 2 步：按它的引导一步步走

**「开源管家」会问你 4-5 个问题**：

**问题 1：你的项目路径？**
```
你：~/Code/codex-dream-skin
```
（Mac 路径，Windows 改成 `D:\codex-dream-skin`）

**问题 2：你的 Codex 装在哪？**
- Mac：`/Applications/Codex.app`
- Mac（Homebrew）：`/usr/local/Caskroom/codex`
- Windows：`C:\Users\你的用户名\AppData\Local\Programs\Codex`

**问题 3：你用 Mac 还是 Windows？**
```
你：Mac
```

**问题 4：你的 Codex 正在运行吗？**
```
开源管家：先关掉 Codex 的桌面端，否则会冲突。
你：（关掉 Codex，回到 QClaw）
开源管家：已关闭，现在可以继续。
```

**问题 5：是否需要先安装 Node.js？**
- 如果你以前没装过 Node.js，**让它帮你装**（它会自动跑 `brew install node` 或 Windows 的 msi 安装包）。
- 如果你已经装了，让它**用现有的**。

### 3.3 第 3 步：开源管家跑命令

开源管家会自动跑下面的命令，**你什么都不用动，看着它跑就行**：

```bash
# 1. 克隆仓库
git clone https://github.com/Fei-Away/Codex-Dream-Skin.git ~/Code/codex-dream-skin
cd ~/Code/codex-dream-skin

# 2. (Mac 用户)启动安装脚本
open macos/Install\ Codex\ Dream\ Skin.command

# 3. (Windows 用户)启动 PowerShell 脚本
powershell -ExecutionPolicy Bypass -File windows/scripts/install-dream-skin.ps1
powershell -ExecutionPolicy Bypass -File windows/scripts/start-dream-skin.ps1
```

**Mac 的最后一步**（这是精华）：脚本会让 Codex 启动一个**带有调试端口的实例**——一般是：
```bash
# 自动启动 Codex + 注入主题
codex --remote-debugging-port=9222
```

启动完成后，浏览器会弹出主题预览。你可以：

| 操作 | 结果 |
|------|------|
| **看到默认主题** | 安装成功 ✅ |
| **想换主题** | 去 `codex-dream-skin/skins/` 文件夹替换图片 |
| **想还原** | 重启 Codex 就行 |

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260716170521370.png)
---

## 四、5 个常见问题（开源管家答不上来时的兜底）

### 4.1 Q：还没开通Codex ？

**A**：加我开通：aiwf365

### 4.2 Q：双击 `.command` 提示"无法打开，因为来自身份不明的开发者"？

**A**：macOS 安全机制。两种方法：

**方法 1：右键点击 → 打开**（不是双击）

**方法 2：在终端允许一次**：
```bash
chmod +x "macos/Install Codex Dream Skin.command"
xattr -d com.apple.quarantine "macos/Install Codex Dream Skin.command"
```

### 4.3 Q：PowerShell 提示"无法加载脚本，因为在此系统上禁止运行脚本"？

**A**：Windows 默认禁止 PowerShell 脚本。三种方法：

```powershell
# 方法 1：以管理员身份运行 PowerShell，然后：
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# 方法 2：临时绕过（不需要改设置）
powershell -ExecutionPolicy Bypass -File windows/scripts/install-dream-skin.ps1
```

### 4.4 Q：装完后主题没生效？

**A**：检查 3 件事：
1. Codex 是否跑在 `--remote-debugging-port=9222` 模式
2. 主题 CSS/JS 文件是否下载成功（断网会失败）
3. 重启一次 Codex

### 4.5 Q：升级 Codex 后主题失效？

**A**：正常。Codex 升级会清掉 CDP 配置，**重新跑一次 install 脚本**就行。

```bash
# Mac
open "macos/Install Codex Dream Skin.command"

# Windows
powershell -ExecutionPolicy Bypass -File windows/scripts/start-dream-skin.ps1
```

---

## 五、5 个进阶玩法

装上之后，5 个进阶玩法让你玩透：

### 5.1 换张图片做主题

```
你：我想把我的微信头像做成 Codex 背景，怎么做？
开源管家：
  1. 把图片放到 skins/default/ 目录
  2. 文件名命名为 cover.jpg（或对应主题的命名）
  3. 重启 Codex
搞定。
```

### 5.2 自定义配色

仓库的 `skins/` 目录下每个主题都有 `theme.json`，改它就行：

```json
{
  "name": "my-theme",
  "background": "cover.jpg",
  "primaryColor": "#FF5B1F",
  "font": "PingFang SC"
}
```

### 5.3 还原官方主题

终端跑：

```bash
# Mac
killall codex
open /Applications/Codex.app

# Windows
Stop-Process -Name "Codex" -Force
Start-Process "C:\Program Files\Codex\Codex.exe"
```

启动时**不传 `--remote-debugging-port` 参数**，就是官方默认主题。

### 5.4 多个主题切换

`skins/` 目录下可以放多个主题文件夹，**通过命令行参数切换**：

```bash
codex --remote-debugging-port=9222 --skin=my-theme
```

### 5.5 自己 fork 后加新主题

```
1. Fork 仓库
2. 在 skins/ 下新建 my-theme/ 目录
3. 加 cover.jpg + theme.json
4. 跑 npm install
5. 提交 PR，全世界都能用你的主题
```

---

## 六、底层的"安全边界"（小白也能看懂）

很多读者会担心——**"装这个会不会让我的 Codex 变黑户？"**

**答案是：不会。** 仓库作者在 README 里专门有一段"安全边界"：

| 做了 | 没做 |
|------|------|
| ✅ 只绑 `127.0.0.1`（本机回环） | ❌ 不改官方安装目录 |
| ✅ 不破坏代码签名 | ❌ 不上传 / 抓取你的 API Key |
| ✅ 一键还原官方外观 | ❌ 不修改 Codex 的 Base URL（中转） |

**简单说**：换肤和 API 配置是**完全独立的**两件事，**它不会改你的 API 设置**，**也不会盗你的 Key**。

但是有一个**安全提醒**：

⚠️ **使用期间，主题需要绑定 127.0.0.1 调试端口**。
这时候**不要跑来路不明的本机程序**，否则可能会被注入恶意代码。

简单说：**开启主题时，别开其他可疑工具**。

---

## 七、写在最后

**给 Codex 换皮肤，**

它**不破坏你的 Codex**、**不花一分钱**、**任何一天都能还原**，却能让你的开发桌从此告别"灰头土脸"。

Codex-Dream-Skin 只是一个起点。

类似的开源"桌面换肤"项目还有：

- ⚡ **OpenCode 主题定制**：让 OpenCode 命令行变好看
- 🎨 **AtomCode 主题包**：给 AtomCode 桌面端换皮肤
- 🔧 **WorkBuddy 自定义皮肤**：WorkBuddy 也支持

**只要你想让自己的工具变好看，开源世界就是你的。**

---

**👇 立刻试试**

👉 不懂技术别焦虑，在 QClaw 专家广场搜索"**开源管家**"：

有问题评论区告诉我，我帮你看。

我是晚枫，祝你玩得开心。

---

## 相关阅读

- [学AI编程别瞎忙！3步走，从零基础到能做实战项目](https://mp.weixin.qq.com/s/VXmJjQwsQlY-2IHjA3OAYA)
- [用上 OpenCode 的5 个免费大模型，省了我 200 刀 ChatGPT 年费](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [论文被查出AI率40%？我用AI反降AI率，导师直接过了](https://mp.weixin.qq.com/s/z0y3wByLzfI2JRMxAT2wpQ)
- [我的建站搭子skill，入职腾讯QClaw了！动动嘴就能建网站](https://mp.weixin.qq.com/s/XEe9yMpseRvMizhWcbnEoA)
- [最全AI Coding Plan和Token购买攻略：大厂价格一站汇总](https://mp.weixin.qq.com/s/Bk6d9bbSh5kSEd9i9dAahw)
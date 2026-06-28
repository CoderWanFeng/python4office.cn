---
title: "怎么用 npm 安装 OpenCode：完整图文教程"
date: 2026-06-26 22:25:00
tags: ["OpenCode", "npm", "Node.js", "教程", "AI工具"]
categories: ["AI工具", "教程"]
description: "零基础教程：用 npm 安装 OpenCode（开源 AI 编程助手），全程 4 步：装 Node → 装 OpenCode → 打开 → 配置大模型"
cover: https://images.unsplash.com/photo-1629654297299-c8506221a04b?q=80&w=1200&auto=format&fit=crop
---

大家好，我是程序员晚枫。

**今天这篇教程，专门写给完全没接触过 npm 的小白。**

**学会后，你也能在自己的电脑上跑 OpenCode（开源 AI 编程助手）。**

---

## 一、本教程适合谁？

✅ 完全没用过 npm 的小白
✅ 不想折腾、想直接上手的人
✅ 想要一份能照着做的图文教程

**看完后你会**：

- ✅ 装好 Node.js
- ✅ 用 npm 装 OpenCode
- ✅ 启动 OpenCode
- ✅ 配置自己的大模型（OpenAI / DeepSeek / Ollama 等）

---

## 二、准备工作

**在开始前，你需要**：

1. **一台电脑**（Windows / Mac / Linux 都行）
2. **20 分钟时间**
3. **稳定的网络**

---

## 三、第 1 步：安装 Node.js

> ⚠️ **这一步是关键**：npm 是 Node.js 自带的包管理工具，装了 Node.js 就有了 npm。

### 3.1 下载 Node.js

**官网地址**：https://nodejs.org/

📸 **截图位置**：Node.js 官网首页
<!-- TODO 截图：Node.js 官网首页截图 -->

**建议下载 LTS 版本**（长期支持版，最稳定）。

### 3.2 安装 Node.js

#### Windows 用户：

1. 双击下载的 `.msi` 文件
2. 一路点击 `Next`
3. 看到 `Install` 点击安装
4. 等待 2-3 分钟
5. 安装完成

#### Mac 用户：

1. 双击下载的 `.pkg` 文件
2. 一路点击 `继续`
3. 输入密码
4. 安装完成

#### Linux 用户：

```bash
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# CentOS/RHEL
curl -fsSL https://rpm.nodesource.com/setup_lts.x | sudo bash -
sudo yum install -y nodejs
```

### 3.3 验证安装

**打开终端**（Windows：`Win+R` → 输入 `cmd`；Mac：搜索 `Terminal`）

**输入以下命令**：

```bash
node -v
npm -v
```

📸 **截图位置**：终端验证截图
<!-- TODO 截图：终端验证 Node.js 和 npm 版本 -->

**应该看到**：

```
v22.x.x      ← Node.js 版本
10.x.x       ← npm 版本
```

✅ 看到版本号 = 安装成功

> ⚠️ **注意**：OpenCode 需要 Node.js v18.0.0 或更高版本，如果版本太低请重新安装最新的 LTS 版。

---

## 四、第 2 步：用 npm 安装 OpenCode

> 🎉 **恭喜！** Node.js 装好了，npm 也就有了。现在开始装 OpenCode。

### 4.1 打开终端

**Windows 用户**：
- 按 `Win + R`
- 输入 `cmd`
- 回车

**Mac 用户**：
- 按 `Command + 空格`
- 输入 `Terminal`
- 回车

### 4.2 全局安装 OpenCode

**在终端输入以下命令**：

```bash
npm install -g opencode-ai
```

📸 **截图位置**：npm install 命令执行中
<!-- TODO 截图：npm install -g opencode-ai 命令执行截图 -->

**这个命令的意思是**：

- `npm` = 用 npm 工具
- `install` = 安装
- `-g` = 全局（任何地方都能用）
- `opencode-ai` = OpenCode 这个包

### 4.3 等待安装

**安装过程大约 30 秒 - 2 分钟**：

```
added 1 package in 30s
```

✅ 看到 `added` 字样 = 安装成功

### 4.4 验证 OpenCode 安装

**输入以下命令**：

```bash
opencode --version
```

📸 **截图位置**：验证 OpenCode 版本
<!-- TODO 截图：opencode --version 命令执行截图 -->

**应该看到版本号**，例如：

```
0.10.0
```

✅ 看到版本号 = OpenCode 装好了

### 4.5 安装失败的解决方法

#### 问题 1：`EACCES: permission denied`

**Windows 解决方法**：用管理员身份打开 cmd

**Linux/Mac 解决方法**：

```bash
sudo npm install -g opencode-ai
```

#### 问题 2：`command not found: npm`

**原因**：Node.js 没装好，或没加入 PATH。

**解决方法**：重新装 Node.js，安装时勾选 `Add to PATH`。

#### 问题 3：国内下载很慢

**解决方法**：切换 npm 国内镜像

```bash
npm config set registry https://registry.npmmirror.com
```

然后重新安装。

#### 问题 4：Node.js 版本太低

**解决方法**：升级到 Node.js v18.0.0 以上版本。

---

## 五、第 3 步：启动 OpenCode

### 5.1 进入项目目录

**先进入你想让 OpenCode 工作的项目目录**：

```bash
cd your-project
```

比如：

```bash
cd D:\MyProject
```

### 5.2 启动 OpenCode

**在终端输入**：

```bash
opencode
```

📸 **截图位置**：OpenCode 启动后界面
<!-- TODO 截图：opencode 启动后的主界面截图 -->

**第一次启动会**：

- 自动分析项目
- 生成 `AGENTS.md` 文件
- 显示欢迎界面

### 5.3 初始化项目（推荐）

**OpenCode 启动后，建议执行初始化**：

```
/init
```

📸 **截图位置**：/init 命令执行
<!-- TODO 截图：/init 命令执行截图 -->

**这一步会**：

- 让 OpenCode 理解你的项目
- 生成 `AGENTS.md` 文件
- 后续 commit 到 Git

---

## 六、第 4 步：配置自己的大模型

> 🎯 **最关键的一步**：配置好 API Key，OpenCode 才能正常工作。

### 6.1 两种配置方式

#### 方式 1：使用 /connect 命令（最简单）

**在 OpenCode 中输入**：

```
/connect
```

📸 **截图位置**：/connect 命令截图
<!-- TODO 截图：/connect 命令执行截图 -->

**步骤**：

1. 选择 `opencode`（官方推荐的 OpenCode Zen）
2. 浏览器会打开 https://opencode.ai/auth
3. 注册并登录
4. 添加付款信息
5. 复制 API Key
6. 粘贴回终端

**这个方式的好处**：

- ✅ 经过 OpenCode 团队测试验证
- ✅ 中文支持好
- ✅ 模型质量高

#### 方式 2：手动配置环境变量（推荐高级用户）

**使用场景**：

- 想用 OpenAI / DeepSeek / Ollama 等其他模型
- 国内用户想用国内模型
- 想用本地模型

##### 配置 OpenAI：

**Mac / Linux 用户**：

```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxxx"
```

**Windows PowerShell 用户**：

```powershell
$env:OPENAI_API_KEY="sk-xxxxxxxxxxxxx"
```

##### 配置 DeepSeek（国内推荐）：

**Mac / Linux 用户**：

```bash
export OPENAI_BASE_URL="https://api.deepseek.com/v1"
export OPENAI_API_KEY="sk-xxxxxxxxxxxxx"
```

**Windows PowerShell 用户**：

```powershell
$env:OPENAI_BASE_URL="https://api.deepseek.com/v1"
$env:OPENAI_API_KEY="sk-xxxxxxxxxxxxx"
```

##### 配置 Ollama（本地模型）：

**Mac / Linux 用户**：

```bash
export OPENAI_BASE_URL="http://localhost:11434/v1"
export OPENAI_API_KEY="ollama"
```

##### 永久配置（推荐）：

Mac / Linux 用户，把环境变量写入 shell 配置文件：

```bash
# Bash 用户
echo 'export OPENAI_API_KEY="sk-xxxxxxxxxxxxx"' >> ~/.bashrc
source ~/.bashrc

# Zsh 用户
echo 'export OPENAI_API_KEY="sk-xxxxxxxxxxxxx"' >> ~/.zshrc
source ~/.zshrc
```

### 6.2 验证配置

**输入一个测试问题**：

```
How is authentication handled in this project?
```

📸 **截图位置**：测试对话截图
<!-- TODO 截图：OpenCode 中发送测试消息的截图 -->

**如果 AI 正常回复 = 配置成功！** 🎉

---

## 七、5 大常见错误及解决

### 错误 1：`command not found`

**原因**：OpenCode 没装好

**解决**：

```bash
npm install -g opencode-ai
```

### 错误 2：`No API key found`

**原因**：环境变量没配置

**解决**：

- 检查 `OPENAI_API_KEY` 环境变量是否设置
- 重新打开终端，让环境变量生效

### 错误 3：初始化失败

**原因**：项目目录权限不足

**解决**：

- 用管理员权限运行
- 或切换到有写权限的目录

### 错误 4：连接超时

**原因**：网络问题或 API 配置错误

**解决**：

- 检查网络是否稳定
- 检查 `OPENAI_BASE_URL` 是否正确
- 尝试切换到国内代理

### 错误 5：权限错误

**Windows 解决**：用管理员身份运行终端

**Linux/Mac 解决**：

```bash
sudo npm install -g opencode-ai
```

---

## 八、5 大使用技巧

### 技巧 1：常用命令

| 命令 | 说明 |
|------|------|
| `opencode` | 启动 OpenCode |
| `opencode --version` | 查看版本 |
| `/connect` | 连接大模型 |
| `/init` | 初始化项目 |
| `/help` | 查看帮助 |
| `@文件名` | 模糊搜索文件 |

### 技巧 2：用 `@` 引用文件

**在问题中用 `@` 引用项目文件**：

```
How is authentication handled in @packages/functions/src/api/index.ts
```

📸 **截图位置**：@ 引用文件
<!-- TODO 截图：@ 文件引用截图 -->

**好处**：

- AI 准确理解项目结构
- 回答更精准

### 技巧 3：Plan 模式（先规划后执行）

**按 `Tab` 键切换到 Plan 模式**：

📸 **截图位置**：Plan 模式
<!-- TODO 截图：Plan 模式截图 -->

**Plan 模式的好处**：

- AI 先给出修改方案
- 不会直接改代码
- 适合复杂功能开发

### 技巧 4：定期更新 OpenCode

```bash
npm update -g opencode-ai
```

📸 **截图位置**：升级命令执行
<!-- TODO 截图：npm update -g opencode-ai 命令执行截图 -->

**建议每月更新一次**。

### 技巧 5：commit AGENTS.md 到 Git

**初始化后生成的 `AGENTS.md` 应该 commit 到 Git**：

```bash
git add AGENTS.md
git commit -m "chore: add AGENTS.md for OpenCode"
```

**好处**：

- 团队成员都能用上 OpenCode
- 项目规范统一

---

## 九、卸载 OpenCode

**不再需要时**：

```bash
npm uninstall -g opencode-ai
```

**卸载会**：

- 删除 OpenCode 包
- 保留 npm 本身
- **保留**项目中的 `AGENTS.md`（如果想下次再用）

如果想**完全清理**，手动删除 AGENTS.md：

```bash
rm AGENTS.md
```

---

## 十、4 大安装方式对比

OpenCode 官方提供了 4 种安装方式：

| 安装方式 | 适合人群 | 是否需要 Node.js |
|---------|---------|----------------|
| **Desktop App** | 普通用户 / 非开发者 | ❌ |
| **curl 一行命令** | macOS / Linux 用户 | ❌ |
| **Homebrew / 系统包管理器** | 熟悉包管理器的用户 | ❌ |
| **npm / bun** | 前端 / Node.js 开发者 | ✅ |

**本教程重点讲的是 npm 方式**，适合前端/Node.js 开发者。

**如果你想用其他方式**：

- **Desktop App**：去 https://opencode.ai 下载桌面版
- **curl 方式**：`curl -fsSL https://opencode.ai/install | bash`
- **Homebrew**：`brew install opencode`

---

## 十一、最后的最后

**4 步总结**：

1. **装 Node.js**：去官网下载 LTS 版（v18+）
2. **装 OpenCode**：`npm install -g opencode-ai`
3. **启动**：终端输入 `opencode`
4. **配置大模型**：用 `/connect` 或环境变量

**整个过程不超过 20 分钟**。

---

## 相关阅读

- [2026 年学习编程，你需要的不是更多教程](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)
- [我用AI做PPT，同事说你是PPT设计师吗](https://mp.weixin.qq.com/s/aLo7mW3BLnglwhSZCKoOow)
- [设计师花3天做的图，我用 AI 15分钟搞定了](https://mp.weixin.qq.com/s/BQZUEFVCWhx8lLDaQsbRTg)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [HR看简历只花6秒，我用AI让我的简历过了第一关](https://mp.weixin.qq.com/s/XD8bk9Wf6p47HEoP8h84RQ)
- [我用AI做数字人播报，老板问"你什么时候请的主持人？"](https://mp.weixin.qq.com/s/7vngGHvX-HxIsUsQHGp1Dw)

---

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！
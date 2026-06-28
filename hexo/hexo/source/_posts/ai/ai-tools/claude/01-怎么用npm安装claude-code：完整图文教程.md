---
title: 怎么用 npm 安装 Claude Code：完整图文教程
date: 2026-06-26 22:12:36
tags:
  - Claude
  - Claude Code
  - npm
  - Node.js
  - 教程
  - AI工具
categories:
  - AI工具
  - 教程
description: 零基础教程：用 npm 安装 Claude Code（@anthropic-ai/claude-code），全程 4 步：装 Node → 装 Claude Code → 打开 → 配置大模型
cover: https://images.unsplash.com/photo-1629654297299-c8506221a04b?q=80&w=1200&auto=format&fit=crop
---

![](https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/20260627215850758.png)


大家好，我是程序员晚枫。

**今天这篇教程，专门写给完全没接触过 npm 的小白。**

**学会后，你也能在自己的电脑上跑 Claude Code（Anthropic 官方 AI 编程助手）。**

---

## 一、本教程适合谁？

✅ 完全没用过 npm 的小白
✅ 不想折腾、想直接上手的人
✅ 想要一份能照着做的图文教程

**看完后你会**：

- ✅ 装好 Node.js
- ✅ 用 npm 装 Claude Code
- ✅ 启动 Claude Code
- ✅ 配置自己的大模型（官方 API 或国内代理）

---

## 二、准备工作

**在开始前，你需要**：

1. **一台电脑**（Windows / Mac / Linux 都行）
2. **20 分钟时间**
3. **稳定的网络**

---

## 三、第 1 步：安装 Node.js

> ⚠️ **这一步是关键**：npm 是 Node.js 自带的包管理工具，装了 Node.js 就有了 npm。

### 1.1 下载 Node.js

**官网地址**：https://nodejs.org/



**建议下载 LTS 版本**（长期支持版，最稳定）。

### 1.2 安装 Node.js

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

### 1.3 验证安装

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

---

## 四、第 2 步：用 npm 安装 Claude Code

> 🎉 **恭喜！** Node.js 装好了，npm 也就有了。现在开始装 Claude Code。

### 2.1 打开终端

**Windows 用户**：
- 按 `Win + R`
- 输入 `cmd`
- 回车

**Mac 用户**：
- 按 `Command + 空格`
- 输入 `Terminal`
- 回车

### 2.2 全局安装 Claude Code

**在终端输入以下命令**：

```bash
npm install -g @anthropic-ai/claude-code
```

📸 **截图位置**：npm install 命令执行中
<!-- TODO 截图：npm install -g @anthropic-ai/claude-code 命令执行截图 -->

**这个命令的意思是**：

- `npm` = 用 npm 工具
- `install` = 安装
- `-g` = 全局（任何地方都能用）
- `@anthropic-ai/claude-code` = Anthropic 官方的 Claude Code 包

### 2.3 等待安装

**安装过程大约 30 秒 - 2 分钟**：

```
added 1 package in 30s
```

✅ 看到 `added` 字样 = 安装成功

### 2.4 验证 Claude Code 安装

**输入以下命令**：

```bash
claude --version
```

📸 **截图位置**：验证 Claude Code 版本
<!-- TODO 截图：claude --version 命令执行截图 -->

**应该看到版本号**，例如：

```
1.0.0
```

✅ 看到版本号 = Claude Code 装好了

### 2.5 安装失败的解决方法

#### 问题 1：`EACCES: permission denied`

**Windows 解决方法**：用管理员身份打开 cmd

**Linux/Mac 解决方法**：

```bash
sudo npm install -g @anthropic-ai/claude-code
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

---

## 五、第 3 步：启动 Claude Code

### 3.1 进入项目目录

**先进入你想让 Claude 工作的项目目录**：

```bash
cd your-project
```

比如：

```bash
cd D:\MyProject
```

### 3.2 启动 Claude Code

**在终端输入**：

```bash
claude
```

📸 **截图位置**：Claude Code 启动后界面
<!-- TODO 截图：claude 启动后的主界面截图 -->

**第一次启动会**：

- 显示欢迎界面
- 询问是否信任目录
- 可能弹出浏览器让你登录

### 3.3 信任工作目录

**首次启动时，Claude Code 会问你**：

```
Do you trust the files in this folder?
```

📸 **截图位置**：信任目录的提问
<!-- TODO 截图：信任目录的提问截图 -->

**选择**：按 `y` 然后回车

### 3.4 登录（首次使用）

**如果弹出浏览器，按提示登录**：

📸 **截图位置**：Claude Code 登录页面
<!-- TODO 截图：Claude Code 登录页面截图 -->

**支持的登录方式**：

- ✅ **Claude Pro/Max 订阅**（个人用户）
- ✅ **Claude for Teams/Enterprise**（团队用户）
- ✅ **Anthropic Console**（API 按量付费）

💡 如果浏览器没自动打开，按 `c` 键复制登录链接，手动粘贴到浏览器。

---

## 六、第 4 步：配置自己的大模型

> 🎯 **最关键的一步**：配置好 API Key，Claude Code 才能正常工作。

### 4.1 两种配置方式

#### 方式 1：使用官方 API Key（推荐海外用户）

**适用人群**：

- 有 Anthropic Console 账户
- 能访问 Anthropic 官方服务

**配置步骤**：

**Mac / Linux 用户**，在终端输入：

```bash
export ANTHROPIC_API_KEY="sk-ant-xxxxxxxxxxxxx"
```

**Windows PowerShell 用户**：

```powershell
$env:ANTHROPIC_API_KEY="sk-ant-xxxxxxxxxxxxx"
```

**Windows CMD 用户**：

```cmd
set ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

**永久配置**（推荐）：

Mac / Linux 用户，把环境变量写入 shell 配置文件：

```bash
# Bash 用户
echo 'export ANTHROPIC_API_KEY="sk-ant-xxxxxxxxxxxxx"' >> ~/.bashrc
source ~/.bashrc

# Zsh 用户
echo 'export ANTHROPIC_API_KEY="sk-ant-xxxxxxxxxxxxx"' >> ~/.zshrc
source ~/.zshrc
```

#### 方式 2：使用国内代理（推荐国内用户）

**适用人群**：

- 国内用户
- 没有 Anthropic 账户
- 想要稳定访问

**配置步骤**：

**Mac / Linux 用户**：

```bash
export ANTHROPIC_BASE_URL="https://your-proxy-url.com"
export ANTHROPIC_API_KEY="your-proxy-key"
```

**Windows PowerShell 用户**：

```powershell
$env:ANTHROPIC_BASE_URL="https://your-proxy-url.com"
$env:ANTHROPIC_API_KEY="your-proxy-key"
```

#### 方式 3：使用配置文件（最推荐）

**配置文件位置**：

- **Mac / Linux**：`~/.claude/settings.json`
- **Windows**：`C:\Users\你的用户名\.claude\settings.json`

📸 **截图位置**：配置文件路径
<!-- TODO 截图：配置文件路径截图 -->

**配置内容**（使用官方 API）：

```json
{
  "env": {
    "ANTHROPIC_API_KEY": "sk-ant-xxxxxxxxxxxxx"
  }
}
```

**配置内容**（使用代理）：

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://your-proxy-url.com",
    "ANTHROPIC_AUTH_TOKEN": "your-proxy-key",
    "API_TIMEOUT_MS": "3000000"
  }
}
```

📸 **截图位置**：配置文件内容
<!-- TODO 截图：配置文件内容截图 -->

### 4.2 验证配置

**输入一个测试命令**：

```bash
claude "你好，请用一句话介绍你自己"
```

📸 **截图位置**：测试对话截图
<!-- TODO 截图：Claude Code 中发送测试消息的截图 -->

**如果 AI 正常回复 = 配置成功！** 🎉

---

## 七、5 大常见错误及解决

### 错误 1：`command not found`

**原因**：Claude Code 没装好

**解决**：

```bash
# 重新安装
npm install -g @anthropic-ai/claude-code
```

### 错误 2：`connection error`

**原因**：网络问题或 API 配置错误

**解决**：

- 检查 API Key 是否正确
- 检查网络是否稳定
- 检查 BASE_URL 是否正确

### 错误 3：登录失败

**原因**：国内访问海外服务受限

**解决**：使用国内代理服务（看上面的方式 2、3）

### 错误 4：环境变量没生效

**原因**：终端未重新启动

**解决**：

- **关闭所有终端**
- **重新打开终端**
- 再次输入 `claude --version`

### 错误 5：权限错误

**Windows 解决**：用管理员身份运行终端

**Linux/Mac 解决**：

```bash
sudo npm install -g @anthropic-ai/claude-code
```

---

## 八、5 大使用技巧

### 技巧 1：常用命令

| 命令 | 说明 |
|------|------|
| `claude` | 启动 Claude Code |
| `claude --version` | 查看版本 |
| `/login` | 登录 |
| `/logout` | 登出 |
| `/help` | 查看帮助 |

### 技巧 2：环境变量优先级

**生效优先级**（从高到低）：

1. `settings.json` 配置文件
2. shell 配置文件（`.bashrc` / `.zshrc`）
3. 当前终端会话的临时环境变量

**建议**：统一在 `settings.json` 配置，便于管理。

### 技巧 3：定期更新 Claude Code

```bash
npm update -g @anthropic-ai/claude-code
```

📸 **截图位置**：升级命令执行
<!-- TODO 截图：npm update -g @anthropic-ai/claude-code 命令执行截图 -->

**建议每月更新一次**。

### 技巧 4：配置多个模型

**可以在 `settings.json` 中配置多个模型**：

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://your-proxy-url.com",
    "ANTHROPIC_AUTH_TOKEN": "your-key",
    "ANTHROPIC_MODEL": "claude-sonnet-4-5",
    "ANTHROPIC_SMALL_FAST_MODEL": "claude-haiku-4-5"
  }
}
```

### 技巧 5：使用 cc-switch 工具

**cc-switch 是第三方配置切换工具**：

```bash
npm install -g cc-switch
cc-switch
```

📸 **截图位置**：cc-switch 界面
<!-- TODO 截图：cc-switch 工具界面截图 -->

**好处**：

- 多账号切换
- 多模型切换
- 可视化配置

---

## 九、卸载 Claude Code

**不再需要时**：

```bash
npm uninstall -g @anthropic-ai/claude-code
```

**卸载会**：

- 删除 Claude Code 包
- 保留 npm 本身
- **保留** `settings.json` 配置文件（如果你想下次再用）

如果想**完全清理**，手动删除配置文件：

```bash
rm -rf ~/.claude
```

---

## 十、最后的最后

**4 步总结**：

1. **装 Node.js**：去官网下载 LTS 版
2. **装 Claude Code**：`npm install -g @anthropic-ai/claude-code`
3. **启动**：终端输入 `claude`
4. **配置 API Key**：填到环境变量或 settings.json

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
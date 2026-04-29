---
title: 飞书 CLI 办公 Skill 快速上手：19个官方Skill让AI接管你的工作
date: 2026-04-06 10:34:00
tags: [飞书, CLI, Lark, Skill, AI办公, 教程]
categories: [AI Skills, 平台攻略]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<p align="center">
    <a target="_blank" href='https://github.com/larksuite/lark-cli'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
    </a>
</p>

<!-- more -->

大家好，我是正在实战各种 AI 项目的程序员晚枫。

**2026 年 3 月 28 日**，飞书官方正式开源 **Lark CLI**——这是一个专为 AI Agent 设计的命令行工具。装上它，你的 AI（如 Claude Code、Cursor）就能直接操控飞书的日历、文档、多维表格、消息等全部核心功能。

这意味着什么？**你的 AI 助手终于能真正"进入"你的办公系统了。**

---

## 一、飞书 CLI 是什么？

### 一句话解释
飞书 CLI 是飞书官方提供的**命令行接口**，把飞书开放平台的 2500+ API 封装成了 200+ 个命令，让 AI Agent 可以通过自然语言指令直接操作飞书。

### 核心特点
| 特点 | 说明 |
|---|---|
| 🚀 AI Agent 原生适配 | 内置 19 个 Agent Skills，主流大模型无需额外学习 |
| 📦 200+ 命令 | 覆盖消息、文档、日历、邮件等 11 大业务域 |
| 🔓 开源免费 | MIT 协议，可商用、可二次开发 |
| 🔒 安全可靠 | 官方出品，数据安全有保障 |

### 适合谁用？
- 飞书重度用户（企业、团队）
- 想用 AI 自动化飞书办公流程的人
- 开发者（可基于 CLI 开发自定义工具）

---

## 二、安装飞书 CLI

### 环境要求
- macOS / Linux / Windows
- Node.js 16+（推荐）或 Go 1.20+

### 安装方式

**方式 1：npm 安装（推荐）**
```bash
npm install -g @larksuite/lark-cli
```

**方式 2：Homebrew（macOS）**
```bash
brew install larksuite/tap/lark-cli
```

**方式 3：直接下载**
```bash
# macOS
curl -L https://github.com/larksuite/lark-cli/releases/latest/download/lark-cli-darwin-amd64 -o lark-cli
chmod +x lark-cli
sudo mv lark-cli /usr/local/bin/

# Linux
curl -L https://github.com/larksuite/lark-cli/releases/latest/download/lark-cli-linux-amd64 -o lark-cli
chmod +x lark-cli
sudo mv lark-cli /usr/local/bin/
```

### 验证安装
```bash
lark-cli --version
# 输出：lark-cli version 1.0.0
```

---

## 三、配置飞书 CLI

### 步骤 1：创建飞书应用
1. 访问 [飞书开放平台](https://open.feishu.cn/)
2. 登录后点击 "创建企业自建应用"
3. 填写应用名称（如：AI 办公助手）
4. 记录 **App ID** 和 **App Secret**

### 步骤 2：配置权限
在应用后台，开启以下权限：
- `contact:contact:readonly`（读取通讯录）
- `im:chat:readonly`（读取群聊信息）
- `im:message:send`（发送消息）
- `docs:document:readonly`（读取文档）
- `docs:document:write`（编辑文档）
- `calendar:calendar:readonly`（读取日历）
- `calendar:calendar:write`（编辑日历）
- `bitable:bitable:app:readonly`（读取多维表格）
- `bitable:bitable:app:write`（编辑多维表格）

### 步骤 3：初始化配置
```bash
lark-cli config init
```
按提示输入：
- App ID
- App Secret
- 企业域名（如：yourcompany.feishu.cn）

### 步骤 4：验证配置
```bash
lark-cli user info
# 应显示当前登录用户信息
```

---

## 四、19 个官方 Agent Skills 详解

飞书 CLI 内置了 19 个 Agent Skills，分为 5 大类：

### 📨 消息类 Skills（4个）

| Skill | 功能 | 示例指令 |
|---|---|---|
| `message.send` | 发送消息 | "给张三发消息说会议改到3点" |
| `message.read` | 读取消息 | "查看研发群的最新消息" |
| `message.reply` | 回复消息 | "回复这条消息说收到" |
| `message.forward` | 转发消息 | "把这条消息转发给李四" |

### 📄 文档类 Skills（5个）

| Skill | 功能 | 示例指令 |
|---|---|---|
| `doc.create` | 创建文档 | "创建一个项目计划文档" |
| `doc.read` | 读取文档 | "读取产品需求文档" |
| `doc.edit` | 编辑文档 | "在文档末尾添加待办事项" |
| `doc.share` | 分享文档 | "把文档分享给项目组" |
| `doc.search` | 搜索文档 | "搜索包含'Q2规划'的文档" |

### 📅 日历类 Skills（3个）

| Skill | 功能 | 示例指令 |
|---|---|---|
| `calendar.create` | 创建日程 | "创建一个明天下午3点的会议" |
| `calendar.read` | 查看日程 | "查看我这周的日程安排" |
| `calendar.delete` | 删除日程 | "取消明天下午的销售会议" |

### 📊 多维表格类 Skills（4个）

| Skill | 功能 | 示例指令 |
|---|---|---|
| `bitable.read` | 读取表格 | "读取客户管理表格的数据" |
| `bitable.write` | 写入表格 | "在表格中添加一条新记录" |
| `bitable.update` | 更新表格 | "更新张三的跟进状态为'已签约'" |
| `bitable.query` | 查询表格 | "查询本月新增的客户数量" |

### 👥 通讯录类 Skills（3个）

| Skill | 功能 | 示例指令 |
|---|---|---|
| `user.search` | 搜索用户 | "查找研发部张三的联系方式" |
| `group.search` | 搜索群组 | "查找'产品周会'群聊" |
| `dept.list` | 部门列表 | "查看技术部的成员列表" |

---

## 五、在 AI 中使用飞书 CLI

### Claude Code 配置

**步骤 1：安装 Claude Code**
```bash
npm install -g @anthropic-ai/claude-code
```

**步骤 2：配置飞书 CLI 集成**
在 Claude Code 设置中添加：
```json
{
  "mcpServers": {
    "lark-cli": {
      "command": "lark-cli",
      "args": ["mcp", "start"]
    }
  }
}
```

**步骤 3：开始使用**
```
你：帮我查看今天的日程安排

Claude：我来帮你查看今天的日程。
🔧 Using tool: calendar.read
   date: 2026-04-06
   
📤 Result:
   今天有 3 个日程：
   1. 10:00 产品周会
   2. 14:00 客户演示
   3. 16:00 团队复盘
```

### Cursor 配置

在 Cursor 的 `.cursor/mcp.json` 中添加：
```json
{
  "mcpServers": {
    "lark": {
      "type": "stdio",
      "command": "lark-cli",
      "args": ["mcp"]
    }
  }
}
```

---

## 六、实战场景

### 场景 1：自动发送日报
```
你：帮我发送今天的日报到"研发部"群

AI：我来帮你发送日报。
🔧 Using tool: doc.read
   doc: 日报模板
🔧 Using tool: bitable.query
   table: 任务追踪表
   filter: 今日完成
🔧 Using tool: message.send
   to: 研发部群
   
📤 Result:
   日报已发送！
   今日完成任务：5个
   明日计划：3个
```

### 场景 2：自动安排会议
```
你：帮我安排一个明天下午的产品评审会，邀请张三、李四、王五

AI：我来帮你安排会议。
🔧 Using tool: user.search
   users: 张三, 李四, 王五
🔧 Using tool: calendar.create
   title: 产品评审会
   time: 明天 14:00-15:00
   attendees: 张三, 李四, 王五
🔧 Using tool: message.send
   to: 张三, 李四, 王五
   content: 会议邀请已发送
   
📤 Result:
   会议已创建，邀请已发送！
```

### 场景 3：自动整理文档
```
你：帮我把"项目资料"文件夹里的所有文档整理成一份汇总文档

AI：我来帮你整理文档。
🔧 Using tool: doc.search
   folder: 项目资料
   found: 10个文档
🔧 Using tool: doc.read (x10)
🔧 Using tool: doc.create
   title: 项目资料汇总
   content: [自动生成的汇总内容]
   
📤 Result:
   汇总文档已创建！
```

---

## 七、常见问题

### Q1：飞书 CLI 和飞书 API 有什么区别？
- **飞书 API**：需要写代码调用 2500+ 个接口
- **飞书 CLI**：把 API 封装成命令，AI 可以直接用自然语言调用

### Q2：数据安全吗？
- 飞书 CLI 是官方出品，数据不经过第三方
- 建议在企业内部网络使用
- 敏感操作可以设置二次确认

### Q3：可以自定义 Skill 吗？
可以。飞书 CLI 支持插件机制，可以开发自定义命令：
```bash
lark-cli plugin install ./my-plugin
```

### Q4：和其他平台 CLI 有什么区别？
| 平台 | 特点 |
|---|---|
| 飞书 CLI | 专注飞书生态，19个官方Skill |
| Google gws | 专注 Google Workspace |
| Microsoft Graph CLI | 专注 Microsoft 365 |

---

## 八、相关资源

- **GitHub 仓库**：https://github.com/larksuite/lark-cli
- **官方文档**：https://open.feishu.cn/document/cli
- **飞书开放平台**：https://open.feishu.cn/

---

## 九、下一步学习

- [《飞书 CLI 自定义 Skill 开发指南》](/ai-skills/skill-dev/feishu-cli-custom-skill/)
- [《Coze 扣子 Skill 商店全攻略》](/ai-skills/platform-guides/coze-skill-guide/)
- [《OpenClaw Skill 安装与管理指南》](/ai-skills/platform-guides/openclaw-skill-guide/)

---

## 💬 加入交流群

飞书 CLI 使用问题？加群交流：

👉 **[加入AI编程学习交流群](https://www.python4office.cn/wechat-group/)**

![点击加入](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

---

*飞书 CLI 的开源，标志着 AI Agent 正式接管办公系统的时代来临。19 个官方 Skills 只是开始，更多可能等你探索！*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



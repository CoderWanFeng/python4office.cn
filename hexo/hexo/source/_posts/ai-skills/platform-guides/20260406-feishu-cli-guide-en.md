---
title: "Feishu CLI Office Skill Quick Start: 19 Official Skills Let AI Take Over Your Work"
date: 2026-04-06 10:34:00
tags: [Feishu, CLI, Lark, Skill, AI Office, Tutorial]
categories: [AI Skills, Platform Guide]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<p align="center">
    <a target="_blank" href='https://github.com/larksuite/lark-cli'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
    </a>
</p>

<!-- more -->

![Feishu CLI Office Skill Quick Start: 19 Official Skills Let AI Take Over Your Work - 配图1](https://images.unsplash.com/photo-1456513?w=800&h=400&fit=crop)


Hello everyone, I'm Programmer Wanfeng,实战 various AI projects.

**March 28, 2026**, Feishu officially open-sourced **Lark CLI** - a command-line tool designed specifically for AI Agents. With it installed, your AI (like Claude Code, Cursor) can directly control Feishu's calendar, documents, bitable, messages and all core functions.

What does this mean? **Your AI assistant can finally truly "enter" your office system.**

---

## 1. What is Feishu CLI?

### One Sentence Explanation
Feishu CLI is Feishu's officially provided **command-line interface**, encapsulating Feishu open platform's 2500+ APIs into 200+ commands, allowing AI Agents to directly operate Feishu through natural language instructions.

### Core Features
| Feature | Description |
|---|---|
| 🚀 AI Agent Native | Built-in 19 Agent Skills, mainstream LLMs need no extra learning |
| 📦 200+ Commands | Cover message, document, calendar, email and other 11 major business domains |
| 🔓 Open Source Free | MIT license, can be used commercially, can be secondary developed |
| 🔒 Safe and Reliable | Official product, data security guaranteed |

### Who is it for?
- Heavy Feishu users (enterprises, teams)
- People who want to automate Feishu office workflows with AI
- Developers (can develop custom tools based on CLI)

---

## 2. Install Feishu CLI

### Environment Requirements
- macOS / Linux / Windows
- Node.js 16+ (recommended) or Go 1.20+

### Installation Methods

**Method 1: npm install (recommended)**
```bash
npm install -g @larksuite/lark-cli
```

**Method 2: Homebrew (macOS)**
```bash
brew install larksuite/tap/lark-cli
```

**Method 3: Direct download**
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

### Verify Installation
```bash
lark-cli --version
# Output: lark-cli version 1.0.0
```

---

## 3. Configure Feishu CLI

### Step 1: Create Feishu App
1. Visit [Feishu Open Platform](https://open.feishu.cn/)
2. After logging in, click "Create Enterprise Self-built App"
3. Fill in app name (e.g.: AI Office Assistant)
4. Record **App ID** and **App Secret**

### Step 2: Configure Permissions
In app backend, enable the following permissions:
- `contact:contact:readonly` (read contacts)
- `im:chat:readonly` (read group chat info)
- `im:message:send` (send messages)
- `docs:document:readonly` (read documents)
- `docs:document:write` (edit documents)
- `calendar:calendar:readonly` (read calendar)
- `calendar:calendar:write` (edit calendar)
- `bitable:bitable:app:readonly` (read bitable)


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



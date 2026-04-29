---
title: "Lecture 10: Feishu CLI Platform Deep Dive"
date: 2026-04-06 16:00:00
tags: ["AI Skill", "Feishu", "CLI", "Enterprise"]
categories: ["AI Skills Course"]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---

<!-- more -->

![Lecture 10: Feishu CLI Platform Deep Dive - 配图1](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)
![Lecture 10: Feishu CLI Platform Deep Dive - 配图2](https://images.unsplash.com/photo-151707730?w=800&h=400&fit=crop)

# Lecture 10: Feishu CLI Platform Deep Dive

> Master enterprise-level Skill platform Feishu CLI, develop team collaboration Skills.

## 1. Feishu CLI Introduction

### 1.1 What is Feishu CLI?

Feishu CLI is Feishu's open **AI Agent Skill development framework**:
- ✅ Deep integration with Feishu ecosystem
- ✅ Enterprise-level permission management
- ✅ Native support for group chat, approval, calendar
- ✅ Just open-sourced on March 28 (bonus period)

### 1.2 Core Capabilities

| Capability | Description | Scenario |
|------|------|------|
| **Group Chat Bot** | Interact in group chats | Team assistant |
| **Approval Integration** | Connect approval flows | Automated approval |
| **Calendar Operations** | Manage schedules | Meeting assistant |
| **Document Collaboration** | Operate Feishu documents | Knowledge management |
| **Bitable** | Operate Bitable | Data management |

---

## 2. Environment Setup

### 2.1 Install Feishu CLI

```bash
# Install
npm install -g @larksuite/cli

# Verify
feishu --version
```

### 2.2 Initialize Project

```bash
# Create project
feishu init my-feishu-skill

# Select template
cd my-feishu-skill
```

### 2.3 Project Structure

```
my-feishu-skill/
├── skill.json          # Skill configuration
├── index.js            # Main entry
├── handlers/           # Event handlers
│   ├── message.js      # Message handling
│   ├── command.js      # Command handling
│   └── event.js        # Event handling
├── utils/              # Utility functions
└── package.json
```

---

## 3. Develop Your First Feishu Skill

### 3.1 Configuration File

```json
// skill.json
{
  "name": "team-assistant",


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



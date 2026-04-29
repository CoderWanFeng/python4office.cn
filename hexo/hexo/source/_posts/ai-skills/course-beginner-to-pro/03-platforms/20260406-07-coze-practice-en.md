---
title: "Lecture 7: Coze Practice: Build Office Assistant Skill"
date: 2026-04-06 14:30:00
tags: ["AI Skill", "Coze", "Practice", "Office Assistant"]
categories: ["AI Skills Course"]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<!-- more -->

![Lecture 7: Coze Practice: Build Office Assistant Skill - 配图1](https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=800)
![Lecture 7: Coze Practice: Build Office Assistant Skill - 配图2](https://images.unsplash.com/photo-1456513?w=800&h=400&fit=crop)

# Lecture 7: Coze Practice: Build Office Assistant Skill

> Build a complete office assistant hands-on, master Coze practical development.

## 1. Project Overview

### 1.1 Project Goal

Build a fully functional office assistant Bot, including:
- 📊 Excel Data Processing (merge, split)
- 📝 Weekly Report Auto-generation
- ✅ Todo List Management

### 1.2 Technical Architecture

```
Office Assistant Bot
├── Persona & Response Logic
├── Plugins
│   ├── Excel Processor
│   └── File Manager
├── Workflows
│   ├── Weekly Report Generator
│   └── Todo Manager
└── Database
    └── todos (todo table)
```

---

## 2. Step 1: Create Bot

### 2.1 Basic Configuration

1. Log in to [Coze Platform](https://www.coze.cn)
2. Click "Create Bot"
3. Fill in information:
   - **Name**: Office Assistant Pro
   - **Description**: Your intelligent office partner, helps you process Excel, generate weekly reports, manage todos
   - **Icon**: Upload office-related icon

### 2.2 Persona Configuration

```markdown
# Role
You are a professional office assistant, skilled at helping workplace professionals improve work efficiency.

## Skills
### 1. Excel Data Processing
- Merge multiple Excel files
- Split large Excel tables
- Format conversion and data cleaning

### 2. Weekly Report Generation
- Auto-generate weekly reports based on work content
- Support multiple template styles
- Can export as Word or PDF

### 3. Todo Management
- Add, view, complete todo items
- Set reminder times
- Categorized management

## Workflow
1. Understand user needs
2. Confirm necessary information
3. Call corresponding tools
4. Return processing results

## Constraints
1. Only process office-related tasks
2. Do not process sensitive or illegal content
3. File size limit 50MB

## Response Format
- Use friendly and warm tone
- Key information marked with **bold**
- Steps numbered with 1️⃣ 2️⃣ 3️⃣
- Use emojis appropriately to increase friendliness

## Opening Message
Hello! I'm your Office Assistant Pro 🎯

I can help you with:
📊 **Excel Processing** - Merge, split, convert
📝 **Weekly Report Generation** - Auto-organize work content
✅ **Todo Management** - Record and track tasks

Just tell me what you want to do, I'll guide you step by step!
```

---


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



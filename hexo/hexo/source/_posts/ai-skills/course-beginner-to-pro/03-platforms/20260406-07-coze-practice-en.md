---
title: "Lecture 7: Coze Practice: Build Office Assistant Skill"
date: 2026-04-06 14:30:00
tags: ["AI Skill", "Coze", "Practice", "Office Assistant"]
categories: ["AI Skills Course"]
---

<!-- more -->
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

---
title: "Daily Report Auto-Generation Skill Configuration Tutorial: Save 30 Minutes Every Day"
date: 2026-04-06 10:44:00
tags: [Daily Report, Automation, Skill, AI Office, Work Report, Tutorial]
categories: [AI Skills, Skill Tutorial]
cover: https://images.unsplash.com/photo-1677442136019-235d647109c6?q=80&w=1200&auto=format&fit=crop
---

<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
</p>

<!-- more -->

![Daily Report Auto-Generation Skill Configuration Tutorial: Save 30 Minutes Every Day - 配图1](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)


Hello everyone, I'm Programmer Wanfeng, practicing various AI projects.

What's the most painful thing every day before getting off work? **Writing daily reports** - recalling what you did today, organizing data, writing summaries, at least 30 minutes.

Today I teach you how to configure **Daily Report Auto-Generation Skill**, let AI automatically help you summarize data and generate daily reports.

---

## 1. Skill Introduction

### Function Overview
Daily Report Auto-Generation Skill can:
- ✅ Automatically summarize task management tool data (Feishu tasks/DingTalk/Notion, etc.)
- ✅ Automatically read calendar events
- ✅ Automatically count code commits/Git records
- ✅ Automatically read email/message summaries
- ✅ Generate structured daily report documents
- ✅ Scheduled automatic sending

### Applicable Crowd
| Crowd | Benefit |
|---|---|
| Programmers | Auto-summarize code commits, Bug fixes |
| Product Managers | Auto-summarize requirement progress, meeting records |
| Sales | Auto-summarize customer follow-ups, order data |
| Operations | Auto-summarize data reports, activity progress |
| Project Managers | Auto-summarize project progress, risk warnings |

---

## 2. Install Skill

### Coze Installation
1. Open [Coze Official Website](https://www.coze.cn)
2. Enter "Skill Store"
3. Search "Daily Report Generation" or "Work Report"
4. Click "Install"

### OpenClaw Installation
```bash
openclaw skills install daily-report
openclaw skills install calendar-tools
openclaw skills install git-tools
```

### Feishu CLI
Feishu CLI natively supports calendar, task, and document operations, can be directly used for daily report generation.

---

## 3. Configuration Tutorial

### Configuration 1: Connect Data Source

#### Connect Feishu Calendar
```
You: Connect my Feishu calendar, read today's meetings and schedule

AI: Connecting Feishu calendar...
🔧 Using skill: calendar-tools
   action: connect
   platform: feishu

📤 Result:
   Connection successful!
   Authorized to access calendar data
```

#### Connect Feishu Tasks
```
You: Connect Feishu tasks, read today's task completion status

AI: Connecting Feishu tasks...
🔧 Using skill: task-tools
   action: connect
   platform: feishu

📤 Result:
   Connection successful!
   Authorized to access task data
```

#### Connect Git (For Programmers)
```
You: Connect Git repository, read today's code commit records

AI: Connecting Git...


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



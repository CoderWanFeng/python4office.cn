---
title: "Lecture 11: Feishu CLI Practice: Team Collaboration Skill"
date: 2026-04-06 16:30:00
tags: ["AI Skill", "Feishu", "Practice", "Team Collaboration"]
categories: ["AI Skills Course"]
---

<!-- more -->
# Lecture 11: Feishu CLI Practice: Team Collaboration Skill

> Build an enterprise-level team collaboration Skill hands-on, master Feishu ecosystem development.

## 1. Project Goal

Develop "Team Butler" Skill, functions include:
- 📅 Smart meeting management
- ✅ Task assignment and tracking
- 📝 Daily report auto-collection
- 📊 Team data statistics

## 2. Function Design

### 2.1 Meeting Management

```
User: @Team Butler create weekly meeting
Skill: Sure! Creating weekly meeting:
      📅 Time: Next Monday 14:00 (default)
      👥 Participants: @everyone
      📍 Location: Online

      Reply "confirm" to confirm, reply with specific info to modify
```

### 2.2 Task Assignment

```
User: @Team Butler assign task
Skill: Please provide task info:
      1. Task content
      2. Person in charge (@member)
      3. Deadline

User: Complete requirements document @Zhangsan this Friday
Skill: ✅ Task assigned:
      📋 Complete requirements document
      👤 Person in charge: Zhangsan
      ⏰ Deadline: This Friday 18:00

      Zhangsan has been notified
```

## 3. Core Code

### 3.1 Meeting Management Module

```javascript
// handlers/meeting.js
const { CalendarAPI } = require('../utils/calendar');

class MeetingHandler {
  async createMeeting(ctx, params) {
    const { title, time, attendees } = params;

    // Create calendar event
    const event = await CalendarAPI.createEvent({
      summary: title,
      start: { dateTime: time },
      end: { dateTime: time + 3600000 },
      attendees: attendees.map(id => ({ email: id }))
    });

    // Send notification
    await ctx.sendMessage({
      content: `📅 Meeting created\nTitle: ${title}\nTime: ${formatTime(time)}`,
      mention: attendees
    });

    return event;
  }

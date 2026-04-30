---
title: "Lecture 4: Your First Skill: Hello World Practice"
date: 2026-04-06 13:00:00
tags: ["AI Skill", "Practice", "Coze", "Beginner"]
categories: ["AI Skills Course"]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<!-- more -->

![Lecture 4: Your First Skill: Hello World Practice](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)
![Lecture 4: Your First Skill: Hello World Practice](https://images.unsplash.com/photo-1517077304055-8e7232e8e848?w=800&h=400&fit=crop)

# Lecture 4: Your First Skill: Hello World Practice

> Create your first AI Skill hands-on, completing the leap from theory to practice.

---

## 1. Preparation

### 1.1 Register a Coze Account

1. Visit [https://www.coze.cn](https://www.coze.cn)
2. Register with phone number or Douyin account
3. Complete real-name authentication (if publishing to store)

### 1.2 Understand Coze Interface

```
┌─────────────────────────────────────────────────────────┐
│  Coze Workspace                                             │
├──────────────┬──────────────────────────────────────────┤
│              │                                              │
│   Sidebar    │              Edit Area                      │
│   ├── Team Space │          ┌─────────────────────┐       │
│   ├── Personal Space │      │   Persona & Response Logic │       │
│   ├── Plugins     │          │   ├── Role Setting    │       │
│   ├── Workflows   │          │   ├── Skill Config   │       │
│   └── Knowledge Base │       │   └── Opening Message │       │
│              │          └─────────────────────┘       │
│              │          ┌─────────────────────┐       │
│              │          │   Preview & Debug Area │       │
│              │          │   └── Right chat window │       │
│              │          └─────────────────────┘       │
└──────────────┴──────────────────────────────────────────┘
```

---

## 2. Create Your First Skill: Weather Assistant

### 2.1 Create Bot

1. Click "Create Bot"
2. Fill in basic information:
   - **Name**: Weather Assistant
   - **Description**: Helps you check weather for cities across China
   - **Icon**: Upload or select system icon
3. Click "Confirm"

### 2.2 Configure Persona & Response Logic

In the "Persona & Response Logic" area, enter:

```
# Role
You are a professional weather query assistant, able to accurately answer various weather-related questions.

## Skills
- Query real-time weather for specified cities
- Query 3-day weather forecast
- Provide clothing and travel advice

## Constraints
- Can only query weather for Chinese cities
- If user doesn't specify city, ask for their location
- Reply in Chinese, friendly and warm tone
```

### 2.3 Add Weather Query Plugin

1. Click "+" on the right side of "Plugins"
2. Search "weather"
3. Select "Moji Weather" or "Seniverse Weather" plugin
4. Click "Add"

### 2.4 Test Your Skill

In the right preview area, enter:

```
How's the weather in Beijing today?
```

Expected output:
```
Today's weather in Beijing is sunny, temperature 15-25°C, air quality is good, suitable for outdoor activities.
Suggested clothing: Light jacket + long sleeves
```

---

## 3. Advanced: Make Your Skill Smarter

### 3.1 Add Workflow

Create a new workflow "weather_workflow":

```
Start node
    ↓
Parameter extraction node (extract city name)
    ↓
Weather query plugin node (call weather API)
    ↓
Data processing node (format weather information)
    ↓
Suggestion generation node (generate clothing/travel suggestions)
    ↓
End node (return result)
```

### 3.2 Workflow Detailed Configuration

**Parameter extraction node:**

```python
# Use large model to extract parameters
prompt = """
Extract city name from user input:
User input: {{input}}

Return JSON format:
{
  "city": "City name",
  "date": "Date (today/tomorrow/day after tomorrow)"
}
"""
```

**Weather query node:**

```python
# Call Moji weather plugin
plugin: weather_moji
action: get_weather
params:
  city: {{city}}
  days: 3
```

**Suggestion generation node:**

```python
prompt = """
Based on the following weather information, generate clothing and travel suggestions:
City: {{city}}
Weather: {{weather}}
Temperature: {{temp_low}}°C - {{temp_high}}°C
Air quality: {{aqi}}

Please provide:
1. One-sentence weather summary
2. Clothing suggestions
3. Travel suggestions
"""
```

### 3.3 Bind Workflow to Bot

1. Return to Bot edit page
2. Add "weather_workflow" in the "Workflow" area
3. Add in "Persona & Response Logic":

```
When user asks about weather, call weather_workflow workflow to get weather information.
```

---

## 4. Code Implementation: Build Weather Skill from Scratch

If you want to implement with code, here's a complete example:

### 4.1 Project Structure

```
weather-skill/
├── main.py          # Main program
├── intent.py        # Intent recognition
├── weather_api.py   # Weather API wrapper
├── advisor.py       # Suggestion generation
└── requirements.txt # Dependencies
```

### 4.2 Core Code

**main.py**

```python
import json
from intent import IntentClassifier
from weather_api import WeatherAPI


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



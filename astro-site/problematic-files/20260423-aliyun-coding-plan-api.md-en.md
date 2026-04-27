---
title: "Alibaba Cloud Bailian Coding Plan API Tutorial: How Programmers Integrate Tongyi Qianwen Large Model"
keywords: [Alibaba Cloud Bailian API, Tongyi Qianwen API, AI Programming Integration, Programmer Wan Feng]
description: Programmer Wan Feng teaches you: Alibaba Cloud Bailian Coding Plan API integration tutorial, integrate Tongyi Qianwen in 3 steps, with code examples.
date: 2026-04-23 20:00:00
tags: [Alibaba Cloud, Bailian, Tongyi Qianwen, API Tutorial, AI Programming]
categories: [AI Programming, Tutorial]
---

<!-- more -->

> **Article Author: Programmer Wan Feng | AI Programming Evangelist | Focused on AI Tool Reviews and Teaching**

> 400k+ followers across platforms, 6 years Python development experience, author of open source project python-office

> 💡 **Technology is not high-cold, AI is very easy to use** 👉 **[Click to integrate Tongyi Qianwen](https://www.aliyun.com/benefit/scene/codingplan?scm=20140722.S_card@@%E6%B4%BB%E5%8A%A8@@4220167._.ID_card@@%E6%B4%BB%E5%8A%A8@@4220167-RL_codingplan-LOC_2024SPSearchCard-OR_ser-PAR1_2127e66a17744276040951204d0c48-V_4-RE_new13-P0_0-P1_0&source=5176.29345612&userCode=t6duaoe1)**

Hello everyone, this is programmer Wan Feng.

Today brings you **Alibaba Cloud Bailian API integration tutorial**, hand-holding you through integrating Tongyi Qianwen into your own projects.

## 1. Preparation

### 1. Activate Service

First make sure you've activated Alibaba Cloud Bailian Coding Plan:
**👉 [Click to activate](https://www.aliyun.com/benefit/scene/codingplan?scm=20140722.S_card@@%E6%B4%BB%E5%8A%A8@@4220167._.ID_card@@%E6%B4%BB%E5%8A%A8@@4220167-RL_codingplan-LOC_2024SPSearchCard-OR_ser-PAR1_2127e66a17744276040951204d0c48-V_4-RE_new13-P0_0-P1_0&source=5176.29345612&userCode=t6duaoe1)**

### 2. Get API-KEY

1. Enter Alibaba Cloud Bailian console
2. Find "API-KEY"
3. Create API-KEY, save it

## 2. API Call Examples

### Python Example

```python
import requests

# Configuration
api_key = "Your API-KEY"

# Call Tongyi Qianwen API
def call_qwen(prompt):
    url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "qwen-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()

# Usage
result = call_qwen("Help me write Python quicksort")
print(result)
```

### JavaScript Example

```javascript
// Node.js calls Tongyi Qianwen
const axios = require('axios');

async function callQwen(prompt) {
  const response = await axios.post(
    'https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions',
    {
      model: 'qwen-turbo',
      messages: [
        { role: 'user', content: prompt }
      ]
    },
    {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer Your API-KEY'
      }
    }
  );
  return response.data;
}

// Usage
const result = await callQwen('Help me write JS debounce function');
console.log(result);
```

## 3. Usage in E-commerce Projects
---

## 🎓 AI Programming Course

Want to learn AI programming systematically? Check out **CoderWanFeng's AI Programming Course**!

- 👉 **Enroll Now**: [Click here to sign up — first 3 lessons are free](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **Free Preview**: [Watch the first 3 lessons on Bilibili for free](https://www.bilibili.com/cheese/play/ss982042944)


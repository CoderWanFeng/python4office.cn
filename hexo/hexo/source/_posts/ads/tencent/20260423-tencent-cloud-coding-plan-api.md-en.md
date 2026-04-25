---
title: "Tencent Cloud Coding Plan API Tutorial: How Programmers Integrate Tencent Hunyuan Large Model"
keywords: [Tencent Cloud Coding Plan API, Tencent Hunyuan API, AI Programming Integration, 程序员晚枫]
description: Programmer Wan Feng teaches you: Tencent Cloud Coding Plan API integration tutorial, integrate Hunyuan in 3 steps, with code examples.
date: 2026-04-23 15:00:00
tags: [Tencent Cloud, Tencent Hunyuan, API Tutorial, AI Programming]
categories: [AI Programming, Tutorial]
---

<!-- more -->

> **Article Author: Programmer Wan Feng | AI Programming Evangelist | Focused on AI Tool Reviews and Teaching**
>
> 400k+ followers across platforms, 6 years Python development experience, author of open source project python-office

> 💡 **Technology is not high-cold, AI is very easy to use** 👉 **[Click to experience Tencent Hunyuan](https://curl.qcloud.com/Z9TkzRuj)**

Hello everyone, this is programmer Wan Feng.

Today brings you **Tencent Cloud Coding Plan API integration tutorial**, hand-holding you through integrating Hunyuan into your own projects.

## 1. Preparation

### 1. Activate Service

First make sure you've activated Tencent Cloud Coding Plan:
**👉 [Click to activate](https://curl.qcloud.com/Z9TkzRuj)**

### 2. Get Keys

1. Enter Tencent Cloud console
2. Find "Cloud API Keys"
3. Create keys, save SecretId and SecretKey

## 2. API Call Examples

### Python Example

```python
import requests

# Configuration
secret_id = "Your SecretId"
secret_key = "Your SecretKey"
region = "ap-guangzhou"

# Call Hunyuan API
def call_hunyuan(prompt):
    url = f"https://hunyuan.cloud.tencent.com/api/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "X-TC-Action": "ChatCompletions"
    }

    data = {
        "model": "hunyuan-pro",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    # Actually needs signature when used, simplified here
    response = requests.post(url, json=data, headers=headers)
    return response.json()

# Usage
result = call_hunyuan("Help me write Python quicksort")
print(result)
```

### JavaScript Example

```javascript
// Node.js calls Tencent Hunyuan
const axios = require('axios');

async function callHunyuan(prompt) {
  const response = await axios.post(
    'https://hunyuan.cloud.tencent.com/api/v1/chat/completions',

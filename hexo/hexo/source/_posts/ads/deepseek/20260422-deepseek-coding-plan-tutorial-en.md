---
title: "DeepSeek Coding Plan Tutorial: API Call + Local Deployment, 2 Ways to Play - Can't Learn Both? I'll Beat You"
date: 2026-04-22 19:25:00
tags: ["deepseek", "coding plan tutorial", "api call", "local deployment", "open source"]
categories: ["DeepSeek Practice"]
description: "Programmer Wan Feng teaches you hands-on how to play DeepSeek Coding Plan, 2 ways: API call and local deployment. There's always one suitable for you."
hreflang:
en: /20260422-deepseek-coding-plan-tutorial/
zh: /20260422-deepseek-coding-plan-tutorial/
canonical: /20260422-deepseek-coding-plan-tutorial/
translation: complete
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<!-- more -->

![DeepSeek Coding Plan Tutorial: API Call + Local Deployment, 2 Ways to Play - Can't Learn Both? I'll Beat You - 配图1](https://images.pexels.com/photos/8386440/pexels-photo-8386440.jpeg?auto=compress&cs=tinysrgb&w=800)
![DeepSeek Coding Plan Tutorial: API Call + Local Deployment, 2 Ways to Play - Can't Learn Both? I'll Beat You - 配图2](https://images.unsplash.com/photo-161160569?w=800&h=400&fit=crop)


Brothers!!!

DeepSeek Coding Plan tutorial is here.

I'm Programmer Wan Feng, 300k+ followers across platforms, author of the python-office open source project.

Today I'll teach you 2 ways to play:
1. **API Call** (simple and fast)
2. **Local Deployment** (save money and free)

Choose based on your situation.

---

## 🚀 Way 1: API Call

### Step 1: Get API Key

1. Visit DeepSeek official website
2. Register an account
3. Get API Key

### Step 2: Code Call

```python
import openai

# Configure DeepSeek API
openai.api_base = "https://api.deepseek.com"
openai.api_key = "your API Key"

# Call DeepSeek
response = openai.ChatCompletion.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Help me write a Python quicksort"}
    ]
)

print(response.choices[0].message.content)
```

### Step 3: Integrate with IDE

Supports VS Code, JetBrains and other mainstream IDEs.

---

## 💻 Way 2: Local Deployment

Recommended for those with some technical skills.

Benefits:
- No API call fees
- Completely private data
- Can be used offline

### Hardware Requirements

| Model Size | Minimum VRAM | Recommended Config |
|------------|--------------|-------------------|
| 7B | 6GB | GTX 1060+ |
| 13B | 12GB | RTX 3060+ |
| 33B | 24GB | RTX 4090+ |
| 67B | 48GB | Multi-card server |

### Deployment Steps

**1. Install Ollama**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**2. Download Model**
```bash
ollama pull deepseek-coder:6.7b
```

**3. Run**
```bash
ollama run deepseek-coder:6.7b
```

**4. Call**
```python
import openai

openai.api_base = "http://localhost:11434/v1"
openai.api_key = "ollama"

response = openai.ChatCompletion.create(
    model="deepseek-coder:6.7b",
    messages=[
        {"role": "user", "content": "Help me write a Python quicksort"}
    ]
)

print(response.choices[0].message.content)
```

---

## 📊 Comparison of Two Methods

| Dimension | API Call | Local Deployment |
|-----------|---------|-----------------|
| Difficulty | Low | Medium |
| Cost | API fees | One-time hardware investment |
| Data Security | Data on cloud | Completely private |
| Offline Available | ❌ | ✅ |
| Model Updates | Automatic | Manual |

---

## 🎯 How to Choose?

- Want to get started quickly → **API Call**
- Pursuing lowest cost → **Local Deployment**
- Have technical skills → **Local Deployment**
- Don't want to tinker → **API Call**

---

## 📚 Want to Learn More?

- [DeepSeek Coding Plan Introduction](https://www.python4office.cn/ads/deepseek/20260422-deepseek-coding-plan-intro/)
- [Who is DeepSeek Suitable For?](https://www.python4office.cn/ads/deepseek/20260422-deepseek-coding-plan-who-should-use/)
- [DeepSeek vs Claude Code, Which is Better?](https://www.python4office.cn/2026/20260422-deepseek-vs-claude/)

Also welcome to the "30 Lectures · AI Programming Training Camp" that I collaborated with Turing Community on. 30 systematic lectures + 15+ practical projects, I'll take you from 0 to 1 in mastering AI programming.

👉 [Click to view training camp details](https://www.python4office.cn/course/ai-related/posts-people/ads/260209-499/)

---

## 💡 Finally

The 2 ways to play DeepSeek have no superiority or inferiority, only suitability or unsuitability.

Just choose based on your situation.

I'm Programmer Wan Feng, see you next time.

---

*For more AI programming content, welcome to visit my website: https://www.python4office.cn/

---

## 🤖 Developer Efficiency Tool Recommendations

👉 Want to experience **MiniMax Token Plan**? [Click here for 10% discount](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

💡 **Pay-per-use, very cost-effective!** Imagine going to a vegetable market—buy a ticket to get in, and the vegetables are all yours. Charged per use, no limit on quota, pay for what you use. Perfect for developers!
---

## 🎓 AI Programming Course

Want to learn AI programming systematically? Check out **CoderWanFeng's AI Programming Course**!

- 👉 **Enroll Now**: [Click here to sign up — first 3 lessons are free](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **Free Preview**: [Watch the first 3 lessons on Bilibili for free](https://www.bilibili.com/cheese/play/ss982042944)


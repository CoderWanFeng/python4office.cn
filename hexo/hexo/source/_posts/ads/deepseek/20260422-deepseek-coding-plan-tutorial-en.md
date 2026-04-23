---
title: "DeepSeek Coding Plan Tutorial: API Call + Local Deployment, 2 Ways to Use It, If You Can't Learn You Can Blame Me"
date: 2026-04-22 19:25:00
tags: ["deepseek", "coding plan tutorial", "api call", "local deployment", "open source"]
categories: ["DeepSeek Practice"]
description: "Programmer Wanfeng teaches you how to use DeepSeek Coding Plan step by step, two ways: API call and local deployment, there's always one suitable for you."
---

<!-- more -->

Hey everyone!!!

The DeepSeek Coding Plan tutorial is here.

I'm Programmer Wanfeng, with over 300k followers across the web, author of the python-office open source project.

Today I'll tell you 2 ways to use it:
1. **API Call** (simple and fast)
2. **Local Deployment** (cost-saving and flexible)

Choose according to your situation.

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
openai.api_key = "Your API Key"

# Call DeepSeek
response = openai.ChatCompletion.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Write a quick sort in Python for me"}
    ]
)

print(response.choices[0].message.content)
```

### Step 3: Integrate with IDE

Supports mainstream IDEs such as VS Code, JetBrains, etc.

---

## 💻 Way 2: Local Deployment

For those with certain technical capabilities, local deployment is recommended.

Benefits:
- No API call fees
- Data is completely private
- Can be used offline

### Hardware Requirements

| Model Size | Minimum VRAM | Recommended Configuration |
|------------|--------------|---------------------------|
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
        {"role": "user", "content": "Write a quick sort in Python for me"}
    ]
)

print(response.choices[0].message.content)
```

---

## 📊 Comparison of Two Methods

| Dimension | API Call | Local Deployment |
|-----------|----------|------------------|
| Difficulty to Get Started | Low | Medium |
| Cost | API fees | One-time hardware investment |
| Data Security | Data in cloud | Completely private |
| Offline Available | ❌ | ✅ |
| Model Updates | Automatic | Manual |

---

## 🎯 How to Choose?

- Want to get started quickly → **API Call**
- Pursue lowest cost → **Local Deployment**
- Have technical capabilities → **Local Deployment**
- Don't want to hassle → **API Call**

---

## 📚 Want to Learn More?

- [DeepSeek Coding Plan Introduction](https://www.python4office.cn/ads/deepseek/20260422-deepseek-coding-plan-intro/)
- [Who Is DeepSeek Suitable For?](https://www.python4office.cn/ads/deepseek/20260422-deepseek-coding-plan-who-should-use/)
- [DeepSeek vs Claude Code: Which Is Better?](https://www.python4office.cn/2026/20260422-deepseek-vs-claude/)

You are also welcome to join the "30 Lectures · AI Programming Training Camp" that I collaborate on with Turing Community. 30 systematic courses + 15+ practical projects, I'll guide you to master AI programming from 0 to 1.

👉 [Click to view training camp details](https://www.python4office.cn/course/ai-related/posts-people/ads/260209-499/)

---

## 💡 Final Word

These two ways of using DeepSeek have no distinction between good and bad, only suitable or not.

Just choose according to your situation.

I'm Programmer Wanfeng, see you next time.

---

*For more AI programming content, welcome to visit my website: https://www.python4office.cn/

---

## 🤖 开发者效率工具推荐

👉 想体验 **MiniMax Token Plan**？[点击这里享受 9 折优惠](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

💡 **按次计费，非常划算！** 想象成去菜市场买菜——买张门票进去，菜随便拿。按使用次数收费，不限额度，用多少付多少，特别适合开发者！


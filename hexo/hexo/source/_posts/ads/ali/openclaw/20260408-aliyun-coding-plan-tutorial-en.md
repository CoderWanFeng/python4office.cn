---
title: Alibaba Cloud Coding Plan Usage Tutorial: Complete Guide from Subscription to Getting Started
date: 2026-04-08 00:41:00
tags: [Alibaba Cloud CodingPlan tutorial, how to use Bailian CodingPlan, Tongyi Qianwen programming, Alibaba Cloud AI programming introduction, CodingPlan configuration]
categories: [AI Programming, Tutorials]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<!-- more -->

![Alibaba Cloud Coding Plan Usage Tutorial: Complete Guide from Subscription to Getting Started](https://images.unsplash.com/photo-155849494?w=800&h=400&fit=crop)

Hello everyone, this is Programmer Wanfeng.

Bought Alibaba Cloud Coding Plan but don't know how to use it? Today's tutorial will teach you step by step, covering the complete process from subscription to getting started.

## 1. Subscribe to Coding Plan

### Step 1: Open the subscription page
Visit: [Alibaba Cloud Coding Plan Subscription Page](https://www.aliyun.com/benefit/scene/codingplan?userCode=t6duaoe1)

### Step 2: Choose a plan
- Pay-as-you-go: Suitable for light usage
- Monthly/Annual subscription: Suitable for heavy users, more cost-effective

### Step 3: Complete payment
Supports common payment methods such as Alipay and bank cards.

## 2. Get API Key

After successful subscription, you need to get an API Key to access various tools.

### Operation Steps

1. **Log in to Alibaba Cloud Bailian Console**
   Visit: https://bailian.console.aliyun.com/

2. **Enter the Coding Plan page**
   Find the "Coding Plan" product entry in the console

3. **Create API Key**
   - Click "API Key Management"
   - Click "Create API Key"
   - Give the Key a name (e.g., "For Cursor")
   - Copy and save the Key (note: Key is only displayed once)

4. **View available models**
   Alibaba Cloud Coding Plan supports multiple models:
   - Qwen3.5-Plus - Strong general capabilities
   - Qwen3-Max - Flagship model
   - Qwen3-Coder-Next - Specially optimized for programming
   - Qwen3-Coder-Plus - Code generation expert
   - Third-party models such as MiniMax M2.5, GLM-5, Kimi-k2.5, etc.

## 3. Access Common Tools

### Access Qwen Code (Official CLI Tool)

Qwen Code is a command-line AI programming tool officially launched by Alibaba Cloud.

#### Installation Steps

```bash
# Install Qwen Code
pip install qwen-code

# Verify installation
qwen --version
```

#### Configuration Steps

1. Open the terminal and enter:
   ```bash
   qwen auth
   ```

2. Paste your Alibaba Cloud Coding Plan API Key

3. Select the default model (Qwen3-Coder-Plus is recommended)

4. Start using:
   ```bash
   qwen "Write a Python function to read CSV files"
   ```

### Access Cursor

Cursor is one of the most popular AI programming IDEs currently.

#### Configuration Steps

1. Open Cursor settings (Settings)
2. Find the "Models" or "OpenAI API" option
3. Select "Add custom model"
4. Fill in the information:
   - **API Key**: Paste your Alibaba Cloud Coding Plan API Key
   - **Base URL**: `https://dashscope.aliyuncs.com/compatible-mode/v1`
   - **Model**: Select the model you want to use (e.g., `qwen3-coder-plus`)
5. Save settings and start using

### Access VS Code

If you use VS Code, you can install the Continue plugin.

#### Configuration Steps

1. Search for "Continue" in the VS Code extension store and install it
2. Open Continue settings
3. Add custom model:
   ```json
   {
     "models": [
       {
         "title": "Alibaba Cloud Tongyi Qianwen",
         "provider": "openai",
         "model": "qwen3-coder-plus",
         "apiKey": "Your API Key",
         "apiBase": "https://dashscope.aliyuncs.com/compatible-mode/v1"
       }
     ]
   }
   ```
4. Restart VS Code and start using

## 4. Model Selection Suggestions

Different scenarios are suitable for different models:

| Scenario | Recommended Model | Reason |
|----------|-------------------|--------|
| Daily code completion | Qwen3.5-Plus | Fast speed, strong general capabilities |
| Complex algorithms | Qwen3-Coder-Plus | High code generation quality |
| Chinese projects | Qwen3-Max | Best Chinese understanding |
| Rapid prototyping | Qwen3-Coder-Next | Special optimization for programming |
| Long text processing | Kimi-k2.5 | Long text expert |
| Creative programming | MiniMax M2.5 | Strong creative generation |

Speaking of this, let me share a personal example.

I usually use Qwen3-Coder-Plus for daily development, and switch to Qwen3-Max when encountering complex algorithm problems. One subscription covers all needs, which is very convenient.

## 5. Common Problem Solutions

### Q1: What if the API Key is invalid?
Check:
- Whether the Key is copied completely
- Whether the account balance is sufficient
- Whether the Key has been deleted or disabled

### Q2: Slow response speed?
Try:
- Switch to different models
- Check network connection
- Simplify request content

### Q3: Unsatisfactory code generation quality?
Suggestions:
- Try different models
- Optimize prompt description
- Provide more context

### Q4: How to check usage?
In the Alibaba Cloud Bailian Console, you can view:
- Token usage
- Number of calls
- Cost details

## 6. Advanced Tips

### Tip 1: Multi-model backup
Configure multiple models in the tool, so you can switch immediately if one has problems.

### Tip 2: Custom Prompts
Use different system Prompts for different scenarios to improve generation quality.

### Tip 3: Combine with Alibaba Cloud ecosystem
Coding Plan + Alibaba Cloud ECS + Alibaba Cloud OSS, double the efficiency.

## 7. Final Thoughts

Accessing Alibaba Cloud Coding Plan is actually very simple, the key is to try it yourself.

**Don't pursue perfect configuration, use it first, then optimize slowly.**

AI is a lever, not an opponent.

By the way, if you want to learn how to use AI tools more systematically, **on April 12 I will participate in Tencent Cloud Community's "Lobster Open Class" in Zhengzhou**, demonstrating on site how to configure Coding Plan and how to build a complete AI workflow.

Hands-on teaching on site is more intuitive than reading articles.

👉 **Registration link: https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg**

The choice is in your hands.

---

## 🎁 Bonus Time

I'll send you a "**Alibaba Cloud Coding Plan Configuration Template**":
- Qwen Code configuration template
- Cursor configuration template
- VS Code configuration template
- Recommended model parameter settings

👉 [Click to get it for free](https://www.python-office.com/openclaw/)

---

## 📚 Want to learn AI programming systematically?

<p align="center" id='AI编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png" width="80%"/>
    </a>   
</p>

"**30 Lectures · AI Programming Training Camp**" — Master AI programming practice from 0 to 1.

---

> Also, everyone go give Xiaoming's Xiaohongshu account below a like~!

[Xiaohongshu QR Code]

---

[Official Account QR Code]

---

**🧧 Get a red envelope before you leave~**

[Red Envelope QR Code]

---

Programmer Wanfeng, focuses on AI programming training, a Python programmer who switched from a law master's degree, author of the open source project [python-office](https://www.python-office.com/).

---

## 🎓 AI Programming Course

Want to learn AI programming systematically? Check out **CoderWanFeng's AI Programming Course**!

- 👉 **Enroll Now**: [Click here to sign up — first 3 lessons are free](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **Free Preview**: [Watch the first 3 lessons on Bilibili for free](https://www.bilibili.com/cheese/play/ss982042944)

---

## 🤖 Developer Productivity Tools

👉 Want to try **MiniMax Token Plan**? [Click here for 10% off](https://platform.minimaxi.com/subscribe/token-plan?code=8T7rWtR7CZ&source=link)

💡 **Pay-per-use pricing — super cost-effective!** Think of it like a farmers market: buy a ticket, and all the veggies are free. Pay based on actual usage, no limits, no monthly fees. Perfect for developers!
---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)

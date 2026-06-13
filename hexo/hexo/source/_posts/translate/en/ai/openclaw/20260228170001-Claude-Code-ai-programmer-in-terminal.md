---
title: "I Hired an AI Programmer in My Terminal. After 3 Days, I Was Alarmed."
date: 2026-02-28 17:00:00
tags: [AI Programming]
cover: https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop
translation:
  source: ai/openclaw/20260228170001-Claude-Code-终端里的AI程序员.md
  source_title: "我在终端里雇了一个AI程序员，3天后我慌了"
  status: completed
  translator: ai-claude-gpt4
  date: 2026-06-14
---

# I Hired an AI Programmer in My Terminal. After 3 Days, I Was Alarmed.

Hello, I'm Wanfeng, a programmer.

Last week, Anthropic released Claude Code, dubbed "the AI programmer that lives in your terminal."

As a 10-year veteran coder, my first reaction was: **Yet another toy?**

After 3 days of using it, I started to panic—**this thing can really do work.**

---

## What Is Claude Code?

Simply put, it's a command-line tool that understands your entire codebase and helps you:

- Write new features
- Fix bugs
- Refactor code
- Run tests
- Even commit to Git

**All in natural language. No need to remember complex commands.**

---

## Real-world Usage Scenarios

### Scenario 1: Onboarding to an Unfamiliar Project

Last week, a colleague left and tossed me a Python project he had been working on for 2 years.

Old me: read the README, then chew through the code, spend at least half a day understanding the structure.

With Claude Code:
```
Me: What does this project do?
Claude: This is an e-commerce order processing system. The core modules are...

Me: What's the flow when a user places an order?
Claude: Let me check...the flow is A→B→C, with the key code in file X.

Me: If I want to add coupon validation during ordering, where should I change?
Claude: You need to add validation logic in function Z of file Y. I suggest...
```

**10 minutes, and I understood what would have taken half a day.**

### Scenario 2: Fixing a Bug

There was a production bug. The log showed the error in some deep call.

Old way: set breakpoints, step through, search for ages.

Now:
```
Me: What does this error mean? How do I fix it?
Claude: The cause is XXX, you should add a C check at point B in file A.

Me: Help me fix it.
Claude: Done. Want me to run the tests to verify?
```

**5 minutes to solve, with test cases included.**

### Scenario 3: Writing a New Feature

I needed to add an Excel export function to the system.

Me: Help me add a feature to export orders to Excel.
Claude: Sure, I need to:
1. Install the openpyxl library
2. Add an export function in the orders module
3. Add an endpoint in the API route
4. Write unit tests

Want me to do it all?

Me: Go.
Claude: (does the work) Done, tests pass.

**The whole time, I only said two sentences.**

---

## How Strong Is It Really?

I ran a side-by-side comparison test. Same requirement, with:

| Approach | Time | Quality |
|----------|------|---------|
| Pure hand-coding | 2 hours | Medium |
| Copilot-assisted | 1.5 hours | Medium-plus |
| Claude Code | 20 minutes | High (with tests) |

**6× efficiency gain, and the code is more standardized.**

---

## But There Are Caveats

After several days, I noticed a few things to be careful about:

⚠️ **Complex architecture design still requires a human** — It can implement features, but system design you must control.
⚠️ **Security-sensitive code must be reviewed** — Code involving permissions or payments must be manually inspected.
⚠️ **Some programming foundation is required** — Someone who knows nothing about code may not know what to ask.

**Conclusion: It's a super assistant, not a replacement.**

---

## Who Is It For?

✅ **Programmers** — A productivity booster, hand off the repetitive work.
✅ **Technical managers** — Quickly review code and understand projects.
✅ **Programming learners** — Have a 24/7 online mentor.
✅ **Indie developers** — One person doing the work of two.

❌ **Complete beginners** — Learn the basics first, otherwise you won't know what to ask.
❌ **Those who want a hands-off solution** — It still needs your guidance and review.

---

## How to Get Started?

### 1. Install
```bash
npm install -g @anthropics/claude-code
```

### 2. Configure your API Key
Go to the Anthropic website to apply. New users get a free credit.

### 3. Run in your project directory
```bash
claude
```

Then just start talking!

---

## A Word of Caution

Claude Code is powerful, but if you **don't know the basics of programming, can't read code, don't know what an API is**…

Then it's a black box to you. You won't be able to use it effectively.

**It's like being given a Ferrari when you haven't gotten your driver's license yet.**

So if you really want to use these AI tools well, **you should first fill in your programming basics.**

---

## Final Words

The emergence of tools like Claude Code means: **programmer productivity is exploding.**

But programmers who don't know how to use AI may be replaced by programmers who do.

**The future belongs to those who understand AI.**

In 2026, let's embrace the change together.

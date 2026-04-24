---
title: "Lecture 6: Coze Platform Deep Dive"
date: 2026-04-06 14:00:00
tags: ["AI Skill", "Coze", "Platform"]
categories: ["AI Skills Course"]
---

<!-- more -->
# Lecture 6: Coze Platform Deep Dive

> Comprehensively master Coze platform's core features and advanced techniques.

## 1. Coze Platform Architecture

### 1.1 Overall Architecture

```
Coze Platform
├── Application Layer
│   ├── Bot (Chatbot)
│   ├── Plugin
│   ├── Workflow
│   └── Knowledge Base
│
├── Capability Layer
│   ├── Large Model (LLM)
│   ├── Multi-modal (Image/Voice)
│   └── Tool Calling (Function Calling)
│
└── Ecosystem Layer
    ├── Coze Store
    ├── Doubao (Douyin)
    ├── Feishu
    └── WeChat
```

### 1.2 Core Concept Relationships

```
Bot (Robot)
    ├── Persona & Response Logic (Prompt)
    ├── Plugins (Extended capabilities)
    ├── Workflows (Complex logic)
    ├── Knowledge Base (Private data)
    └── Database (Persistence)
```

---

## 2. Bot Development Deep Dive

### 2.1 Bot Configuration Full Analysis

**Basic Configuration**:
- **Name**: Bot display name
- **Description**: One-sentence introduction of Bot's functionality
- **Icon**: Visual identifier
- **Tags**: For classification and search

**Advanced Configuration**:
- **Model Selection**:
  - Doubao large model (default)
  - GPT-4 (needs application)
  - Claude (needs application)
- **Response Length**: Control detail level of responses
- **Context Length**: How many conversation rounds to remember

### 2.2 Persona & Response Logic

**Structured Prompt Template**:

```markdown
# Role
You are [role name], [role positioning]

## Background
[User group] uses your service, their pain points are [pain point description]

## Skills
### Skill 1: [Skill name]
- Function: [Specific function]
- Trigger condition: [When to use]
- How to use: [How to use]

### Skill 2: [Skill name]
...

## Workflow
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Constraints
- [Constraint 1]
- [Constraint 2]

## Output Format
[Format requirements]

## Examples

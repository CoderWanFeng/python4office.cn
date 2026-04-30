---
title: "Lecture 3: Core Concepts of Skills: Intent, Action, Tool"
date: 2026-04-06 12:00:00
tags: ["AI Skill", "Beginner", "Core Concepts"]
categories: ["AI Skills Course"]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<!-- more -->

![Lecture 3: Core Concepts of Skills: Intent, Action, Tool](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)
![Lecture 3: Core Concepts of Skills: Intent, Action, Tool](https://images.unsplash.com/photo-151707730?w=800&h=400&fit=crop)

# Lecture 3: Core Concepts of Skills: Intent, Action, Tool

> Understand the three core concepts of Skills, build the correct technical cognitive framework.

---

## 1. Skill Architecture Model

### 1.1 A Complete Skill Interaction Flow

```
User input: "Convert this PDF to Word document"
    ↓
[Intent Recognition] → Intent: file format conversion
    ↓
[Parameter Extraction] → source: PDF, target: Word, file: xxx.pdf
    ↓
[Tool Selection] → Call PDF parsing tool + Word generation tool
    ↓
[Action Execution] → Read PDF → Extract content → Generate Word → Save
    ↓
[Result Return] → "Conversion complete, download link: xxx"
```

### 1.2 Three Core Concepts

| Concept | English | Function | Analogy |
|------|------|------|------|
| **Intent** | Intent | Understand what user wants to do | Brain's thought |
| **Action** | Action | Execute specific operations | Behavior of hands |
| **Tool** | Tool | External resources providing capabilities | Tools in hands |

---

## 2. Intent: Skill's "Brain"

### 2.1 What is Intent?

**Intent** is the semantic understanding result of user input, telling Skill "what does the user want".

**Examples:**

```
User says:
- "Help me merge these two Excel files"
- "Combine these sheets"
- "Can you integrate these two Excel files"

Intent recognition result:
{
  "intent": "file_merge",
  "confidence": 0.95,
  "entities": {
    "file_type": "excel",
    "action": "merge",
    "count": 2
  }
}
```

### 2.2 Intent Classification

| Type | Description | Example |
|------|------|------|
| **Task** | Complete specific tasks | "Merge files", "Send email" |
| **Query** | Get information | "What's the weather today" |
| **Conversational** | Casual chat | "Hello", "Thanks" |
| **Control** | Control flow | "Cancel", "Start over" |

### 2.3 Key Technologies for Intent Recognition

```python
# Intent recognition example based on large model
import openai

def recognize_intent(user_input):
    prompt = f"""
    Analyze user input intent, return JSON format:
    {{
      "intent": "intent name",
      "confidence": confidence (0-1),
      "entities": {{extracted parameters}}
    }}

    User input: {user_input}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.choices[0].message.content)

# Test
result = recognize_intent("Convert report.pdf to Word")
print(result)
# {"intent": "file_convert", "confidence": 0.98, "entities": {"source": "pdf", "target": "word", "filename": "report.pdf"}}
```

---

## 3. Action: Skill's "Hands"

### 3.1 What is Action?

**Action** is the specific operation executed by Skill, serving as a bridge connecting Intent and Tool.

**Action Composition:**

```python
class Action:
    def __init__(self, name, parameters, tool):
        self.name = name          # Action name
        self.parameters = parameters  # Input parameters
        self.tool = tool          # Tool used
        self.output = None        # Execution result

    def execute(self):
        """Execute action"""
        self.output = self.tool.run(self.parameters)
        return self.output
```

### 3.2 Action Types

| Type | Description | Example |
|------|------|------|
| **File Operation** | Read/write files | read_file, write_file, copy_file |
| **Data Processing** | Transform data | parse_json, filter_data, sort_list |
| **Network Request** | Call API | http_get, http_post, download |
| **System Command** | Execute commands | run_shell, execute_script |
| **AI Call** | Call models | chat_completion, text_embedding |

### 3.3 Action Execution Flow

```python
class SkillExecutor:
    """Skill executor"""

    def execute(self, intent, context):
        # 1. Select Action chain based on Intent
        actions = self.plan_actions(intent)

        # 2. Execute each Action in sequence
        results = []
        for action in actions:
            try:
                result = action.execute()
                results.append(result)

                # Update context for subsequent Actions
                context.update(result)

            except Exception as e:
                # Error handling
                return self.handle_error(e, action)

        # 3. Integrate results and return
        return self.format_output(results)
```

---

## 4. Tool: Skill's "Arsenal"

### 4.1 What is Tool?

**Tool** is external capabilities that Skill can call, which can be code libraries, APIs, services, etc.

**Tool Characteristics:**
- 🔧 **Single function**: Each Tool does only one thing
- 📦 **Reusable**: Multiple Skills can share the same Tool
- 🔌 **Extensible**: New Tools can be added anytime
- 📖 **Self-describing**: Tools come with functionality descriptions

### 4.2 Tool Definition Method

```python
# Standard Tool definition format
excel_tool = {
    "name": "excel_processor",
    "description": "Handle Excel file read/write, merge, split and other operations",
    "parameters": {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["read", "write", "merge", "split"],
                "description": "Operation to execute"
            },


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



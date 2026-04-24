---
title: "Lecture 5: Skill Interaction Design: Making Conversations More Natural"
date: 2026-04-06 14:00:00
tags: ["AI Skill", "Interaction Design", "Prompt", "User Experience"]
categories: ["AI Skills Course"]
---

<!-- more -->
# Lecture 5: Skill Interaction Design: Making Conversations More Natural

> Master core skills of Skill interaction design, make your Skill as natural and smooth as a real person.

---

## 1. Why is Interaction Design Important?

### 1.1 User Experience Differences

```
❌ Poor interaction:
User: Check Beijing weather
Skill: {"city": "Beijing", "weather": "Sunny", "temp": "25"}

✅ Excellent interaction:
User: How's the weather in Beijing today?
Skill: Today's weather in Beijing is sunny☀️, temperature 15-25°C, air quality is good, suitable for outdoor activities!
Suggestions: Wear a light jacket, remember to apply sunscreen～
```

### 1.2 Good Interaction Design Standards

| Dimension | Standard | Example |
|------|------|------|
| **Natural** | Like real person conversation | Use colloquial expressions, avoid robot voice |
| **Clear** | Clear information structure | Highlight key points, clear hierarchy |
| **Friendly** | Warm tone | Use emojis appropriately, express emotions |
| **Fault-tolerant** | Can handle wrong input | Guide users, don't just report errors |
| **Efficient** | Reduce interaction rounds | Provide complete information at once |

---

## 2. Prompt Engineering Basics

### 2.1 What is Prompt?

**Prompt** is instructions for the large model, telling it:
- Who you are (role setting)
- What to do (task description)
- How to do it (constraints)
- Output format (format requirements)

### 2.2 Basic Prompt Structure

```
# Role
You are [role name],具备[相关能力]。

## Task
Your task is [specific task description].

## Workflow
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Constraints
- [Constraint 1]
- [Constraint 2]

## Output Format
[Format description]
```

### 2.3 Example: Weather Assistant Prompt

```markdown
# Role
You are a professional weather query assistant, speak in a warm and friendly manner, like a friend.

## Task
Help users check weather and provide practical clothing and travel suggestions.

## Workflow
1. Confirm the city user wants to check
2. Get weather information for that city
3. Analyze weather data, generate suggestions
4. Reply to user in a friendly tone

## Constraints
- Only check weather for Chinese cities
- Temperature in Celsius
- Replies should include emojis
- Suggestions should be specific and practical

## Output Format
🌤️ [City] Weather Forecast

📅 Date: [Date]
🌡️ Temperature: [Low]°C ~ [High]°C
☁️ Weather: [Weather condition]

💡 Suggestions:
- Clothing: [Clothing suggestions]
- Travel: [Travel suggestions]
```

---

## 3. Making Conversations More Natural

### 3.1 Use Colloquial Expressions

```
❌ Robot voice:
"Query result: Today's Beijing weather is sunny, temperature range 15-25 Celsius degrees."

✅ Colloquial:
"Today's weather in Beijing is amazing!☀️ Sunny with sunshine, temperature between 15-25°C, not cold or hot, just right～"
```

**Skills checklist:**
- Use "you" instead of "user"
- Add filler words: "ne", "o", "ya", "ha"
- Use abbreviations: "today" instead of "this day"
- Use emojis appropriately to express emotions

### 3.2 Proactively Guide Conversation

```python
# When information is incomplete, proactively ask
class DialogManager:
    def handle_incomplete(self, missing_info):
        """Handle incomplete information"""

        prompts = {
            'city': [
                "Which city's weather do you want to check?",
                "Tell me which city you're in, I'll help you check the weather～",
                "Which city is it?"
            ],
            'date': [
                "Do you want to check today's, tomorrow's or day after tomorrow's weather?",
                "Which day's weather do you need?"
            ]
        }

        return random.choice(prompts.get(missing_info, ["Could you be more specific?"]))
```

### 3.3 Handle Ambiguous Input

```python
def handle_ambiguous(self, user_input):
    """Handle ambiguous input"""

    # Example: User says "how's the weather there"
    if '那里' in user_input or '那边' in user_input:
        # Check context
        last_city = self.context.get('last_city')
        if last_city:
            return f"Are you asking about {last_city}'s weather?"
        else:
            return "Which city does 'there' refer to?"

    # Example: User says "will it rain tomorrow"
    if '下雨' in user_input:
        return self.check_rain(user_input)
```

### 3.4 Emotional Design

```python
class EmotionalResponse:
    """Emotional response generator"""

    def generate(self, weather_data, user_mood=None):
        """Generate response based on weather and user mood"""

        condition = weather_data['condition']
        temp = weather_data['temp_high']

        # Choose tone based on weather
        if '晴' in condition and temp > 25:
            opening = [
                "Today's sunshine is amazing!☀️",
                "What a sunny day!🌤️",
                "A day of bright sunshine～"
            ]
        elif '雨' in condition:
            opening = [
                "It's rainy today, remember to bring an umbrella☔",
                "Roads are slippery in the rain, walk carefully🌧️",
                "Even though it's raining, your mood can be sunny🌈"
            ]
        else:
            opening = [
                "Today's weather is like this～",
                "Here's the weather situation:",
                "Here's today's weather for you:"

---
title: 第5讲：Skill 的交互设计：让对话更自然
date: 2026-04-06 14:00:00
tags: ["AI Skill", "交互设计", "Prompt", "用户体验"]
categories: ["AI Skills 课程"]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<!-- more -->

![第5讲：Skill 的交互设计：让对话更自然](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)

# 第5讲：Skill 的交互设计：让对话更自然

> 掌握 Skill 交互设计的核心技巧，让你的 Skill 像真人一样自然流畅。

---

## 一、为什么交互设计很重要？

### 1.1 用户体验的差异

```
❌ 糟糕的交互：
用户：查北京天气
Skill：{"city": "北京", "weather": "晴", "temp": "25"}

✅ 优秀的交互：
用户：北京今天天气怎么样？
Skill：北京今天天气晴朗☀️，气温 15-25°C，空气质量良，适合户外活动！
建议穿薄外套，记得涂防晒哦～
```

### 1.2 好的交互设计标准

| 维度 | 标准 | 示例 |
|------|------|------|
| **自然** | 像真人对话 | 使用口语化表达，避免机器腔 |
| **清晰** | 信息结构清楚 | 重点突出，层次分明 |
| **友好** | 语气亲切 | 适当使用 emoji，表达情感 |
| **容错** | 能处理错误输入 | 引导用户，不直接报错 |
| **高效** | 减少交互轮次 | 一次给出完整信息 |

---

## 二、Prompt 工程基础

### 2.1 什么是 Prompt？

**Prompt** 是给大模型的指令，告诉它：
- 你是谁（角色设定）
- 你要做什么（任务描述）
- 怎么做（约束条件）
- 输出格式（格式要求）

### 2.2 Prompt 的基本结构

```
# 角色
你是[角色名称]，具备[相关能力]。

## 任务
你的任务是[具体任务描述]。

## 工作流程
1. [步骤1]
2. [步骤2]
3. [步骤3]

## 约束条件
- [约束1]
- [约束2]

## 输出格式
[格式说明]
```

### 2.3 示例：天气助手的 Prompt

```markdown
# 角色
你是一个专业的天气查询助手，说话亲切友好，像朋友一样。

## 任务
帮用户查询天气，并提供实用的穿衣和出行建议。

## 工作流程
1. 确认用户要查询的城市
2. 获取该城市的天气信息
3. 分析天气数据，生成建议
4. 用友好的语气回复用户

## 约束条件
- 只查询中国城市的天气
- 温度用摄氏度表示
- 回复要包含表情符号
- 建议要具体实用

## 输出格式
🌤️ [城市] 天气预报

📅 日期：[日期]
🌡️ 温度：[最低温]°C ~ [最高温]°C
☁️ 天气：[天气状况]
💨 风力：[风力信息]

💡 建议：
- 穿衣：[穿衣建议]
- 出行：[出行建议]
```

---

## 三、让对话更自然的技巧

### 3.1 使用口语化表达

```
❌ 机器腔：
"查询结果：北京市今日天气为晴，温度范围 15-25 摄氏度。"

✅ 口语化：
"北京今天天气超棒！☀️ 阳光明媚，温度在 15-25°C 之间，不冷不热刚刚好～"
```

**技巧清单：**
- 使用"你"而不是"用户"
- 加入语气词："呢"、"哦"、"呀"、"哈"
- 使用缩略语："今天"而不是"今日"
- 适当使用 emoji 表达情绪

### 3.2 主动引导对话

```python
# 当信息不完整时，主动询问
class DialogManager:
    def handle_incomplete(self, missing_info):
        """处理信息不完整的情况"""
        prompts = {
            'city': [
                "你想查哪个城市的天气呢？",
                "告诉我你在哪个城市，我帮你查天气～",
                "请问是哪个城市呀？"
            ],
            'date': [
                "你想查今天、明天还是后天的天气？",
                "需要查哪天的天气呀？"
            ]
        }
        
        return random.choice(prompts.get(missing_info, ["能再说详细一点吗？"]))
```

### 3.3 处理模糊输入

```python
def handle_ambiguous(self, user_input):
    """处理模糊输入"""
    
    # 示例：用户说"那边天气怎么样"
    if '那边' in user_input or '那里' in user_input:
        # 查看上下文
        last_city = self.context.get('last_city')
        if last_city:
            return f"你是问 {last_city} 的天气吗？"
        else:
            return "请问'那边'是指哪个城市呢？"
    
    # 示例：用户说"明天会下雨吗"
    if '下雨' in user_input:
        return self.check_rain(user_input)
```

### 3.4 情感化设计

```python
class EmotionalResponse:
    """情感化回复生成器"""
    
    def generate(self, weather_data, user_mood=None):
        """根据天气和用户心情生成回复"""
        
        condition = weather_data['condition']
        temp = weather_data['temp_high']
        
        # 根据天气选择语气
        if '晴' in condition and temp > 25:
            opening = [
                "今天阳光超棒！☀️",
                "好天气来啦！🌤️",
                "阳光明媚的一天～"
            ]
        elif '雨' in condition:
            opening = [
                "今天有雨，出门记得带伞哦☔",
                "雨天路滑，小心慢行🌧️",
                "虽然下雨，但心情可以晴朗呀🌈"
            ]
        else:
            opening = [
                "今天的天气是这样的～",
                "来看看天气情况：",
                "为你查询到今天的天气："
            ]
        
        return random.choice(opening)
```

---

## 四、多轮对话管理

### 4.1 对话状态管理

```python
class ConversationManager:
    """对话管理器"""
    
    def __init__(self):
        self.sessions = {}  # 存储对话状态
    
    def get_session(self, user_id):
        """获取或创建会话"""
        if user_id not in self.sessions:
            self.sessions[user_id] = {
                'history': [],      # 对话历史
                'context': {},      # 上下文信息
                'state': 'idle'     # 当前状态
            }
        return self.sessions[user_id]
    
    def update_context(self, user_id, key, value):
        """更新上下文"""
        session = self.get_session(user_id)
        session['context'][key] = value
    
    def get_context(self, user_id, key, default=None):
        """获取上下文"""
        session = self.get_session(user_id)
        return session['context'].get(key, default)
```

### 4.2 对话流程设计

```
【天气查询对话流程】

开始
  ↓
用户输入 → 识别意图
  ↓
信息完整？
  ├── 否 → 询问缺失信息 → 等待用户回复 → 回到"用户输入"
  ↓
  └── 是
        ↓
    查询天气
        ↓
    生成回复
        ↓
    更新上下文（记录城市、日期等）
        ↓
    结束本轮
```

### 4.3 代码实现

```python
class WeatherDialog:
    """天气查询对话管理"""
    
    def __init__(self):
        self.context = {}
        self.required_slots = ['city']  # 必需的信息槽
    
    def process(self, user_input):
        """处理用户输入"""
        
        # 提取信息
        extracted = self.extract_info(user_input)
        self.context.update(extracted)
        
        # 检查必需信息
        missing = self.check_missing_slots()
        
        if missing:
            # 信息不完整，询问缺失项
            return self.ask_for_missing(missing[0])
        
        # 信息完整，执行查询
        return self.execute_query()
    
    def extract_info(self, text):
        """从输入中提取信息"""
        info = {}
        
        # 提取城市
        cities = ['北京', '上海', '广州', '深圳', '杭州']
        for city in cities:
            if city in text:
                info['city'] = city
                break
        
        # 提取日期
        if '明天' in text:
            info['date'] = 'tomorrow'
        elif '后天' in text:
            info['date'] = 'day_after_tomorrow'
        else:
            info['date'] = 'today'
        
        return info
    
    def check_missing_slots(self):
        """检查缺失的信息槽"""
        missing = []
        for slot in self.required_slots:
            if slot not in self.context or not self.context[slot]:
                missing.append(slot)
        return missing
    
    def ask_for_missing(self, slot):
        """询问缺失信息"""
        prompts = {
            'city': [
                "你想查哪个城市的天气呢？",
                "请告诉我城市名称～",
                "哪个城市呀？"
            ]
        }
        import random
        return random.choice(prompts.get(slot, ["还需要一些信息..."]))
    
    def execute_query(self):
        """执行查询"""
        city = self.context['city']
        date = self.context.get('date', 'today')
        
        # 调用天气 API
        weather = self.query_weather(city, date)
        
        # 生成回复
        return self.format_response(weather)
```

---

## 五、错误处理与边界情况

### 5.1 常见错误类型

| 错误类型 | 示例 | 处理方式 |
|----------|------|----------|
| **输入错误** | 城市名拼写错误 | 模糊匹配，给出建议 |
| **数据错误** | API 返回异常 | 使用默认值，告知用户 |
| **逻辑错误** | 参数缺失 | 引导用户补充 |
| **系统错误** | 服务不可用 | 友好提示，提供替代方案 |

### 5.2 错误处理代码

```python
class ErrorHandler:
    """错误处理器"""
    
    def handle(self, error, context):
        """统一错误处理"""
        
        error_type = type(error).__name__
        
        handlers = {
            'CityNotFoundError': self.handle_city_not_found,
            'APIError': self.handle_api_error,
            'ValidationError': self.handle_validation_error,
            'TimeoutError': self.handle_timeout
        }
        
        handler = handlers.get(error_type, self.handle_unknown_error)
        return handler(error, context)
    
    def handle_city_not_found(self, error, context):
        """城市不存在"""
        city = context.get('city', '未知')
        suggestions = self.get_city_suggestions(city)
        
        return f"""抱歉，我没有找到"{city}"的天气信息。
        
你是不是想找：
{chr(10).join([f"• {s}" for s in suggestions[:3]])}

请确认城市名称后重试～"""
    
    def handle_api_error(self, error, context):
        """API 调用失败"""
        return """抱歉，天气服务暂时不可用😅

你可以：
• 稍后再试
• 访问 weather.com.cn 查询
• 试试其他城市的天气

给我造成不便，非常抱歉！"""
    
    def handle_timeout(self, error, context):
        """超时"""
        return "查询超时了，可能是网络问题，请稍后再试～"
```

### 5.3 边界情况处理

```python
def handle_edge_cases(self, user_input):
    """处理边界情况"""
    
    # 1. 用户说"不查了"
    if any(word in user_input for word in ['不', '算了', '取消']):
        self.reset_context()
        return "好的，有需要随时叫我～"
    
    # 2. 用户说"谢谢"
    if '谢谢' in user_input or '感谢' in user_input:
        return "不客气！有问题随时问我😊"
    
    # 3. 用户说"你好"
    if user_input in ['你好', '您好', 'hi', 'hello']:
        return "你好！我是天气小助手，可以帮你查询天气～"
    
    # 4. 用户输入乱码或无意义内容
    if len(user_input) < 2 or not any('\u4e00' <= c <= '\u9fff' for c in user_input):
        return "抱歉，我没理解你的意思。你可以说：'北京天气'"
    
    return None  # 没有匹配到边界情况
```

---

## 六、实战：优化天气助手

### 6.1 优化前的版本

```python
# 简单版本
user: 北京天气
skill: 北京今天晴，15-25度
```

### 6.2 优化后的版本

```python
# 完整优化版本
class OptimizedWeatherSkill:
    """优化后的天气助手"""
    
    def __init__(self):
        self.dialog = WeatherDialog()
        self.error_handler = ErrorHandler()
        self.emotional = EmotionalResponse()
    
    def run(self, user_input):
        try:
            # 1. 检查边界情况
            edge_response = self.handle_edge_cases(user_input)
            if edge_response:
                return edge_response
            
            # 2. 处理对话
            response = self.dialog.process(user_input)
            
            # 3. 添加情感化元素
            if '天气' in response:
                emotion = self.emotional.generate({'condition': '晴', 'temp_high': 25})
                response = emotion + '\n' + response
            
            return response
            
        except Exception as e:
            # 4. 错误处理
            return self.error_handler.handle(e, self.dialog.context)
```

### 6.3 对话示例

```
【优化后的对话体验】

用户：你好
Skill：你好！我是天气小助手☀️ 可以帮你查询全国各地的天气，
      还能给你穿衣和出行建议哦～

用户：北京天气
Skill：今天阳光超棒！☀️
      
      🌤️ 北京天气预报
      
      📅 日期：2026-04-06
      🌡️ 温度：15°C ~ 25°C
      ☁️ 天气：晴
      💨 风力：北风 3级
      🌫️ 空气质量：良
      
      💡 建议：
      👔 穿衣：建议穿薄外套，早晚温差大
      🚗 出行：天气不错，适合户外活动
      🌬️ 空气：空气质量不错，可以开窗通风

用户：那明天呢？
Skill：明天北京多云🌤️，温度 16-24°C，可能会有点凉，
      建议带件外套出门～

用户：谢谢
Skill：不客气！有问题随时问我😊 祝你有个美好的一天！
```

---

## 七、下节预告

**第6讲：Coze 扣子平台深度解析**

我们将深入学习：
- Coze 平台的核心功能和特性
- 工作流的高级用法
- 插件生态系统的使用
- 如何发布和推广你的 Skill

---

## 加入学习群

学习过程中遇到问题？欢迎加入交流群：

👉 **[加入AI编程学习交流群](https://www.python4office.cn/wechat-group/)**

![点击加入](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

---

*本讲是《Skills 从入门到实践》系列课程的第5讲，下一讲我们将深入 Coze 平台。*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



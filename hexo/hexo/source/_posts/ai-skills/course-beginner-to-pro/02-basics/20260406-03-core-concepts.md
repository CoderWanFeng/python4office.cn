---
title: "第3讲：Skill 的核心概念：Intent、Action、Tool"
date: 2026-04-06 12:00:00
tags: ["AI Skill", "入门", "核心概念"]
categories: ["AI Skills 课程"]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---

<!-- more -->

![第3讲：Skill 的核心概念：Intent、Action、Tool - 配图1](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)

# 第3讲：Skill 的核心概念：Intent、Action、Tool

> 理解 Skill 的三大核心概念，建立正确的技术认知框架。

---

## 一、Skill 的架构模型

### 1.1 一个完整的 Skill 交互流程

```
用户输入: "把这份 PDF 转成 Word 文档"
    ↓
[Intent 识别] → 意图：文件格式转换
    ↓
[参数提取] → source: PDF, target: Word, file: xxx.pdf
    ↓
[Tool 选择] → 调用 PDF 解析工具 + Word 生成工具
    ↓
[Action 执行] → 读取 PDF → 提取内容 → 生成 Word → 保存
    ↓
[结果返回] → "转换完成，下载链接：xxx"
```

### 1.2 三大核心概念

| 概念 | 英文 | 作用 | 类比 |
|------|------|------|------|
| **意图** | Intent | 理解用户想做什么 | 大脑的想法 |
| **动作** | Action | 执行具体的操作 | 手的行为 |
| **工具** | Tool | 提供能力的外部资源 | 手中的工具 |

---

## 二、Intent（意图）：Skill 的"大脑"

### 2.1 什么是 Intent？

**Intent** 是用户输入的语义理解结果，告诉 Skill "用户想要什么"。

**示例：**

```
用户说：
- "帮我合并这两个 Excel 文件"
- "把表格合一下"
- "这两个 Excel 能整合吗"

Intent 识别结果：
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

### 2.2 Intent 的分类

| 类型 | 说明 | 示例 |
|------|------|------|
| **任务型** | 完成具体任务 | "合并文件"、"发送邮件" |
| **查询型** | 获取信息 | "今天天气怎么样" |
| **对话型** | 闲聊互动 | "你好"、"谢谢" |
| **控制型** | 控制流程 | "取消"、"重新来" |

### 2.3 Intent 识别的关键技术

```python
# 基于大模型的 Intent 识别示例
import openai

def recognize_intent(user_input):
    prompt = f"""
    分析用户输入的意图，返回 JSON 格式：
    {{
      "intent": "意图名称",
      "confidence": 置信度(0-1),
      "entities": {{提取的参数}}
    }}
    
    用户输入：{user_input}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return json.loads(response.choices[0].message.content)

# 测试
result = recognize_intent("把 report.pdf 转成 Word")
print(result)
# {"intent": "file_convert", "confidence": 0.98, "entities": {"source": "pdf", "target": "word", "filename": "report.pdf"}}
```

---

## 三、Action（动作）：Skill 的"手"

### 3.1 什么是 Action？

**Action** 是 Skill 执行的具体操作，是连接 Intent 和 Tool 的桥梁。

**Action 的组成：**

```python
class Action:
    def __init__(self, name, parameters, tool):
        self.name = name          # 动作名称
        self.parameters = parameters  # 输入参数
        self.tool = tool          # 使用的工具
        self.output = None        # 执行结果
    
    def execute(self):
        """执行动作"""
        self.output = self.tool.run(self.parameters)
        return self.output
```

### 3.2 Action 的类型

| 类型 | 说明 | 示例 |
|------|------|------|
| **文件操作** | 读写文件 | read_file, write_file, copy_file |
| **数据处理** | 转换数据 | parse_json, filter_data, sort_list |
| **网络请求** | 调用 API | http_get, http_post, download |
| **系统命令** | 执行命令 | run_shell, execute_script |
| **AI 调用** | 调用模型 | chat_completion, text_embedding |

### 3.3 Action 的执行流程

```python
class SkillExecutor:
    """Skill 执行器"""
    
    def execute(self, intent, context):
        # 1. 根据 Intent 选择 Action 链
        actions = self.plan_actions(intent)
        
        # 2. 依次执行每个 Action
        results = []
        for action in actions:
            try:
                result = action.execute()
                results.append(result)
                
                # 更新上下文，供后续 Action 使用
                context.update(result)
                
            except Exception as e:
                # 错误处理
                return self.handle_error(e, action)
        
        # 3. 整合结果并返回
        return self.format_output(results)
```

---

## 四、Tool（工具）：Skill 的"武器库"

### 4.1 什么是 Tool？

**Tool** 是 Skill 可调用的外部能力，可以是代码库、API、服务等。

**Tool 的特点：**
- 🔧 **功能单一**：每个 Tool 只做一件事
- 📦 **可复用**：多个 Skill 可以共用同一个 Tool
- 🔌 **可扩展**：随时添加新的 Tool
- 📖 **自描述**：Tool 自带功能说明

### 4.2 Tool 的定义方式

```python
# Tool 的标准定义格式
excel_tool = {
    "name": "excel_processor",
    "description": "处理 Excel 文件的读写、合并、拆分等操作",
    "parameters": {
        "type": "object",
        "properties": {
            "action": {
                "type": "string",
                "enum": ["read", "write", "merge", "split"],
                "description": "要执行的操作"
            },
            "file_path": {
                "type": "string",
                "description": "Excel 文件路径"
            },
            "data": {
                "type": "object",
                "description": "要写入的数据"
            }
        },
        "required": ["action", "file_path"]
    }
}
```

### 4.3 常用 Tool 分类

| 类别 | Tool 示例 | 用途 |
|------|-----------|------|
| **文件处理** | pdf_parser, docx_generator, image_converter | 文档格式转换 |
| **数据处理** | pandas, numpy, json_parser | 数据分析和处理 |
| **网络服务** | http_client, email_sender, ftp_transfer | 网络通信 |
| **AI 能力** | openai_api, embedding_model, ocr_engine | 智能处理 |
| **系统工具** | file_system, process_manager, scheduler | 系统操作 |

### 4.4 Tool 的实现示例

```python
import pandas as pd
from typing import List, Dict, Any

class ExcelTool:
    """Excel 处理工具"""
    
    def read(self, file_path: str, sheet_name: str = None) -> pd.DataFrame:
        """读取 Excel 文件"""
        if sheet_name:
            return pd.read_excel(file_path, sheet_name=sheet_name)
        return pd.read_excel(file_path)
    
    def merge(self, files: List[str], output_path: str) -> str:
        """合并多个 Excel 文件"""
        dfs = [pd.read_excel(f) for f in files]
        merged = pd.concat(dfs, ignore_index=True)
        merged.to_excel(output_path, index=False)
        return output_path
    
    def write(self, data: Dict[str, Any], file_path: str) -> str:
        """写入数据到 Excel"""
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False)
        return file_path

# 使用示例
tool = ExcelTool()
df = tool.read("data.xlsx")
tool.merge(["file1.xlsx", "file2.xlsx"], "merged.xlsx")
```

---

## 五、三者的协作关系

### 5.1 完整流程图解

```
┌─────────────────────────────────────────────────────────┐
│                      用户输入                            │
│              "合并这两个 Excel 文件"                      │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│  Intent 识别                                           │
│  ├── 意图：file_merge                                   │
│  ├── 实体：file_type=excel, count=2                     │
│  └── 置信度：0.96                                       │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│  Action 规划                                           │
│  ├── Action 1: 读取文件1 (Tool: ExcelTool.read)         │
│  ├── Action 2: 读取文件2 (Tool: ExcelTool.read)         │
│  └── Action 3: 合并保存  (Tool: ExcelTool.merge)        │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│  Tool 执行                                             │
│  ├── Tool: ExcelTool                                   │
│  ├── 操作: merge()                                     │
│  └── 结果: merged.xlsx                                 │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│                     返回结果                             │
│         "合并完成！共处理 100 行数据"                     │
└─────────────────────────────────────────────────────────┘
```

### 5.2 代码层面的实现

```python
class Skill:
    """Skill 基类"""
    
    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.action_planner = ActionPlanner()
        self.tools = {}
    
    def register_tool(self, tool):
        """注册工具"""
        self.tools[tool.name] = tool
    
    def run(self, user_input: str) -> str:
        """运行 Skill"""
        # Step 1: 识别 Intent
        intent = self.intent_classifier.classify(user_input)
        
        # Step 2: 规划 Actions
        actions = self.action_planner.plan(intent, self.tools)
        
        # Step 3: 执行 Actions
        context = {"user_input": user_input}
        for action in actions:
            tool = self.tools.get(action.tool_name)
            result = tool.run(action.parameters)
            context[action.name] = result
        
        # Step 4: 生成回复
        return self.generate_response(context)
```

---

## 六、实战练习

### 练习 1：分析一个简单 Skill

分析以下 Skill 的 Intent、Action、Tool：

```
用户："把 meeting_notes.pdf 转成 Word 文档"
```

**答案：**
- **Intent**: file_convert (文件格式转换)
- **Entities**: source=pdf, target=docx, filename=meeting_notes.pdf
- **Actions**: 
  1. read_pdf(file_path)
  2. convert_to_docx(content)
  3. save_document(output_path)
- **Tools**: PDFReader, DOCXGenerator

### 练习 2：设计一个邮件发送 Skill

设计一个 Skill，实现以下功能：

```
用户："给张三发邮件，主题是项目进度，内容是说本周完成了 80%"
```

**思考要点：**
1. Intent 是什么？需要提取哪些实体？
2. 需要哪些 Actions？执行顺序如何？
3. 需要什么 Tools？

---

## 七、常见误区

### ❌ 误区 1：Intent 越多越好

**正确做法**：Intent 应该精简、明确，相似意图合并。

```
❌ 不好：
- merge_excel
- combine_excel  
- join_excel

✅ 好：
- file_merge（支持多种文件类型）
```

### ❌ 误区 2：Action 过于复杂

**正确做法**：Action 应该原子化，一个 Action 只做一件事。

```
❌ 不好：
Action: 读取 Excel + 处理数据 + 生成图表 + 发送邮件

✅ 好：
Action 1: 读取 Excel
Action 2: 处理数据
Action 3: 生成图表
Action 4: 发送邮件
```

### ❌ 误区 3：Tool 没有文档

**正确做法**：每个 Tool 都要有清晰的描述和参数说明。

---

## 八、下节预告

**第4讲：你的第一个 Skill：Hello World 实战**

我们将动手实现：
- 在 Coze 平台创建第一个 Skill
- 实现简单的 Intent 识别
- 调用外部 Tool 完成一个具体任务
- 测试和调试你的 Skill

---

## 加入学习群

学习过程中遇到问题？欢迎加入交流群：

👉 **[加入AI编程学习交流群](https://www.python4office.cn/wechat-group/)**

![点击加入](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

---

*本讲是《Skills 从入门到实践》系列课程的第3讲，下一讲我们将动手创建第一个 Skill。*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



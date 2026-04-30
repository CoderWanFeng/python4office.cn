---
title: 第7讲：Coze 实战：搭建办公助手 Skill
date: "2026-04-06 14:30:00"
tags: ["AI Skill", "Coze", "实战", "办公助手"]
categories: ["AI Skills 课程"]
cover: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop"
---


<!-- more -->

![第7讲：Coze 实战：搭建办公助手 Skill](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)

# 第7讲：Coze 实战：搭建办公助手 Skill

> 动手搭建一个完整的办公助手，掌握 Coze 实战开发。

## 一、项目概述

### 1.1 项目目标

搭建一个功能完整的办公助手 Bot，包含：
- 📊 Excel 数据处理（合并、拆分）
- 📝 周报自动生成
- ✅ 待办事项管理

### 1.2 技术架构

```
办公助手 Bot
├── 人设与回复逻辑
├── 插件
│   ├── Excel Processor（Excel处理）
│   └── File Manager（文件管理）
├── 工作流
│   ├── Weekly Report Generator（周报生成）
│   └── Todo Manager（待办管理）
└── 数据库
    └── todos（待办表）
```

---

## 二、步骤一：创建 Bot

### 2.1 基础配置

1. 登录 [Coze 平台](https://www.coze.cn)
2. 点击「创建 Bot」
3. 填写信息：
   - **名称**：办公小助手 Pro
   - **描述**：你的智能办公伙伴，帮你处理Excel、生成周报、管理待办
   - **图标**：上传办公相关图标

### 2.2 人设配置

```markdown
# 角色
你是专业的办公助手，擅长帮助职场人士提升工作效率。

## 技能
### 1. Excel 数据处理
- 合并多个 Excel 文件
- 拆分大型 Excel 表格
- 格式转换和数据清洗

### 2. 周报生成
- 根据工作内容自动生成周报
- 支持多种模板风格
- 可导出为 Word 或 PDF

### 3. 待办管理
- 添加、查看、完成待办事项
- 设置提醒时间
- 分类管理

## 工作流程
1. 理解用户需求
2. 确认必要信息
3. 调用相应工具
4. 返回处理结果

## 限制
1. 只处理办公相关任务
2. 不处理敏感或违法内容
3. 文件大小限制 50MB

## 回复格式
- 使用友好亲切的语气
- 关键信息用 **粗体** 标注
- 步骤用 1️⃣ 2️⃣ 3️⃣ 编号
- 适当使用 emoji 增加亲和力

## 开场白
你好！我是你的办公小助手 Pro 🎯

我可以帮你：
📊 **Excel 处理** - 合并、拆分、转换
📝 **周报生成** - 自动整理工作内容
✅ **待办管理** - 记录和追踪任务

直接告诉我你想做什么，我会一步步引导你完成！
```

---

## 三、步骤二：开发 Excel 处理插件

### 3.1 创建插件

1. 点击「插件」→「创建插件」
2. 配置：
   - 名称：Excel Processor
   - 描述：专业的 Excel 文件处理工具
   - 运行方式：云侧插件

### 3.2 创建工具：合并 Excel

**工具配置**：
```yaml
名称: merge_excel
描述: 合并多个 Excel 文件

输入参数:
  file_urls:
    类型: array
    描述: Excel 文件的 URL 列表
    必填: true
  merge_mode:
    类型: string
    描述: 合并方式
    必填: false
    默认值: vertical
    枚举值: [vertical, horizontal]

输出参数:
  result_url:
    类型: string
    描述: 合并后的文件下载链接
  row_count:
    类型: number
    描述: 总行数
  success:
    类型: boolean
    描述: 是否成功
```

**代码实现**：
```python
import pandas as pd
import requests
from io import BytesIO

def main(args):
    file_urls = args.get('file_urls', [])
    merge_mode = args.get('merge_mode', 'vertical')
    
    if not file_urls:
        return {"error": "请提供文件", "success": False}
    
    try:
        # 读取所有文件
        dfs = []
        for url in file_urls:
            response = requests.get(url, timeout=30)
            df = pd.read_excel(BytesIO(response.content))
            dfs.append(df)
        
        # 合并
        if merge_mode == 'vertical':
            result = pd.concat(dfs, ignore_index=True)
        else:
            result = pd.concat(dfs, axis=1)
        
        # 保存到临时存储（实际使用云存储）
        output = BytesIO()
        result.to_excel(output, index=False)
        output.seek(0)
        
        # 上传获取 URL（伪代码）
        result_url = upload_to_storage(output)
        
        return {
            "result_url": result_url,
            "row_count": len(result),
            "success": True
        }
    except Exception as e:
        return {"error": str(e), "success": False}
```

### 3.3 创建工具：拆分 Excel

```python
def split_excel(args):
    file_url = args.get('file_url')
    split_column = args.get('split_column')
    
    # 读取文件
    response = requests.get(file_url)
    df = pd.read_excel(BytesIO(response.content))
    
    # 按列拆分
    grouped = df.groupby(split_column)
    result_urls = []
    
    for name, group in grouped:
        output = BytesIO()
        group.to_excel(output, index=False)
        output.seek(0)
        url = upload_to_storage(output, f"{name}.xlsx")
        result_urls.append({"name": name, "url": url})
    
    return {
        "files": result_urls,
        "count": len(result_urls),
        "success": True
    }
```

---

## 四、步骤三：创建周报生成工作流

### 4.1 工作流设计

```
开始（接收工作内容）
    │
    ▼
大模型节点（整理和润色）
    │
    ▼
代码节点（生成文档）
    │
    ▼
结束（返回下载链接）
```

### 4.2 节点配置

**开始节点**：
```yaml
输入参数:
  work_items:
    类型: array
    描述: 本周完成的工作列表
  challenges:
    类型: string
    描述: 遇到的问题
  next_week_plan:
    类型: string
    描述: 下周计划
```

**大模型节点**：
```
系统提示：
你是一个专业的周报撰写助手。请根据用户提供的工作内容，
生成一份结构清晰、语言专业的周报。

周报结构：
1. 本周工作总结
2. 重点项目进展
3. 问题与反思
4. 下周工作计划

要求：
- 使用专业但不生硬的语气
- 突出成果和亮点
- 问题部分要体现解决方案
```

**代码节点**：
```python
from docx import Document
from docx.shared import Pt, RGBColor

def main(args):
    content = args.get('report_content')
    
    # 创建 Word 文档
    doc = Document()
    
    # 标题
    title = doc.add_heading('工作周报', 0)
    title.alignment = 1  # 居中
    
    # 日期
    doc.add_paragraph(f'报告周期：{get_week_range()}')
    doc.add_paragraph()
    
    # 内容
    doc.add_heading('一、本周工作总结', level=1)
    doc.add_paragraph(content['summary'])
    
    doc.add_heading('二、重点项目进展', level=1)
    for project in content['projects']:
        doc.add_heading(project['name'], level=2)
        doc.add_paragraph(project['progress'])
    
    # 保存
    output = BytesIO()
    doc.save(output)
    output.seek(0)
    
    url = upload_to_storage(output, "周报.docx")
    
    return {"download_url": url}
```

---

## 五、步骤四：创建待办管理工作流

### 5.1 数据库设计

```sql
表名: todos
字段:
  - id: 主键
  - user_id: 用户ID
  - content: 待办内容
  - status: 状态 (pending/done)
  - priority: 优先级 (high/medium/low)
  - created_at: 创建时间
  - due_date: 截止日期
```

### 5.2 工作流：添加待办

```
开始（接收待办内容）
    │
    ▼
代码节点（保存到数据库）
    │
    ▼
结束（返回确认）
```

```python
def add_todo(args):
    user_id = args.get('user_id')
    content = args.get('content')
    priority = args.get('priority', 'medium')
    
    # 插入数据库
    database.insert('todos', {
        'user_id': user_id,
        'content': content,
        'status': 'pending',
        'priority': priority,
        'created_at': datetime.now()
    })
    
    return {
        "message": f"✅ 已添加待办：{content}",
        "success": True
    }
```

### 5.3 工作流：查看待办

```python
def list_todos(args):
    user_id = args.get('user_id')
    status = args.get('status', 'pending')
    
    # 查询数据库
    todos = database.query('todos', {
        'user_id': user_id,
        'status': status
    })
    
    # 格式化输出
    result = []
    for todo in todos:
        emoji = "🔴" if todo['priority'] == 'high' else "🟡" if todo['priority'] == 'medium' else "🟢"
        result.append(f"{emoji} {todo['content']}")
    
    return {
        "todos": result,
        "count": len(result)
    }
```

---

## 六、步骤五：整合到 Bot

### 6.1 添加插件

在 Bot 编辑页面：
1. 点击「插件」→「+」
2. 选择「Excel Processor」
3. 添加到 Bot

### 6.2 添加工作流

1. 点击「工作流」→「+」
2. 选择「周报生成」和「待办管理」
3. 添加到 Bot

### 6.3 更新人设

```markdown
## 工具使用说明

当用户需要处理 Excel 时：
1. 询问文件和合并/拆分方式
2. 调用 Excel Processor 插件
3. 返回处理结果

当用户需要生成周报时：
1. 收集工作内容、问题、计划
2. 调用周报生成工作流
3. 返回文档下载链接

当用户需要管理待办时：
1. 识别具体操作（添加/查看/完成）
2. 调用待办管理工作流
3. 返回操作结果
```

---

## 七、步骤六：测试与优化

### 7.1 测试用例

| 场景 | 输入 | 预期结果 |
|------|------|----------|
| Excel 合并 | "合并这3个Excel" | 询问文件和方式，返回合并结果 |
| 周报生成 | "帮我生成本周周报" | 收集信息，生成文档 |
| 添加待办 | "记得下午开会" | 保存待办，返回确认 |
| 查看待办 | "有什么待办" | 返回待办列表 |

### 7.2 常见问题

**Q1：插件调用失败**
- 检查 API 地址是否正确
- 查看日志中的错误信息
- 确认网络连接

**Q2：工作流执行超时**
- 优化代码执行效率
- 减少不必要的计算
- 使用异步处理

---

## 八、步骤七：发布

### 8.1 发布配置

1. 点击「发布」
2. 选择发布渠道：
   - ✅ Coze 商店
   - ✅ 豆包
   - ⬜ 飞书（可选）
3. 填写发布信息：
   - 分类：效率工具
   - 标签：Excel, 周报, 待办, 办公

### 8.2 推广技巧

- 生成分享二维码
- 编写使用教程
- 收集用户反馈

---

## 九、课后作业

### 作业1：扩展功能

为办公助手添加：
- PDF 转 Word 功能
- 数据统计图表生成
- 定时提醒功能

### 作业2：优化体验

- 添加更多错误处理
- 优化对话流程
- 增加使用示例

---

## 十、下节预告

**第8讲：OpenClaw 平台深度解析**

我们将学习：
- OpenClaw 的架构和特点
- 本地开发环境搭建
- ClawHub 生态使用

---

## 加入学习群

实战遇到问题？欢迎加入交流群：

👉 **[加入AI编程学习交流群](https://www.python4office.cn/wechat-group/)**

![点击加入](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

---

*本讲是《Skills 从入门到实践》系列课程的第7讲，恭喜你完成了第一个完整的办公助手 Skill！*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



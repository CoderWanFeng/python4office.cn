---
title: "第6讲：Coze 扣子平台深度解析"
date: 2026-04-06 14:00:00
tags: ["AI Skill", "Coze", "扣子", "平台"]
categories: ["AI Skills 课程"]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<!-- more -->

![第6讲：Coze 扣子平台深度解析 - 配图1](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)

# 第6讲：Coze 扣子平台深度解析

> 全面掌握 Coze 平台的核心功能和高级技巧。

## 一、Coze 平台架构

### 1.1 整体架构

```
Coze 平台
├── 应用层
│   ├── Bot（对话机器人）
│   ├── 插件（Plugin）
│   ├── 工作流（Workflow）
│   └── 知识库（Knowledge）
│
├── 能力层
│   ├── 大模型（LLM）
│   ├── 多模态（图片/语音）
│   └── 工具调用（Function Calling）
│
└── 生态层
    ├── Coze 商店
    ├── 豆包（抖音）
    ├── 飞书
    └── 微信
```

### 1.2 核心概念关系

```
Bot（机器人）
    ├── 人设与回复逻辑（Prompt）
    ├── 插件（扩展能力）
    ├── 工作流（复杂逻辑）
    ├── 知识库（私有数据）
    └── 数据库（持久化）
```

---

## 二、Bot 开发详解

### 2.1 Bot 配置全解析

**基础配置**：
- **名称**：Bot 的显示名称
- **描述**：一句话介绍 Bot 的功能
- **图标**：视觉标识
- **标签**：分类和搜索用

**高级配置**：
- **模型选择**：
  - 豆包大模型（默认）
  - GPT-4（需申请）
  - Claude（需申请）
- **回复长度**：控制回复的详细程度
- **上下文长度**：记忆多少轮对话

### 2.2 人设与回复逻辑

**结构化 Prompt 模板**：

```markdown
# 角色
你是[角色名称]，[角色定位]

## 背景
[用户群体]使用你的服务，他们的痛点是[痛点描述]

## 技能
### 技能1：[技能名称]
- 功能：[具体功能]
- 触发条件：[什么时候使用]
- 使用方式：[如何使用]

### 技能2：[技能名称]
...

## 工作流程
1. [步骤1]
2. [步骤2]
3. [步骤3]

## 限制
- [限制1]
- [限制2]

## 输出格式
[格式要求]

## 示例
### 示例1
用户：[输入]
助手：[输出]

### 示例2
...
```

### 2.3 开场白设计

**开场白的作用**：
- 建立第一印象
- 说明 Bot 能力
- 引导用户开始

**优秀开场白示例**：

```
你好！我是你的办公小助手 🤖

我可以帮你：
📊 处理 Excel 文件（合并、拆分、转换）
📄 转换 PDF 格式
📷 识别发票信息
📝 生成工作周报

直接告诉我你想做什么，或者发送"帮助"查看详细说明！
```

---

## 三、插件系统详解

### 3.1 插件类型

| 类型 | 说明 | 适用场景 |
|------|------|----------|
| **官方插件** | Coze 提供的标准插件 | 通用能力（天气、新闻等） |
| **市场插件** | 第三方开发者分享 | 特定功能（OCR、翻译等） |
| **自定义插件** | 自己开发的插件 | 私有 API、定制功能 |

### 3.2 自定义插件开发

**步骤1：创建插件**

```
插件管理 → 创建插件
├── 插件名称：发票识别
├── 插件描述：识别增值税发票信息
├── 运行方式：云侧插件（Coze 服务器运行）
│             或 端侧插件（本地运行）
└── 创建工具
```

**步骤2：配置工具**

```yaml
# 工具配置示例
工具名称: recognize_invoice
工具描述: 识别发票图片，提取金额、日期、发票号等信息

输入参数:
  image_url:
    类型: string
    描述: 发票图片的 URL 地址
    必填: true
    
  invoice_type:
    类型: string
    描述: 发票类型
    必填: false
    枚举值: [增值税普通发票, 增值税专用发票, 电子发票]

输出参数:
  invoice_code:
    类型: string
    描述: 发票代码
  
  invoice_number:
    类型: string
    描述: 发票号码
  
  amount:
    类型: number
    描述: 金额
  
  date:
    类型: string
    描述: 开票日期
```

**步骤3：编写代码**

```python
import requests
import json

def main(args):
    image_url = args.get('image_url')
    invoice_type = args.get('invoice_type', '增值税普通发票')
    
    # 调用 OCR API
    api_url = "https://api.ocr-service.com/recognize"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "image_url": image_url,
        "type": invoice_type
    }
    
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        result = response.json()
        
        return {
            "invoice_code": result.get('code'),
            "invoice_number": result.get('number'),
            "amount": result.get('amount'),
            "date": result.get('date'),
            "success": True
        }
    except Exception as e:
        return {
            "error": str(e),
            "success": False
        }
```

### 3.3 插件最佳实践

✅ **DO**：
- 参数命名清晰（使用英文，描述用中文）
- 提供默认值和枚举值
- 完善的错误处理
- 添加超时控制

❌ **DON'T**：
- 参数过多（建议不超过 5 个）
- 返回数据过大（建议不超过 10KB）
- 没有错误处理
- 硬编码敏感信息

---

## 四、工作流高级技巧

### 4.1 工作流节点类型

| 节点类型 | 功能 | 使用场景 |
|----------|------|----------|
| **开始** | 定义输入参数 | 每个工作流必需 |
| **大模型** | 调用 AI 处理 | 意图识别、文本生成 |
| **代码** | 执行 Python/Node | 数据处理、逻辑判断 |
| **知识库** | 检索私有数据 | FAQ、文档问答 |
| **选择器** | 条件分支 | 多意图处理 |
| **循环** | 批量处理 | 处理列表数据 |
| **结束** | 返回结果 | 每个工作流必需 |

### 4.2 复杂工作流示例：智能客服

```
开始（接收用户问题）
    │
    ▼
大模型节点（意图识别）
    │
    ├── 产品咨询 ──► 知识库检索 ──► 大模型生成回答 ──► 结束
    │
    ├── 订单查询 ──► 代码节点（查询数据库） ──► 格式化输出 ──► 结束
    │
    ├── 投诉建议 ──► 代码节点（记录工单） ──► 结束
    │
    └── 其他 ──► 大模型（通用回答） ──► 结束
```

### 4.3 代码节点技巧

**技巧1：数据处理**

```python
def main(args):
    # 接收输入
    raw_data = args.get('data', [])
    
    # 数据处理
    processed = []
    for item in raw_data:
        processed.append({
            "id": item.get('id'),
            "name": item.get('name').strip(),
            "amount": float(item.get('amount', 0)),
            "status": "已完成" if item.get('done') else "进行中"
        })
    
    # 排序
    processed.sort(key=lambda x: x['amount'], reverse=True)
    
    # 返回
    return {
        "result": processed,
        "count": len(processed),
        "total_amount": sum(item['amount'] for item in processed)
    }
```

**技巧2：API 调用**

```python
import requests

def main(args):
    city = args.get('city', '北京')
    
    # 调用外部 API
    url = f"https://api.weather.com/v1/current?city={city}"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        
        return {
            "city": city,
            "weather": data.get('weather'),
            "temp": data.get('temperature'),
            "success": True
        }
    except requests.Timeout:
        return {"error": "请求超时", "success": False}
    except Exception as e:
        return {"error": str(e), "success": False}
```

**技巧3：条件判断**

```python
def main(args):
    score = args.get('score', 0)
    
    if score >= 90:
        level = "优秀"
        emoji = "🌟"
    elif score >= 80:
        level = "良好"
        emoji = "👍"
    elif score >= 60:
        level = "及格"
        emoji = "✅"
    else:
        level = "不及格"
        emoji = "💪"
    
    return {
        "score": score,
        "level": level,
        "emoji": emoji,
        "message": f"你的成绩是{score}分，{level}{emoji}"
    }
```

---

## 五、知识库使用

### 5.1 知识库类型

| 类型 | 说明 | 适用场景 |
|------|------|----------|
| **文本** | 纯文本文档 | FAQ、帮助文档 |
| **表格** | 结构化数据 | 产品规格、价格表 |
| **图片** | 带文字的图片 | 说明书、海报 |

### 5.2 知识库配置

**创建知识库**：
1. 点击「知识库」→「创建知识库」
2. 选择类型：文本/表格/图片
3. 上传文档或手动输入
4. 配置检索参数

**检索参数**：
- **匹配度阈值**：0-1，越高要求越严格
- **最大召回数量**：一次返回多少条结果
- **重排序**：是否使用模型优化排序

### 5.3 在工作流中使用

```
用户问题
    │
    ▼
知识库检索节点
    ├── 找到相关内容 ──► 大模型生成回答
    └── 未找到 ──► 大模型基于通用知识回答
```

---

## 六、数据库功能

### 6.1 数据库用途

- 保存用户数据（待办、偏好设置）
- 记录使用日志
- 实现多轮对话记忆

### 6.2 数据库操作

**添加数据**：
```javascript
// 代码节点中操作数据库
const { database } = require('coze');

async function main(args) {
    await database.insert('todos', {
        user_id: args.user_id,
        content: args.content,
        status: 'pending',
        created_at: new Date()
    });
    
    return { success: true };
}
```

**查询数据**：
```javascript
async function main(args) {
    const todos = await database.query('todos', {
        user_id: args.user_id,
        status: 'pending'
    });
    
    return { todos: todos };
}
```

---

## 七、发布与运营

### 7.1 发布渠道

| 渠道 | 说明 | 适合场景 |
|------|------|----------|
| **Coze 商店** | 官方应用市场 | 获取自然流量 |
| **豆包** | 抖音生态 | C 端用户 |
| **飞书** | 企业办公 | B 端用户 |
| **微信** | 公众号/小程序 | 私域流量 |
| **API** | 接口调用 | 集成到自有产品 |

### 7.2 数据分析

在「数据分析」页面查看：
- 对话次数
- 活跃用户
- 满意度评分
- 常见问题

### 7.3 持续优化

根据数据反馈优化：
1. 查看用户常问的问题
2. 补充知识库内容
3. 优化 Prompt
4. 修复用户反馈的问题

---

## 八、实战：开发一个完整的办公助手

### 8.1 需求分析

**功能列表**：
1. Excel 文件处理（合并、拆分）
2. PDF 转换
3. 待办事项管理
4. 周报生成

### 8.2 架构设计

```
办公助手 Bot
├── 人设：专业办公助手
├── 插件：
│   ├── Excel 处理插件
│   ├── PDF 转换插件
│   └── 文件存储插件
├── 工作流：
│   ├── 周报生成工作流
│   └── 待办管理工作流
└── 数据库：
    └── 待办数据表
```

### 8.3 开发步骤

1. 创建 Bot，配置人设
2. 开发 Excel 处理插件
3. 开发 PDF 转换插件
4. 创建周报生成工作流
5. 创建待办管理工作流
6. 配置数据库
7. 测试并发布

---

## 九、下节预告

**第7讲：Coze 实战：搭建办公助手 Skill**

我们将动手：
- 从零搭建一个完整的办公助手
- 实现 Excel 处理和周报生成功能
- 发布到 Coze 商店

---

## 加入学习群

Coze 使用有疑问？欢迎加入交流群：

👉 **[加入AI编程学习交流群](https://www.python4office.cn/wechat-group/)**

![点击加入](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

---

*本讲是《Skills 从入门到实践》系列课程的第6讲，下一讲我们将进行 Coze 实战。*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



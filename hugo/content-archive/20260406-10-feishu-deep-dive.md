---
title: "\"第10讲：飞书 CLI 平台深度解析\""
date: "2026-04-06T16:00:00+08:00"
tags:
  - "AI Skill"
  - ""
  - "飞书"
  - ""
  - "Feishu"
  - ""
  - "CLI"
  - ""
  - "企业"
categories:
  - "AI Skills 课程"
---


<!-- more -->
# 第10讲：飞书 CLI 平台深度解析

> 掌握企业级 Skill 平台飞书 CLI，开发团队协作 Skill。

## 一、飞书 CLI 简介

### 1.1 什么是飞书 CLI？

飞书 CLI 是飞书开放的 **AI Agent Skill 开发框架**：
- ✅ 与飞书生态深度集成
- ✅ 企业级权限管理
- ✅ 群聊、审批、日历原生支持
- ✅ 3月28日刚开源（红利期）

### 1.2 核心能力

| 能力 | 说明 | 场景 |
|------|------|------|
| **群聊机器人** | 在群聊中交互 | 团队助手 |
| **审批集成** | 对接审批流程 | 自动化审批 |
| **日历操作** | 管理日程 | 会议助手 |
| **文档协作** | 操作飞书文档 | 知识管理 |
| **多维表格** | 操作 Bitable | 数据管理 |

---

## 二、环境搭建

### 2.1 安装飞书 CLI

```bash
# 安装
npm install -g @larksuite/cli

# 验证
feishu --version
```

### 2.2 初始化项目

```bash
# 创建项目
feishu init my-feishu-skill

# 选择模板
cd my-feishu-skill
```

### 2.3 项目结构

```
my-feishu-skill/
├── skill.json          # Skill 配置
├── index.js            # 主入口
├── handlers/           # 事件处理器
│   ├── message.js      # 消息处理
│   ├── command.js      # 命令处理
│   └── event.js        # 事件处理
├── utils/              # 工具函数
└── package.json
```

---

## 三、开发第一个飞书 Skill

### 3.1 配置文件

```json
// skill.json
{
  "name": "team-assistant",
  "description": "团队协作助手",
  "version": "1.0.0",
  "entry": "index.js",
  "permissions": [
    "im:chat",
    "im:message",
    "calendar:calendar"
  ]
}
```

### 3.2 主程序

```javascript
// index.js
const { Skill } = require('@larksuite/skill-sdk');
const messageHandler = require('./handlers/message');
const commandHandler = require('./handlers/command');

const skill = new Skill({
  name: 'team-assistant',
  version: '1.0.0'
});

// 处理消息
skill.on('message', messageHandler);

// 处理命令
skill.on('command', commandHandler);

// 启动
skill.start();
```

### 3.3 消息处理器

```javascript
// handlers/message.js
module.exports = async (ctx) => {
  const { message, user } = ctx;
  const content = message.content;
  
  // 识别意图
  if (content.includes('创建会议')) {
    return handleCreateMeeting(ctx);
  } else if (content.includes('查看待办')) {
    return handleViewTodos(ctx);
  } else {
    return {
      content: '我可以帮你：\n1. 创建会议\n2. 查看待办\n3. 发送通知'
    };
  }
};

async function handleCreateMeeting(ctx) {
  const { user, message } = ctx;
  
  // 创建日历事件
  const event = await ctx.calendar.createEvent({
    title: '团队周会',
    start_time: Date.now() + 3600000,
    end_time: Date.now() + 7200000,
    attendees: [user.open_id]
  });
  
  return {
    content: `已创建会议：团队周会\n时间：${formatTime(event.start_time)}`
  };
}
```

---

## 四、企业级特性

### 4.1 权限管理

```javascript
// 检查权限
const hasPermission = await ctx.auth.checkPermission({
  user: user.open_id,
  permission: 'calendar:write'
});

if (!hasPermission) {
  return { content: '你没有创建会议的权限' };
}
```

### 4.2 审批集成

```javascript
// 发起审批
const approval = await ctx.approval.create({
  approval_code: 'MEETING_ROOM',
  form_data: {
    room: '会议室A',
    date: '2026-04-10',
    time: '14:00-16:00'
  }
});
```

---

## 五、下节预告

**第11讲：飞书 CLI 实战：团队协作 Skill**

我们将开发一个完整的团队助手，集成：
- 会议管理
- 任务分配
- 日报收集

---

## 加入学习群

👉 **[加入AI编程学习交流群](https://www.python4office.cn/wechat-group/)**

![点击加入](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

---

*本讲是《Skills 从入门到实践》系列课程的第10讲。*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



---
title: 第11讲：飞书 CLI 实战：团队协作 Skill
date: "2026-04-06 16:30:00"
tags: ["AI Skill", "飞书", "实战", "团队协作"]
categories: ["AI Skills 课程"]
cover: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop"
---


<!-- more -->

![第11讲：飞书 CLI 实战：团队协作 Skill](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)

# 第11讲：飞书 CLI 实战：团队协作 Skill

> 动手开发企业级团队协作 Skill，掌握飞书生态开发。

## 一、项目目标

开发「团队管家」Skill，功能包括：
- 📅 智能会议管理
- ✅ 任务分配与追踪
- 📝 日报自动收集
- 📊 团队数据统计

## 二、功能设计

### 2.1 会议管理

```
用户：@团队管家 创建周会
Skill：好的！创建周会：
      📅 时间：下周一 14:00（默认）
      👥 参与人：@所有人
      📍 地点：线上
      
      确认请回复"确认"，修改请回复具体信息
```

### 2.2 任务分配

```
用户：@团队管家 分配任务
Skill：请提供任务信息：
      1. 任务内容
      2. 负责人（@成员）
      3. 截止时间

用户：完成需求文档 @张三 本周五
Skill：✅ 任务已分配：
      📋 完成需求文档
      👤 负责人：张三
      ⏰ 截止：本周五 18:00
      
      已通知张三
```

## 三、核心代码

### 3.1 会议管理模块

```javascript
// handlers/meeting.js
const { CalendarAPI } = require('../utils/calendar');

class MeetingHandler {
  async createMeeting(ctx, params) {
    const { title, time, attendees } = params;
    
    // 创建日历事件
    const event = await CalendarAPI.createEvent({
      summary: title,
      start: { dateTime: time },
      end: { dateTime: time + 3600000 },
      attendees: attendees.map(id => ({ email: id }))
    });
    
    // 发送通知
    await ctx.sendMessage({
      content: `📅 会议已创建\n标题：${title}\n时间：${formatTime(time)}`,
      mention: attendees
    });
    
    return event;
  }
  
  async remindMeeting(ctx, eventId) {
    const event = await CalendarAPI.getEvent(eventId);
    
    // 提前15分钟提醒
    await ctx.sendMessage({
      content: `⏰ 会议提醒\n${event.summary} 将在15分钟后开始`,
      mention: event.attendees
    });
  }
}

module.exports = MeetingHandler;
```

### 3.2 任务管理模块

```javascript
// handlers/task.js
const BitableAPI = require('../utils/bitable');

class TaskHandler {
  constructor() {
    this.taskTable = new BitableAPI('tasks');
  }
  
  async createTask(ctx, content, assignee, dueDate) {
    // 创建任务记录
    const task = await this.taskTable.create({
      content,
      assignee,
      dueDate,
      status: 'pending',
      createdBy: ctx.user.open_id,
      createdAt: new Date()
    });
    
    // 通知负责人
    await ctx.sendMessage({
      content: `📋 新任务\n${content}\n截止：${dueDate}`,
      open_id: assignee
    });
    
    return task;
  }
  
  async getUserTasks(userId) {
    return await this.taskTable.query({
      assignee: userId,
      status: 'pending'
    });
  }
  
  async completeTask(taskId) {
    return await this.taskTable.update(taskId, {
      status: 'completed',
      completedAt: new Date()
    });
  }
}

module.exports = TaskHandler;
```

## 四、部署上线

### 4.1 打包发布

```bash
# 打包
feishu package

# 发布到企业
feishu publish --enterprise YOUR_ENTERPRISE_ID

# 安装到群聊
feishu install --chat CHAT_ID
```

### 4.2 配置机器人

1. 进入飞书管理后台
2. 创建自定义机器人
3. 配置 Webhook 地址
4. 设置权限范围

---

## 五、下节预告

**第12讲：Excel 自动化 Skill 开发**

进入办公场景实战章节，开发 Excel 处理 Skill。

---

## 加入学习群

👉 **[加入AI编程学习交流群](https://www.python4office.cn/wechat-group/)**

![点击加入](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

---

*本讲是《Skills 从入门到实践》系列课程的第11讲。*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



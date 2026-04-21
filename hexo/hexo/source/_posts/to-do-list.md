---
title: "程序员晚枫2022年学习计划 | 待办事项清单(持续更新)"
date: 2022-01-24 21:15:48
tags: ["学习计划", "程序员成长", "Python学习", "待办清单", "2022计划"]
categories: ["学习方法"]
description: "程序员晚枫2022年学习计划清单，包含Python、Flask、Celery、Git等技术学习目标。附个人成长路线规划和执行记录。"
---

<!-- more -->
# 程序员晚枫2022年学习计划 | 待办事项清单(持续更新)

> 本文记录我的个人学习计划和待办事项，持续更新中。

---

## 学习计划总览

| 类别 | 学习目标 | 状态 | 完成时间 |
|------|----------|------|----------|
| Python进阶 | pandas数据分析 | ⏳进行中 | 2022-04 |
| Web开发 | Flask框架 | 📅计划中 | 2022-04 |
| 云服务 | 腾讯云认证 | 📅计划中 | 2022-04 |
| 数据库 | SQL语法精通 | 📅计划中 | 2022-04 |
| 设计模式 | 常用设计模式 | 📅计划中 | 2022-04 |

---

## 2022年4月学习目标

### ✅ 已完成

- [x] pandas数据分析 - 完成基础学习
- [x] 腾讯云认证 - 备考中

### 📋 进行中

- [ ] Flask Web开发
- [ ] SQL高级语法
- [ ] 设计模式

---

## 2022年2月学习目标

### ✅ 已完成

- [x] Git熟练操作
  - 分支管理
  - 冲突解决
  - 常用命令

- [x] APScheduler定时任务
  - [原理详解](https://www.python4office.cn/apscheduler-study/)
  - 跑通demo

### 📋 进行中

- [ ] Hyper-V网络配置

---

## 2022年1月学习成果

### ✅ 已完成项目

| 项目 | 说明 | 教程链接 |
|------|------|----------|
| Celery异步任务 | 分布式任务队列 | [Celery入门教程](https://www.python4office.cn/celery-setup/) |
| Nginx反向代理 | 多项目端口配置 | [Nginx配置教程](../nginx-config/) |
| Supervisor进程管理 | Linux服务管理 | [Supervisor使用详解](../supervisor-config/) |
| Hexo博客优化 | 图片文件夹配置 | [Hexo安装配置](../hexo-setup-config-bug/) |
| Python单元测试 | unittest框架 | [B站视频教程](https://www.bilibili.com/video/BV1BF411e7hD) |

### 📝 技术笔记

#### Hyper-V端口映射命令

```bash
# 添加端口映射
netsh interface portproxy add v4tov4 listenport=外网端口 listenaddress=主IP connectaddress=私网IP connectport=私网IP端口
```

#### Nginx多项目配置

```nginx
# 同一域名不同路径配置不同端口
server {
    listen 80;
    server_name example.com;
    
    location /api1/ {
        proxy_pass http://localhost:3000/;
    }
    
    location /api2/ {
        proxy_pass http://localhost:4000/;
    }
}
```

---

## 学习资源推荐

### Python进阶
- [Pandas数据分析实战](https://www.python4office.cn/)
- [Python自动化办公合集](https://www.python4office.cn/)

### Web开发
- [Flask入门教程](https://www.python4office.cn/)
- [Django vs Flask对比](https://www.python4office.cn/)

### DevOps
- [Nginx配置详解](https://www.python4office.cn/nginx-config/)
- [Supervisor使用教程](https://www.python4office.cn/supervisor-config/)
- [Git进阶技巧](https://www.python4office.cn/)

---

## 关于我

我叫**程序员晚枫**，专注Python自动化办公和AI编程培训。

如果你也需要学习计划指导，可以联系我：

👉 [添加我的微信](https://www.python4office.cn/wechat-qrcode/)

---

## 相关阅读

- [刻意练习比1万小时更重要](https://www.python4office.cn/tobeu/)
- [程序员学习方法论](https://www.python4office.cn/)
- [《30讲·AI编程训练营》](https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA)

---

*程序员晚枫专注AI编程培训，帮助10000+学员从零基础到能做实战项目。*

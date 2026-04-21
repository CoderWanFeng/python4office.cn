---
title: 想用AI写代码？先申请个"API Key"身份证
date: 2026-04-16 16:55:00
author: 程序员晚枫
categories:
- AI
- 基础概念
tags:
- API Key
- API
order: 2
description: 每次看AI教程都让你"申请API Key"搞不懂？程序员晚枫用大白话帮你搞懂API Key是什么，怎么用，怎么保安全！
---

> **作者：程序员晚枫**

每次看AI教程都让你"申请API Key"搞不懂？程序员晚枫用大白话帮你搞懂API Key是什么，怎么用，怎么保安全！

---

## 👋 先问个扎心的问题

你有没有遇到过这种情况：
- 想用AI写代码，教程第一步就说"去申请API Key"
- 看到API Key这串乱码，完全不知道是啥
- 怕乱填会被扣钱，所以一直不敢用

别慌，今天咱们用大白话把**API Key**彻底讲清楚。

---

## 🎯 一句话先说清楚

::: tip 核心结论
**API Key = 使用AI服务的"身份证号"**

想用别人的AI服务？先申请一个"身份证号"，每次请求都带上，证明"这是我"。
:::

---

## 💡 API Key到底是啥？

咱们用个生活场景类比你就懂了：

### 🏦 去银行办事

| 场景 | 没有身份证 | 有身份证 |
|------|------------|----------|
| 去银行存钱 | ❌ 柜员拒绝办理 | ✅ 知道你是谁，可以办 |
| 查询余额 | ❌ 不知道是谁的账户 | ✅ 知道是你，给你查 |
| 办理业务 | ❌ 无法确认身份 | ✅ 正常办理 |
| **API Key** | **没有API Key** | **有API Key** |
| **AI服务** | ❌ AI不知道你是谁，拒绝 | ✅ AI识别你，开始工作 |

### 🤖 调用AI服务

```python
# 想用ChatGPT帮你写代码，你得先"亮明身份"

response = call_ai_service(
    api_key="sk-proj-AbCdEf1234...",  # 这是你的"身份证号"
    message="帮我写一个Python爬虫"     # 你的需求
)

# AI拿到API Key → 验证身份 → 知道是你 → 开始工作
```

**没有API Key，AI服务会直接拒绝你，就像去银行没带身份证一样。**

---

## 🔍 API Key长什么样？

API Key通常是一串乱码，看起来像这样：

```
OpenAI的API Key：
sk-proj-AbCdEf1234...XyZ

通用的格式：
{平台前缀}-{随机字符串}
```

| 平台 | API Key格式示例 |
|------|----------------|
| OpenAI/ChatGPT | sk-proj-xxxxx |
| 阿里云千问 | sk-xxxxx |
| 百度文心一言 | xxxx-xxxx-xxxx |
| Claude | sk-ant-xxxxx |

**记住：API Key = 密码级别的隐私！**

---

## 🚀 API Key在哪用？

### 场景1：写代码调用AI

```python
# 最常见的场景：在自己的Python脚本里用AI
import openai

openai.api_key = "sk-proj-xxxxx..."  # 填你的API Key

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "帮我写代码"}]
)
print(response.choices[0].message)
```

### 场景2：配置到环境变量

```bash
# 更安全的做法：把API Key配置到环境变量
export OPENAI_API_KEY="sk-proj-xxxxx..."
export ANTHROPIC_API_KEY="sk-ant-xxxxx..."

# 程序里读取环境变量
import os
api_key = os.getenv("OPENAI_API_KEY")
```

### 场景3：AI工具配置

很多AI工具（如Cursor、Windsurf、GitHub Copilot）也需要API Key：

```
工具设置 → 填入你的API Key → 开始使用
```

---

## 🛡️ API Key安全吗？千万别泄露！

::: danger 重要警告
**API Key = 密码！泄露了会被人白嫖！**
:::

### ❌ 千万别做这些事：

| 错误做法 | 后果 |
|----------|------|
| 📱 发朋友圈/群里配图展示API Key | 别人看到了会盗用你账号 |
| 💻 上传代码到GitHub时没删API Key | 全世界都能看到你的密钥 |
| 🌐 写在HTML/JS前端代码里 | 所有人都能F12看到 |
| 📧 发邮件给同事时直接贴明文 | 邮件可能被截获或转发泄露 |

### ✅ 正确做法：

| 正确做法 | 原因 |
|----------|------|
| 🔒 用`.gitignore`忽略包含API Key的文件 | 防止上传到代码仓库 |
| 🗝️ 使用环境变量存储 | 不暴露在代码里 |
| 📝 使用`.env`文件并添加到`.gitignore` | 开发时方便，上线时安全 |
| 🔄 定期更换API Key | 万一泄露了降低损失 |

### 安全配置示例：

```python
# ✅ 正确：从环境变量读取
import os
api_key = os.getenv("OPENAI_API_KEY")

# ❌ 错误：直接硬编码
api_key = "sk-proj-xxxxx..."  # 这种千万别写！
```

---

## 💰 API Key和钱的关系？

是的，API Key和你的钱包直接相关！

### 计费逻辑：

```
你的API Key 
  ↓
AI系统识别你的账号
  ↓
记录你用了多少Token（参考上一讲）
  ↓
按Token数量从你账户扣钱
  ↓
给你发账单
```

### ⚠️ API Key泄露的后果：

1. **账户被盗用**：别人用你的钱用AI
2. **产生巨额账单**：几分钟刷几千块都有可能
3. **账户被封**：平台检测到异常直接封号

---

## 🔥 新闻里那些API Key术语，到底是什么意思？

### "需要先申请API Key"
= 想用这个AI服务？先去注册账号，然后在控制台申请一个"钥匙"

**怎么申请（以OpenAI为例）：**
1. 去 platform.openai.com 注册账号
2. 找到"API Keys"页面
3. 点击"Create new secret key"
4. 复制生成的API Key（注意只显示一次！）

### "API Key泄露了"
= 你的"身份证号"被别人知道了，可能被盗用

**泄露了怎么办：**
1. **立即去平台撤销该API Key**
2. 申请新的API Key
3. 检查最近的使用记录，看有没有异常

### "平台配置API Key"
= 在AI工具里"绑定"你的账号，让它能帮你调用AI服务

---

## ⚠️ 常见误区避坑

### ❌ 误区1："API Key可以随便给人"
**❌ 错！这是密码级别的隐私！**
- API Key能直接访问你的AI账户
- 给别人等于把你的"钱包"给出去

### ❌ 误区2："GitHub上代码都写API Key，没事吧"
**❌ 危险！GitHub是公开的！**
- GitHub上所有人都能看到你的代码
- 包括API Key
- 爬虫会专门扫GitHub找密钥

### ❌ 误区3："API Key用别人的也行"
**❌ 违规！**
- 大部分平台禁止共享API Key
- 被发现会封号
- 别人的API Key随时可能失效

---

## 🎓 为什么要懂API Key？

1. **必须会用**：想用AI写代码，API Key是第一步
2. **必须会申请**：每个平台都有申请流程
3. **必须会保护**：泄露了会损失钱
4. **职业必备**：程序员日常开发中经常用

---

## ✨ 总结

::: success 核心要点回顾
- API Key = 使用AI服务的"身份证号"
- 没有API Key，AI服务会拒绝你
- API Key是密码级别的隐私，千万别泄露
- 从环境变量读取API Key，不要硬编码
- GitHub上传代码前要删除API Key
:::

---

## 💬 互动时间

看完这篇文章，下次再看到"申请API Key"是不是就有底了？

**你现在能搞明白：**
- ✅ 为什么AI服务需要API Key？
- ✅ API Key泄露了会有什么后果？
- ✅ 怎么安全地保存和使用API Key？

**如果这篇文章对你有帮助：**
- 👍 **点个赞**让更多人看到
- 💬 **评论区说说**你有没有因为API Key踩过坑？
- 🔄 **转发给朋友**，下次别再不敢申请API Key了

---

## 📚 课程导航

👆 **上一讲**：[什么是开源？](./01-open-source) - 为什么有的AI能免费用

👇 **下一讲**：[什么是Token？](./03-token) - AI怎么按"Token"收费

---

> 📢 **程序员晚枫**专注分享：程序员副业、AI工具、Python办公自动化

关注公众号【程序员晚枫】，回复【AI词汇】，获取全套课程原文


---

## 相关阅读

- [好险！差点被裁，多亏我学了AI](https://mp.weixin.qq.com/s/Jr1bGTob2SU2TTX6q-b2hA)
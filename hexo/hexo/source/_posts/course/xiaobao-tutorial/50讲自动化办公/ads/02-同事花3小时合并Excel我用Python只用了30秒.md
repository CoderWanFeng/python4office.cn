---
title: 同事花3小时合并Excel我用Python只用了30秒
date: 2026-04-17 10:00:00
tags: [Python自动化办公, Excel, 效率, 50讲]
cover: https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop
---

![同事花3小时合并Excel我用Python只用了30秒 - 配图1](https://images.unsplash.com/photo-152637909?w=800&h=400&fit=crop)
![同事花3小时合并Excel我用Python只用了30秒 - 配图2](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)


大家好，这里是程序员晚枫，专注Python自动化办公5年了。

昨天群里有个小伙伴吐槽：

> "老板给了我50个Excel，让我合并成一个，搞了一下午还没搞完……"

我说：**30秒就够了。**

---

## 一行代码合并Excel

```python
import pandas as pd

# 读取当前文件夹所有Excel
files = ["销售1月.xlsx", "销售2月.xlsx", "销售3月.xlsx"]
df = pd.concat([pd.read_excel(f) for f in files])

# 保存
df.to_excel("销售汇总.xlsx", index=False)
```

**50个文件也一样，改成循环就行。**

---

## 但这只是冰山一角

Python能自动化的不只是合并Excel：

- 📊 数据筛选：按条件自动过滤
- 📈 图表生成：柱状图、折线图、饼图
- 🔄 数据清洗：去重、填充缺失值、格式统一
- 📧 自动发送：处理完直接邮件发出去

---

## 50讲完整教程

从零基础到自动化高手：

👉 [50讲Python自动化办公教程](/course/xiaobao-tutorial/50讲自动化办公/)

- 第1-10讲：Python入门 + 开发环境
- 第11-20讲：Excel自动化
- 第21-30讲：Word/PDF自动化
- 第31-40讲：邮件/文件/网络自动化
- 第41-50讲：综合实战

**每天学一讲，50天从小白变高手。**

---

程序员晚枫专注AI编程培训，小白看完他和图灵社区合作的教程[《30讲·AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)就能上手做AI项目。


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



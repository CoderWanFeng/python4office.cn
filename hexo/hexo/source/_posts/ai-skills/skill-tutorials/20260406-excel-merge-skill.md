---
title: Excel批量合并Skill使用指南：3分钟合并100个表格
date: 2026-04-06 10:38:00
tags: [Excel, Skill, 批量合并, AI办公, 教程]
categories: [AI Skills, Skill使用教程]
---

<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
</p>

<!-- more -->

大家好，我是正在实战各种 AI 项目的程序员晚枫。

每个月底，财务、运营、销售的同学都要做一件事：**把几十个甚至上百个 Excel 文件合并成一个**。

以前用 Python 写代码？太复杂。
现在，装上 **Excel 批量合并 Skill**，3 分钟搞定。

---

## 一、Skill 简介

### 功能概述
Excel 批量合并 Skill 可以：
- ✅ 合并多个 Excel 文件为一个
- ✅ 自动识别表头，智能对齐列
- ✅ 支持按指定列排序
- ✅ 支持去重、筛选
- ✅ 保留原始格式

### 适用场景
| 场景 | 示例 |
|---|---|
| 月度报表汇总 | 合并 30 个每日销售报表 |
| 数据清洗 | 合并多个部门的数据文件 |
| 历史数据归档 | 合并历年数据到一个文件 |
| 数据迁移 | 合并旧系统导出的多个文件 |

---

## 二、安装 Skill

### Coze 扣子安装
1. 打开 [Coze 官网](https://www.coze.cn)
2. 进入 "技能商店"
3. 搜索 "Excel 批量合并"
4. 点击 "安装"

### OpenClaw 安装
```bash
openclaw skills install excel-tools
```

### 飞书 CLI
飞书 CLI 暂不支持 Excel 处理，建议配合 Coze 或 OpenClaw 使用。

---

## 三、使用教程

### 基础用法：合并多个文件

**步骤 1：准备文件**
把要合并的 Excel 文件放在同一个文件夹，例如：
```
/data/
  ├── 2024-01-销售数据.xlsx
  ├── 2024-02-销售数据.xlsx
  ├── 2024-03-销售数据.xlsx
  └── ...
```

**步骤 2：告诉 AI 你的需求**
```
你：帮我把 /data/ 目录下的所有 Excel 文件合并成一个

AI：我来帮你合并 Excel 文件。
🔧 Using skill: excel-tools
   action: merge
   files: 12个文件
   
📤 Result:
   已合并为: /data/merged_20240406.xlsx
   总行数: 15,234
   总列数: 8
   耗时: 2.3秒
```

**步骤 3：下载合并后的文件**
从 AI 返回的路径下载合并后的文件。

---

### 进阶用法 1：按日期排序

```
你：帮我把这些 Excel 合并，按"日期"列从早到晚排序

AI：我来帮你合并并排序。
🔧 Using skill: excel-tools
   action: merge
   sort_by: 日期
   sort_order: ascending
   
📤 Result:
   已合并并排序！
   文件: /data/merged_sorted.xlsx
```

---

### 进阶用法 2：去重合并

```
你：合并这些 Excel，去掉重复的行（根据"订单号"去重）

AI：我来帮你合并并去重。
🔧 Using skill: excel-tools
   action: merge
   deduplicate: true
   deduplicate_key: 订单号
   
📤 Result:
   合并前总行数: 15,234
   去重后行数: 14,892
   重复行数: 342
   文件: /data/merged_deduplicated.xlsx
```

---

### 进阶用法 3：选择性合并

```
你：只合并"销售额"大于 1000 的行

AI：我来帮你筛选并合并。
🔧 Using skill: excel-tools
   action: merge
   filter: 销售额 > 1000
   
📤 Result:
   原始总行数: 15,234
   筛选后行数: 8,456
   文件: /data/merged_filtered.xlsx
```

---

### 进阶用法 4：按列合并（横向合并）

```
你：把这些 Excel 按"员工ID"横向合并（类似 SQL 的 JOIN）

AI：我来帮你横向合并。
🔧 Using skill: excel-tools
   action: join
   join_key: 员工ID
   join_type: left
   
📤 Result:
   已横向合并！
   文件: /data/merged_joined.xlsx
```

---

## 四、参数详解

### 支持的参数

| 参数 | 说明 | 示例 |
|---|---|---|
| `files` | 要合并的文件路径 | `/data/*.xlsx` |
| `output` | 输出文件名 | `merged.xlsx` |
| `sheet` | 指定工作表 | `Sheet1` |
| `sort_by` | 排序列 | `日期` |
| `sort_order` | 排序方式 | `ascending` / `descending` |
| `deduplicate` | 是否去重 | `true` / `false` |
| `deduplicate_key` | 去重依据列 | `订单号` |
| `filter` | 筛选条件 | `销售额 > 1000` |
| `join_key` | 合并键 | `员工ID` |
| `join_type` | 合并类型 | `left` / `right` / `inner` / `outer` |

---

## 五、常见问题

### Q1：文件格式不一致怎么办？
Skill 会自动识别表头，尝试对齐列。如果列名不同，可以：
```
你：合并这些 Excel，把"金额"和"销售额"当成同一列

AI：已识别同义列名，合并时会统一处理。
```

### Q2：合并后格式乱了？
可以指定保留格式：
```
你：合并这些 Excel，保留第一个文件的格式

AI：将保留 /data/2024-01.xlsx 的格式作为模板。
```

### Q3：文件太大合并失败？
可以分批处理：
```
你：先把前 50 个文件合并，再把后 50 个合并，最后把两个合并

AI：分三批处理，避免内存不足。
```

### Q4：合并后数据类型变了？
可以强制指定数据类型：
```
你：合并时把"订单号"列保留为文本格式，不要变成数字

AI：已设置"订单号"列的数据类型为文本。
```

---

## 六、实战案例

### 案例 1：财务月度报表合并

**背景**：财务小李每月要合并 30 个分公司的报表

**以前的做法**：
- 手动复制粘贴
- 耗时 2 小时
- 容易出错

**现在的做法**：
```
你：帮我把"分公司报表"文件夹里的 30 个 Excel 合并，
    按"分公司"和"日期"排序，
    去掉重复的汇总行

AI：处理完成！
   合并文件: 分公司报表_汇总_202404.xlsx
   总行数: 45,678
   耗时: 3.2秒
```

**效果**：从 2 小时缩短到 3 秒，准确率 100%

---

### 案例 2：销售数据清洗

**背景**：销售小张要合并全年的客户数据，去重后导入 CRM

**操作**：
```
你：合并"客户数据"文件夹，
    根据"手机号"去重，
    只保留"状态"为"有效"的客户

AI：处理完成！
   原始客户数: 12,456
   去重后: 10,234
   筛选后: 8,567
   文件: 客户数据_清洗后.xlsx
```

---

## 七、相关 Skill 推荐

| Skill | 功能 | 搭配使用场景 |
|---|---|---|
| excel-chart | 生成图表 | 合并后自动生成可视化报表 |
| excel-pivot | 数据透视 | 合并后进行多维度分析 |
| excel-format | 格式美化 | 合并后统一格式 |
| pdf-tools | PDF 转换 | 合并后导出为 PDF 分享 |

---

## 八、下一步学习

- [《PDF 合并拆分 Skill 完整教程》](/ai-skills/skill-tutorials/pdf-merge-skill/)
- [《发票 OCR 识别 Skill 实战》](/ai-skills/skill-tutorials/invoice-ocr-skill/)
- [《从零开发 Excel 处理 Skill》](/ai-skills/skill-dev/excel-skill-dev/)

---

## 💬 加入交流群

Excel 处理遇到问题？加群交流：

👉 **[加入AI编程学习交流群](https://www.python4office.cn/wechat-group/)**

![点击加入](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

---

*Excel 合并只是开始，更多自动化技能等你探索！*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



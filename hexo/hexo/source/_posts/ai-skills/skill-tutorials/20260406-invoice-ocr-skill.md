---
title: 发票OCR识别Skill实战：自动提取信息生成报销表
date: "2026-04-06 10:42:00"
tags: ["OCR", "发票识别", "Skill", "AI办公", "财务自动化", "教程"]
categories: ["AI Skills", "Skill使用教程"]
cover: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop"
---


<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
</p>

<!-- more -->

大家好，我是正在实战各种 AI 项目的程序员晚枫。

每个月报销时，最烦的是什么？**手动录入发票信息**——发票代码、发票号码、金额、日期……一张张敲进 Excel，既枯燥又容易出错。

今天教你用 **发票 OCR 识别 Skill**，拍照/上传发票，自动提取信息生成报销表。

---

## 一、Skill 简介

### 功能概述
发票 OCR 识别 Skill 可以：
- ✅ 识别增值税发票（电子/纸质）
- ✅ 识别火车票、机票行程单
- ✅ 识别出租车票、定额发票
- ✅ 自动提取关键字段（金额、日期、税号等）
- ✅ 导出为 Excel/JSON 格式
- ✅ 自动查重、验真

### 支持的发票类型

| 发票类型 | 支持状态 | 识别字段 |
|---|---|---|
| 增值税电子普通发票 | ✅ 完整支持 | 全字段 |
| 增值税纸质普通发票 | ✅ 完整支持 | 全字段 |
| 增值税专用发票 | ✅ 完整支持 | 全字段 |
| 火车票 | ✅ 支持 | 车次、金额、日期、乘客 |
| 机票行程单 | ✅ 支持 | 航班、金额、日期、乘客 |
| 出租车票 | ✅ 支持 | 金额、日期、起止地点 |
| 定额发票 | ✅ 支持 | 金额、发票代码、号码 |
| 电子客票 | ✅ 支持 | 全字段 |

---

## 二、安装 Skill

### Coze 扣子安装
1. 打开 [Coze 官网](https://www.coze.cn)
2. 进入 "技能商店"
3. 搜索 "发票识别" 或 "OCR"
4. 点击 "安装"

### OpenClaw 安装
```bash
openclaw skills install ocr-tools
openclaw skills install invoice-ocr
```

---

## 三、使用教程

### 基础用法 1：单张发票识别

**步骤 1：上传发票图片**
把发票照片或截图发给 AI。

**步骤 2：告诉 AI 识别需求**
```
你：识别这张发票的信息

AI：我来识别发票。
🔧 Using skill: invoice-ocr
   action: recognize
   type: auto_detect
   
📤 Result:
   发票类型: 增值税电子普通发票
   发票代码: 011001900111
   发票号码: 12345678
   开票日期: 2024-03-15
   购买方名称: XX科技有限公司
   购买方税号: 91110108XXXXXXXX
   销售方名称: YY商贸有限公司
   销售方税号: 91110105XXXXXXXX
   金额: ¥1,250.00
   税额: ¥162.50
   价税合计: ¥1,412.50
   商品名称: 办公用品
```

---

### 基础用法 2：批量识别

```
你：识别 /invoices/ 目录下的所有发票图片

AI：批量识别中...
🔧 Using skill: invoice-ocr
   action: batch_recognize
   files: 25张图片
   
📤 Result:
   识别完成！
   成功: 25张
   失败: 0张
   总金额: ¥35,680.50
   导出文件: /invoices/发票识别结果.xlsx
```

---

### 基础用法 3：生成报销表

```
你：识别这些发票并生成报销表，包含：日期、类型、金额、发票号码

AI：识别并生成报销表...
🔧 Using skill: invoice-ocr
   action: recognize_and_export
   format: excel
   fields: [日期, 类型, 金额, 发票号码]
   
📤 Result:
   报销表已生成！
   文件: /invoices/报销表_2024年3月.xlsx
   包含记录: 25条
   总金额: ¥35,680.50
```

---

## 四、进阶用法

### 进阶 1：自动分类

```
你：识别这些发票并按类型分类：交通费、住宿费、餐饮费、办公用品

AI：识别并分类中...
🔧 Using skill: invoice-ocr
   action: recognize_and_classify
   categories: [交通费, 住宿费, 餐饮费, 办公用品]
   
📤 Result:
   分类完成！
   交通费: 8张, ¥2,450.00
   住宿费: 5张, ¥8,600.00
   餐饮费: 6张, ¥3,240.50
   办公用品: 6张, ¥21,390.00
   导出文件: /invoices/分类报销表.xlsx
```

---

### 进阶 2：发票查重

```
你：识别这些发票并检查是否有重复的

AI：识别并查重中...
🔧 Using skill: invoice-ocr
   action: recognize_and_dedup
   
📤 Result:
   识别完成！
   总发票数: 30张
   重复发票: 2张
   - 发票 12345678 (重复 2 次)
   - 发票 87654321 (重复 2 次)
   有效发票: 28张
   导出文件: /invoices/去重后报销表.xlsx
```

---

### 进阶 3：发票验真

```
你：识别这些发票并在税务局网站验证真伪

AI：识别并验真中...
🔧 Using skill: invoice-ocr
   action: verify
   source: 国家税务总局
   
📤 Result:
   验证完成！
   总发票数: 25张
   验证通过: 24张
   验证失败: 1张
   - 发票 12345678: 查无此票
   导出文件: /invoices/验真报告.xlsx
```

---

### 进阶 4：按项目分组

```
你：识别这些发票并按项目分组，生成每个项目的费用汇总

AI：识别并分组中...
🔧 Using skill: invoice-ocr
   action: group_by_project
   
📤 Result:
   项目 A: 10张, ¥15,680.00
   项目 B: 8张, ¥12,450.50
   项目 C: 7张, ¥7,550.00
   导出文件: /invoices/项目费用汇总.xlsx
```

---

## 五、导出格式详解

### Excel 格式
```
导出列：
- 序号
- 发票类型
- 发票代码
- 发票号码
- 开票日期
- 购买方名称
- 购买方税号
- 销售方名称
- 销售方税号
- 金额（不含税）
- 税额
- 价税合计
- 商品名称
- 分类（交通/住宿/餐饮等）
- 项目
- 备注
```

### JSON 格式
```json
{
  "invoices": [
    {
      "type": "增值税电子普通发票",
      "code": "011001900111",
      "number": "12345678",
      "date": "2024-03-15",
      "buyer": {
        "name": "XX科技有限公司",
        "tax_id": "91110108XXXXXXXX"
      },
      "seller": {
        "name": "YY商贸有限公司",
        "tax_id": "91110105XXXXXXXX"
      },
      "amount": 1250.00,
      "tax": 162.50,
      "total": 1412.50,
      "items": ["办公用品"]
    }
  ]
}
```

---

## 六、批量处理技巧

### 技巧 1：拍照批量识别

```
你：我拍了 20 张发票照片，都在 /photos/ 目录，全部识别并生成报销表

AI：批量处理中...
🔧 Using skill: invoice-ocr
   action: batch_recognize
   input: /photos/*.jpg
   output_format: excel
   
📤 Result:
   处理完成！
   识别成功: 20张
   识别失败: 0张
   生成报销表: /photos/报销表.xlsx
```

---

### 技巧 2：PDF 发票识别

```
你：这个 PDF 里有 10 张电子发票，提取识别所有发票信息

AI：PDF 发票提取中...
🔧 Using skill: invoice-ocr
   action: extract_from_pdf
   
📤 Result:
   提取完成！
   发现发票: 10张
   全部识别成功
   导出文件: /invoices/PDF发票识别结果.xlsx
```

---

### 技巧 3：微信/钉钉发票识别

```
你：识别我微信卡包里的所有发票

AI：需要授权访问微信卡包...
   授权后提取发票...
🔧 Using skill: invoice-ocr
   action: import_from_wechat
   
📤 Result:
   提取完成！
   共 15张发票
   已全部识别并生成报销表
```

---

## 七、实战案例

### 案例 1：月度报销自动化

**背景**：财务小李每月要处理 50+ 张发票

**以前的做法**：
- 一张张查看发票
- 手动录入 Excel
- 检查是否有重复
- 计算各类费用总额
- 耗时 2 天

**现在的做法**：
```
你：识别 /invoices/3月/ 目录下的所有发票，
    按费用类型分类，
    检查重复，
    生成报销表和汇总统计

AI：处理完成！
   识别发票: 52张
   发现重复: 2张（已标出）
   分类统计:
   - 交通费: ¥3,250.00
   - 住宿费: ¥12,800.00
   - 餐饮费: ¥4,560.50
   - 办公用品: ¥15,070.00
   总金额: ¥35,680.50
   生成文件:
   - 报销表.xlsx
   - 汇总统计.xlsx
   - 重复发票报告.xlsx
```

**效果**：从 2 天缩短到 5 分钟

---

### 案例 2：项目费用核算

**背景**：项目经理需要核算每个项目的差旅费用

**操作**：
```
你：识别这些发票，
    按项目名称分组，
    生成每个项目的费用明细和汇总，
    导出为项目费用报告

AI：处理完成！
   项目 A 费用明细: 15张, ¥28,450.00
   项目 B 费用明细: 20张, ¥35,680.50
   项目 C 费用明细: 10张, ¥15,230.00
   已生成项目费用报告.xlsx
```

---

## 八、常见问题

### Q1：识别准确率如何？
- 清晰的发票照片：准确率 > 98%
- 模糊/倾斜的照片：准确率 85-95%
- 建议：拍照时保持光线充足、发票平整

### Q2：手写发票能识别吗？
- 定额发票的手写金额：可以识别
- 完全手写的发票：识别率较低

### Q3：识别失败怎么办？
```
你：这张发票识别失败了，手动输入：
    发票代码: 011001900111
    发票号码: 12345678
    金额: 1250.00
    ...

AI：已手动录入，添加到报销表中。
```

### Q4：如何导出为财务系统格式？
```
你：导出为用友财务系统导入格式

AI：已转换为用友格式：
   - 列名映射完成
   - 编码规则转换完成
   - 文件: 用友导入模板.xlsx
```

---

## 九、相关 Skill 推荐

| Skill | 功能 | 搭配使用场景 |
|---|---|---|
| excel-tools | Excel 处理 | 识别结果进一步处理 |
| pdf-utils | PDF 处理 | 电子发票归档 |
| file-manager | 文件管理 | 发票图片整理 |
| calendar-tools | 日历管理 | 按日期筛选发票 |

---

## 十、下一步学习

- [《Excel 批量合并 Skill 使用指南》](/ai-skills/skill-tutorials/excel-merge-skill/)
- [《PDF 合并拆分 Skill 完整教程》](/ai-skills/skill-tutorials/pdf-merge-skill/)
- [《从零开发 OCR 识别 Skill》](/ai-skills/skill-dev/ocr-skill-dev/)

---

## 💬 加入交流群

发票识别遇到问题？加群交流：

👉 **[加入AI编程学习交流群](https://www.python4office.cn/wechat-group/)**

![点击加入](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

---

*发票 OCR 识别是财务自动化的第一步，从此告别手动录入！*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



---
title: PDF合并拆分Skill完整教程：一键处理上百个PDF文件
date: 2026-04-06 10:40:00
tags: [PDF, Skill, 合并, 拆分, AI办公, 教程]
categories: [AI Skills, Skill使用教程]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
</p>

<!-- more -->

大家好，我是正在实战各种 AI 项目的程序员晚枫。

合同归档、报告整理、发票汇总……这些场景都离不开 **PDF 处理**。

今天教你用 **PDF 合并拆分 Skill**，一键处理上百个 PDF 文件。

---

## 一、Skill 简介

### 功能概述
PDF 处理 Skill 可以：
- ✅ 合并多个 PDF 为一个
- ✅ 按页码/范围拆分 PDF
- ✅ 提取指定页面
- ✅ 旋转页面
- ✅ 压缩 PDF 大小
- ✅ 添加/删除水印
- ✅ PDF 转图片

### 适用场景
| 场景 | 示例 |
|---|---|
| 合同归档 | 把 50 份合同合并为一个文件 |
| 报告整理 | 按章节拆分大型报告 |
| 发票汇总 | 合并月度发票提交财务 |
| 资料分享 | 提取报告中的关键页面 |
| 文件优化 | 压缩 PDF 便于邮件发送 |

---

## 二、安装 Skill

### Coze 扣子安装
1. 打开 [Coze 官网](https://www.coze.cn)
2. 进入 "技能商店"
3. 搜索 "PDF 工具" 或 "PDF 合并"
4. 点击 "安装"

### OpenClaw 安装
```bash
openclaw skills install pdf-utils
```

---

## 三、使用教程

### 基础用法 1：合并多个 PDF

**步骤 1：准备文件**
```
/contracts/
  ├── 合同_001.pdf
  ├── 合同_002.pdf
  ├── 合同_003.pdf
  └── ...
```

**步骤 2：告诉 AI 你的需求**
```
你：帮我把 /contracts/ 目录下的所有 PDF 合并成一个文件

AI：我来帮你合并 PDF。
🔧 Using skill: pdf-utils
   action: merge
   files: 50个PDF
   
📤 Result:
   已合并为: /contracts/合同汇总_2024.pdf
   总页数: 1,250页
   文件大小: 45.6MB
   耗时: 5.8秒
```

---

### 基础用法 2：按页码拆分

```
你：把这个 PDF 每 10 页拆分成一个文件

AI：我来帮你拆分。
🔧 Using skill: pdf-utils
   action: split
   split_by: pages
   pages_per_file: 10
   
📤 Result:
   已拆分为 12 个文件:
   - 合同_第1-10页.pdf
   - 合同_第11-20页.pdf
   - ...
   保存位置: /contracts/split/
```

---

### 基础用法 3：按范围拆分

```
你：把 PDF 的前 5 页、中间 10-20 页、最后 3 页分别提取出来

AI：我来帮你提取。
🔧 Using skill: pdf-utils
   action: extract
   ranges: [1-5, 10-20, -3]
   
📤 Result:
   已提取 3 个文件:
   - 封面部分.pdf (5页)
   - 正文部分.pdf (11页)
   - 附录部分.pdf (3页)
```

---

## 四、进阶用法

### 进阶 1：添加水印

```
你：给这个 PDF 添加"机密文件"水印，红色、半透明、居中

AI：我来添加水印。
🔧 Using skill: pdf-utils
   action: watermark
   text: 机密文件
   color: #FF0000
   opacity: 0.3
   position: center
   
📤 Result:
   已添加水印！
   文件: /contracts/合同_加水印.pdf
```

---

### 进阶 2：删除水印

```
你：帮我去掉这个 PDF 的水印

AI：我来去除水印。
🔧 Using skill: pdf-utils
   action: remove_watermark
   method: auto_detect
   
📤 Result:
   已去除水印！
   文件: /contracts/合同_去水印.pdf
```

---

### 进阶 3：压缩 PDF

```
你：把这个 100MB 的 PDF 压缩到 10MB 以下，保持清晰度

AI：我来压缩。
🔧 Using skill: pdf-utils
   action: compress
   target_size: 10MB
   quality: high
   
📤 Result:
   压缩完成！
   原始大小: 100.5MB
   压缩后: 8.3MB
   压缩率: 91.7%
   文件: /contracts/报告_压缩.pdf
```

---

### 进阶 4：PDF 转图片

```
你：把这个 PDF 的每一页转成 PNG 图片，分辨率 300dpi

AI：我来转换。
🔧 Using skill: pdf-utils
   action: to_images
   format: png
   dpi: 300
   
📤 Result:
   已转换为 25 张图片:
   - page_001.png
   - page_002.png
   - ...
   保存位置: /contracts/images/
```

---

### 进阶 5：旋转页面

```
你：把这个 PDF 的第 3、5、7 页顺时针旋转 90 度

AI：我来旋转。
🔧 Using skill: pdf-utils
   action: rotate
   pages: [3, 5, 7]
   angle: 90
   
📤 Result:
   已旋转指定页面！
   文件: /contracts/文档_旋转.pdf
```

---

## 五、批量处理技巧

### 技巧 1：批量添加水印

```
你：给 /contracts/ 目录下的所有 PDF 都添加"机密"水印

AI：批量处理中...
🔧 Using skill: pdf-utils
   action: batch_watermark
   files: /contracts/*.pdf
   text: 机密
   
📤 Result:
   已处理 50 个文件！
   输出目录: /contracts/watermarked/
```

---

### 技巧 2：批量合并并按月份分组

```
你：把发票按月份合并，每个月一个 PDF

AI：我来分组合并。
🔧 Using skill: pdf-utils
   action: merge_by_group
   group_by: filename_month
   
📤 Result:
   已生成 12 个文件:
   - 发票_2024-01.pdf
   - 发票_2024-02.pdf
   - ...
   保存位置: /invoices/by_month/
```

---

### 技巧 3：提取所有 PDF 的第一页做封面

```
你：提取每个 PDF 的第一页，合并成一个"目录"文件

AI：我来提取并合并。
🔧 Using skill: pdf-utils
   action: extract_first_page
   merge: true
   
📤 Result:
   已生成目录文件！
   包含 50 个封面
   文件: /contracts/目录_封面汇总.pdf
```

---

## 六、参数详解

### 合并参数

| 参数 | 说明 | 示例 |
|---|---|---|
| `files` | 要合并的文件 | `/docs/*.pdf` |
| `output` | 输出文件名 | `merged.pdf` |
| `bookmark` | 添加书签 | `true` |
| `outline` | 保留目录 | `true` |

### 拆分参数

| 参数 | 说明 | 示例 |
|---|---|---|
| `split_by` | 拆分方式 | `pages` / `size` / `outline` |
| `pages_per_file` | 每文件页数 | `10` |
| `ranges` | 页码范围 | `[1-5, 10-20]` |

### 水印参数

| 参数 | 说明 | 示例 |
|---|---|---|
| `text` | 水印文字 | `机密文件` |
| `color` | 颜色 | `#FF0000` |
| `opacity` | 透明度 | `0.3` |
| `position` | 位置 | `center` / `diagonal` |
| `font_size` | 字体大小 | `48` |

### 压缩参数

| 参数 | 说明 | 示例 |
|---|---|---|
| `target_size` | 目标大小 | `10MB` |
| `quality` | 质量 | `high` / `medium` / `low` |
| `images_only` | 仅压缩图片 | `true` |

---

## 七、实战案例

### 案例 1：合同归档系统

**背景**：法务部每月要归档 100+ 份合同

**完整流程**：
```
步骤 1：合并所有合同
你：合并本月所有合同为一个 PDF

步骤 2：添加页码
你：给合并后的 PDF 添加页码，格式"第 X 页 / 共 Y 页"

步骤 3：生成目录
你：提取每个合同的第一页作为目录

步骤 4：添加水印
你：添加"内部资料"水印

步骤 5：压缩
你：压缩到 50MB 以下便于存档
```

**结果**：原本需要 1 天的工作，10 分钟完成

---

### 案例 2：发票管理系统

**背景**：财务需要按月整理发票提交审计

**操作**：
```
你：把发票按月份分组，每个月合并一个 PDF，
    添加"发票汇总-2024年X月"封页，
    生成一个总目录

AI：处理完成！
   生成 12 个月度汇总文件
   生成 1 个总目录文件
   所有文件已添加水印
```

---

## 八、常见问题

### Q1：合并后链接失效了？
可以保留链接：
```
你：合并 PDF 时保留所有超链接

AI：将保留原文档中的所有链接。
```

### Q2：合并后文件太大？
```
你：合并后自动压缩到 20MB 以下

AI：合并 + 压缩处理中...
```

### Q3：扫描版 PDF 无法处理？
扫描版 PDF 需要先 OCR：
```
你：先对这些扫描版 PDF 进行 OCR，然后再合并

AI：OCR 处理中...
   识别完成后进行合并
```

### Q4：密码保护的 PDF 怎么办？
```
你：合并这些 PDF，密码是 123456

AI：使用提供的密码解密后合并
```

---

## 九、相关 Skill 推荐

| Skill | 功能 | 搭配使用场景 |
|---|---|---|
| ocr-tools | OCR 识别 | 扫描版 PDF 先识别再处理 |
| image-tools | 图片处理 | PDF 转图片后编辑 |
| excel-tools | Excel 处理 | PDF 表格提取到 Excel |
| file-manager | 文件管理 | 批量重命名、移动文件 |

---

## 十、下一步学习

- [《发票 OCR 识别 Skill 实战》](/ai-skills/skill-tutorials/invoice-ocr-skill/)
- [《图片去水印 Skill 使用指南》](/ai-skills/skill-tutorials/image-watermark-skill/)
- [《从零开发 PDF 处理 Skill》](/ai-skills/skill-dev/pdf-skill-dev/)

---

## 💬 加入交流群

PDF 处理遇到问题？加群交流：

👉 **[加入AI编程学习交流群](https://www.python4office.cn/wechat-group/)**

![点击加入](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

---

*PDF 处理是办公自动化的基础技能，掌握它，效率提升 10 倍！*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



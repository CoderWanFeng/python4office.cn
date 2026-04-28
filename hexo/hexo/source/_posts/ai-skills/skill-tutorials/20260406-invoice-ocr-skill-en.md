---
title: "Invoice OCR Recognition Skill Practice: Auto-Extract Information to Generate Reimbursement Form"
date: 2026-04-06 10:42:00
tags: [OCR, Invoice Recognition, Skill, AI Office, Finance Automation, Tutorial]
categories: [AI Skills, Skill Tutorial]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---

<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
</p>

<!-- more -->

Hello everyone, I'm Programmer Wanfeng, practicing various AI projects.

What's the most annoying thing every month when reimbursing? **Manually entering invoice information** - invoice code, invoice number, amount, date... typing into Excel one by one, both boring and error-prone.

Today I teach you to use **Invoice OCR Recognition Skill**, take photo/upload invoice, auto-extract information to generate reimbursement form.

---

## 1. Skill Introduction

### Function Overview
Invoice OCR Recognition Skill can:
- ✅ Recognize VAT invoices (electronic/paper)
- ✅ Recognize train tickets, flight itineraries
- ✅ Recognize taxi receipts,定额 invoices
- ✅ Auto-extract key fields (amount, date, tax number, etc.)
- ✅ Export to Excel/JSON format
- ✅ Auto-deduplicate, verify

### Supported Invoice Types

| Invoice Type | Support Status | Recognized Fields |
|---|---|---|
| VAT Electronic Ordinary Invoice | ✅ Fully supported | All fields |
| VAT Paper Ordinary Invoice | ✅ Fully supported | All fields |
| VAT Special Invoice | ✅ Fully supported | All fields |
| Train ticket | ✅ Supported | Train number, amount, date, passenger |
| Flight itinerary | ✅ Supported | Flight, amount, date, passenger |
| Taxi receipt | ✅ Supported | Amount, date, start/end locations |
| 定额 invoice | ✅ Supported | Amount, invoice code, number |
| E-ticket | ✅ Supported | All fields |

---

## 2. Install Skill

### Coze Installation
1. Open [Coze Official Website](https://www.coze.cn)
2. Enter "Skill Store"
3. Search "Invoice Recognition" or "OCR"
4. Click "Install"

### OpenClaw Installation
```bash
openclaw skills install ocr-tools
openclaw skills install invoice-ocr
```

---

## 3. Usage Tutorial

### Basic Usage 1: Single Invoice Recognition

**Step 1: Upload invoice image**
Send invoice photo or screenshot to AI.

**Step 2: Tell AI recognition needs**
```
You: Recognize this invoice's information

AI: I'll recognize the invoice.
🔧 Using skill: invoice-ocr
   action: recognize
   type: auto_detect

📤 Result:


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



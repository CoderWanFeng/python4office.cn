---
title: "Lecture 23: Project Practice - Financial Intelligent Assistant Development Implementation"
date: 2026-04-06 40:00:00
tags: ["AI Skill", "Project Practice", "Finance"]
categories: ["AI Skills Course"]
---

<!-- more -->
# Lecture 23: Project Practice - Financial Intelligent Assistant Development Implementation

> Implement core functions of the Financial Intelligent Assistant, including invoice recognition, report generation, and data processing.

## 1. Project Structure

```
finance_assistant/
├── __init__.py
├── main.py              # Entry point
├── config.py            # Configuration
├── models/              # Data models
│   ├── __init__.py
│   ├── invoice.py       # Invoice model
│   └── report.py        # Report model
├── services/            # Business services
│   ├── __init__.py
│   ├── ocr_service.py   # OCR service
│   ├── invoice_service.py
│   └── report_service.py
├── utils/               # Utility functions
│   ├── __init__.py
│   ├── db.py           # Database
│   └── excel.py        # Excel processing
└── templates/           # Report templates
    ├── balance_sheet.xlsx
    └── income_statement.xlsx
```

## 2. Core Code Implementation

### 2.1 Invoice Recognition Service

```python
# services/invoice_service.py
from typing import Dict, List
import re
from datetime import datetime

class InvoiceService:
    """Invoice service"""

    def __init__(self, ocr_service, db):
        self.ocr = ocr_service
        self.db = db

    def recognize_invoice(self, image_path: str) -> Dict:
        """Recognize invoice"""
        # 1. OCR recognition
        raw_text = self.ocr.recognize(image_path)

        # 2. Extract structured information
        invoice_info = self._extract_invoice_info(raw_text)

        # 3. Validate invoice
        validation = self._validate_invoice(invoice_info)
        invoice_info['validation'] = validation

        # 4. Save to database
        self.db.save_invoice(invoice_info)

        return invoice_info

    def _extract_invoice_info(self, text: str) -> Dict:
        """Extract invoice information"""
        info = {
            'invoice_code': self._extract_pattern(text, r'Invoice Code[:：]\s*(\d{12})'),
            'invoice_number': self._extract_pattern(text, r'Invoice Number[:：]\s*(\d{8,20})'),
            'date': self._extract_date(text),
            'buyer_name': self._extract_buyer(text),
            'buyer_tax_id': self._extract_pattern(text, r'Buyer.*Tax ID[:：]\s*([A-Z0-9]+)'),
            'seller_name': self._extract_seller(text)


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



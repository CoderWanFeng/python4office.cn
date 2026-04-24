---
title: "PDF Merge Split Skill Complete Tutorial: One-Click Process Hundreds of PDF Files"
date: 2026-04-06 10:40:00
tags: [PDF, Skill, Merge, Split, AI Office, Tutorial]
categories: [AI Skills, Skill Tutorial]
---

<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
</p>

<!-- more -->

Hello everyone, I'm Programmer Wanfeng, practicing various AI projects.

Contract archiving, report organization, invoice summary... these scenarios are inseparable from **PDF processing**.

Today I teach you to use **PDF Merge Split Skill**, one-click process hundreds of PDF files.

---

## 1. Skill Introduction

### Function Overview
PDF Processing Skill can:
- ✅ Merge multiple PDFs into one
- ✅ Split PDF by page number/range
- ✅ Extract specified pages
- ✅ Rotate pages
- ✅ Compress PDF size
- ✅ Add/remove watermarks
- ✅ PDF to images

### Applicable Scenarios
| Scenario | Example |
|---|---|
| Contract archiving | Merge 50 contracts into one file |
| Report organization | Split large reports by chapter |
| Invoice summary | Merge monthly invoices to submit to finance |
| Material sharing | Extract key pages from reports |
| File optimization | Compress PDF for email sending |

---

## 2. Install Skill

### Coze Installation
1. Open [Coze Official Website](https://www.coze.cn)
2. Enter "Skill Store"
3. Search "PDF Tools" or "PDF Merge"
4. Click "Install"

### OpenClaw Installation
```bash
openclaw skills install pdf-utils
```

---

## 3. Usage Tutorial

### Basic Usage 1: Merge Multiple PDFs

**Step 1: Prepare files**
```
/contracts/
  ├── contract_001.pdf
  ├── contract_002.pdf
  ├── contract_003.pdf
  └── ...
```

**Step 2: Tell AI your needs**
```
You: Help me merge all PDFs in /contracts/ directory into one file

AI: I'll help you merge PDFs.
🔧 Using skill: pdf-utils
   action: merge
   files: 50 PDFs

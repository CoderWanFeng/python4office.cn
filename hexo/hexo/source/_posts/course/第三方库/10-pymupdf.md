---
title: 揭秘PyMuPDF：掌握PDF编辑与转换的终极指南
date: 2024-12-09 10:16:17
tags: [ 第三方库,自动化办公,pdf ]
---

大家好，这里是程序员晚枫，今天给大家分享一个PDF自动化办公的第三方库：PyMuPDF。

> 官网地址：[https://pymupdf.readthedocs.io/en/latest/index.html](https://pymupdf.readthedocs.io/en/latest/index.html)


PyMuPDF（也称为`pymupdf`）是一个强大的Python库，用于处理PDF和其他图形文件格式。以下是一些基本的步骤和示例，帮助你开始使用PyMuPDF。



## 安装PyMuPDF

首先，你需要安装PyMuPDF。你可以通过pip安装：

```bash
pip install pymupdf
```

> 在1.24.3版本发布之前，这个库的顶级Python导入名称是“fitz”。在1.24.3版本中，这个名称已被弃用，取而代之的是“pymupdf”。

## 基本操作

1. **打开PDF文件**

```python
import pymupdf  # PyMuPDF

# 打开一个PDF文件
doc = pymupdf.open("程序员晚枫.pdf")
```

2. **读取和显示页面内容**

```python
# 获取文档页数
page_count = doc.page_count

# 遍历每一页
for page_num in range(page_count):
    page = doc.load_page(page_num)  # 加载页面
    text = page.get_text()  # 获取页面文本
    print(text)
```

3. **插入文本**

```python
# 打开文档
doc = pymupdf.open("程序员晚枫.pdf")

# 获取第一页
page = doc[0]

# 插入文本
page.insert_text((50, 50), "Hello, World!", fontname="helv", fontsize=12)

# 保存文档
doc.save("程序员晚枫_modified.pdf")
```

4. **插入图像**

```python
# 打开文档
doc = pymupdf.open("程序员晚枫.pdf")

# 获取第一页
page = doc[0]

# 插入图像
page.insert_image((50, 50, 200, 200), filename="image.png")

# 保存文档
doc.save("程序员晚枫_with_image.pdf")
```

5. **合并PDF文件**

```python
import pymupdf

# 打开两个PDF文件
doc1 = pymupdf.open("document1.pdf")
doc2 = pymupdf.open("document2.pdf")

# 将第二个文档插入到第一个文档的末尾
doc1.insert_pdf(doc2)

# 保存合并后的文档
doc1.save("merged_document.pdf")
```

6. **提取页面**

```python
# 打开文档
doc = pymupdf.open("程序员晚枫.pdf")

# 提取第一页
page = doc[0]

# 保存提取的页面为新的PDF文件
page.save("extracted_page.pdf")
```

7. **加密PDF文件**

```python
import pymupdf

# 创建一个新的PDF文档
doc = pymupdf.open()
page = doc.new_page()

# 插入一些文本
page.insert_text((50, 50), "Secret Information")

# 设置密码和权限
doc.needs_pass = "user_password"  # 用户密码
doc权限 = pymupdf.PDF_PERM_PRINT | pymupdf.PDF_PERM_COPY  # 允许打印和复制
doc.encrypt_user_password("owner_password", doc权限)  # 设置所有者密码和权限

# 保存加密的PDF文件
doc.save("encrypted.pdf")
```

这些只是PyMuPDF库的一些基本用法。PyMuPDF的功能非常丰富，包括但不限于修改PDF内容、添加注释、提取图像和文本、转换PDF页面等。你可以根据需要探索更多的功能和方法。


## 相关课程

- [给小白的《50讲 · Python自动化办公》](https://mp.weixin.qq.com/s/lOx4cAp9AllsCrhsUqVn8g)
- [给小白的《10讲 · Python微信机器人》](https://mp.weixin.qq.com/s/-oR2dUakXEY3vmPbzVtrnA)
- [给小白的《5讲 · Python实现发票批量识别》](https://mp.weixin.qq.com/s/pGim7ifpgLwYUJ9a-FHvaw)


---



![](https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/ads/gzh/sub-py.jpg)

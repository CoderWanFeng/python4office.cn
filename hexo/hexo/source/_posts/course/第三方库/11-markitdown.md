---
title: 微软开源新工具 MarkItDown，Office 文件轻松转换为 Markdown 格式
date: 2024-12-18 20:56:36
tags: 第三方库
---

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/h0MExYJag6hLnQg26yx98w)，上周刚给大家发布了一个功能：[仅需1行代码，Excel秒变Markdown！](https://mp.weixin.qq.com/s/ISE2SLf-F6k_38SEQqTGPg)

打算本周再增加更多文件转Markdown的功能，在检索实现方案的过程中，我突然发现：就在前几天，微软自己开源了一个工具：MarkItDown。

**我竟然和微软想到一块去了？？**


> 微软开源的MarkItDown工具可以帮助你将多种文件格式转换为Markdown格式。

以下是如何使用MarkItDown的基本步骤：

## 1. **安装MarkItDown**：
   你可以通过pip命令来安装MarkItDown：
   ```
   pip install markitdown
   ```
   或者从源码安装：
   ```
   pip install -e .
   ```
   

## 2. **环境准备**：
   MarkItDown需要Python 3.10或更高版本。你可以使用virtualenv或pipenv来创建和管理虚拟环境：
   ```
   # 使用virtualenv
   virtualenv -p python3.10 env
   source venv/bin/activate
   pip install markitdown

   # 使用pipenv
   pipenv --python 3.10
   pipenv shell
   pipenv install markitdown
   ```
   

## 3. **基本使用**：
   使用MarkItDown转换文件非常简单，首先你需要导入MarkItDown模块并创建一个实例，然后调用convert方法进行转换：
   ```python
   from markitdown import MarkItDown
   markitdown = MarkItDown()
   result = markitdown.convert("python-office.xlsx")
   print(result.text_content)
   ```
   你可以转换多种文件类型，包括PDF、PowerPoint、Word、Excel等。

## 4. **处理网络资源**：
   你可以直接从URL转换文件，或者处理HTTP响应：
   ```python
   # 直接从URL转换
   url_result = markitdown.convert("https://python-office.com/document.pdf")
   print(url_result.text_content)
   
   # 处理HTTP响应
   import requests
   response = requests.get("https://python-office.com/document")
   response_result = markitdown.convert(response)
   print(response_result.text_content)
   ```
   

## 5. **处理流式数据**：
   如果你需要处理流式数据，可以使用convert_stream方法：
   ```python
   with open("python-office.pdf", "rb") as f:
       result = markitdown.convert_stream(f)
       print(result.text_content)
   ```
   

## 6. **命令行使用**：
   MarkItDown还提供了命令行工具，支持多种输入方式：
   ```
   # 直接转换文件
   markitdown python-office.pdf > output.md
   # 通过管道输入
   cat python-office.pdf | markitdown > output.md
   # 通过重定向输入
   markitdown < python-office.pdf > output.md
   ```
   

## 7. **高级特性**：
   你可以自定义会话和模型，例如集成OpenAI等AI模型来处理图片描述：
   ```python
   from markitdown import MarkItDown
   from openai import OpenAI
   client = OpenAI()
   md = MarkItDown(mlm_client=client, mlm_model="gpt-4")
   result = md.convert("python-office.jpg")
   print(result.text_content)
   ```
   

以上是MarkItDown的基本使用方法，你可以根据需要选择合适的方式来转换文件。更多详细信息和高级用法，可以访问MarkItDown的GitHub仓库：[https://github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)。


## 相关课程

- [给小白的《50讲 · Python自动化办公》](https://www.python-office.com/course/50-python-office.html)
- [给小白的《10讲 · Python微信机器人》](https://www.python-office.com/course-002/10-PyOfficeRobot/10-PyOfficeRobot.html)
- [给小白的《5讲 · Python实现发票批量识别》](https://www.python-office.com/course-002/5-poocr/5-poocr.html)


---




![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')



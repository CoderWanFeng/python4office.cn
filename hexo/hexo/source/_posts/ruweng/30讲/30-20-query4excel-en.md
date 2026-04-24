---
title: "Python Batch Query Excel Content: Find All Cells Containing Keywords in 1 Second, Supports Multiple Files"
date: 2025-08-22 00:00:00
tags: [星河计划]
---


<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">Project Website: https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="https://www.python4office.cn/wechat-group/">Open Source Project Discussion Group</a> 👈
</p>



<p align="center" name="atomgit">
  <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>
</p>
<p align="center" name="atomgit">
	<a href="https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw">
  <img src="https://img.shields.io/badge/Learn-AI%20Programming-red" alt="AI Programming">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/Join-AI%20Discussion%20Group-brightgreen" alt="AI Discussion Group">
</a>

</p>

<!-- more -->


Main Content

-------------------------------------------------------------------------------

>Python Official released python-office, a library for Python automation: [Breaking! Official Released Third-Party Library: python-office, Built for Python Automation](https://mp.weixin.qq.com/s/v2n0DTVTZUaw7QOnA0Zlow)
>No need to write code yourself, just call the ready-made methods.

Hello everyone, this is CoderWanFeng, focusing on sharing: Python Automation.
**This series of tutorials introduces the features of python-office automation, one by one.**
## 1. Feature Introduction
Today we introduce one of the features of this library:
> **Query All Excel Files for Specified Content Occurrences**: Only one line of code to query and count occurrences of a specified keyword in all Excel files in a directory, and save as an Excel file.
## 2. Usage Instructions
#### Download poexcel
Only one command is needed to automatically download and install poexcel
```
pip install poexcel
```
#### Call the Function
Copy the code below, modify the file location, right-click and select Run
```python
import poexcel

poexcel.query4excel(query_content='小红书',
                    query_path=r'./test_files/30-20-query4excel',
                    output_path=r'./test_files/out',
                    output_name='query4excel.xlsx')
# Parameter explanation:
# query_content: Keyword to search for
# query_path: Path where Excel files to search are located
# output_path: Output path for result file
# output_name: Name of the result file
```

## 3. Submit Requirements
Is it simple to implement complex functions with just 1 line of code? The python-office automation library is still under continuous development.
Everyone is welcome to join the discussion group to share your feature requests~

Also welcome developers with technical skills to enrich this project together:
> - Your star & fork & pr are welcome! ⭐
> - Open Source Address:
> - https://gitee.com/CoderWanFeng/python-office
> - https://github.com/CoderWanFeng/python-office





CoderWanFeng focuses on AI programming training. Beginners can start making AI projects after watching his tutorial [《30 Lectures · AI Programming Training Camp》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw) collaborated with Turing Community.

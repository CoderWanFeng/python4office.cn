---
title: "Python Chinese to Pinyin: 1 Line of Code, Supports Tone Marks, Polyphone Auto-Recognition, Build a Pinyin Tool"
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
> **Generate Pinyin for Chinese Characters**: Only one line of code to output pinyin for Chinese characters, with options for tone marks and tone format.
## 2. Usage Instructions
#### Download pohan
Only one command is needed to automatically download and install pohan
```
pip install pohan
```
#### Call the Function
Copy the code below, modify the file location, right-click and select Run
```python
import pohan
from pohan.pinyin.pinyin import Style

# Without tone marks
pinyin_list = pohan.pinyin.han2pinyin(hans="程序员晚枫", style=Style.NORMAL)
print(f'Result without tone marks: {pinyin_list}')

# With tone marks
pinyin_list = pohan.pinyin.han2pinyin(hans="程序员晚枫", style=Style.TONE)
print(f'Result with tone marks: {pinyin_list}')

# With numeric tone marks
pinyin_list = pohan.pinyin.han2pinyin(hans="程序员晚枫", style=Style.TONE3)
print(f'Result with numeric tone marks: {pinyin_list}')

# Parameter explanation:
# hans: Text to convert to pinyin
# style: Available tone formats: Style.NORMAL: without tone marks; Style.TONE: with tone marks; Style.TONE3: with numeric tone marks
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

---
title: Python自动化办公，最近更新了哪些功能？
date: 2023-12-23 23:16:17
tags: 日志
---



<!-- more -->
<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="https://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>



<p align="center" name="atomgit">
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>	
	    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>




大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA)，今天给大家分享一下Python自动化办公，最近1个月更新的功能。

> 以下代码，全部都可以免费使用哦~！




## 彩色的输出

有没有觉得python自带的无色输出看腻了？增加了彩色输出的功能，可以实现无痛替换。

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pocode/%E5%BD%A9%E8%89%B2%E6%89%93%E5%8D%B0/Snipaste_2023-12-24_03-23-37.jpg)

上面效果的实现代码如下，👇

```python

## 以前
print('我是传统打印')
print('我是传统打印')
print('我是传统打印')

print('=' * 10)

## 现在

from pocode.api.color import random_color_print

random_color_print('我是彩色打印')
random_color_print('我是彩色打印')
random_color_print('我是彩色打印')

```

## 自动收发邮件

这个12月发布了一个开源项目：``poemail``，增加了自动收发邮件的功能。

```python

import os
from datetime import datetime

import poemail

key = os.getenv('EMAIL_KEY')
msg_from = os.getenv('EMAIL_FROM')
msg_to = os.getenv('EMAIL_TO')
msg_cc = 'ai163361ia@163.com'
attach_files = [r'./test_files/4-send_mail_content_file/程序员晚枫.doc',
                r'./test_files/4-send_mail_content_file/0816.jpg']

poemail.send.send_email(key=key,
                        msg_from=msg_from,
                        msg_to=msg_to,
                        msg_cc=msg_cc,
                        msg_subject='带附件的邮件' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                        content='测试邮件发送' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
                        attach_files=attach_files)
```
## Word里提取图片

下面这1行代码，可以实现从Wotd里提取出所有的图片，包括表格中的。

```python
# pip install python-office
import office

office.word.docx4imgs(word_path=r'./test_files/50-24-docx4imgs/程序员晚枫.docx',
                      img_path=r'./test_files/out')
```

## OCR识别

ocr这个库发布很久了，这次增加了更多识别后直接保存为Excel的操作。

```python


# pip install poocr
import poocr

poocr.ocr2excel.VatInvoiceOCR2Excel(input_path=r'test_files/50-15-VatInvoiceOCR2Excel/',
                                    output_path=r'test_files/50-15-VatInvoiceOCR2Excel',
                                    output_excel='程序员晚枫的发票.xlsx',
                                    id='id',
                                    key='key')

# 全部100多个识别功能，举例如下。
# # 识别增值税发票
# ressult = poocr.ocr.VatInvoiceOCR()
# # 识别银行卡
# ressult = poocr.ocr.BankCardOCR()
# # 识别身份证
# ressult = poocr.ocr.IDCardOCR()
```


## 金融做T

同时开发了单次做T和批量做T的代码，我用单次做T比较多，至于赚了还是赔了，别问了，答应我。


```python

from pofinance import MakeT
import pofinance as pf
# pip install pofinance

t = MakeT()
print(t.single_t(27.11, 26.9, 300))

print(pf.t0(12.2, 12.3, 1000))
```
------

大家学习 或 使用代码过程中，有任何问题，都可以加入读者群交流哟~👇


![](https://cos.python-office.com/group/0816.jpg)



![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg)
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg)


## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA)


程序员晚枫专注AI编程培训，小白看完他和图灵社区合作的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA)就能上手做AI项目。
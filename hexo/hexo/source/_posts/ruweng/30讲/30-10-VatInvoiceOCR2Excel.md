---
title: 发票识别
date: 2025-08-22
tags: [星河计划]
---


<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='http://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
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
	<a href="https://mp.weixin.qq.com/s/7rH5U6s91hnTKCKZy4BHCg">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>

<!-- more -->


这里是正文

-------------------------------------------------------------------------------

>Python官网发布了Python自动化办公的库：python-office，相关信息：[重磅！官网发布第三方库：python-office，为Python自动化办公而生](https://mp.weixin.qq.com/s/v2n0DTVTZUaw7QOnA0Zlow)
>不需要自己写代码，直接调用写好的方法就行。

大家好，这里是码农如瓮，专注于分享：Python自动化办公。
**这个系列教程，用来逐一介绍python-office自动化办公的功能。**
## 1. 功能介绍
今天我们介绍这个库的功能之一：
> **识别发票并将结果转为excel**: 只需要一行代码，识别发票图片，将识别结果存为excel。
> -  首先在下面链接拿到id和key：https://cloud.tencent.com/act/cps/redirect?redirect=34190&cps_key=ca76be5a2293ba3906d6d5407aea15ee
> - 在代码中输入得到的key和id
## 2. 使用说明
#### 下载poocr
只需要下面这一条命令，就可以自动下载和安装下载poocr
```
pip install poocr
```
#### 调用功能
照抄下面代码，修改文件存放位置，右键选择运行
```python
# pip install poocr
import poocr

poocr.ocr2excel.VatInvoiceOCR2Excel(input_path=r'test_files/30-10-VatInvoiceOCR2Excel/',
                                    output_path=r'test_files/30-10-VatInvoiceOCR2Excel',
                                    output_excel='程序员晚枫的发票.xlsx',
                                    id='AKIDmaBRaWFk4D9sWAd9lEYgdNuDQQbhZDqI',
                                    key='JOGuLacQ1OXTBfv53oMispcCH4e1B8rN')
# 参数解释：
# input_path: 输入文件路径，可以是单个文件或文件夹
# output_path: 输出Excel文件的路径，表示使用函数默认文件名并保存在当前目录
# output_excel: 输出Excel文件的名称
# id: OCR引擎的用户ID
# key: OCR引擎的用户密钥
```

## 3.提交需求
1行代码实现复杂功能，是不是很简单？目前python-office这个自动化办公的第三方库正在持续开发中。
欢迎大家加入交流群，来沟通你的功能需求~

也欢迎有技术开发能力的同学，一起来丰富这个项目：
> - 欢迎大家的star & fork & pr！⭐
> - 开源地址：
> - https://gitee.com/CoderWanFeng/python-office
> - https://github.com/CoderWanFeng/python-office




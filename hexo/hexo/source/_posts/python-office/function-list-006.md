---
title: 盘点10个Python自动化办公操作，1行代码搞定，小白也能用
date: 2023-09-30 01:25:17
tags: python-office
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
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
<a href="https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>

大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)，小红书/小破站都叫这个名。

我工作中的主力语言是C++，在工作之余我搜集了很多有特色的自动化办公代码：**可以用1行代码，帮助编程小白解决复杂的办公问题。**

下面给大家分享其中的10个代码对应的演示视频。👇

## 1、批量识别发票，并且保存到Excel中

听起来十分复杂的操作，竟然也能用1行代码搞定。

```python
# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：python-office : http://www.python4office.cn/wechat-qrcode/
@个人网站      ：www.python-office.com
@代码日期    ：2023/9/10 22:35 
@本段代码的视频说明     ：https://www.python-office.com/course/docs/50-15-VatInvoiceOCR2Excel.html
'''

# pip install poocr
import poocr

# 免费体验：https://cloud.tencent.com/act/cps/redirect?redirect=34190&cps_key=ca76be5a2293ba3906d6d5407aea15ee
# 拿到id和key：https://cloud.tencent.com/act/cps/redirect?redirect=36394&cps_key=ca76be5a2293ba3906d6d5407aea15ee
poocr.ocr2excel.VatInvoiceOCR2Excel(input_path=r'test_files/50-15-VatInvoiceOCR2Excel/',
                                    output_path=r'test_files/50-15-VatInvoiceOCR2Excel',
                                    output_excel='程序员晚枫的发票.xlsx',
                                    id='AKIDb1SsDTXO2QZVGg2MTKjtz89xnQnxuc4F',
                                    key='2pX6Us1vaBl26uUv5B9tbDagW8UcEZ8c')

# 全部100多个识别功能：https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg
# 识别增值税发票
ressult = poocr.ocr.VatInvoiceOCR()
# 识别银行卡
ressult = poocr.ocr.BankCardOCR()
# 识别身份证
ressult = poocr.ocr.IDCardOCR()

```


## 2、PDF转Word

很多PDF转Word的软件需要收费，用Python不收费，速度还很快呢！

```python
# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：python-office : http://www.python4office.cn/wechat-qrcode/
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/22 23:28 
@本段代码的视频说明     ：https://www.bilibili.com/video/BV1em4y1H7ir/
'''

# pip install python-office
import office  # 导入第三方库

office.pdf.pdf2docx(file_path=r'./test_files/50-04-pdf2docx',
                    output_path=r'./test_files/50-04-pdf2docx/pdf2docx')
# 上面这种是Windows用户

# 如果你是尊贵的Mac和Linux用户，用下面这个代码
# pip install popdf
# import popdf
#
#
# popdf.pdf2docx(file_path=r'./test_files/50-04-pdf2docx/程序员晚枫.pdf',
#                output_path=r'./test_files/50-04-pdf2docx/pdf2docx')

```


## 3、PPT转成1张长图

用手机看PPT、分享给别人都很麻烦，那就用Python转成1张长图吧！

```python
# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：python-office : http://www.python4office.cn/wechat-qrcode/
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/22 23:28 
@本段代码的视频说明     ：https://www.bilibili.com/video/BV1em4y1H7ir/
'''

# pip install python-office
import office  # 导入第三方库

office.pdf.pdf2docx(file_path=r'./test_files/50-04-pdf2docx',
                    output_path=r'./test_files/50-04-pdf2docx/pdf2docx')
# 上面这种是Windows用户

# 如果你是尊贵的Mac和Linux用户，用下面这个代码
# pip install popdf
# import popdf
#
#
# popdf.pdf2docx(file_path=r'./test_files/50-04-pdf2docx/程序员晚枫.pdf',
#                output_path=r'./test_files/50-04-pdf2docx/pdf2docx')

```


## 4、用Python创建Excel

数据分析，少了Excel怎么行？👉[连微软都把Python加入Excel了](https://mp.weixin.qq.com/s/tJVilW1MmYJE2r4cYWt0Mg)

```python
# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：python-office : http://www.python4office.cn/wechat-qrcode/
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/25 22:27 
@本段代码的视频说明     ：https://www.bilibili.com/video/BV18m4y1u7Kq
'''

# pip install python-office
import office

# 代码、文档，见置顶评论
# 能模拟的数据有哪些？http://python4office.cn/python-office/fake2excel/

# 普通
office.excel.fake2excel(columns=['name', 'company', 'phone_number'],
                        rows=10,
                        path=r'./test_files/50-07-fake2excel/中文-1.xlsx')


import poexcel


poexcel.fake2excel()
```


## 5、图片加水印

作为博主，被抄袭是一件既开心又烦恼的事情。开心的是自己的作品被抄袭说明有流量了，烦恼是流量给了别人...

用1行代码，给所有图片加个水印吧。

```python
# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@读者群     ：http://www.python4office.cn/wechat-group/
@个人网站 ：www.python-office.com
@Date    ：2023/6/30 22:06 
@Description     ：https://www.python-office.com/course/docs/cooperator/01-add_watermark.html
'''

import poimage

poimage.add_watermark(file=r'D:\download\金融最新资讯新闻解读宣传实景风公众号首图.jpg', mark='B站：程序员晚枫', output_path=r'mark_img',color='#000000',opacity=0.04,
                      space=55,size=30,)
```



## 6、根据内容搜索文件

文件搜索软件我也用过，但是能通过内容搜索的功能，我只发现Python做到了。

```python
# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：python-office : http://www.python4office.cn/wechat-qrcode/
@个人网站      ：www.python-office.com
@代码日期    ：2023/9/4 1:24 
@本段代码的视频说明     ： https://www.bilibili.com/video/BV1Lm4y1M7Pz/
'''
import office

office.file.search_by_content(
    search_path=r'D:\workplace\code\gitee\python-office.com\docs-pages\vuepress\course\code\test_files\50-09-search4content',
    content='import office')

```


## 7、数据可视化

下面这种词云图片，大家都不陌生了吧？如果告诉你用1行Python代码就可以制作，你想不想学习一下？

```python
# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：python-office : http://www.python4office.cn/wechat-qrcode/
@个人网站      ：www.python-office.com
@代码日期    ：2023/9/8 22:29 
@本段代码的视频说明     ：https://www.bilibili.com/video/BV1ph4y1v7MN/
'''

import office

office.image.txt2wordcloud(filename=r'./test_files/50-11-txt2wordcloud/python-office.txt', color="black", result_file="your_wordcloud.png")

```

## 8、把自己的代码打包成Exe软件

这么多好用的功能，怎么分享给朋友们呢？自己打包一个exe软件吧！

```python
# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：python-office : http://www.python4office.cn/wechat-qrcode/
@个人网站      ：www.python-office.com
@代码日期    ：2023/9/10 11:43 
@本段代码的视频说明     ：https://www.bilibili.com/video/BV1Fw411S7kV/
'''
# 这段代码太长了，请见：https://www.python-office.com/course/docs/50-13-ppt2pdf.html
```


## 9、自动下载图片

提起Python，你肯定听说过爬虫吧？1行代码就实现的爬虫，听说过吗？

```python
# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：python-office : http://www.python4office.cn/wechat-qrcode/
@个人网站      ：www.python-office.com
@代码日期    ：2023/9/13 20:09 
@本段代码的视频说明     ： https://www.bilibili.com/video/BV14p4y1j7jg/
'''
import office

office.image.down4img(url='https://raw.atomgit.com/CoderWanFeng1/website/raw/main/icon3.jpg',
                      output_path=r'D:\workplace\code\gitee\python-office.com\docs-pages\vuepress\course\code\test_files\50-16-down4img')

```


## 10、微信机器人

现在人工智能怎么火，怎么能少了微信聊天机器人，1行代码直接用，再也不怕学习成本大了。

```python
# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信     ：python-office : http://www.python4office.cn/wechat-qrcode/
@个人网站      ：www.python-office.com
@代码日期    ：2023/8/28 21:05 
@本段代码的视频说明     ：https://www.bilibili.com/video/BV1Fu4y1v7xH
'''

import office

office.wechat.chat_robot(who='每天进步一点点')  # 智能聊天

# 所有代码，在置顶评论，24小时自动获取
# office.wechat.send_message()  # 发消息
# office.wechat.send_file()  # 发文件
# office.wechat.send_message_by_time()  # 定时发送
# office.wechat.chat_by_keywords()  # 根据关键词回复
# # 批量加好友
# #  群发

```



-------

这次我整理了50个自动化办公的实用共鞥你，都是1行Python代码就能实现的，录制了给小白的课程，需要可以加入学习哟~

- 加入学习👉[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)

大家学习 或 使用代码过程中，有任何问题，都可以加微信和我交流哟~👇

![python-office](https://cos.python-office.com/wechat/qr-code.jpg)


## 原创课程

- [给小白的《50讲 · Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)
- [给小白的《5讲 · Python发票批量识别保存为Excel》](https://www.python-office.com/course-002/5-poocr/5-poocr.html)
- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)


![](https://cos.python-office.com/course/50%E8%AE%B2%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8A%9E%E5%85%AC/free-link.jpg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。
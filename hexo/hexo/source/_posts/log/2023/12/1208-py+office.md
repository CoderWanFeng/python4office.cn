---
title: Python终于可以操作Office了
date: 2023-12-8 14:16:17
tags: 自动化办公
---

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/python-office/1209-py-office/cover.jpg)

大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)。

在小破站账号：Python自动化办公社区，更新Python教程4年多了。

> 我在和读者的沟通中，发现很多非程序员的朋友学习Python，不是为了成为Python大师，而只是为了提高自己的办公能力。

之前也给大家分享了一套入门课程：[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)。

今天在给大家分享一波Python操作Office的代码，涉及的软件很多：Excel、Word、PPT、PDF...赶紧学起来~

## 1、操作Excel：创建Excel

处理Excel的库：poexcel，下载命令如下：👇

```shell
pip install poexcel -U
```

这个库里的功能很多，本文举例一个功能：**创建Excel**，代码如下：👇

```python
# pip install python-office
import poexcel

# 代码、文档，见置顶评论
# 能模拟的数据有哪些？http://python4office.cn/python-office/fake2excel/

# 普通
poexcel.fake2excel(columns=['name', 'company', 'phone_number'],
                    rows=10,
                    path=r'./test_files/50-07-fake2excel/程序员晚枫-1.xlsx')
```

## 2、操作Word：word转pdf


处理Word的库：poword，下载命令如下：👇

```shell
pip install poword -U
```

这个库里的功能很多，本文举例一个功能：**word转pdf**，代码如下：👇

```python


# 下载教程：https://www.bilibili.com/video/BV1m14y1y76g
import poword

poword.docx2pdf(path=r'./test_files/程序员晚枫-docx2pdf',
                output_path=r'./test_files/50-05-docx2pdf/docx2pdf')
```

## 3、操作PDF：pdf转word
处理PDF的库：popdf，下载命令如下：👇

```shell
pip install popdf -U
```

这个库里的功能很多，本文举例一个功能：**pdf转word**，代码如下：👇

```python
# pip install popdf
import popdf


popdf.pdf2docx(file_path=r'./test_files/50-04-pdf2docx/程序员晚枫.pdf',
               output_path=r'./test_files/50-04-pdf2docx/pdf2docx')


```

## 4、操作PPT：ppt转图片

处理PPT的库：poppt，下载命令如下：👇

```shell
pip install poppt -U
```

这个库里的功能很多，本文举例一个功能：**ppt转图片**，代码如下：👇

```python
# pip install poppt
import poppt

poppt.ppt2img(input_path=r'./test_files/50-06-ppt2img/ppt-程序员晚枫.pptx',
                output_path=r'./test_files/50-06-ppt2img/output',
                merge=True)


```

## 5、操作文件：创建文件夹

处理文件的库：pofile，下载命令如下：👇

```shell
pip install pofile -U
```

这个库里的功能很多，本文举例一个功能：**创建文件夹**，代码如下：👇

```python
# pip install pofile
import pofile

pofile.mkdir(r'./test_files/50-32-mkdir/程序员晚枫-02')
pofile.mkdir(r'./test_files/50-32-mkdir/程序员晚枫-01/程序员晚枫-03')

```

## 6、操作图片：图片加水印

处理图片的库：poiamge，下载命令如下：👇

```shell
pip install poiamge -U
```

这个库里的功能很多，本文举例一个功能：**图片加水印**，代码如下：👇

```python
import poiamge

# office.image.add_watermark(file='./要添加水印的图片.png',mark='python办公自动化',output_path=r'已添加水印',opacity=0.2)

poiamge.add_watermark(file='./程序员晚枫-要添加水印的图片.png',
                           mark='python办公自动化',
                           output_path=r'已添加水印',
                           color="#ff0000", size=80, opacity=0.5, space=600, angle=30)
```

----

以上所有仓库的核心功能，我都加入了原创课程:[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)都是1行Python代码就能实现的，适合纯小白的课程，需要可以加入学习哟~

- 加入学习👉[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)

大家学习 或 使用代码过程中，有任何问题，都可以加入读者群交流哟~👇


![](https://cos.python-office.com/group/0816.jpg)


## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)就能上手做AI项目。
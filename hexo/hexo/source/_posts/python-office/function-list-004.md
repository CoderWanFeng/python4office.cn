---
title: 5 个 Python 代码来自动化你的日常工作，网友：早知道就好了
date: 2023-09-27 01:25:17
tags: python-office
---


![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/5%E4%B8%AA%E6%9D%80%E6%89%8B%E7%BA%A7Python%E4%BB%A3%E7%A0%81%2F5ge.jpg)


大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，小红书也叫这个名字。

最近在B站更新一套课程：[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)，并且建了一个课程群，用来沟通大家的学习问题和需求。

在更新课程的这1个多月里，又发现了一些新需求，今天整理出来，分享给大家~


> 全是自动化办公的常用工具，网友：早知道就好了

## 1、从Word里提取所有图片

1行代码，提取Word中的图片。

需要强调的是：这个功能需求不仅来自课程群，就连代码都是课程群里王鹏大哥开发的，我们这套课程针对小白入门Python，看来是有效果的。


### 安装第三方库
```
pip install python-office
```

代码

```
import office

office.word.docx4imgs(word_path=r'./程序员晚枫的文档.docx', img_path='./python-office/out')

# 参数说明：
# word_path：需要提取图片的word路径
# img_path：保存图片的文件夹位置，程序会自动在指定位置，用word文件的名称创建一个子文件夹
```

## 2、制作渐变国旗头像

不知从何时开始，每年国庆都流行换国旗头像。

用Python一行代码就可以制作，而且不用自己准备国旗。

安装第三方库
```
pip install poimage

```

代码
```
import poimage

poimage.flag2profile( profile_path=r'D://程序员晚枫的头像.jpg',
                      output_path=r'D://out/国旗头像.png')
# 参数说明：
# profile_path：存放自己头像的路径
# output_path：存放合成头像的路径
```



## 3、汉字转拼音

后台问少儿编程的朋友比较多，所以这次也开发了一个汉字转拼音的小玩意。

还是群里王鹏大哥，做了一个GUI版本。如下图所示，👇。

这段代码比较长，需要的朋友，请复制下方链接，在浏览器打开，自己领取。

[https://github.com/CoderWanFeng/python-office/blob/master/contributors/wangpeng/pinyin_gui.py](https://github.com/CoderWanFeng/python-office/blob/master/contributors/wangpeng/pinyin_gui.py)

## 4、自动识别发票，并且保存Excel中

有些人说发票都电子化了，不用自己识别录入了。

但每次更新发票识别功能，都有很多人点赞，我很疑惑？

安装第三方库
```
pip install poocr

```

代码
```
# pip install poocr
import poocr

# 免费体验：https://cloud.tencent.com/act/cps/redirect?redirect=34190&cps_key=ca76be5a2293ba3906d6d5407aea15ee
# 拿到id和key：https://cloud.tencent.com/act/cps/redirect?redirect=36394&cps_key=ca76be5a2293ba3906d6d5407aea15ee
poocr.ocr2excel.VatInvoiceOCR2Excel(input_path=r'test_files/50-15-VatInvoiceOCR2Excel/',
                                    output_path=r'test_files/50-15-VatInvoiceOCR2Excel',
                                    output_excel='程序员晚枫的发票.xlsx',
                                    id='AKIDb1SsDTXO2QZVGg2MTKjtz89xnQnxuc4F',
                                    key='2pX6Us1vaBl26uUv5B9tbDagW8UcEZ8c')
```

## 5、自动整理文件夹

有多少人文件夹乱七八糟的，自己又不想整理？

用1行Python代码，可以根据文件类型，自动分类整理，赶紧试试~

安装第三方库
```
pip install pofile

```

代码
```
# 导入这个库
import pofile

pofile.group_by_name(r"d://你的文件夹")
```
---

以上功能，都来自python-office这个自动化办公的专用库，更多功能和视频教程，可以访问官网：``www.python-office.com``


![](https://cos.python-office.com/course/50%E8%AE%B2%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8A%9E%E5%85%AC/free-link.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
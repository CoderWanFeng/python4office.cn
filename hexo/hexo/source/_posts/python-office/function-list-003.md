---
title: 5 个 Python 代码来自动化你的日常工作，网友：早知道就好了
date: 2022-10-31 01:25:17
tags: python-office
---


![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/5%E4%B8%AA%E6%9D%80%E6%89%8B%E7%BA%A7Python%E4%BB%A3%E7%A0%81%2F5ge.jpg)

重复性任务总是耗时且无聊，想一想你想要一张一张地裁剪 100 张照片或 核对、纠正拼写和语法等工作，所有这些任务都很耗时，为什么不自动化它们呢？在今天的文章中，我将与你分享 5 个 Python 自动化办公的快捷功能。

所以，请你把这篇文章放在你的收藏清单上，以备不时之需，现在，让我们开始吧。


> 网友：早知道就好了

## 1、PDF转word

有时候我们想编辑PDF，但是很多编辑软件需要收费，这时候我们可以先把PDF转换成Word文档。

### 安装第三方库
```
pip install popdf
```

代码

```
import popdf

# 1行代码，实现 PDF 转 Word
popdf.pdf2docx(file_path='程序员晚枫.pdf')

# 参数说明：
# file_path:存放PDF的位置 + PDF的文件名，例如：c://test//程序员晚枫.pdf
```

## 2、给图片添加水印

辛苦设计的100张图片，传到网上容易被盗版怎么办？用Python批量添加浅浅的水印。

安装第三方库
```
pip install poimage

```

代码
```
import poimage

poimage.add_watermark(file='程序员晚枫.jpg', mark='你的水印')
```


## 3、多个Excel表格的关联查询

这个功能是防疫期间开发的：根据身份证号码，从100个Excel文件里面，找到这个人的所有信息。

安装第三方库
```
pip install poexcel

```

代码
```
import poexcel

poexcel.find_excel_data(search_key='你要搜索的内容', target_dir='存放excel的文件夹位置')
```

## 4、简易爬虫下载图片

一行代码，实现网上图片的下载

安装第三方库
```
pip install poimage

```

代码
```
import poimage

poimage.down4img(
    url='https://cos.python-office.com/group%2Ffree-group.jpg',
    output_name='程序员晚枫',
    type='jpg')
```

## 5、翻译

安装第三方库
```
pip install wftools

```

代码
```
# 导入这个库
import wftools  
  
# to_lang，是翻译的结果使用哪种语言，支持全球100多个语言；content，是你想翻译的文本内容
wftools.transtools(to_lang='Chinese', content='hello world')
```
---

以上功能，都来自python-office这个自动化办公的专用库，更多功能和视频教程，可以访问官网：``www.python-office.com``



![](https://cos.python-office.com/course/50%E8%AE%B2%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8A%9E%E5%85%AC/free-link.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)就能上手做AI项目。
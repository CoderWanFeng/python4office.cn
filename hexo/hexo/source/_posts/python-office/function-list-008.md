---
title: 分享10个免费的Python代码仓库，轻松实现自动化办公（下）
date: 2023-10-22 01:25:17
tags: python-office
---



大家好，这里是程序员晚枫，小红书/小破站都叫这个名。

Python是我工作中的主力语言之一（另一个是C++），在工作之余我给大家（非程序员）搜集了很多实用的自动化办公代码：**可以用1行代码，帮助编程小白解决复杂的办公问题。**

下面给大家分享其中的10个常用第3方库和对应的代码，相关的演示视频，都在我的小破站账号：**Python自动化办公社区**里。👇

> 这一篇给大家分享的是前5个：excel、pdf、ppt、文件管理和图片，下一篇给大家分享剩下的5个，大家可以关注我的主页查看更新。

## 1、Python + Excel = poexcel

普通打工人使用最多的软件：Excel，如何自动化操作？你可以看一下poexcel这个库。

全部功能 &　下载链接：``https://pypi.org/project/poexcel/``


> 功能举例：从100个Excel文件中，查找一个信息怎么办？poexcel1行代码搞定。
```python
# 导入这个库：pip install poexcel
import poexcel

poexcel.query4excel(query_content='小红书',
                    query_path=r'./test_files/50-20-query4excel',
                    output_path=r'./test_files/out',
                    output_name='query4excel.xlsx')

```


## 2、Python + PDF = popdf

网上很多PDF软件要收费，但用Python可以免费。

全部功能 &　下载链接：``https://pypi.org/project/popdf/``


> 功能举例：很多PDF转Word的软件需要收费，用Python不收费，速度还很快呢！

```python
# pip install popdf
import popdf


popdf.pdf2docx(file_path=r'./test_files/50-04-pdf2docx/程序员晚枫.pdf',
               output_path=r'./test_files/50-04-pdf2docx/pdf2docx')

```


## 3、Python + PPT = poppt

如果你平时使用PPT比较多，而且很繁琐，你可以看看这个库。

全部功能 &　下载链接：``https://pypi.org/project/poppt/``


> 功能举例：把PPT转成PDF，用poppt没什么难度，因为它还可以把PPT转成一张长图，比PDF方便~

```python
# pip install poppt
import poppt

poppt.ppt2img(input_path=r'./test_files/50-06-ppt2img/ppt-程序员晚枫.pptx',
                   output_path=r'./test_files/50-06-ppt2img/output',
                   merge=True)
```


## 4、Python + 文件管理 = pofile

批量重命名、通过内容查找文件、自动给文件分类等等自动化处理文件的功能，pofile库都有了。

全部功能 &　下载链接：``https://pypi.org/project/pofile/``


> 功能举例：网上通过文件名查找文件看腻了，看一下如何通过内容搜索文件吧！


```python
# pip install pofile
import pofile

pofile.search_by_content(
    search_path=r'..\test_files\50-09-search4content',
    content='import office')
```


## 5、Python + 图片 = poimage

这个图片处理库的功能也有很多，我个人最常用的就是加水印功能。

全部功能 &　下载链接：``https://pypi.org/project/poimage/``


> 功能举例：批量给图片加水印，只要你的电脑能装下，一次性处理多少图片都可以！


```python
import poimage

poimage.add_watermark(file=r'D:\download\程序员晚枫的图片.jpg', mark='B站：程序员晚枫', output_path=r'mark_img',color='#000000',opacity=0.04,
                      space=55,size=30,)
```




-------

以上所有仓库的功能介绍，我都加入了原创课程:[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/lOx4cAp9AllsCrhsUqVn8g)都是1行Python代码就能实现的，适合纯小白的课程，需要可以加入学习哟~

- 加入学习👉[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/lOx4cAp9AllsCrhsUqVn8g)

大家学习 或 使用代码过程中，有任何问题，都可以加入读者群交流哟~👇


![](https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/0816.jpg)

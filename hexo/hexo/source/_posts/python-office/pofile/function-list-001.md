---
title: 5大文件管理操作，Python自动化办公，整明白了
date: 2023-09-30 13:31:42
tags: 自动化办公
---




![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/5%E4%B8%AA%E6%9D%80%E6%89%8B%E7%BA%A7Python%E4%BB%A3%E7%A0%81%2F5ge.jpg)


大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)，小红书也叫这个名字。

最近在B站更新一套课程：[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)，并且建了一个课程群，用来沟通大家的学习问题和需求。

在更新课程的这1个多月里，又发现了一些新需求，今天整理出来，分享给大家~


> 全是自动化办公的常用工具，网友：早知道就好了

## 1、批量压缩文件夹

电脑空间不够用了？别怕，批量压缩一下文件吧~


### 安装第三方库
```
pip install pofile
```

代码

```
import pofile

pofile.zip4dir(path=r'..\程序员晚枫的文件夹\50-28-zip4dir')
```

## 2、批量重命名

在网上下载的资料，名称上有广告？直接批量删除。

安装第三方库
```
pip install python-office

```

代码
```
import office

office.file.replace4filename(path=r'./test_files/50-23-replace4filename',
                             del_content='程序员晚枫',
                             replace_content='小H书-程序员晚枫',
                             dir_rename=False,
                             suffix='.py')
```



## 3、根据内容查找文件

根据标题查找文件，大家都用过了。

如果我忘了标题，根据文件里的内容查找文件，你用过吗？

安装第三方库
```
pip install python-office

```

代码
```
import office

office.file.search_by_content(
    search_path=r'..\程序员晚枫\50-09-search4content',
    content='import office')
```

## 4、自动创建Excel

在没有Python之前，处理数据的软件，非Excel莫属！

安装第三方库
```
pip install poexcel

```

代码
```
import poexcel

poexcel.fake2excel(columns=['name', 'company', 'phone_number'],
                        rows=10,
                        path=r'./程序员晚枫/50-07-fake2excel/中文-1.xlsx')
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

pofile.group_by_name(r"d://程序员晚枫的文件夹")
```
---

以上功能，都来自python-office这个自动化办公的专用库，更多功能和视频教程，可以百度一下：``python-office``





## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
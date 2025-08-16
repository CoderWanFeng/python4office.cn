---
title: 05-PPT转PDF
date: 2025-08-05 23:41:49
tags: [10讲Python自动化办公]
---
哈喽，大家好，今天开始学习我们的第5讲，用Python代码将PPT文件转换成PDF文件。

首先，还是老规矩，我们要确保自己电脑上已经成功安装了Python和pycharm，然后这一讲我们需要使用到的库是python-office。

这里，我们只需要执行一行命令就可以成功安装这个库，也就是`pip install python-office`.

如果你电脑的网速不好，那我推荐你用下面这个命令去执行一下，也就是给下载加上清华源，大家不用管命令是什么意思，直接抄我的命令去执行就好。


```python
pip install python-office -i https://pypi.tuna.tsinghua.edu.cn/simple
```
好，大家看这个目录，这里有一个叫晚枫师兄的PPT文件，我们要实现的需求是将它转换成PDF文件。

该怎么做呢？

很简单，我们一行代码就可以完成，来，我们看一下代码是怎么写的。

第一行代码是导入我们的office库，第二行代码是实现该功能的关键代码，它需要传递2个参数，第一个参数是你要转换为PDF的PPT文件，第二个参数是你转换成功之后的文件的存放位置路径。

提醒一下大家，路径前面的小r不要忘记了，否则会报错的。

然后，这个路径也不用手敲，像我这样复制即可。

好的，我们来执行一下代码，看下效果。

怎么运行呢？

很简单，鼠标右键，找到这个三角形，点击就能运行了。

好的，运行成功，我们可以看到文件夹下多了一个PDF文件，并且原来的PPT文件也还在。

那这一讲就到这里，大家课后一定要对着代码敲一遍，加深一下印象，这样下次遇到这个需求时就可以直接去用了。

行，如果你喜欢视频，可以点赞收藏转发，我们下一讲再见。

本讲视频代码如下：

```python
# -*- coding: UTF-8 -*-
'''
@作者  ：晚枫师兄
@微信     ：wfdev7
@代码日期    ：2025/8/5
'''

# 导入库：python-office，简写为：office
# pip install python-office
# pip install python-office -i https://pypi.tuna.tsinghua.edu.cn/simple

import office

# 填入你的ppt目录
office.ppt.ppt2pdf(path=r'C:\Users\Administrator\Desktop\10讲python自动化办公\05-PPT转PDF',\
                   output_path=r'C:\Users\Administrator\Desktop\10讲python自动化办公\05-PPT转PDF\output')
```
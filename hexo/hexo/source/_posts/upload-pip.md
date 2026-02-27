---
title: 以最简洁的方式打包发布你自己的pip项目
date: 2022-01-05 16:03:35
tags: 开源项目
---



<p align="center">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://raw.atomgit.com/CoderWanFeng1/website/raw/main/github-nav.jpg" alt="github license"/>
    </a>   
</p>
<p align="center">
	<strong>🍬python for office</strong>
</p>
<p align="center">
	👉 <a href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>


<p align="center" name="图标-github">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/contributors/CoderWanFeng/python-office" alt="github contributors"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/forks/CoderWanFeng/python-office" alt="github forks"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues/CoderWanFeng/python-office" alt="github issues"/>
    </a>	
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues-pr/CoderWanFeng/python-office" alt="github license"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/license/CoderWanFeng/python-office" alt="github license"/>
    </a>   
</p>

<p align="center" name="gitee">
	<a target="_blank" href='https://gitee.com/CoderWanFeng/python-office/'>
		<img src='https://gitee.com/CoderWanFeng/python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
		<img src="https://gitee.com/CoderWanFeng/python-office/badge/fork.svg?theme=white" alt="gitee fork"/>
	</a>
	<a href="https://mp.weixin.qq.com/s/yaSmFKO3RrBpyanW3nvRAQ">
	<img src="https://img.shields.io/badge/QQ-163434413-orange"/></a>
</p>




你有没有过这种经历？

> 花费很长时间写了一套代码，逻辑很复杂，功能很丰富，让你很自豪，但你却发现，你没法把他分享出去？让更多的人看到？

当有了一些成果以后，如何发布宣传是一件很重要的事，
开源也是Python发展这么迅速一个非常重要的原因，所以Python官方也给大家提供了分享自己代码和项目的地方：pypi
今天向大家介绍一下如何向全球公开发布自己的pip项目。
> 如果你还没学完Python基础，推荐你这套👉[Python基础精讲课程](https://www.python-office.com/video/video.html)

### 1.注册一个pypi账号

<!-- more -->


 网址在这里 https://pypi.org/ 很简单，直接注册就好 



### 2.编写一个自己的python 项目

 要发布项目，必须得先有一个自己的项目，我们把代码放在一个文件夹里像下面这样 

- 文件夹：heyWFeng
  - 文件：heyWfeng.py
  - 文件：__ __init__ __.py
- 文件：setup.py

 这是一个名为heyWFeng的文件夹，heyWFeng.py是这个项目的主要代码，__ __init__ __.py文件是必须的，这是一个package的象征，可以什么都不写，但必须有。

### 3.编写setup.py文件的内容

这个文件是用来打包的，内容如下。

```python
#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: heyWFeng
# Mail: 1957875073@qq.com
# Created Time:  2022-1-5 10:17:34
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "heyWFeng",      #这里是pip项目发布的名称
    version = "0.0.1",  #版本号，数值大的会优先被pip
    keywords = ("pip", "heyWFeng"),
    description = "A successful sign for python setup",
    long_description = "A successful sign for python setup",
    license = "MIT Licence",

    url = "http://python4office.cn/upload-pip/",     #项目相关文件地址，一般是github
    author = "heyWFeng",
    author_email = "1957875073@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []          #这个项目需要的第三方库
)


```



### 4.本地打包项目文件

 在命令行上先 cd 到存放setup.py文件的目录，然后用下面的命令 

```python
python setup.py sdist  
```

这个命令会在目录下生成两个文件夹，其中dist里的压缩包是我们接下来要上传到pypi官网发布的内容。

### 5.上传项目到pypi官网

然后转到命令行，下载一个上传工具。

```python
pip install twine
```

下载好后，就可以上传自己的库了。

```python
twine upload dist/heyWFeng-0.0.1.tar.gz
```



### 6.上传成功

上传成功之后，会显示你自己项目的地址:https://pypi.org/project/heyWFeng/ ，赶快打开去看看吧~

参考链接：[CSDN](https://liangjunfeng.blog.csdn.net/article/details/80037315?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-2.pc_relevant_paycolumn_v2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-2.pc_relevant_paycolumn_v2&utm_relevant_index=5)



---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。
---
title: 用Python实现微信多开，1行代码搞定
date: 2023-10-22 10:41:04
tags: [开源项目,自动化办公,wftools]
---

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，小破站也叫这个名字。

今天给大家分享一个实用功能：微信多开。

## 为什么有这个功能？

现在我的小破站账号有10w+粉丝了，已经很少和别人+微信了。

但是我刚开始做博主的时候，是很主动和别人加微信的。但当时一个微信号又只能加5000个好友，所以我就申请了一堆的微信。

导致我现在每次打开电脑办公，都要同时开几个微信，防止漏掉什么重要的读者留言。

**所以我就写了1行代码，我指定打开几个微信，就可以打开几个微信。**


## 1行代码的说明书

先看一下代码，你可以直接复制这段代码去用。

```python
import wftools

soft_path = r"D:\software\程序员晚枫的文件夹\WeChat.exe"
wftools.open_soft(soft_path=soft_path, num=2)
```

运行这段代码，注意几个细节：

1. 运行代码之前，在电脑上下载wftools这个库。命令：``pip install wftools``，视频教程见50讲自动化办公的第3讲，[点我直达](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)
2. soft_path这里，改成自己电脑上微信.exe的存储位置。
3. num这里，改成你要打开几个微信。

## 写在后面

Python可以替代你很多日常办公中的工作，但是学会Python不容易。

我是一个程序员，利用业余时间，专门为非程序员整理了10个微信机器人的代码，都是1行代码就可以用的。

方便大家快速入门Python，大家可以点击课程进行学习：[给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)。

这套课程主要教给你Python自动化办公应该怎么用，而不是给你讲深奥的Python编程理论。

> 毕竟，对于大多数打工人来说，我们只想用Python解决问题，而不是成为Python大师。

学习过程中有任何问题，也欢迎加入读者群进行交流~👇

![](https://cos.python-office.com/group/0816.jpg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)就能上手做AI项目。
---
title: 用Python下载B站视频？1行命令搞定，悄悄用
date: 2022-08-16 16:05:25
tags: python-office
---



![](https://www.python-office.com/api/img-cdn/python-office/you-get/cover.jpg)

大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)。

本周**知识星球：Python读者圈**里的同学，给我提了一个问题：
> B站的课程很好，但是上班没有网，也不想用B站的视频缓存功能。**怎么把B站的视频下载下来，存到百度网盘里看？**

安排~！

## 1、解决思路

我把这个功能集成到[自动化办公的专用库python-office](http://t.cn/A6aWzuyn)里了，所以你只需要做2步：

1. 下载python-office库
2. 在电脑终端里输入下载视频的命令

我们一起来操作一下~
<!-- more -->

## 2、下载python-office

安装python-office这个库

- 这行命令的作用：下载 + 更新；
- 如果你之前用过这个库，也要运行一下这行命令，进行一下更新。否则没有本文功能。

```
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```

运行这行命令之前，你的电脑里必须有python环境。

如果你的电脑里还没有python环境，去看这个``6分钟的傻瓜式安装视频：https://www.bilibili.com/video/BV1Q44y1u7rV``

## 3、在电脑终端里输入下载视频的命令
打开你电脑的任意一个文件夹，
1. mac系统用户：直接打开你的终端，App列表里就可以直接找到，
2. windows系统用户：如下图所示打开终端，
  - 在文件路径的位置，``输入cmd，然后敲击回车``，会弹出一个黑色的终端。
3. 在终端中输入：``you-get https://www.bilibili.com/video/BV1pT4y1k7FH`` (后面的这个链接，可以替换成你想下载的视频的链接)

> 如果有的教程有几百集（分P），那你就在上面这个命令的后面，加一个空格和一个参数：``-l``（小写的L），例如：``you-get https://www.bilibili.com/video/BV1wB4y1w7KV -l``

![](https://www.python-office.com/api/img-cdn/python-office/you-get/cmd.jpg)


**快去试试吧~**

> 如果我有没说清楚的，或者在使用过程中有问题，欢迎大家在评论区和我交流~

----


---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)就能上手做AI项目。
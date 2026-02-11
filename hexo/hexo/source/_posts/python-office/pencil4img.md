---
title: AI画画到什么水平了？1行代码生成素描画，又一批人要失业啦！
date: 2022-10-20 22:34:33
tags: python-office
---


![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pencil4img-cover.jpg)
大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)，读者交流群🏠[点我直达](http://www.python4office.cn/wechat-group/)

之前给大家介绍了：👉[25个Python学习资源（文字版），摸鱼必备，可以用到就业](https://mp.weixin.qq.com/s/-mlsV7PFc27JElOTCskMsg)

今天，给大家介绍python-office近期更新的功能之一：**1行代码，画出美女的素描**。


真的很实用！

## 1. 安装python-office
安装很简单，在有python环境的电脑上，只需要执行下面这一行命令。
> 如果你之前使用过python-office这个库，也需要执行一下，可以下载到最新版本.

安装
```
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```
>如果你的电脑里还没有安装python环境，可以看一下下面这个6分钟的傻瓜式安装教程，有电脑就能操作：https://www.bilibili.com/video/BV18g411h7jJ?p=3

## 2. PDF合并
直接上代码！

代码
```
# 导入这个库：python-office，简写为office
import office

office.image.pencil4img(input_img=r'D:\workplace\code\test\down4img\girl.jpg')


#参数作用：
# input_img = 原图片的名字
```


## 3.开源项目

1行代码，解决办公问题的第三方库是：python-office

- ⭐GitHub：https://github.com/CoderWanFeng/python-office

## 4. python-office库，近期添加的功能

- [生成二维码、翻译、提取音频、重命名文件/文件夹、图片加水印](https://mp.weixin.qq.com/s/4Pt0YWakkPhfEWVMHwXe8g)
- [实现Word批量转换PDF](https://mp.weixin.qq.com/s/eBn3N_FEx1dlC_-ttmlOwg)
- [一行Python代码，给PDF文件添加水印，快速而且免费~](https://mp.weixin.qq.com/s/yJDs5RoytRL5hl-ybXkZOA)

---

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
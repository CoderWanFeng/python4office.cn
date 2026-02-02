---
title: 用Python发一个优雅的朋友圈，1行代码搞定
date: 2023-10-24 00:08:24
tags: [开源项目,poimage]
---

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，这段时间给大家分享多个微信自动化的代码：

- [用Python实现微信多开，1行代码免费用](https://mp.weixin.qq.com/s/qlubpfAytr_coV8GilG9RA)
- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)


今天再给大家分享一个：**用Python发一个好看的朋友圈的代码。**


## 效果展示

最近很多P图软件实现了一个效果：把一张图片分成9张，如下图所示。👇


``切割之前的朋友圈``

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poimage/split4img/origin.png)



``切割之后的朋友圈``

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poimage/split4img/cut.png)

我们一起来看一下，如何用1行Python代码实现~


## 代码说明

实现这个功能的是第三方库：``poimage``，下载命令如下：

```python
pip install poimage
```

下载以后，切割图片只需要下面这1行代码：

```python

import poimage

poimage.split4img(img_path=r"./imgs/icon2.jpg", output_path=r'D:\程序员晚枫的文件夹\output')
```

参数说明：
- img_path：需要切割的图片，存放路径；
- output_path：切割后的图片，存放在哪里。

## 参考链接

- [分享10个免费的Python代码仓库，轻松实现自动化办公（上）](https://mp.weixin.qq.com/s/3eKDWOiJv5CCiMliCDtAWA)
- [分享10个免费的Python代码仓库，轻松实现自动化办公（下）](https://mp.weixin.qq.com/s/bkB9LavphP4jqPLvGSAnFA)

----


我今年发布了一个原创课程:[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)都是1行Python代码就能实现的，适合纯小白的课程，需要可以加入学习哟~

- 加入学习👉[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)

大家学习 或 使用代码过程中，有任何问题，都可以加入读者群交流哟~👇


![](https://cos.python-office.com/group/0816.jpg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)就能上手做AI项目。
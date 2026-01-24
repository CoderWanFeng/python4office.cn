---
title: 免费制作国旗微信头像，1行Python代码搞定，小白可用
date: 2023-09-25 00:08:24
tags: 开源项目
---



![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poimage/flag2profile/cover.png)

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，B站/小红书/知乎，都叫这个名。

又到了一年一度制作国庆头像的时候了，这次我们看如何用1行Python代码，轻松制作自己的国旗头像。

<iframe src="//player.bilibili.com/player.html?bvid=BV15u4y147ow" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=100%, height=500> </iframe>


## 代码演示

该功能来自第三方库：``poimage``，使用下面的命令，可以自动下载和安装这个库：

```shell
pip install poimage
```

下载以后，直接使用下面这一行代码，生成自己的国旗头像。
```python
# pip install poimage
import poimage

poimage.flag2profile( flag_path=r'D://国旗的图片.png', 
                      profile_path=r'D://程序员晚枫的头像.jpg',
                      output_path=r'D://out/国旗头像.png')
```

## 参数说明

- flag_path：存放国旗的路径，[国旗下载，官方地址](https://mp.weixin.qq.com/s/zm6wQcadvH5sfcMSlJIapg)
- profile_path：存放自己头像的路径
- output_path：存放合成头像的路径

## 写在最后

Python自动化办公除了可以帮助我们更好的工作，也有很多趣味小应用。

更多实用功能，大家可以查看课程👉[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)



![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5/auto-work.jpg)

![](https://ads-1300615378.cos.ap-guangzhou.myqcloud.com/alipay/hong-3.jpg)
---
title: 1行Python代码实现AI换脸，难辨真假！网友：细思极恐
date: 2023-02-03 23:33:58
tags:
---



![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poai%2Fface_merge%2Fcover.jpg)

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。

之前**杨幂换脸事件**登上了热搜，让大家关注到AI换脸这件事，并且有部分网友担心：这要是被用到爱情动作片里去可该咋整？

更有甚者，有人用此技术行骗，真假难辨，大家一定要警惕！

今天我们就来看一下：**1行Python代码实现AI换脸是多么的简单**，赶紧转发给身边的朋友，普及一下常识~

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poai%2Fface_merge%2Fweibo.jpg)



## AI换脸，1行代码就够了

先假设一个应用案例：找一张你的照片，把自己的脸换成刘德华的，是个美好的例子吧？

实现这个案例，只需要下面这一行代码就够了代码，👇。
```python
# pip install pobaidu
import pobaidu

pobaidu.face.face_merge(
    face_img_path='https://article-1300615378.cos.ap-nanjing.myqcloud.com/poai/face_merge/刘德华的照片.jpg',
    base_img_path='https://article-1300615378.cos.ap-nanjing.myqcloud.com/poai/face_merge/你自己的照片.jpg',
    output_path=r'.\python-office\换脸后的照片.jpg',
    configPath=r'配置文件，见下文说明')
```

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poai%2Fface_merge%2Fres.jpg)

## 注意事项

本文功能实现依托于百度的AI平台，每个人有500次免费调用的次数（有效期1年），如需获取免费使用额度，请在下列公众号的后台，发送关键词：**换脸学习**，即可24小时自动领取~

公众号：Python自动化办公社区

领取额度后，配置方法，见春节期间发布的简易教程：[我用一行Python代码还原了黑白照片，外婆哭了](https://mp.weixin.qq.com/s/fJLtyTCWBU767xieRTohIQ)

## 相关阅读

- [开源中国推荐：python-office自动化办公，每个功能只需一行代码，做到了真正的开箱即用。](https://mp.weixin.qq.com/s/d2m7xYCLXF8QUlr-5sSuPA)

- [Python实现图片文字提取，准确率高达99%，100多个功能全给你！](https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg)

- [别总写代码，这130个网站比涨工资都重要！](https://mp.weixin.qq.com/s/iUNSioJ8GjYgiAoYFpXOaQ)


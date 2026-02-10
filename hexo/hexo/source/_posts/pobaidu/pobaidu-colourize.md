---
title: pobaidu-colourize
date: 2023-01-25 01:19:28
tags: [pobaidu,AI]
---


大家过年好，这里是程序员晚枫。

作为一个除了敲代码啥也不会的程序员，我一直在想自己能给身边的人带来什么帮助。

这次过年，我用1行Python代码，把年代久远的黑白照片还原为了彩色，唤起了家人的许多回忆。

本篇文章，给大家分享一下1行代码的操作步骤，免费且有趣~

## 先上代码
实现思路很简单，直接调用百度AI平台开放的功能就可以了。如何调用？我给大家封装成了下面这1行代码，直接使用。关于如何配置百度AI平台的信息，见本文第二部分。

```python
# 导入pobaidu这个第三方库
import pobaidu

# 调用给黑白照片上色的功能
pobaidu.imageprocess.colourize(img_path=r'img/img_1.png')
```

代码非常简单，直接复制到你的编辑器即可运行~

### 参数说明
``img_path``：你黑白照片的存放位置，必填。
``output_path``：增加了颜色的照片存放位置，选填。

## 注意事项

### 1、下载第三方库

在terminal里运行以下代码：``pip install pobaidu``
怎么下载第三方库，这是一个在往期文章里重复了一万遍的问题了，还有不懂的同学，去看这篇文章：[使用阿里镜像的黑科技，加速下载Python第三方库](https://mp.weixin.qq.com/s/EnhHNRCwEXXseBS3aTNuMg)


### 2、配置信息

本功能调用了百度AI平台的功能，每个用户都有免费的1000次调用额度，应该是足够用了。
如果有不会用百度AI的同学，开通的教程和地址我也给大家准备好了。在下列公众号的后台回复：**黑白照片**，即可24小时自动获取~


开通百度AI平台的账号以后，在py文件的同级目录，增加一个文件：``baidu-config.toml``，内容如下：
```shell
[baidu-ai]
client_id = '百度AI平台的id'
client_api = '百度AI平台的应用id'
client_secret = '百度AI平台的应用key'
```

### 3、联系作者

如果有更多问题，你可以直接联系我来帮你操作：
- 连Python都不会用，但是想实现本文功能；
- 想在本文基础上进行2次开发；
- 其它的定制化需求。
我的微信：[python-office](http://www.python4office.cn/wechat-qrcode/)，扫码下图直接添加。👇

![](https://cos.python-office.com/wechat/qr-code.jpg)

## 写在最后

感谢大家一年来对公众号/B站：Python自动化办公社区的关注和支持，再次祝福大家新的一年：身体健康，事事如意！

----




## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
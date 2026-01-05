---
title: 免费搭建一个有脾气的聊天机器人,1行Python代码就够了！
date: 2023-06-30 22:24:23
tags: 机器人
---




![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/porobot/chat/cover.jpg?q-sign-algorithm=sha1&q-ak=AKIDrM1I6pqTnpZybbxSvZ804Vn2aHUVYKgUg6sAyccQbfIlOzoScUwG-k4bloRnQ-F3&q-sign-time=1688134241;1688137841&q-key-time=1688134241;1688137841&q-header-list=host&q-url-param-list=ci-process&q-signature=92a188ef94d8c28fddb58d0f6f76f58896c6413b&x-cos-security-token=CGcfrvPEyFcFuNlAwH6HiKRxfwFYu6ca8e1136aad872c83218ea42a3b17ed3cc39O0ObyjMjlprA4jUCJZPMjPCs2bq7219AsgEC6HiXy9effy8A3iuZNsmupr7qZk4iGhneYWh1tTXXCquOHzJgyYlFUIU-m9CzSikj9bH4vKcJSx6aeNRUImLSIxGa0L6KKDvwm-__dDuKRZjhqNDzRqhm2FP0owI4JpsTo828v4vFSDfzQaUUlDVgFKuOia&ci-process=originImage)

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/h0MExYJag6hLnQg26yx98w)。

之前给大家免费分享了[【8讲】用Python制作一个微信机器人，1行代码人人可用](https://mp.weixin.qq.com/s/9aspEHdCiAdXK17AvHlu9Q)，很多人还想要**免费的智能聊天功能**。

今天终于开发出来了，让我们一起看一下，如何用1行代码，实现智能聊天。

我测试了很多次，回复一直很稳定，赶紧去试一下，这个机器人的回复是有脾气的哟~

<!-- more -->

## 1、先上代码

本次机器人功能，来自第三方库：``porobot``，下载命令如下：

```python
pip install porobot
```

下载完成后，只需要1行命令就可以聊天啦~

```python
import porobot

print(porobot.normal.chat("你好，我是程序员晚枫"))
```
运行上面几行代码的结果，如下图所示。👇

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/porobot/chat/chat.png?q-sign-algorithm=sha1&q-ak=AKIDKTiu1xTCXhUh_X1XYxP_nxRorqICJ3I908Rnq5up3L83P-Rp15K1tKQkvpwfyqeN&q-sign-time=1688132789;1688136389&q-key-time=1688132789;1688136389&q-header-list=host&q-url-param-list=ci-process&q-signature=92a518ec8d03e52902b231455ecbc467a65261c6&x-cos-security-token=CGcfrvPEyFcFuNlAwH6HiKRxfwFYu6ca3f6ad089337f2a284fdb2179fd41ccf439O0ObyjMjlprA4jUCJZPMnkWLiPJCO2nWB_drUGDWhCNlnMoDRp5o-RJr-FxAnUqnKRZMmky9M9B4G292nWfcTXE1GotjBCJT6_aBCeitf0N6vwL-joxigTi4tezujytY-O9vPBgtVQMFXTPOuCraNC-gvRg3baMavcaAf-Kv69oXIqnk9UXWs4g8nHK9u-&ci-process=originImage)

## 2、开源仓库

本次使用的第三方库来自开源项目：``python-office``，其下含有日常办公、学习、生活常用的数十个不同功能的仓库。例如：

- poword：一个处理word的自动化办公仓库。
- pohan：一个神奇的汉语编程库。
- poocr：一个通用型的文字识别库，可以识别发票、车牌、身份证等。
- pofinance：一个用来摸鱼炒股的工具包。
- poppt：一个免费操作ppt的库，例如：可以把ppt转化为一张图片。
- 全部功能的介绍，详见官网：www.python-office.com

## 3、参与开发

开源项目离不开大家的支持，尤其是离不开大家对代码的共同开发和维护。

如果你开发了新的功能代码或者发现了代码中存在的Bug，请通过issue或者pr的形式，直接提交到以下项目的代码仓库里：

- 💻GitHub：https://github.com/CoderWanFeng/python-office
- 国内用户，可以使用Gitee：https://gitee.com/CoderWanFeng/python-office/

----

对本文内容有任何疑问或者觉得本文有帮助，请在评论区告诉我吧~




---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)
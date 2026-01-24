---
title: 二维码绑定商品信息，实现动态更新
date: 2024-01-24 12:22:05
tags: 1v1
---

以下是今晚的沟通总结，本链接永久有效，并且下次课程也会更新在这里面，请收藏关注。


## 需求

今晚沟通的需求也很清晰明了：

> 电商行业，想通过二维码实现商品信息的动态展示，其中必备信息有：二维码被扫码的次数、商品图片、商品名称。

交付给厂家一个二维码，厂家就可以进行印刷了。

目前技术水平为零基础，曾经接触过C语言。

## 实现方案

Linux（服务器） + mongdb（数据库） + django（后端接口）


整体流程如下：

**用django编写接口代码，动态更新存放在数据库里的数据，最后将代码和数据库，一起存放在云服务器里。**

最后数据库可以直接导出Excel表格。


##　学习资料

最快明晚，更新本部分内容。

以下是相关的学习资料，点击链接直达，👇

### 第一步，学习Linux，只需要学习下面这一套课程


1. [Linux实战技能100讲](http://gk.link/a/111MW)

服务器的购买链接：[点我直达](https://curl.qcloud.com/3csDz9jU)

### 第二步，学习数据库

这里先学习数据库基础，再学习专用数据库：MongDB，

其中MySQL是基础，MongDB不用专门学习。

2. [MySQL 必知必会](http://gk.link/a/110o3)，这个课程，是数据库的基础。

### 第三步，学习Python，用来开发接口
首先学习Python基础，这一步不能跳过，不然看不懂Django的课程。

3. [从 0 到 1，快速上手 Python](https://mp.weixin.qq.com/s/Rn0_Tyu9uVP_NRO3LkhJoQ)，学习django搭建接口之前，建议熟练掌握Python。
4. [Django快速开发实战：从开发到部署，掌握项目开发全流程](https://www.bilibili.com/video/BV1zi4y1t7YU)

## 联系我

在学习和开发过程中，有任何问题，都可以联系我的微信，👇

![](https://cos.python-office.com/wechat/qr-code.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg)
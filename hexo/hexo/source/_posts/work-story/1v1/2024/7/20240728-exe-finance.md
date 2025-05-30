---
title: 开发一个自己的盯盘软件？
date: 2024-07-28 18:14:24
tags: 1对1
---

今天的沟通和A股有关，正好我最近也在研究股票、量化的开发，所以就深入的聊了聊。

## 需求

写一个自己的A股数据分析系统，实现数据的存储、筛选、分析，未来可能会增加功能。

有一定的计算机基础，会C语言，对网络编程不熟悉。

经过沟通，主要分为2个业务模块：
1. 业务模块1：利用api接口（付费的）定时获取数据，存储到数据库中；
2. 业务模块2：有一个网站展示数据，并且可以自定义一些筛选条件，包含增加备注的功能。

## 学习计划和细节

针对以上业务实现，主要需要学习3个方面的知识：接口请求、数据库、网站开发。


这3个方面的重点需要关注的细节有：

1. 接口请求：是用哪种请求方式，最好是https接口；接口的QPS有多高？最好是5以上。
2. 数据库：重点学一下如何设计数据表；
3. 网站开发：如何搭建一个网站，如何根据功能划分不同的页面。

## 学习资料

上面3个学习步骤，分别对应的学习资料如下：

> 尽量按顺序学习。


1. 接口请求：[Python爬虫从入门到高级实战](https://www.bilibili.com/video/BV1y54y1y74F)。这套课听懂就可以，不需要全部跟着做。
2. 数据库：[MySQL数据库入门到大牛](https://www.bilibili.com/video/BV1iq4y1u7vj/?spm_id_from=333.337.search-card.all.click&vd_source=ca20bb8763fcb18660aa74d7a87234fa)，这套课不用学习安装，其余都要学。
3. 网站开发：[从开发到部署，掌握项目开发全流程](https://www.bilibili.com/video/BV1zi4y1t7YU)。这套课全部都跟着做一遍，哪里不懂就直接问。

## 答疑

- 有没有现成的软件可以用？
- 文华T8，QMT，Ptrade，广发操盘手，这几个都可以看看。


接下来的学习过程中，有问题请随时联系我，👇

![](https://cos.python-office.com/wechat/qr-code.jpg)
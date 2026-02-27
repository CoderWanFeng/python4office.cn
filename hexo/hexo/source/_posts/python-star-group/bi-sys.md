---
title: 用Python制作一个大屏数据可视化系统
date: 2022-08-16 16:13:12
tags:
---


![](https://www.python-office.com/api/img-cdn/wanfeng/python-star-group/bi-course/cover.jpg)

大家好，这里是Python程序员晚枫。

之前给大家分享过一个视频👇
![](https://www.python-office.com/api/img-cdn/wanfeng/python-star-group/bi-course/3-min.jpg)

今天收到了[知识星球：Python读者圈](http://www.python4office.cn/wechat-group/)里的提问：晚枫，如何使用Python开发这样一个大屏数据可视化系统？完整的技术方案是什么？

于是我就写了一篇文章，给他详细讲了一下实现方案 + 学习计划 + 推荐资料。

今天我就给大家分享一下我们沟通时使用的素材：开发这个系统的学习路径，小白也能看懂。

如果实在看不懂，没关系，+我微信，我1对1给你讲明白：[python-office](http://www.python4office.cn/wechat-qrcode/)

我也写了一个全套系统的简单demo，拿走即用，后台回复：**大屏数据**，24小时即可自动获取视频教程~

## 1、实现思路

实现这个系统，主要需要**4个部分：页面、接口、数据、部署**。

用大白话说就是：

- 页面：这个炫酷的``数据可视化``页面，你需要自己写出来。当然了，网上有很多模板。
- 接口：页面上动态地显示变化的数据，这个数据从哪里来？需要一个``提供数据``的地方，也就是接口。
- 数据：接口的作用的是传输 - 把数据传输给页面，``从哪里取出数据``呢？一般是数据库里。
- 部署：上面这3个部分写完了，怎么给别人看？放在自己的电脑上，别人看不到吧？所以需要一个``安装这些代码的地方``，这就叫做部署。

下面我们分别来看一下，分别使用到的技术，以及它们的学习教程。

## 2、技术选型


根据以上4个部分的实现思路，可以选择的技术，如下图所示。
![](https://www.python-office.com/api/img-cdn/wanfeng/python-star-group/bi-course/system-1.png)

**技术选型和配套教程：**

- 页面：
  - 有代码基础的同学 or 企业级开发中：Vue + Echarts
    - Vue教程：``http://gk.link/a/11973``
    - Echarts教程：``https://www.bilibili.com/video/BV19z4y167Tb``
    
  - 0基础基础的同学 or 爱好者学习：基础前端 + Echarts
    - 基础前端教程：``https://mp.weixin.qq.com/s/9jflDQOhOZpD1z5gXUZCLQ``
  
- 接口：
  - 企业级开发：Django，``https://mp.weixin.qq.com/s/2BPiuy_gRA4j6CTWG7jVtQ``
  - 0基础 or Demo开发：Flask，``https://mp.weixin.qq.com/s/5sf9rb4BPVBcLK2vg2psxg``
- 数据：
  - 必学：SQL alchemy
  - MySQL：``http://gk.link/a/110o3``
- 部署：
  - Linux：``http://gk.link/a/11yJA``

## 3、学习时长

以上技术看起来很多，但其实每种都有快速的学习方法，如果你只需要一些简单的数据展示，全程自己操作3-5周也许就够了。

但具体需要多少时间，或者有没有必要你自己来搭建，你可以和我沟通一下。**这也是我建立知识星球，提供答疑服务的价值。**

> 当你需要学习Python时，网上有大量的免费资料，但是按照什么计划学习？使用哪些资料？如何系统掌握？这些问题的答案，可能就需要一位有经验的程序员给你答复了。

我自己是自学了2年，转行成为Python程序员的。所以0基础如何快速、系统的学习Python，我能给你提供有针对性的帮助，我的微信：[python-office](http://www.python4office.cn/wechat-qrcode/)

----
#### 更多阅读
- [用Python自动生成 图文并茂的数据分析 报告](https://mp.weixin.qq.com/s/STSRuN9Q9NpETKdYQBmxqQ)
- [揭秘！Excel还是Python？自动化办公软件，应该学哪一个？](https://mp.weixin.qq.com/s/rMsMpSdQHqS3Q9eSsA0VeA)
- [开源中国推荐：python-office自动化办公，每个功能只需一行代码，做到了真正的开箱即用。](https://mp.weixin.qq.com/s/d2m7xYCLXF8QUlr-5sSuPA)




## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。
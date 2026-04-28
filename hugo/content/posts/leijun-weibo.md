---
title: "用Python爬了雷军的微博，我发现了什么？网友：不OK，绝对不OK！"
date: "2022-10-31T01:28:00+08:00"
tags:
---



<!-- more -->
![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BE%AE%E5%8D%9A%E7%88%AC%E8%99%AB%2Fweibo.jpg)
大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)，今天给大家分享一个爬取微博的项目。


## 使用的框架
只用了一个框架：Scrapy

教程：https://www.bilibili.com/video/BV1LV411m7Ym

## 实现的功能

- 用户信息采集
```
cd weibospider
python run_spider.py user
```

- 用户粉丝列表采集
```
python run_spider.py fan
```
- 用户关注列表采集
```
python run_spider.py follow
```
- 用户的微博采集
```
python run_spider.py tweet
```
- 微博评论采集
```
python run_spider.py comment
```
- 微博转发采集
```
python run_spider.py repost
```
- 基于关键词的微博检索
```
python run_spider.py search
```

## 注意事项

运行之前，改一下自己的cookie。

---

<p align="center" id='1w副业-banner'>
    <a target="_blank" href='http://t.cn/A6KiaiqK'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2F1w-pro.jpg" width="100%"/>
    </a>   
</p>

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)


程序员晚枫专注AI编程培训，小白看完他和图灵社区合作的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)就能上手做AI项目。


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


---
title: 近期项目知识点整理
date: 2022-01-26 10:41:49
tags:
---



## Redis

#### 数据类型

Redis支持五种数据类型：

| 类型                       | 特点                                                         | 命令                       | 场景                                                         |
| -------------------------- | ------------------------------------------------------------ | -------------------------- | ------------------------------------------------------------ |
| string（字符串）           | 最基本的类型<br>二进制安全，可以包含任何数据<br/>最大能存储512MB | set<br/>get                |                                                              |
| hash（哈希）               | 适合于存储对象                                               | hset<br/>hmset             | 存储、读取、修改用户属性                                     |
| list（列表）               | 双向链表                                                     | lpush<br/>                 | 1,最新消息排行等功能(比如朋友圈的时间线) <br/>2,消息队列     |
| set（集合）                | 无序、不重复                                                 | sadd<br/>sinter：交集<br/> | 1、共同好友 <br/>2、利用唯一性,统计访问网站的所有独立ip<br/> 3、好友推荐时,根据tag求交集,大于某个阈值就可以推荐 |
| zset(sorted set：有序集合) | 有序，不重复<br/>每个元素对应一个double类型的分数，分数可以重复 | zadd<br/>zincrby           | 1、排行榜<br/> 2、带权重的消息队列                           |



#### 参考链接

- [Redis 数据类型 | 菜鸟教程 (runoob.com)](https://www.runoob.com/redis/redis-data-types.html)
- [redis常用命令大全 - chenxiangxiang - 博客园 (cnblogs.com)](https://www.cnblogs.com/cxxjohnson/p/9072383.html)



## Supervisor

#### 参考链接

- [Supervisor使用详解](http://www.python4office.cn/supervisor-config/)



## Celery

### 协程和异步

#### 原理和实现

不是计算机提供的，是人为创造的，通过一个线程实现代码块之间的切换执行。

```python
#实现协程的几种方式
greenlet
yield
asyncio - 3.4：遇到io阻塞会自动切换
async&await关键字：3.5
```

#### 协程的意义

基于协程实现的编程，叫做异步编程。



#### 阻塞

进程运行的三个状态：运行、就绪、阻塞

阻塞：程序运行时，遇到了IO，程序挂起，CPU被切走

非阻塞：程序没有遇到IO；或者程序遇到IO，但是我通过某种手段，让CPU强行运行我的程序。



#### 参考链接

- [任务调度利器：Celery - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/article/903701468278784)
- [ByYuan celery从语法到案例精讲课程_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV19S4y1j7iv?p=1)

## 装饰器

#### python中@classmethod @staticmethod区别

- @staticmethod 不需要访问和类相关的属性或数据(感觉只是概念上的区别，你这样声明了用的人就知道了，如果你非要在这个方法中访问test.xxx 它就和@classmethod的作用一样了。）
- @classmethod 可以访问和类相关（不和实例相关)的属性，

## APScheduler

APScheduler是基于Quartz的一个Python定时任务框架。提供了基于日期、固定时间间隔以及crontab类型的任务，并且可以持久化任务。在线文档：https://apscheduler.readthedocs.io/en/latest/userguide.html

#### 参看链接

- [花10分钟让你彻底学会Python定时任务框架apscheduler_somezz的专栏-CSDN博客_apscheduler](https://blog.csdn.net/somezz/article/details/83104368)
- [Python定时任务框架APScheduler_架构师专栏-CSDN博客_python定时任务框架](https://blog.csdn.net/chosen0ne/article/details/7842421?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-1.pc_relevant_paycolumn_v3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-1.pc_relevant_paycolumn_v3&utm_relevant_index=2)

## Flask

#### 请求钩子
中间层
#### 上下文
> https://www.bilibili.com/video/BV1L64y1C7ce?p=5
- 请求上下文
    - request
    - session
- 应用上下文
    - current_app
        - 伴随request产生和消灭
    - g对象
        - 在方法之间传递参数
        - 本次请求之内有效
- 上下文实现的原理
    - Threadlocal：线程局部变量

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)就能上手做AI项目。
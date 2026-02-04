---
title: Python定时库APScheduler原理及用法
date: 2022-02-09 10:16:17
tags: APScheduler
---

<p align="center" id='支付宝-banner'>
    <a target="_blank" href='http://www.python4office.cn/fuli/zhifubao-0923/'>
    <img src="https://ads-1300615378.cos.ap-guangzhou.myqcloud.com/alipay/hong-3.jpg" width="100%"/>
    </a>   
</p>


<p align="center" id='外卖-banner'>
    <a target="_blank" href='https://kzurl19.cn/7CAHjq'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2F%E5%A4%96%E5%8D%96-1040-100.jpg" width="100%"/>
    </a>   
</p>

## 1. APScheduler简介

APscheduler全称Advanced Python Scheduler

作用为在指定的时间规则执行指定的任务，指定的任务就是一个Python函数。

## 2. APScheduler组件

核心组件有4个：Job、JobStore、Trigger、Executor
除了以下组件，还有Event 事件、 Listener 监听事件、 Scheduler 调度器

但需要自己操作的，只有
- Job：也就是自定义的函数
- JobStore：存储任务的方式，默认是存在内存，可以选择存储在数据库里，例如：redis

###  Job 作业

**作用**

Job作为APScheduler最小执行单位。
创建Job时指定执行的函数，函数中所需参数，Job执行时的一些设置信息。


**构建说明**

```text
id：指定作业的唯一ID

name：指定作业的名字

trigger：apscheduler定义的触发器，用于确定Job的执行时间，根据设置的trigger规则，计算得到下次执行此job的
时间， 满足时将会执行

executor：apscheduler定义的执行器，job创建时设置执行器的名字，根据字符串你名字到scheduler获取到执行此
job的 执行器，执行job指定的函数

max_instances：执行此job的最大实例数，executor执行job时，根据job的id来计算执行次数，根据设置的最大实例数
来确定是否可执行

next_run_time：Job下次的执行时间，创建Job时可以指定一个时间[datetime],不指定的话则默认根据trigger获取触
发时间

misfire_grace_time：Job的延迟执行时间，例如Job的计划执行时间是21:00:00，但因服务重启或其他原因导致
21:00:31才执行，如果设置此key为40,则该job会继续执行，否则将会丢弃此job

coalesce：Job是否合并执行，是一个bool值。例如scheduler停止20s后重启启动，而job的触发器设置为5s执行
一次，因此此job错过了4个执行时间，如果设置为是，则会合并到一次执行，否则会逐个执行

func：Job执行的函数

args：Job执行函数需要的位置参数

kwargs：Job执行函数需要的关键字参数
```


### Jobstore 作业存储


Jobstore在scheduler中初始化，另外也可通过scheduler的add_jobstore动态添加Jobstore。每个jobstore
都会绑定一个alias，scheduler在Add Job时，根据指定的jobstore在scheduler中找到相应的jobstore，并
将job添加到jobstore中。

Jobstore主要是通过pickle库的loads和dumps【实现核心是通过python的__getstate__和__setstate__重写
实现】，每次变更时将Job动态保存到存储中，使用时再动态的加载出来，作为存储的可以是redis，也可以
是数据库【通过sqlarchemy这个库集成多种数据库】，也可以是mongodb等


目前APScheduler支持的Jobstore：

```text
MemoryJobStore
MongoDBJobStore
RedisJobStore
RethinkDBJobStore
SQLAlchemyJobStore
ZooKeeperJobStore
```


###  Trigger 触发器


Trigger绑定到Job，在scheduler调度筛选Job时，根据触发器的规则计算出Job的触发时间，然后与当前时间比较
确定此Job是否会被执行，总之就是根据trigger规则计算出下一个执行时间。

Trigger有多种种类，指定时间的DateTrigger，指定间隔时间的IntervalTrigger，像Linux的crontab
一样的CronTrigger


目前APScheduler支持的触发器：

```text
DateTrigger
IntervalTrigger
CronTrigger
```

###  Executor 执行器


Executor在scheduler中初始化，另外也可通过scheduler的add_executor动态添加Executor。 
每个executor都会绑定一个alias，这个作为唯一标识绑定到Job，在实际执行时会根据Job绑定的executor
找到实际的执行器对象，然后根据执行器对象执行Job

Executor的种类会根据不同的调度来选择，如果选择AsyncIO作为调度的库，那么选择AsyncIOExecutor，如果
选择tornado作为调度的库，选择TornadoExecutor，如果选择启动进程作为调度，
选择ThreadPoolExecutor或者ProcessPoolExecutor都可以

Executor的选择需要根据实际的scheduler来选择不同的执行器


目前APScheduler支持的Executor：

```text
AsyncIOExecutor
GeventExecutor
ThreadPoolExecutor
ProcessPoolExecutor
TornadoExecutor
TwistedExecutor
```

## 3. Scheduler工作流程图
![](/images/apscheduler-study/add-job.jpg)

## 4.代码演示
```python
# -*- coding: utf-8 -*-
# File Name: interval.py

from datetime import datetime
import os

from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    REDIS = {
        'host': '127.0.0.1',
        'port': '6379',
        'db': 14,
        'password': 'Hx$hfcmsrx3'
    }
    SCHEDULER_JOBSTORES = {
        'redis': RedisJobStore(**REDIS)
    }
    scheduler = BlockingScheduler(jobstores=SCHEDULER_JOBSTORES)
    scheduler.add_job(tick, 'interval', jobstore='redis', seconds=5)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

```
## 5. 参考链接

[Python定时库APScheduler原理及用法 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/95563033)


---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)就能上手做AI项目。
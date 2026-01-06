---
title: time-datetime
date: 2022-08-05 13:55:03
tags:
---
![](https://www.python-office.com/api/img-cdn/pro-python/time-datetime/cover.jpg)

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。Python学习服务：[点我查看](http://www.python4office.cn/wechat-group/)

在Python中，表示时间的格式一共有3种：时间戳、结构化时间、格式化时间，2个模块：time、datetime。

今天我们来一起看一下。

## 一、3种时间格式，4种生成方式

### 1、时间戳 - 记录时间

时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。

```python
import time

time.time() # 时间戳
# 输出：1659682465.1875775
```
这种方式得到的时间，一般用来数据库存储，非常节省存储空间。

### 2、结构化的时间 - 使用时间


所谓结构化时间，你可以理解成把时间进行了分类，分为了：年月日时分秒，你想用哪个类别，就可以直接取出哪个类别。
如果我们想取出一个时间片段，用这个方法就很简单了，例如：取出当前时间的分钟数。

```python
import time

time.localtime().tm_min # 结构化时间
# 输出：30
```



### 3、格式化的时间 - 展示时间

这个方法，用来给用户展示时间。

```python
import time

time.strftime('%Y-%m-%d %H-%M-%S %A')# 格式化时间
# 输出：'2022-08-04 19-08-35 Friday'

import datetime

datetime.datetime.now()#格式化时间
# 输出：datetime.datetime(2022, 8, 4, 19, 9, 0, 328515)
```


## 二、2个模块：time，为什么有datetime模块？

在前面生成时间的代码中，我们使用了2个模块：time和datetime，好像它们之间的功能也是重复的。

既然有了time模块，为什么还要有datetime？那是为了简化time的使用。

datatime模块重新封装了time模块，提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo。

### 应用场景
在之前的文章中我们讲过：[万字总结！Python 实现定时任务的八种方案](https://mp.weixin.qq.com/s/jWWQyWr6Y3PnFJ2slcK2Xw)

在定时任务中，我想设置一个一周后提醒我的功能。

如果用time模块进行实现
```python
import time

time.time() + 7*24*60*60 # 7天*24小时*60分钟*60秒
```
需要自己计算出7天后的时间戳，而如果使用datetime模块，这件事就很简单了：直接``days + 7``，如下图代码所示。
```python
import datetime

datetime.datetime.now() + datetime.timedelta(days=7)#格式化时间
```


## 三、互相之间的转换

![](https://www.python-office.com/api/img-cdn/pro-python/time-datetime/convert.jpg)

时间戳和结构化数据、字符串数据之间，可以进行转换。这一点的注意事项见上图，这里不再赘述，如有疑问，可以添加我的微信，进行更加详细的沟通👉[python-office](http://www.python4office.cn/wechat-qrcode/)

#### 参考资料
1. [万字总结！Python 实现定时任务的八种方案](https://mp.weixin.qq.com/s/jWWQyWr6Y3PnFJ2slcK2Xw)
2. [1.7w 字总结！Python 如何处理日期与时间？](https://mp.weixin.qq.com/s/8vLnORTr8oMU9rMMf3hzLw)
3. https://www.bilibili.com/video/BV1pT4y1k7FH
-----


<p align="center" id='1w副业-banner'>
    <a target="_blank" href='http://t.cn/A6KiaiqK'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2F1w-pro.jpg" width="100%"/>
    </a>   
</p>

---
title: 原创！10分钟入门Python + Excel自动化办公（pandas版）
date: 2024-12-10 18:32:08
tags: [自动化办公,Excel,pandas]
---

大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)，之前在B站账号：**Python自动化办公社区**发布了一套关于**Excel + Python实现自动化办公**的教程，目前已经有40w+的播放了。

- [给小白的《30讲 · Python数据分析》：https://mp.weixin.qq.com/s/p6MTu8512uzbM2_9vQFWPA](https://mp.weixin.qq.com/s/p6MTu8512uzbM2_9vQFWPA)


其中主要使用的Python第三方库是**pandas**，今天就以pandas为核心内容，给大家分享一下精简版的10分钟入门教程。


我根据pandas的官方文档做了以下修改：

- 改为中文，官网是英文版，这个不用多解释了。
- 把技术上的专用名词改为通俗易懂的日常词汇，因为关注我的朋友有一部分不是程序员。
- 增加了pandas + excel应用的案例，官网文档主要是编程角度的介绍。

因本人能力有限，如果有错误的地方，欢迎大家评论区 或者 加入[读者群](https://mp.weixin.qq.com/s/wx-JkgOUoJhb-7ZESxl93w)交流。

## 0、写在前面


### pandas和Excel的对比

为了方便大家理解，我先用Excel里有的概念，来解释一下pandas里的基本数据类型。如下图所示：

| pandas      | Excel              |
| ----------- | ------------------ |
| `DataFrame` | worksheet          |
| `Series`    | 一列数据（含列名） |
| `Index`     | 行号               |
| row         | 列                 |
| `NaN`       | 空单元格           |




### 演示数据

本文使用的演示Excel中的文件名：``程序员晚枫的账号.xlsx``，存放在我本地的D盘下``work``文件夹里，里面只有一个sheet，如下图所示，大家可以自己在电脑上创建一个。

> 文件的位置：``D:\work\程序员晚枫的账号.xlsx``

|     | platform（平台） | name（账号名）       | fans（粉丝数） | remark（备注） |
| --- | ---------------- | -------------------- | -------------- | -------------- |
| 0   | B站              | Python自动化办公社区 | 140000         | 课程           |
| 1   | 抖音             | 程序员晚枫           | 6000           | vlog           |
| 2   | 公众号           | Python自动化办公社区 | 100000         | 文章           |
| 3   | 小红书           | 程序员晚枫           | 8000           | 工具           |
| 4   | 小红书           | Python自动化办公社区 | 10000          |                |


### 必备软件

Python和PyCharm的安装、第三方库的安装，我就不再每个教程都重复了，大家跟着下面的3个视频顺序安装即可：

- 第1讲：Python的下载、安装和卸载：[``https://www.python-office.com/course/docs/50-01-python.html``](https://www.python-office.com/course/docs/50-01-python.html)
- 第2讲：正版PyCharm的下载和使用教程，还有中文插件哦~：[``https://www.python-office.com/course/docs/50-02-pycharm.html``](https://www.python-office.com/course/docs/50-02-pycharm.html)
- 第3讲：pip的下载、安装和使用：[``https://www.python-office.com/course/docs/50-03-pip.html``](https://www.python-office.com/course/docs/50-03-pip.html)

## 1、读取Excel

首先，把Excel读进Python代码里。

```python

import pandas as pd
platform_df = pd.read_excel('D:\\work\\程序员晚枫的账号.xlsx',sheet_name='sheet1')#和下面这句代码等效
platform_df = pd.read_excel('D:\\work\\程序员晚枫的账号.xlsx',sheet_name=0)
print(platform_df) #查看读取的Excel内容
```

## 2、查看数据

### 查看头/尾数据

```python
print(platform_df.head(3)) #查看前5行数据
print(platform_df.tail(3))  #查看后5行数据
```

### 查看索引、列名和值

```python
print(platform_df.index)    #查看索引
print(platform_df.columns)  #查看列名

```

### 查看某一列的数据分析

查看粉丝数这一列的基本统计信息，包括计数、平均值、标准差、最小值、最大值以及25%、50%、75%分位数。


```python

print(platform_df.fans.describe())

```

## 3、排序

根据某一列的值进行排序，默认是升序。
```python
print(platform_df.sort_values('fans'))
```

如果想降序排列，可以使用``ascending=False``参数。

根据行索引进行排序，代码如下：
```python
print(platform_df.sort_index(ascending=False))
```

## 4、筛选数据

### 筛选出粉丝数大于10w的账号

```python
print(platform_df[platform_df.fans > 100000])
```
### 筛选出备注为空的账号
```python
print(platform_df[platform_df.remark.isna()])
```
## 5、新增一列

```python
platform_df['new'] = 100
print(platform_df)
```


## 6、删除一列
```python
platform_df.drop('new',axis=1,inplace=True) #axis=1表示删除列，inplace=True表示直接在原数据上修改
print(platform_df)
```


## 7、保存数据
```python
platform_df.to_excel('D:\\work\\程序员晚枫的账号.xlsx',sheet_name='sheet1',index=False) #index=False表示不保存索引
```



## 8、参考文档


- [10 minutes to pandas：https://pandas.pydata.org/docs/user_guide/10min.html](https://pandas.pydata.org/docs/user_guide/10min.html)
- [给小白的《30讲 · Python数据分析》：https://mp.weixin.qq.com/s/p6MTu8512uzbM2_9vQFWPA](https://mp.weixin.qq.com/s/p6MTu8512uzbM2_9vQFWPA)


![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')




## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。
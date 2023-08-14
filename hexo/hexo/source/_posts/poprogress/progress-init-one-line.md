---
title: 给程序加个进度条吧！1行Python代码，快速搞定~
date: 2023-03-23 22:11:12
tags: 开源
---



![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/progress/1/cover.jpg)


大家好，这里是程序员晚枫。

你在写代码的过程中，有没有遇到过以下问题？

- 已经写好的程序，想看看程序执行的进度？

- 在写代码批量处理文件的时候，如何显示现在处理到第几个文件了？

👆如上图所示的进度条是一个最好的解决方法，怎么在不修改原来代码的情况下，快速给程序加一个进度条呢？

今天我们来学习一个最简单的方法~

## 1、先上代码

下载进度条的第三方库。

```python
pip install poprogress
```

使用这个库，快速制作进度条

```python
from poprogress import simple_progress

a_list = [1, 2, 3, 4, 5, 6, 7, 8]*100000000

for a in simple_progress(a_list。desc='这个参数是进度条的说明，可以不填'):
    pass
```

效果如下👇。

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/progress/1/Snipaste_2023-03-23_20-29-28.jpg)

## 2、使用说明

细心的你一定发现，这个进度条代码，对我们平时写的代码没有伤害。

平时我们可能会直接循环``list``，而进度条是把这个``list``用``simple_progress()``包起来，在进行循环。

```python
# 平时的代码：
for i in list:
  pass
  
# 加了进度条的代码
for i in simple_progress(list):
  pass
```

所以如果你已经写好的代码，想加上一个进度条，也直接把``for``循环后面的内容，直接用``simple_progress()``包起来就行了~程序员不需要做任何改变。

是不是非常简单？

## 3、实现原理

想进一步了解的同学，可以看一下源码，研究一下它的实现原理：

- ⭐GitHub：https://github.com/CoderWanFeng/poprogress

---

---
title: 如何生成1亿个手机号码？Python生成随机数的22种方法
date: 2022-07-01 13:11:25
tags:
---
![](https://www.python-office.com/api/img-cdn/pro-python/random.py/covage-water.jpg)
大家好，这里是Python程序员晚枫。

最近在网上看到一个python的面试题目：**如何用Python生成1亿个手机号码？**

我第一眼看到的时候心想，这个还不简单？直接``random.randint(1,999999999999)``就完事了。

但是马上就发现了这其中的错误：这个是生成1-99999999之间的随机数，可能是1，也可能是666.

<!-- more -->

但电话号码是11位的，而且前3位只有指定的号段，比如135、136。直接``random.randint(1,999999999999)``这么做并不符合条件。

那么如何生成呢？于是有了下面这段代码：

```
import random
def create_phone_num(num):
    all_phone_nums = set()  # 存放生成的电话号码
    while True:  # 因为set会自动去重，因此死循环生成电话号码，直到等于num个号码停止
        start = random.choice(['135', '136', '137'])  # 存放前3位的号段，从中随机取一个
        end = ''.join(random.sample(string.digits, 8))  # 随机生成后面8位数字
        all_phone_nums.add(f'{start}{end}')  # 拼接前3位和后8位
        if len(all_phone_nums) >= num:  # 如果号码个数等于num，则停止
            break

phone_num(10000 * 10000)
```


经过这次写代码我才发现，原来Python的random里有那么多好用的生成随机数的方法。

**我把它们全部整理出来了，今天我们就来一起学习一下~**

如有遗漏或者错误，欢迎大家多多指点，我的个人微信👉[python-office](http://www.python4office.cn/wechat-qrcode/)

## 随机数是哪个文件生成的？

在上面的代码第一行：``import random``，我们导入了random这个标准库。之前分享过Python的标准库👉[超全！我把 Python 的 200个标准库整理出来了](https://mp.weixin.qq.com/s/aOi3cpidtajM9id15JEJvQ)

这个库只有一个文件：``random.py``，这个文件的结构主要分为``3个``部分（如下图所示），它们的作用分别是：
- 2个主要的类：``Random(_random.Random)``和``SystemRandom(Random)``
    - 其中我们使用最多的是``Random()``
- 有2个测试方法：``_test_generator(n, func, args)``和``_test(N=2000)``
    - 这一部分我们用不到
- 我们调用的函数：使用方法如上面代码的``random.choice``、``random.sample``，具体使用方法，我们接下来会详细解释。
![profile-water](https://www.python-office.com/api/img-cdn/pro-python/random.py/profile-water.jpg)

## random提供了哪些随机数方法？

接下来我们重点讲解作为python的用户，我们会使用到哪些``random``的随机数方法，也就是上文提到的``random.py``文件里的第3部分。

如下图的代码所示，random提供的方法有22个，主要分为2类：
- ``普通用户``常用的方法，一共有``12个``；
- ``科学计算``常用的方法，一共有``10个``。

![def-water](https://www.python-office.com/api/img-cdn/pro-python/random.py/def-water.jpg)

## 普通用户的12个随机数方法怎么用？
对于上面这22个随机数方法，我在这里重点介绍一下普通用户常用的那12个方法。

至于后面这个10个用于科学计算的方法，因为实在是高深，我就不在这里浪费时间了，有兴趣的同学，可以直接去翻一下数学书：《概率论》。

### 1. random.seed & random.getstate & random.setstate

把这3个放到一起说，是因为random本质上生成的是伪随机数，而这3个函数，很好的体现了伪随机数这个特性

> 代码示例:seed

```python
# 指定seed后，生成的随机数一样
random.seed(1)
print('随机数1：', random.random())
random.seed(1)
print('随机数2：', random.random())

# output：
# 随机数1： 0.13436424411240122
# 随机数2： 0.13436424411240122
```

> 代码示例: random.getstate & random.setstate

```python

import random

random.seed(42)

print(random.sample(range(20), k=10))

st = random.getstate()  # 取出生成上一行代码后，random的状态 

print(random.sample(range(20), k=20))  # print 20

random.setstate(st)  # 恢复上一次的随机状态

print(random.sample(range(20), k=10))  # print same first 10
# output：
# [12, 0, 4, 3, 11, 10, 19, 1, 5, 18]
# [4, 9, 0, 3, 10, 8, 16, 7, 18, 17, 14, 6, 2, 1, 5, 11, 15, 13, 19, 12]
# [4, 9, 0, 3, 10, 8, 16, 7, 18, 17]

```

### 2. random.random
随机生成一个[0,1)之间的浮点数
> 代码示例
```python
float = random.random()
"""
float = 0.123565654548978
"""
```

### 3. random.uniform
产生[a,b]范围内一个随机浮点数
> 代码示例
```python
float = random.uniform(11,15)
"""
float = 13.882923467738049
"""
```

### 4. random.randint
随机生成[a,b]范围内一个整数。
> 代码示例
```python
int = random.randint(1, 9)
"""
int = 2
"""
```

### 5. random.choice
从非空序列中随机选取一个数据并带回，该序列可以是list、tuple、str、set。
> 代码示例
```python
str = random.choice("程序员晚枫原创系列")
"""
str = 原
"""
```

### 6. random.choices
Python3.6版本新增。从集群中随机选取k次数据，返回一个列表，可以设置权重。一共有4个参数

- population：集群，必填。
- weights：相对权重。
- cum_weights：累加权重，不常用。不能和weights共用。
- k：选取次数。

> 代码示例
```python
str = ["程", "序", "员", "晚", "枫"]
res = random.choices(str, weights=[0, 0, 1, 0, 0], k=5)
"""
因为给【员】这个字，通过weights参数增加了特别的权重：1，而其他的权重都是0，所以不论随机选多少次，结果都是【员】
res = ['员', '员', '员', '员', '员']
"""
```

### 7. random.randrange(a,b,step)
参考range的用法：
- 不指定step，随机生成[a,b)范围内一个整数。
- 指定step，step作为步长会进一步限制[a,b)的范围，比如randrange(0,11,2)意即生成[0,11)范围内的随机偶数。
- 不指定a，则默认从0开始。
> 代码示例
```python
int = random.randrange(3, 9)
"""
int = 5
"""
```

### 8. random.sample
从集合中选取k个元素，返回一个列表，集群可以是list、tuple、str、set。
- 不会重复：可以理解为发一副扑克牌，确实是随机发，但是不会重复。
- 随机次数，不能超过集合的长度。发牌的时候，一副牌有54张，不可能随机抽取100次。

> 代码示例
```python
str = ["程", "序", "员", "晚", "枫"]
res = random.sample(str, 5)
"""
res = ['员', '序', '程', '枫', '晚']
"""
```

### 9. random.shuffle
打乱原来有顺序的集合，注意：这个方法没有返回值，它直接改变的是原集合的顺序。所以如果你想改变tuple这种不可变的集合，会报错。
> 代码示例
```python
str = ["程", "序", "员", "晚", "枫", "有", "顺", "序"]
random.shuffle(str)
"""
str = ['枫', '顺', '员', '序', '有', '晚', '序', '程']
"""
```

### 10. random.getrandbits
生成指定位数大小的整数。
> 代码示例
```python
int = random.getrandbits(8)
"""
int = 136
"""
```

## 写在最后
虽然自己是Python程序员，但是最近开发中却发现很多基础知识自己没掌握。

于是决定从这一篇开始，我决定带着当时加入Python时，喂马劈柴面朝大海的浪漫情怀，去认真的深入整理分享Python常用的知识点。

希望对你有用。

本系列其它文章还有：
- [1.7w 字总结！Python 如何处理日期与时间？](https://mp.weixin.qq.com/s/8vLnORTr8oMU9rMMf3hzLw)
- [万字总结！Python 实现定时任务的八种方案](https://mp.weixin.qq.com/s/jWWQyWr6Y3PnFJ2slcK2Xw)
- [精品！ 45个 GIT 经典操作场景](https://mp.weixin.qq.com/s/4_54glQ4akTB5MSHyFYwlg)
- [Anaconda介绍、安装及使用保姆级教程](https://mp.weixin.qq.com/s/gYRBE6JCRnHb1TUycGkTLg)

下一篇想看什么，加入读者群告诉我吧👉[Python交流群](http://www.python4office.cn/wechat-group/)


------
#### 参考资料：

1. https://www.136.la/jingpin/show-174885.html
2. https://blog.csdn.net/ckk727/article/details/99548223
3. https://www.e-learn.cn/topic/175983
4. https://www.jc2182.com/python/python-random-getrandbits-method.html

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
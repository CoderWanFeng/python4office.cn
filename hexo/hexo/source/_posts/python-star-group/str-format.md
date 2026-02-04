---
title: 终究还是错付了！这2种Python字符串格式化的写法已经被淘汰了，你是不是还在用？
date: 2022-08-16 15:54:09
tags:
---



![](https://www.python-office.com/api/img-cdn/wanfeng/python-star-group/format/cover.jpg)
大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，**知识星球：Python读者圈。**
![](https://www.python-office.com/api/img-cdn/wanfeng/python-star-group/format/qa.png)

今天我们来讨论一个问题：**python里是如何格式化字符串的？实际工作中使用的是哪一种？**

## 一、3种方式
- %格式化
  - 已淘汰
- format格式化（python2.6新增）
  - 不好用，处于淘汰的边缘。
- f-string格式化（python3.6新增）
  - **目前最常用**

>举个例子，现在需要打印：你好，我是”晚枫“。
以上3种用法的代码如下：

```python

# 1、%格式化
name = '晚枫'
sentence = '你好，我是%s' % (name)
# sentence = 你好，我是晚枫

# 2、format格式化（python2.6新增）
name = '晚枫'
sentence = '你好，我是{}'.format(name)
# sentence = 你好，我是晚枫

# 3、f-string格式化（python3.6新增）
name = '晚枫'
sentence = f'你好，我是{name}'
# sentence = 你好，我是晚枫

```

乍一看，看不出这几种方式的区别，接下来我们通过例子，详细看一下它们的优缺点。


## 二、为什么第3种最流行？

按照时间顺序，每一种新方式的推出，都是对上一种的改进。这3种表达方式，分别改进了上一种的什么不足呢？

原理层面的我们只说一种：每一种的代码运行速度，都比上一种的快。**如果想详细了解它们是如何提高性能的，欢迎留言讨论~**

这里我们主要说一下用法上的改进：

### %格式化
这种表达方式，当变量较多时，很容易混淆，假如我们想写一句：你好，我是``晚枫``，今年``18岁零48个月``，是个``程序员``，喜欢``点赞的人``。

> 使用这种方式，你将陷入百分号（%）的地狱，稍有不慎就会漏写一个，导致程序崩溃。
```
sname = '晚枫'
age = '18岁零48个月'
job = '程序员'
hobby = '点赞的人'
sentence = '你好，我是%s，今年%s，是个%s，喜欢%s。' % (name, age, job, hobby)
```
### format格式化
所以，为了改进上面的问题，python2.6新增了format方法。
同样的例子，使用format方法是下面这样的：
```
sname = '晚枫'
age = '18岁零48个月'
job = '程序员'
hobby = '点赞的人'
sentence = '你好，我是{}，今年{}，是个{}，喜欢{}。'.format(name, age, job, hobby)
# 你还可以这样写
sentence = '你好，我是{name}，今年{age}，是个{job}，喜欢{hobby}。'.format(name, age, job, hobby)
```
去掉了原有的%，取而代之的是{}，甚至还可以把变量名称写进—{}里面进行识别。

虽然比原来的%要清爽一些，但format后面还是要把一大串变量名称重复写一遍，是不是依然很麻烦？

### f-string格式化
于是，python3.6新增了目前最常用的这种格式化方法，直接上代码。
```
sname = '晚枫'
age = '18岁零48个月'
job = '程序员'
hobby = '点赞的人'
sentence = '你好，我是{}，今年{}，是个{}，喜欢{}。'.format(name, age, job, hobby)
# 你还可以这样写
sentence = f'你好，我是{name}，今年{age}，是个{job}，喜欢{hobby}。
```

发现了吗？你只需要在格式化的字符串前面加上一个小写字母：f，这段字符串就可以自动格式化了，既没有%的冗余，也没有format对变量名的重复书写。

## 3、写在最后

每次新的python版本开始研发之时，程序员都会高度关注新版本有哪些新特点。为什么？

>原因无它，python一直在进步，看着自己工作的工具变得越来越高级，生产效率越来越高，也是一种乐趣吧。

据说python3.11的速度将提高2倍，我是相当期待了：[Python 3.11 ，更快更高更强！](http://t.cn/A6S4KRXo)

---

#### 相关阅读
 - [终于把Python后端学习路线整理出来了，包含全套教程~](https://mp.weixin.qq.com/s/JqY0vFpBnG6CzDD1sB3nDw)
- [年轻人只想要退休，是多么悲哀的事](https://mp.weixin.qq.com/s/J3il8mIYyeKsh5GHepkLBA)






## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)就能上手做AI项目。
---
title: 我有一个复杂的Excel操作，想用Python实现，怎么做？
date: 2024-02-24 16:16:17
tags: 技术咨询
---


今天的1对1咨询（我的微信：[CoderWanFeng](https://mp.weixin.qq.com/s/8x7c9qiAneTsDJq9JnWLgA)）是一个关于Excel自动化办公的问题：**在一个文件夹中有若干个excel工作簿，每个工作簿里都有相同个数的工作表，这些工作表的格式都是肯定的。我需要把文件夹中的工作簿汇总成一个工作簿，工作薄中的不同的工作表，也对应汇总。**也想深入学一些Python技术。

说得简单点，可以理解成：如何把多个相同格式的Excel表格汇总到1个Excel表格里？

这是一个工作中常见的需求，如果不用Python也许只能一个一个表格手动打开，然后复制粘贴了。

但如果使用Python，就会有更简单的方法，今天我们一起来看一下实现思路，顺便看一下如果想更好的掌握Excel自动化办公，需要学习哪些有用的技术？

## 实现思路

> 基于今天咨询的朋友和看这篇文章的朋友，基本都不是为了转行程序员，而只是想提高办公效率，我这里就只说和这个案例有关的知识，没用的编程理论不说（有想了解的朋友可以评论区或者后台私信我）


### 第一步

首先看一下目前已有的代码，主要是2个：多个excel汇总到1个Excel的不同sheet里、多个Excel的同一个sheet汇总到1个Excel的同一个sheet里。


- 多个excel汇总到1个Excel的不同sheet里：这个代码的下载和使用，我们在之前的课程里讲解过的：点击查看这套课程的第22讲👉[《给小白的50讲Python自动化办公》](https://mp.weixin.qq.com/s/lOx4cAp9AllsCrhsUqVn8g)
- 多个Excel的同一个sheet汇总到1个Excel的同一个sheet里：这个代码，见下面的代码片段，完整的代码使用方法，可以添加我的微信沟通。👇

```python
# pip install python-office
office.excel.merge2sheet(dir_path)
```


### 第二步

关于汇总Excel表格的功能，目前python-office自动化办公这个代码库里，除了上面已有的代码，没有其它的了。

所以如果还想进一步开发完全匹配自己需求的功能，可以学习一下专门用来处理Excel表格的第三方库：pandas，我这里也推荐一套课程，👇

[Python自动化办公--Pandas玩转Excel（全30集）](https://www.bilibili.com/video/BV1hk4y1C73S/?spm_id_from=333.999.0.0&vd_source=ca20bb8763fcb18660aa74d7a87234fa)


学完这套课程，可以完全自己开发一个Excel自动化办公的代码了。


## 友情提醒

看完上面的实现思路，这里再补充2个友情提示：

- 用Python代码复制Excel里五颜六色的格式，也能做但是很麻烦，不建议小白尝试。
- 关于合并多个Excel、多个sheet的情况，我会排期开发。敬请期待更新：公众号-Python自动化办公社区。


-----

关于今天的文章，有任何疑问欢迎在评论区 or 交流群和我交流~

![](https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/0816.jpg)



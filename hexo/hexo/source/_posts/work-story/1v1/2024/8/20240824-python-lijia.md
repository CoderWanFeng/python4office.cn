---
title: 零基础学习Python-礼嘉1V1
date: 2024-08-24 00:24:04
tags: 1v1
---

这个文档是1v1学习的总结，每次沟通后更新，请收藏此链接：[点我查看](http://www.python4office.cn/work-story/1v1/2024/8/20240824-python-lijia/)。

# 第1讲（2024-08-24）

初次沟通，主要是从需求出发，全面了解Python的环境搭建和使用规范。

### 1、基本概念讲解

初学编程，很容易把编程语言（Python、Java、C++）和软件（微信、迅雷）混为一谈，所以首先要明确以下2点：
- 不同点：编程语言和软件是2个维度的东西，编程是写软件的技术。软件是用来解决具体问题的工具。
- 相同点：都是操作文档的系统。软件和编程，都是文档组成的。

这里有一个答疑：软件.exe和相关文件夹里文件的关系是什么？例如：D盘下的微信.exe所在文件夹，为什么还有其它文件？
> 因为微信.exe是软件的启动入口，而文件夹里的其它文件是软件功能的组成部分。


接下来是软件版本的问题，因为不同版本，安装的软件和软件的配置都不一样，所以需要先了解软件的版本。这里注意几点：
- 不建议使用最新版。因为最新版Bug比较多。
- 不同版本可以共存，但是安装和卸载需要注意一些细节，尤其是卸载的时候，注意环境变量的还原。
- Python和PyCharm的关系，就像中文和Word的关系，2个软件必须安装。
- Python全部版本都免费，PyCharm只有社区版免费。


### 2、软件下载和安装

在软件下载沟通过程中，还聊了一个高效学习/办公的技巧，是关于[搜索指令](https://baike.baidu.com/item/%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E%E9%AB%98%E7%BA%A7%E6%90%9C%E7%B4%A2%E6%8C%87%E4%BB%A4/3660259?fr=ge_ala)的，例如：查找正版软件时，可以搜索"腾讯会议 site:tencent.com"，可以精准的打开官网。

安装时有一些需要注意的细节，建议多卸载安装几次，熟练掌握。

- pip必须安装
- python安装时，选择**bin set in path**
- pycharm安装后，通过interpreter关联python

### 3、虚拟环境

虚拟环境对于Python来说是一个重要的概念，我一直把这个概念作为是否深入学习过Python or 是否写过实用项目的标志。

虚拟环境的重要意义是隔离不同的项目运行环境，虽然都是基于同一个Python版本，但是依赖的第三方库是独立的，互不影响。

虚拟环境在做项目的时候会使用到。


### 4、代码初体验

今天的代码一共写了2个，1个是纯Python代码、1个是用了第三方库(loguru)的。

```python

from loguru import logger as dog

a ,b= 7,7
c = 7
d = a + b + c
dog.info(d)
e = 8
f = d + e
dog.info(f)
h = 9
i = h + f
dog.info(i)

```

# 第2讲（2024-08-25）

今天的学习，主要是围绕Python语法，希望学习完之后可以理解别人写的代码。
主要内容如下：

## 变量
变量是为了存放数据，需要注意每个变量最本质的特征。例如，字符串必须有引号、列表必须有中括号。

### 类型

- 数字
  - int/float
    - a=8
    - b=4.5
- 字符串
  - name='bob'
  - car='benz'
- 列表
  - num_list=[1,2,3]
  - str_list=['a','b',6,[1,2,3]]
    - 中括号
    - 逗号分割
    - 任意类型
- 字典:kv数据
  - class_name = {'name':'bob','age':18}
```python
class_list = [{'name': 'bob', 'age': 18}, 
              {'name': 'alice', 'age': 18},
              {'name': 'eric', 'age': 18}]
for class_item in class_list:
    print(class_item['name'])
```
----
- 元组
- json

a = 5
b = 6


[这是一个公众号](https://mp.weixin.qq.com/)
## 函数
函数的存在，是为了复用代码。

```python
def add(a,b):
    return a+b
```
## 判断&循环

这一部分主要是表达思考逻辑用。

## 面向对象
（本次未学习）
## 处理报错
（本次未学习）

## 操作文件
（本次未学习）



## 参考资料


- [搜索指令](https://baike.baidu.com/item/%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E%E9%AB%98%E7%BA%A7%E6%90%9C%E7%B4%A2%E6%8C%87%E4%BB%A4/3660259?fr=ge_ala)
- [Python3.11的官方文档](https://docs.python.org/3.11/)


  - [Python培训：披着科技外衣的成功学课堂](https://www.bilibili.com/video/BV19X4y1K7TG/?vd_source=ca20bb8763fcb18660aa74d7a87234fa#reply713730985)
  - [学编程，搞副业？快逃！](https://www.bilibili.com/video/BV1wD4y117Zs/?spm_id_from=333.999.0.0&vd_source=ca20bb8763fcb18660aa74d7a87234fa)

- [50讲Python自动化办公](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)
- [30讲Python数据分析](https://mp.weixin.qq.com/s/p6MTu8512uzbM2_9vQFWPA/)
- [10天自学Python，轻松掌握Python基础（精华版）](https://www.bilibili.com/video/BV1MM4y1G76j/)

接下来的学习过程中，有问题请随时联系我，👇

![](https://cos.python-office.com/wechat/qr-code.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)就能上手做AI项目。
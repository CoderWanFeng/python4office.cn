---
title: spark + python安装教程
date: 2022-08-08 16:21:16
tags:  spark
cover: https://images.unsplash.com/photo-1655636044795-5cc862885966?q=80&w=1000&auto=format&fit=crop
---

<!-- more -->

![spark + python安装教程 - 配图1](https://images.pexels.com/photos/7237415/pexels-photo-7237415.jpeg?auto=compress&cs=tinysrgb&w=800)
![spark + python安装教程 - 配图2](https://images.unsplash.com/photo-161160569?w=800&h=400&fit=crop)

- 下载地址：
    - hadoop：https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/
    - spark：https://mirrors.tuna.tsinghua.edu.cn/apache/spark/
    - java:https://www.java.com/zh-CN/download/

- 测试代码
```python
# coding=UTF-8

import os

os.environ['JAVA_HOME'] = r'D:\software\spark\java8'  # 这个路径更换为你自己的java安装目录
import findspark

findspark.init()
from pyspark import SparkContext


def show(x):
    print(x)


sc = SparkContext("local", "First App")
lines = sc.textFile("./test/word.txt").cache()
words = lines.flatMap(lambda line: line.split(" "), True)
pairWords = words.map(lambda word: (word, 1), True)
result = pairWords.reduceByKey(lambda v1, v2: v1 + v2, 3)
result.foreach(lambda x: show(x))
# result.saveAsTextFile("./wc-result2")
```

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


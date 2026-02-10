---
title: spark + python安装教程
date: 2022-08-08 16:21:16
tags:  spark
---

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

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
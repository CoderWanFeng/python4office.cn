---
title: 如何用Python读取Excel文件
date: 2025-08-01 23:41:49
tags: [30讲PythonExcel数据分析]
---
[![9块读者交流群.png](https://raw.gitcode.com/user-images/assets/5027920/48edc8fa-6d2e-4eca-9e14-d71638eadb55/14块读者交流群.png '14块读者交流群.png')](https://mp.weixin.qq.com/s/84c9JDk3a1g9GbvRmO39uA)

大家好，我是楠少，用通俗易懂的方式，教小白学python。

**今天，我们开始学习《30讲Python+Excel数据分析》课程的第3讲。**

这一讲是介绍如何用Python代码读取excel表格的功能。

你们可以想象这样一个场景，就是面对一个有成千上万行的Excel文件，我们需要找到特定行和列的单元格内容，这个时候该怎么做效率最高呢？

**答案是，用Python代码来实现。**

所以，基于这个场景需求，我们团队就开发了用Python代码就能实现自动读取excel表格，然后对其进行操作的功能。

怎么样，是不是很好奇我们这个代码是如何写的呢？

别急，下面我们会给你娓娓道来。

## 01

虽然，我们这个功能的需求很好理解，就是实现自动读取excel表格并对其进行操作的功能，但是关键是我们如何用Python代码来实现。

好吧，这里就不给大家卖关子了，我们直接看代码吧。

代码演示：

```python
import pandas as pd


# 读取Excel文件的方式
# header=None表示Excel表格没有表头
example = pd.read_excel(r"C:\Users\zzqyy\Desktop\Pandas玩转Excel\02读取文件\example-no_header.xlsx",header=None)

# 这行代码表示给Excel表格加上两个表头，学号和姓名
example.columns = ["学号","姓名"]

# 这行代码表示设置学号的那一列为索引
example.set_index("学号",inplace=True)
print(example.columns)

# 这行代码表示将修改后的Excel文件存储到某个路径下
example.to_excel(r"C:\Users\zzqyy\Desktop\Pandas玩转Excel\02读取文件\输出.xlsx")
print("完成！")
```

好的，通过代码演示，我相信你一定已经学会了该如何使用我们这个脚本。

如果你还没有学会，那就照着我们的代码去手动敲一遍，感受一下敲代码的美妙，等你敲个几遍，相信你就一定能记住这几行代码了。

但是，这里我还是要提醒一下：

要想让这几行代码正常运行，你们需要把运行代码的环境给安装配置好。

不知道如何配置环境的可以看《30讲Python+Excel数据分析》的前面1讲内容，我们真的是手把手地教你如何配置环境的，相信我，一点都不难哈。

## 02

OK，到这里我要告诉大家的是，今天这篇文章教给大家的代码的视频讲解都在《30讲Python+Excel数据分析》这套课程的第3讲内容中了，对讲解视频感兴趣的可以去本套课程中学习一下。

这里不得不说的一点是，我们这个课程每一讲都是独立的案例场景讲解。

所以，你们完全可以根据自己的兴趣找到自己感兴趣的内容优先学习，这个不会影响学习效果的。

当然了，我们这门课程的每一节课都包含：视频、文档、代码、软件和答疑群。

所以你们完全不用担心学不会的问题，可以说，只要你认真跟着学习，认真练习敲代码，没有学不会的可能。

## 写在最后：

我们这套《30讲Python+Excel数据分析》课程具备以下2个特点：

第一，适合小白不需要学习复杂的编程知识，拿来就用。

第二，内容丰富，涵盖热门的数据分析的需求。

所以，如果你对这门[《30讲PythonExcel数据分析》](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502505&idx=1&sn=7552c4f09bc5f784e1528c67eb2deec5&scene=21#wechat_redirect)感兴趣，可以点击左边蓝字报名咨询。

![30讲python+excel数据分析海报跳转到付费文章.jpg](https://raw.gitcode.com/user-images/assets/5027920/3b0ef5f6-3839-4f74-b8ab-d244d81d36e7/30讲python_excel数据分析海报跳转到付费文章.jpg '30讲python+excel数据分析海报跳转到付费文章.jpg')

如果你对这门课程还有想了解的，或者购买后有问题，可以加我微信咨询，**nanshaoshixiong**，备注**888**。

![image.png](https://raw.gitcode.com/user-images/assets/5027920/f2a6dd47-3bdb-4b8b-b85b-2478ee4ae4f4/image.png 'image.png')

<center>
  
[Pandas创建excel，1行代码就行](https://mp.weixin.qq.com/s/fC20OOTekhFP3IFT5W_-nA)

<span style="color:#ff9900;">**---END---**</span>
  
<span style="color:#ffc266;">**丝滑一刻~**</span>

点赞、推荐这篇文章，凭点赞推荐截图可以免费领取一套价值99元的Python编程课程，具体请扫下方二维码加我微信，备注666领取。

![微信图片_20250801170859_87.jpg](https://raw.gitcode.com/user-images/assets/5027920/f0cba79d-bb5b-491c-9f2a-5420c9d99eb1/微信图片_20250801170859_87.jpg '微信图片_20250801170859_87.jpg')

点亮【<span style="color:#e60000;">赞</span>】和【<span style="color:#e60000;">推荐</span>】
  
祝你心想事成，发财被爱～

<center>


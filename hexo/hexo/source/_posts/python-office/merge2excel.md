---
title: 1行Python代码，合并100个Excel文件，原来这么方便？
date: 2022-06-30 09:39:51
tags:
---


![bar](https://img-blog.csdnimg.cn/c18ea794b3ae4d96bdafbc9c7268b474.jpeg#pic_center)
大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。

❤先说一个好消息，``python-office自动化办公``的官网上线了，点击直达👉[https://www.python-office.com](https://mp.weixin.qq.com/s/n9aq6QvkFq-FsheDQaIhFg)

今天开源项目[python-office](https://mp.weixin.qq.com/s/d2m7xYCLXF8QUlr-5sSuPA)发布了一个新功能:

> 1行代码，合并你指定的多个Excel文件。

本文给大家详细介绍一下~


## 需求说明

有一位老师，现在有全校1年级12个班级所有同学,``一共12个成绩单Excel文件``，现在老师想把它们合并到一个文件：``一年级.xlsx``里，每个班级作为一个单独的sheet存放。如图所示，

<!-- more -->

![结果图](https://img-blog.csdnimg.cn/img_convert/ce1e4818119ec895ffa9be108ab3e174.png)

> 这里大可放心，哪怕每个表的格式、内容不同，也完全可以无损合并。这里用班级成绩合并举例，只是为了大家更好的理解。



## 1行代码实现

下面我们用一行代码，实现上面这个功能。
#### 安装python-office这个库

```
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```


#### 1行代码
```
# 导入这个库：python-office，简写为office
import office

#1行代码，验证是否绑定成功
office.excel.merge2excel(dir_path=r'C:\程序员晚枫\excel-merge\excel',output_file='test.xlsx')

#参数作用：
# dir_path = 文件夹的位置，建议把需要合并的多个excel文件放到同一个文件夹里。
# output_file = 最终合并的excel文件放在哪里、叫什么名字，可以不填，默认是：merge2excel.xlsx
```
直接运行以上代码，就可以得到一个合并后的excel文件啦~

**快去试试吧~**

> 如果有我没说清楚的，或者在使用过程中有问题，欢迎大家在评论区和我交流~
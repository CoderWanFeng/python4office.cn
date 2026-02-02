---
title: 如何拿到当前文件夹下的所有文件？1行Python代码搞定
date: 2023-04-01 17:59:15
tags: 自动化办公
---




大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。

GitHub上有个开源项目：**python-office**，是专门用来自动化办公的Python第三方库。

在自动化办公中，一个重要的功能就是批量处理文件，那么在处理之前，它是如何一次性获取指定文件夹下所有文件的呢？今天我们一起来学习一下~

## 1、上代码

代码实现很简单,一共有2个参数：path 和 name。

- 功能：获取指定路径下的所有文件
- 参数 **path**: 必填，指定路径
- 参数 **name**: 可以不填，名字中包含的内容
- 返回值: 装满文件路径的列表

如果不填写name参数，效果如下图1框所示，会取出指定目录下所有文件。（包含子文件夹下内容）

如果填写name参数，则只会取出指定路径下，文件名包含name指定内容的文件。例如指定name=‘pdf’，则结果如下图2框所示。

```python

#pip install pofile
import pofile
files_list = pofile.get_files(path=r'D:\workplace\code\github\pofile\tests',name='pdf')
print(files_list)

```

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pofile/get_files/20230401173251.png)

## 2、更多说明

接下来还会开发2个参数：

- :param sub: 可以不填，是否获取子文件夹内容
- :param level: 可以不填，获取第几层文件夹的内容

欢迎感兴趣的朋友通过给开源项目PR的形式，加入一起开发~

- ⭐Github：https://github.com/CoderWanFeng/pofile




---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)就能上手做AI项目。
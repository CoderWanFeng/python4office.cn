---
title: 自动群发节日祝福，1行Python代码搞定!
date: 2023-09-30 15:50:11
tags: 微信机器人
---


大家节日快乐，这里是程序员晚枫，小红薯也叫这个名字。

今天给大家分享一个实用功能：**自动群发祝福消息**。

我相信社会人都体会过，过年过节给别人群发祝福消息的无奈，今天分享的这个工具，可以快速的解决这个烦恼。

我们一起来看一下使用方法吧~

## 下载和安装



自动群发的功能，来自一个Python第三方库：``python-office``，使用下面这行命令，可以免费下载和安装：

（如果没安装Python的朋友，可以去我主页看一下Python的免费安装教程哟）

```shell
pip install python-office
```

国内的朋友，建议使用清华镜像进行安装，使用下面这条命令：


```shell
pip install python-office -i https://mirrors.aliyun.com/pypi/simple/ -U
```

## 1行命令，自动群发

下载完成以后，运行以下代码，即可实现自动群发。


```python
import office

office.wechat.group_send()
```

运行这行命令以后，会出现一个加载页面，如下图所示。👇

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pyrobotoffice/group_send/gui.png)


你可以在里面填写2个内容：

1. 你要群发的内容。例如：程序员晚枫，祝您节日快乐。
2. 你要群发的人。可以同时指定个人或者群聊，不限个数。

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pyrobotoffice/group_send/Excel.png)
![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pyrobotoffice/group_send/content.png)

## 写在后面

这个功能，不仅可以用于群发节日祝福，平时需要群发任何消息，都可以使用。例如：群发广告。

虽然不建议发广告打扰大家，但它是具有这个功能的。

----

使用代码中，有任何问题，欢迎大家在评论区和我交流哟~


## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)就能上手做AI项目。
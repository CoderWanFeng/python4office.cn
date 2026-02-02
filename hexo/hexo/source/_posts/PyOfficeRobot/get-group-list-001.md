---
title: 天呐！1行Python代码，收集微信群资料，太方便了~
date: 2023-02-23 21:40:24
tags: 机器人
---




![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pyrobotoffice/get_group_list/cover.jpg)

大家好，这里是Python程序员晚枫。

建了个[Python自动化办公交流群](https://mp.weixin.qq.com/s/KVaOcfrDiZI5KWscuxtpQg)，最近发现，群里大神可真多呀~

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pyrobotoffice/get_group_list/exe.png)

周一有大佬开发了一个ChatGPT.exe桌面版，今天又有一位朋友给我们的微信机器人增加了功能：收集群友资料~我们一起来看一下。

## 代码实现 & 收集效果

今天下午在群里突然收到了一份excel文件，打开一看，全是群友的信息（都是公开信息，不涉及违规）。

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pyrobotoffice/get_group_list/Snipaste_2023-02-23_21-15-06.jpg)

和作者`` Zijian``沟通后，把代码加到了我们的[PyOfficeRobot](https://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247497235&idx=1&sn=55ccaac85777555d97eadd98dfdf6d38&chksm=eaf55726dd82de30671a1bab434036d4de351db025c60f915d3f0c4ed6de4f77ba4e9cf468a5&token=67549948&lang=zh_CN#rd)里。

1行代码即可调用，使用方式如下：
```
# pip install PyOfficeRobot
# 建议使用阿里镜像的仓库，教程：https://www.bilibili.com/video/BV1SM411y7vw/
import PyOfficeRobot

# 注意：目前不用加参数，自动收集当前打开的微信群，未来会优化
PyOfficeRobot.file.get_group_list()
```

## 更多功能

微信机器人的所有功能，都已经免费放到我们的官网：``www.python-office.com``里了~扫码下图直达👇

另外，也欢迎会使用GitHub的朋友，给项目点点Star，或者通过提交PR的形式，给项目增加功能。

⭐源码地址：https://github.com/CoderWanFeng/PyOfficeRobot


![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pyrobotoffice/get_group_list/list.jpg)

使用过程中有任何问题，请在评论区和我交流~

## 彩蛋区
最近小明开了一家淘宝店：爱吃火锅的少女，卖一些她时常购买的好东西，大家有喜欢的东西可以入手哟~

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pyrobotoffice/get_group_list/taobao.jpg)

---


发

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)就能上手做AI项目。
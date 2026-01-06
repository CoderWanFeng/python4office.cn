---
title: Python终于可以操作微信了
date: 2023-12-9 13:16:17
tags: 自动化办公
---

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/course/10%E8%AE%B2%E6%9C%BA%E5%99%A8%E4%BA%BA-%E6%A8%AA.jpg)

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，只给小白分享有用的**自动化办公**代码。

上次给大家分享了：[Python终于可以操作Office了](https://mp.weixin.qq.com/s/wwzGFIn-282FufnX9oNC7A)，发现大家很喜欢。

> 今天再给大家分享一个受欢迎的内容：**Python操作微信，实现聊天自动化。**



## 1、演示代码

我这次一共整理了10个用Python操作微信机器人的代码。

每个功能都是1行代码就可以调用的，简单粗暴，小白也可以用。

**用自动发消息给大家举个例子**👇

```python
# 首先，将PyOfficeRobot模块导入到我们的代码块中。
import PyOfficeRobot

PyOfficeRobot.chat.send_message(who='程序员晚枫', message='你好，我是你的粉丝')
# who:发给谁
# message:发送的内容
```

以上代码实现的功能是：给程序员晚枫发送一条消息，内容是【你好，我是你的粉丝】。

如果你要使用这1行，你只需修改2个参数：``who(指定发给谁)``和``message（你要发送给的消息内容）``，然后运行代码，就可以实现自动发送消息了。是不是简单易用？

## 2、所有功能

全部10个功能，我都录制了视频，扫码下图直达。👇

图片

- 第1讲：[软件下载和安装](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)
- 第2讲：[自动发消息](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)
- 第3讲：[自动发文件](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)
- 第4讲：[关键词回复](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)
- 第5讲：[自定义功能](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)
- 第6讲：[定时群发](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)
- 第7讲：[获取群信息](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)
- 第8讲：[自动加好友](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)
- 第9讲：[还有桌面版！](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)
- 第10讲：[AI智能聊天](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)

## 3、补充知识

- [用Python实现微信多开，1行代码免费用](https://mp.weixin.qq.com/s/qlubpfAytr_coV8GilG9RA)
- [用Python发一个优雅的朋友圈，1行代码搞定](https://mp.weixin.qq.com/s/pU0LBPUOaQFm_DmP_K_JDw)

---

以上所有机器人的功能，我都加入了原创课程:[给小白的《10讲 · Python微信机器人》（完结）](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)，都是1行Python代码就能实现的，适合纯小白的课程，需要可以加入学习哟~

- 加入学习👉[给小白的《10讲 · Python微信机器人》（完结）](https://mp.weixin.qq.com/s/g9nejIxuitwRzl5NMi177w)

大家学习 或 使用代码过程中，有任何问题，都可以加入读者群交流哟~👇


![](https://cos.python-office.com/group/0816.jpg)




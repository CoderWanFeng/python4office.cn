---
title: 1行Python代码，自动发送邮件
date: 2023-12-19 14:16:17
tags: 自动化办公
---

![](https://course-1300615378.cos.ap-guangzhou.myqcloud.com/poemail/poemail-course.jpg)


大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/h0MExYJag6hLnQg26yx98w)，今天给大家分享：1行Python代码，自动发送邮件。

> 本文来自在小破站：**Python自动化办公社区**更新的入门系列教程：给小白的《6讲 · Python实现自动发邮件（更新中）》。

## 1、准备工作

在使用下面的代码之前，请先完成2项工作：
- 生成自己邮箱的授权码，不会的朋友可以打开这个网址看教程👉[http://www.python4office.cn/log/2023/12/poemail/1219-email002/](http://www.python4office.cn/log/2023/12/poemail/1219-email002/?utm_id=0)
- 安装好：Python和PyCharm，没安装的朋友，可以去看给《小白的50讲Python自动化办公》，前3讲👇[扫码下图，直达安装的视频教程](https://www.python-office.com/course/50-python-office.html)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 2、上代码

用Python自动发邮件，使用的第三方库是：``poemail``，使用下面的命令，自动下载和安装：👇

```shell
pip install poemail
```

如果下载速度比较慢，可以使用清华镜像，之前给大家分享过方法了，👇

- [Python下载第三方库 | 加速 | 清华大学的国内pip镜像如何使用？](https://www.bilibili.com/video/BV1SM411y7vw/)

```python
import poemail

poemail.base.send_text(key='程序员晚枫的权限码', msg_from='程序员晚枫的邮箱@qq.com',
                       msg_to='小红薯也叫这个名@qq.com',
                       msg_subject='测试主题：点赞了吗？', content='测试内容：记得关注我，看后面的功能更新')
"""
发送文本邮件

参数:
key (str): 邮箱免密登录的权限码
msg_from (str): 发件人邮箱地址
msg_to (str): 收件人邮箱地址
msg_subject (str): 邮件主题，默认为空字符串
content (str): 邮件内容，默认为空字符串
"""
```

## 3、开发计划

昨晚刚刚在GitHub发布这个项目：https://github.com/CoderWanFeng/poemail ，功能还有待完善。

接下来的开发计划有：
- 支持多种邮箱平台：目前只支持QQ邮箱；
- 支持带附件发送：目前只支持纯文本；
- 支持批量发送;
- **支持自动收邮件。**

大家有更多功能需求，可以在读者群或者评论区告诉我~

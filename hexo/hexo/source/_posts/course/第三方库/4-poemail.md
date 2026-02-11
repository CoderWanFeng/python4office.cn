---
title: 1行代码计算运行时间的神器：potime库使用指南
date: 2024-11-11 00:41:49
tags: [第三方库,pip]
---


<p align="center" id='腾讯云-banner'>
    <a target="_blank" href='https://curl.qcloud.com/3csDz9jU'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F1040x100-tencent.jpg" width="100%"/>
    </a>   
</p>

> 大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)。这是专栏[优秀的第三方库](http://www.python4office.cn/course/%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93/all/)的第5篇原创文章。




`poemail` 是一个用于自动收发邮件的Python第三方库，它提供了简单易用的接口来实现邮件的发送和接收。以下是`poemail`的一些基本用法：

## 安装`poemail`
你可以通过pip来安装`poemail`：
```bash
pip install poemail
```
如果下载速度慢，可以使用清华镜像加速：
```bash
pip install -i https://mirrors.aliyun.com/pypi/simple/ poemail -U
```

## 发送文本邮件
使用`poemail`发送文本邮件非常简单，以下是一个基本的示例：
```python
import poemail
poemail.base.send_text(
    key='你的邮箱授权码',
    msg_from='你的邮箱@qq.com',
    msg_to='收件人邮箱@qq.com',
    msg_subject='测试主题：点赞了吗？',
    content='测试内容：记得关注我，看后面的功能更新'
)
```
在这个示例中，`key`参数是你的邮箱授权码，`msg_from`是发件人邮箱地址，`msg_to`是收件人邮箱地址，`msg_subject`是邮件主题，`content`是邮件内容。

### 发送带附件的邮件
`poemail`也支持发送带附件的邮件，你只需要在发送邮件的函数中添加`attach_files`参数，如下所示：
```python
poemail.send.send_email(
    key='你的邮箱授权码',
    msg_from='你的邮箱@qq.com',
    msg_to='收件人邮箱@qq.com',
    msg_subject='带附件的邮件主题',
    content='邮件正文',
    attach_files=['附件1的路径', '附件2的路径']
)
```
这里的`attach_files`是一个列表，包含了你想要发送的附件的路径。

## 批量下载附件
`poemail`还可以批量下载收件箱中的所有附件，只需要一行代码：
```python
poemail.receive.receive_email(
    key='你的邮箱授权码',
    msg_from='你的邮箱',
    msg_to='对方的邮箱（可不填）',
    output_path='附件保存的路径',
    status="ALL"
)
```
`output_path`参数指定了附件保存的路径，`status`参数可以设置为"ALL"来下载所有邮件的附件。

以上就是`poemail`的基本用法，它可以帮助自动化邮件的发送和接收，非常适合需要批量处理邮件的场合。

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
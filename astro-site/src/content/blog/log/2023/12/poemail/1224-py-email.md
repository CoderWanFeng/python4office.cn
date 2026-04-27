---
title: Python终于可以操作邮件了
date: 2023-12-24 01:16:17
tags: 自动化办公
---

<!-- more -->
大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)。

今天给大家分享一个可以**用1行代码**自动收发邮件的Python第三方库：``poemail``。

这个库主要有4个功能：

- 1行代码，发送邮件
- 1行代码，发送带附件的邮件
- 1行代码，下载所有收件箱里的附件
- 连接微信机器人，进行邮件的自动收发

今天主要给大家分享前面3个功能，最后一个机器人的功能，后面专门写一篇文章给大家分享。

直接上代码吧！


## 下载

下载很简单，用下面这一条命令就可以了，👇

```shell
pip install poemail
```

## 发邮件

```python
import os

key = os.getenv('EMAIL_KEY')#授权码
msg_from = os.getenv('EMAIL_FROM')#发件
msg_to = os.getenv('EMAIL_TO')#收件人
msg_subject = '程序员晚枫的邮件主题'
msg_cc = '抄送人的邮箱@163.com'
content = '程序员晚枫的邮件正文'

import poemail

poemail.send.send_email(key=key, msg_from=msg_from, msg_to=msg_to, msg_subject=msg_subject, content=content)
```

## 发邮件（带附件）

发送带附件的邮件，只需要给上面的代码，加一个参数。

```python
import os

key = os.getenv('EMAIL_KEY')#授权码
msg_from = os.getenv('EMAIL_FROM')#发件
msg_to = os.getenv('EMAIL_TO')#收件人
msg_subject = '程序员晚枫的邮件主题'
msg_cc = '抄送人的邮箱@163.com'
content = '程序员晚枫的邮件正文'

# 附件列表，可以写多个
attach_files = [r'./test_files/4-send_mail_content_file/程序员晚枫.doc',
                r'./test_files/4-send_mail_content_file/0816.jpg']

import poemail

poemail.send.send_email(key=key, msg_from=msg_from, msg_to=msg_to, msg_subject=msg_subject, content=content,attach_files=attach_files)
```


## 批量下载附件

批量下载所有收件箱的附件，只需要1行代码。

```python
import os

import poemail


poemail.receive.receive_email(key='程序员晚枫的邮箱授权码',
                              msg_from='程序员晚枫的邮箱',
                              msg_to='对方的邮箱（可不填）',
                              output_path=r'./test_files/程序员晚枫的附件',
                              status="ALL")

```

-------

关于**Python自动收发邮件**，我接下来会录制一套课程，感兴趣的同学，可以关注下面这个源码仓库，查看课程进度。

- gitee：[https://gitee.com/CoderWanFeng/poemail](https://gitee.com/CoderWanFeng/poemail)
- github:[https://github.com/CoderWanFeng/poemail](https://github.com/CoderWanFeng/poemail)





## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)


程序员晚枫专注AI编程培训，小白看完他和图灵社区合作的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)就能上手做AI项目。


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


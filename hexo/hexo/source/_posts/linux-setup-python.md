---
title: Linux上安装Python
date: 2022-02-23 15:22:31
tags: [Linux,Python]
---

1、下载相关yum库

yum install -y gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel

2、下载python安装包
下载压缩包，然后解压
wget https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz
> 更多版本，可以直接打开：https://www.python.org/ftp/python/

<!-- more -->
3、make

进入解压后的Python文件
配置make路径
./configure --prefix=/usr/local/python3910
make
make install

4、配置软链接
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3


5、配置环境变量
我不是每个版本的Python都配置，一般是直接使用路径调用

6、常见问题

make&make install不成功，一般是因为第1步里，有些yum库没有安装。


## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)


程序员晚枫专注AI编程培训，小白看完他和图灵社区合作的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)就能上手做AI项目。


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


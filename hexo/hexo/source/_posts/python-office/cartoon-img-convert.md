---
title: 某宝动漫头像一张50元？1行Python代码实现，别再去交智商税了
date: 2022-06-21 11:33:40
tags: python-office
---


![car](https://www.python-office.com/api/img-cdn/cartoon-img.jpg)


大家好，我是Python程序员晚枫。


今天，给大家介绍python-office今天刚刚更新的功能：**1行代码，生成动漫头像**。


听说某宝需要50块钱一张？别再去交智商税了！

<!-- more -->

## 1. 安装python-office
安装很简单，在有python环境的电脑上，只需要执行下面这一行命令。
> 如果你之前使用过python-office这个库，也需要执行一下，可以下载到最新版本~

安装
```
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```
如果你的电脑里还没有安装python环境，可以看一下下面这个6分钟的傻瓜式安装教程，有电脑就能操作~
安装教程：[https://www.bilibili.com/video/BV1Q44y1u7rV](https://www.bilibili.com/video/BV1Q44y1u7rV)

## 2. 生成动漫头像
直接上代码！

代码
```
# 导入这个库：python-office，简写为office
import office

# 1行代码，实现 人像转动漫头像
office.image.img2Cartoon(path = 'd://image//程序员晚枫.jpg')

# 参数说明：
# path:存放自己真人照片的位置 + PDF的文件名，例如：d://image//程序员晚枫.pdf
```
直接运行以上代码，就会得到一张转化后的动漫头像了。

>程序可能需要运行20秒左右。

## 3.全部功能
1行代码实现复杂功能，是不是使用起来很方便？


> 项目已被收录进【开源中国】、【Python官网】等平台，所有功能，免费给大家使用：[GitHub](https://github.com/CoderWanFeng/python-office)


## 4. python-office库，近期添加的功能

- [生成二维码、翻译、提取音频、重命名文件/文件夹、图片加水印](https://mp.weixin.qq.com/s/4Pt0YWakkPhfEWVMHwXe8g)
- [实现Word批量转换PDF](https://mp.weixin.qq.com/s/eBn3N_FEx1dlC_-ttmlOwg)
- [一行Python代码，给PDF文件添加水印，快速而且免费~](https://mp.weixin.qq.com/s/yJDs5RoytRL5hl-ybXkZOA)
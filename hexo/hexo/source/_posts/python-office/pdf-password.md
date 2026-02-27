---
title: 1行python代码，实现PDF加密、解密
date: 2022-05-09 19:44:42
tags:
---

<p align="center">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://raw.atomgit.com/CoderWanFeng1/website/raw/main/github-nav.jpg" alt="github license"/>
    </a>   
</p>
<p align="center">
	<strong>🍬python for office</strong>
</p>
<p align="center">
	👉 <a href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>


<p align="center" name="图标-github">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/contributors/CoderWanFeng/python-office" alt="github contributors"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/forks/CoderWanFeng/python-office" alt="github forks"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues/CoderWanFeng/python-office" alt="github issues"/>
    </a>	
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues-pr/CoderWanFeng/python-office" alt="github license"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/license/CoderWanFeng/python-office" alt="github license"/>
    </a>   
</p>

<p align="center" name="gitee">
	<a target="_blank" href='https://gitee.com/CoderWanFeng/python-office/'>
		<img src='https://gitee.com/CoderWanFeng/python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
		<img src="https://gitee.com/CoderWanFeng/python-office/badge/fork.svg?theme=dark" alt="gitee fork"/>
	</a>
	<a href="https://mp.weixin.qq.com/s/yaSmFKO3RrBpyanW3nvRAQ">
	<img src="https://img.shields.io/badge/QQ-163434413-orange"/></a>
</p>

-------------------------------------------------------------------------------


大家好，我是Python程序员晚枫。

今天，给大家介绍python-office近期更新的功能之一：**1行代码，实现PDF加密、解密**。
前文回顾：

真的很实用！

## 1. 安装python-office
安装很简单，在有python环境的电脑上，只需要执行下面这一行命令。
> 如果你之前使用过python-office这个库，也需要执行一下，可以下载到最新版本~

安装
```
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```
如果你的电脑里还没有安装python环境，可以看一下下面这个6分钟的傻瓜式安装教程，有电脑就能操作~

## 2. PDF加密
直接上代码！

代码
```
# 导入这个库
import office

# PDF加密：填写你的文件位置和密码
office.pdf.encrypt4pdf(path='需要加密的.pdf', password='你想添加的密码')

# 参数说明：
# path：你的文件位置，例如：D:\work\参考.pdf
# password：你的密码，可以随意设置，不能为空
```
如果你想批量加密PDF文件，你可以自己写一个for循环，或者你联系我，我来增加对应的功能。我的个人微信👉CoderWanFeng

## 3. PDF解密
有加密就有解密~
代码
```
# 导入这个库
import office

#PDF解密：填写你的文件位置和密码
office.pdf.decrypt4pdf(path='你的加密文件.pdf', password='该文件的密码')

# 参数说明：
# path：你的文件位置，例如：D:\work\参考.pdf
# password：你的密码，可以随意设置，不能为空
```

## 4.提交需求
1行代码实现复杂功能，是不是很简单？目前python-office这个自动化办公的第三方库正在持续开发中。
欢迎大家加入交流群，来沟通你的功能需求~

也欢迎有技术开发能力的同学，一起来丰富这个项目：
> - 欢迎大家的star & fork & pr！⭐
> - gitee：python-office/python-office
> - github：python-office/python-office

## 5. python-office库，近期添加的功能

- [生成二维码、翻译、提取音频、重命名文件/文件夹、图片加水印](https://mp.weixin.qq.com/s/4Pt0YWakkPhfEWVMHwXe8g)
- [实现Word批量转换PDF](https://mp.weixin.qq.com/s/eBn3N_FEx1dlC_-ttmlOwg)
- [一行Python代码，给PDF文件添加水印，快速而且免费~](https://mp.weixin.qq.com/s/yJDs5RoytRL5hl-ybXkZOA)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。
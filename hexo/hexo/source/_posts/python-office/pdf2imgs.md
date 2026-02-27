---
title: 1行Python代码，实现PDF转图片，速度太太太太太快了
date: 2022-07-11 18:24:09
tags: python-office
---

<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='http://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>




<p align="center" name="atomgit">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>	
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
<a href="https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>


![](https://www.python-office.com/api/img-cdn/python-office/pdf2imgs/pdf2imgs-cover.jpg)

大家好，这里是Python程序员晚枫。

周末给大家汇总了👉[超详细！python-office自动化办公的18个功能汇总](https://mp.weixin.qq.com/s/QhaUoB7Q4CJHR29uD6JSHQ)

今天继续发布新功能：**1行代码，实现PDF转图片**。


速度真的很快！我还以为程序坏掉了，结果是早就运行完了。

## 1. 安装python-office
安装很简单，在有python环境的电脑上，只需要执行下面这一行命令。
> 如果你之前使用过python-office这个库，也需要执行一下，可以下载到最新版本~

安装
```
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```
如果没有Python环境，可以试一下这个6分钟的无脑安装教程👉[来，手把手带你搭建Python环境](https://mp.weixin.qq.com/s/kRjulm_pN_jZGWQ6fsGtkw)

## 2. 1行代码，实现PDF转图片
直接上代码！

代码
```
# 导入这个库：python-office，简写为office
import office

# 一行代码，实现转换
office.pdf.pdf2imgs(
    pdf_path='D://程序员晚枫的文件夹//程序员晚枫.pdf',
    out_dir='./点赞+关注文件夹'
)
# 参数说明：
# pdf_path = 你的PDF文件的地址 
# out_dir = 转换后的图片存放地址，可以不填，默认是PDF的地址
```




## 3.深入阅读
1行代码实现复杂功能，是不是很简单？

更多关于这1行代码的实现功能和背后原理，大家可以查阅：
- [5个有趣的 Python 自动化办公程序，建议收藏！超实用~](https://mp.weixin.qq.com/s/Z_RcTRYxUFpCQBGpShO0ig)
- [Python爬虫如何加速？异步、协程还是多进程？分享一个常用做法，小白也能看懂。](https://mp.weixin.qq.com/s/naH7d4emsUOTy3zO5bv97g)
- [pandas创始人：我写了1本《利用Python进行数据分析》，提供全套代码](https://mp.weixin.qq.com/s/VVGZ6iIGjtxY6K00o89LRA)

---


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。
---
title: 1行Python代码，实现PDF转图片，速度太太太太太快了
date: 2022-07-11 18:24:09
tags: python-office
---

<p align="center" id='进群-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/dfdNNrlnxGCOsDHV4fq6iQ'>
    <img src="https://raw.gitcode.com/user-images/assets/5027920/d78ad96d-6a5e-49fa-9a6d-ba98ec1a1293/image.png" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>




<p align="center" name="gitcode">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
		<img src='https://gitcode.com/CoderWanFeng1/python-office/star/badge.svg?theme=dark' alt='gitcode star'/>
	</a>	
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
  	<a href="https://mp.weixin.qq.com/s/yaSmFKO3RrBpyanW3nvRAQ">
	<img src="https://img.shields.io/badge/QQ-163434413-orange"/>
  </a>
    	<a href="http://www.python4office.cn/wechat-group/">
	<img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E4%BA%A4%E6%B5%81%E7%BE%A4-brightgreen"/>
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
---
title: 头像加国旗
date: 2025-08-22
tags: [ 星河计划 ]
---


<p align="center" id='进群-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/0GrWWSQ8sKs-WA8WoN3Ztg?payreadticket=HPsk3SM42QLKkwlPgzoQN00eTUDy7x7I70-jcY9jIG2bWFmjZvB7r1mF10OiNSkxknfiN08&scene=1&click_id=1'>
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
</p>
<p align="center" name="gitcode">
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
    	<a href="http://www.python4office.cn/wechat-group/">
	<img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E4%BA%A4%E6%B5%81%E7%BE%A4-brightgreen"/>
  </a>

</p>

<!-- more -->


这里是正文

-------------------------------------------------------------------------------

>Python官网发布了Python自动化办公的库：python-office，相关信息：[重磅！官网发布第三方库：python-office，为Python自动化办公而生](https://mp.weixin.qq.com/s/v2n0DTVTZUaw7QOnA0Zlow)
>不需要自己写代码，直接调用写好的方法就行。

大家好，这里是码农如瓮，专注于分享：Python自动化办公。
**这个系列教程，用来逐一介绍python-office自动化办公的功能。**
## 1. 功能介绍
今天我们介绍这个库的功能之一：
> 头像加国旗:只需要一行代码，给自己的头像加上国旗。
## 2. 使用说明
#### 下载poimage
只需要下面这一条命令，就可以自动下载和安装poimage
```
pip install poimage
```
#### 调用功能
照抄下面代码，修改文件存放位置，右键选择运行
```python
import poimage # 导入python-office

poimage.flag2profile(profile_path=r'./test_files/30-17-flag2profile/程序员晚枫的头像.jpg',
                     output_path=r'./test_files/30-17-flag2profile/程序员晚枫的国庆头像.png')
# 参数解释：
# profile_path：需要转换的图片存放位置+图片名
# output_path: 加上国旗后的图片存放位置+图片名
```

## 3.提交需求
1行代码实现复杂功能，是不是很简单？目前python-office这个自动化办公的第三方库正在持续开发中。
欢迎大家加入交流群，来沟通你的功能需求~

也欢迎有技术开发能力的同学，一起来丰富这个项目：
> - 欢迎大家的star & fork & pr！⭐
> - 开源地址：
> - https://gitee.com/CoderWanFeng/python-office
> - https://github.com/CoderWanFeng/python-office

> 注意：这个功能，目前只支持docx格式的文件。
![](https://cos.python-office.com/ads/gzh/sub-py.jpg)


---
title: python-office自动化办公：Word批量转PDF
date: 2022-04-25 10:41:04
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

>Python官网发布了Python自动化办公的库：python-office，相关信息：[重磅！官网发布第三方库：python-office，为Python自动化办公而生](https://mp.weixin.qq.com/s/v2n0DTVTZUaw7QOnA0Zlow)
>不需要自己写代码，直接调用写好的方法就行。

大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)，专注于分享：Python自动化办公。
**这个系列教程，用来逐一介绍python-office自动化办公的功能。**
## 功能介绍
今天我们介绍这个库的功能之一：
> 自动化批量Word转PDF，你只需要输入存放Wor的文件的文件夹位置，剩下的，交给python吧
## 使用说明

#### 下载python-office

只需要下面这一条命令，就可以自动下载和安装python-office
```
pip install python-office
```
> 也欢迎大家参与python-office这个开源项目的建设：
>开源地址：
>https://gitee.com/CoderWanFeng/python-office
>https://github.com/CoderWanFeng/python-office
#### 调用功能
```python
import office # 导入python-office

path = '.'  # path这里，填写你存放word文件的位置，例如：C:/app/workbook
office.word.docx2pdf(path=path)

```
> 注意：这个功能，目前只支持docx格式的文件。

## 更多阅读
- [深度盘点丨史上最全的Python自动化办公库（34个）](https://mp.weixin.qq.com/s/RsBG_cg8GsB2P-9zmhrA1Q)
- [xlwings库 | Excel与Python的完美结合（附使用文档）](https://mp.weixin.qq.com/s/2_qNnsPK6fjEAUu3jf-NFA)
- [Python-Docx库 | Word与Python的完美结合（附使用文档）](https://mp.weixin.qq.com/s/_QzBRGeXsqF65-xlzQfFjQ)



---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)就能上手做AI项目。
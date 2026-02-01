---
title: pdf-add-water-mark
date: 2022-04-26 10:37:11
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

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，专注于分享：Python自动化办公。
**这个系列教程，用来逐一介绍python-office自动化办公的功能。**
## 1、功能介绍

上次我们介绍了python-office这个库的功能之一：[实现批量Word转PDF](https://mp.weixin.qq.com/s/6SM_66BjCIzUkkRWrDe5pQ)，
今天我们介绍这个库的功能之二：
> 一行代码，自动给PDF文件添加你指定的水印内容，快速且免费。
## 2、代码说明

#### 下载python-office

a、如果你是第一次使用python-office，

只需要下面这一条命令，就可以自动下载和安装python-office
```
pip install python-office
```
b、如果你看过之前的文章，已经使用过python-office，那你需要运行下面这行命令，把python-office升级到最新版本。
> python-office的更新很快,建议大家每次使用之前，都更新一下
```python
pip install --upgrade python-office
```
#### 调用功能
安装完python-office，直接复制粘贴，运行下面这个代码
```python
import office  # 导入python-office

office.pdf.add_watermark() # 不需要对代码进行任何修改，直接运行

```
运行后，控制台会出现一些提示文字，中国人开发的python-office，提示文字当然是中文了。
你直接根据需要，输入对应的内容，程序就会自动添加水印了


## 3、关于python-office
python-office是pypi开源的第三方库，专为python自动化办公而生。
>也欢迎大家参与python-office这个开源项目的建设：
> - https://gitee.com/CoderWanFeng/python-office
> - https://github.com/CoderWanFeng/python-office

## 更多阅读
- [深度盘点丨史上最全的Python自动化办公库（34个）](https://mp.weixin.qq.com/s/RsBG_cg8GsB2P-9zmhrA1Q)
- [xlwings库 | Excel与Python的完美结合（附使用文档）](https://mp.weixin.qq.com/s/2_qNnsPK6fjEAUu3jf-NFA)
- [Python-Docx库 | Word与Python的完美结合（附使用文档）](https://mp.weixin.qq.com/s/_QzBRGeXsqF65-xlzQfFjQ)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)就能上手做AI项目。
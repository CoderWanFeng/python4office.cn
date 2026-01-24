---
title: popdf，PDF自动化办公，1行代码搞定
date: 2024-12-08 10:16:17
tags: [ 第三方库,自动化办公,pdf ]
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
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>	
	    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>



<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='http://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，今天给大家分享一个Python自动化办公的第三方库：popdf，专门用来处理PDF文件。

> 源码地址：https://github.com/CoderWanFeng/popdf

## 前置知识

Python和PyCharm的安装，就不再每套课程都重复了，跟着下面视频做就行了。

课程前3讲，主要是Python环境的搭建，包含：python的安装、pycharm的安装和pip的使用。

是学习本套课程、运行课程中的代码必须安装的软件。

> 如果是小白，请务必按顺序听完学会；如果是已经安装并且会使用的大佬，请直接跳转到下一部分的课程。

- 第1讲：[Python的下载、安装和卸载](https://www.python-office.com/course/docs/50-01-python.html)
- 第2讲：[正版PyCharm的下载和使用教程，还有中文插件哦~](https://www.python-office.com/course/docs/50-02-pycharm.html)
- 第3讲：[pip的下载、安装和使用](https://www.python-office.com/course/docs/50-03-pip.html)


## 核心内容


已有功能的说明如下：

| 序号 | 方法名             | 功能         | 视频                                                                    | 文档                                                                                             |
| ---- | ------------------ | ------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 1    | pdf2docx           | 💻PDF 转 Word | 💻 [播放](https://www.bilibili.com/video/BV1em4y1H7ir)                   | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/1-pdf2docx/)           |
| 2    | pdf2imgs           | PDF 转 图片  | 💻[文档](https://mp.weixin.qq.com/s/Ve5FH6q6ZqNbhUUG9RR8aw)              | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/2-pdf2imgs/)           |
| 3    | txt2pdf            | TXT转PDF     | [文档](https://blog.csdn.net/weixin_42321517/article/details/130612189) | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/3-txt2pdf/)            |
| 4    | split4pdf          | 按页切割PDF  | 💻[文档](https://mp.weixin.qq.com/s/Ve5FH6q6ZqNbhUUG9RR8aw)              | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/4-split4pdf/)          |
| 5    | encrypt4pdf        | PDF加密      | [文档](https://blog.csdn.net/weixin_42321517/article/details/129963432) | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/5-encrypt4pdf/)        |
| 6    | decrypt4pdf        | PDF解密      | [文档](https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA)               | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/6-decrypt4pdf/)        |
| 7    | add_text_watermark | PDF加水印    | [播放](https://www.bilibili.com/video/BV1Se411T7au)                     | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/7-add_text_watermark/) |
| 8    | merge2pdf          | 合并PDF      | [文档](https://baijiahao.baidu.com/s?id=1733062611567959337)            | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/8-merge2pdf/)          |
| 9    | del4pdf            | 删除PDF      | [文档](https://baijiahao.baidu.com/s?id=1733062611567959337)            | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/9-del4pdf/)            |



## 加入开源

如果你喜欢以上这些开源项目，欢迎加入我们的开源小组，一起交流学习，一起进步。

> 加我的微信：python-office，备注：开源

关于项目的介绍：

- atomgit：[DeepSeek浪潮下如何撑过35岁职场危机？跨界程序员：我不焦虑，40岁就退休｜CodeMaster#3](https://mp.weixin.qq.com/s/RC54o9C4F87fyAebJUE0kg)
- Python中国大会：[非程序员如何学习和使用 Python-程序员晚枫-科技博主&开源作者](https://www.bilibili.com/video/BV1Y6qWYWEyQ/?spm_id_from=333.1387.homepage.video_card.click&vd_source=ca20bb8763fcb18660aa74d7a87234fa)
- Pypi：[python-office](https://pypi.org/project/python-office/)
- 官网：[python-office.com](https://python-office.com)
- 开源中国：[Python-office Python 自动化办公库](https://www.oschina.net/p/python-office)
- B站视频教程：[官网发布：python-office库 | 专为Python自动化办公而生，一行代码提高办公效率 | 哪里不会点哪里，再也不用学习Python编程](https://www.bilibili.com/video/BV1pT4y1k7FH/?spm_id_from=333.1387.0.0&vd_source=ca20bb8763fcb18660aa74d7a87234fa)



<p align="center" id='CodeMaster-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/B9OOU5bb8fOd9KiG43GqAw'>
    <img src="https://cos.python-office.com/activity/CodeMaster-3.jpg" width="100%"/>
    </a>   
</p>

## 相关课程


- [给小白的《50讲 · Python自动化办公》（完结）](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)
- [给小白的《10讲 · Python微信机器人》（完结）](https://www.python-office.com/course-002/10-PyOfficeRobot/10-PyOfficeRobot.html)
- [给小白的《5讲 · Python实现发票批量识别》](https://www.python-office.com/course-002/5-poocr/5-poocr.html)

---



![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')





## 交流群


![](https://cos.python-office.com/group/0816.jpg)

###　读者福利

<p align="center" id='福利合集-banner'>
    <a target="_blank" href='http://python4office.cn/sideline-pro-list/'>
    <img src="https://cos.python-office.com/ads/fuli/all-1.jpg" width="100%"/>
    </a>   
</p>


---
title: 拆分PDF，1行代码搞定
date: 2024-12-08 10:16:17
tags: [ 第三方库,自动化办公,pdf ]
---


<p align="center">
  <a target="_blank" href='https://github.com/CoderWanFeng/popdf'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/popdf.svg?style=social" alt="github star"/>
    </a>
        <a target="_blank" href='https://gitcode.com/python4office/popdf'>
		<img src='https://gitcode.com/python4office/popdf/star/badge.svg?theme=dark' alt='gitcode star'/>
	</a>
 <a target="_blank" href='https://github.com/CoderWanFeng/popdf'>
<img src="https://static.pepy.tech/badge/popdf" alt="PyPI Downloads">
</a>
</p>


<p align="center" id='进群-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/dfdNNrlnxGCOsDHV4fq6iQ'>
    <img src="https://raw.gitcode.com/user-images/assets/5027920/d78ad96d-6a5e-49fa-9a6d-ba98ec1a1293/image.png" width="100%"/>
    </a>   
</p>

大家好，这里是程序员晚枫，今天给大家分享一个Python自动化办公的第三方库：popdf，专门用来处理PDF文件。

> 源码地址：https://github.com/CoderWanFeng/popdf


## 视频

<iframe src="//player.bilibili.com/player.html?bvid=BV1PYQpY3E8z" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=100%, height=500> </iframe>




## 上代码

首先，下载一个PDF自动化办公的专用库：``popdf``，命令如下，??

```
pip install popdf
```

然后直接1行代码搞定，??

```
# pip install popdf
import popdf

popdf.split4pdf(
            input_file=r'./test_files/pdf/程序员晚枫.pdf',
            from_page=1,
            output_file=r'./test_files/pdf/split4pdf.pdf'
        )
```

#### 参数说明

- input_path：输入PDF的路径一般用于批量操作
- output_path：输出PDF的路径，一般用于批量操作
- input_file: 输入PDF的文件名，可以包含路径，一般用于单个文件的操作
- output_file：输出结果的文件名，可以包含路径，一般用于单个文件的操作
- input_file_list: 输入PDF的文件列表，一般用于批量操作，例如：合并2个pdf文件


## 加入开源

如果你喜欢以上这些开源项目，欢迎加入我们的开源小组，一起交流学习，一起进步。

> 加我的微信：python-office，备注：开源

关于项目的介绍：

- GitCode：[DeepSeek浪潮下如何撑过35岁职场危机？跨界程序员：我不焦虑，40岁就退休｜CodeMaster#3](https://mp.weixin.qq.com/s/RC54o9C4F87fyAebJUE0kg)
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

- [给小白的《50讲 · Python自动化办公》](https://www.python-office.com/course/50-python-office.html)
- [给小白的《10讲 · Python微信机器人》](https://www.python-office.com/course-002/10-PyOfficeRobot/10-PyOfficeRobot.html)
- [给小白的《5讲 · Python实现OCR自动批量识别》](https://www.python-office.com/course-002/5-poocr/5-poocr.html)
- [给小白的《6讲 · Python自动收发邮件》](https://www.python-office.com/course-002/poemail/poemail.html)
- [给小白的《30讲 · Python数据分析》](http://www.python-office.com/course-002/30-Excel/30-Excel.html)
- [给小白的《15讲 · Python入门基础》](http://www.python-office.com/course-002/15-Python/15-Python.html)

---



![](https://cos.python-office.com/ads/gzh/sub-py.jpg)



## 交流群


![](https://cos.python-office.com/group/0816.jpg)

###　读者福利

<p align="center" id='福利合集-banner'>
    <a target="_blank" href='http://python4office.cn/sideline-pro-list/'>
    <img src="https://cos.python-office.com/ads/fuli/all-1.jpg" width="100%"/>
    </a>   
</p>


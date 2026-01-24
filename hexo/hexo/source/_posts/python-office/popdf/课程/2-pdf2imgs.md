---
title: PDF 转图片，一行代码搞定！批量支持已上线！
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



大家好，我是程序员晚枫。今天我要给大家带来一个超实用的功能——`popdf` 现在支持 PDF 转图片了，而且还能批量操作！是不是很激动？别急，我来手把手教你玩转这个功能。


## 视频

<iframe src="//player.bilibili.com/player.html?bvid=BV19WRVYKEEY" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=100%, height=500> </iframe>


## 1. 一行代码搞定单文件转换

`popdf` 的核心就是简单暴力。只需要一行代码，你就能轻松把 PDF 转成图片：

```python
from popdf import pdf2imgs

pdf2imgs(
    input_file=r"程序员晚枫的文件夹/single_file.pdf",
    output_file=r"程序员晚枫的文件夹/single_file.png"
)
```

是不是很简单？小白也能秒上手！



![](https://cos.python-office.com/course/10%E8%AE%B2PDF%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8A%9E%E5%85%AC/popdf-heng.jpg)




## 2. 批量转换，轻松搞定

现在，`popdf` 更是升级了！支持批量转换啦！只需要换两个参数，就能一次性处理一堆 PDF 文件。以下是关键参数的讲解：

- **`input_file` 和 `output_file`**：这组参数用来处理单个文件，适合零散的 PDF 转换。
- **`input_path` 和 `output_path`**：这组参数才是今天的主角！`input_path` 是 PDF 文件夹路径，`output_path` 是输出图片文件夹路径。只要把 PDF 文件丢进输入文件夹，运行代码，图片文件就自动出来了。

批量转换的代码示例如下：

```python
from popdf import pdf2imgs

pdf2imgs(
    input_path=r"程序员晚枫的文件夹/pdf_folder/",  # PDF 文件夹路径
    output_path=r"程序员晚枫的文件夹/img_folder/"  # 输出图片文件夹路径
)
```

是不是超方便？再也不用手动一个个转换了！

## 3. 代码示例，直接上手

为了让大家更直观地感受，我再贴一个完整的代码示例：

```python
from popdf import pdf2imgs

# 单文件转换
pdf2imgs(
    input_file=r"程序员晚枫的文件夹/single_file.pdf",
    output_file=r"程序员晚枫的文件夹/single_file.png"
)

# 批量转换
pdf2imgs(
    input_path=r"程序员晚枫的文件夹/pdf_folder/",
    output_path=r"程序员晚枫的文件夹/img_folder/"
)
```

记住，路径一定要改成你自己的文件夹路径，否则程序会骂你哦！

## 4. 关于我：程序员晚枫

我是程序员晚枫，一个热爱技术、爱折腾的开发者。平时喜欢写一些实用的工具和库，帮助大家解决开发中的小痛点。`popdf` 就是其中之一，希望能帮到更多人。

如果你对这个工具感兴趣，或者有任何问题，欢迎在评论区留言！告诉我你的使用体验，或者提出你想要的功能，说不定下个版本就实现了哦！

快来试试吧，保证让你惊艳！有问题留言区见！ 😄

GitHub 项目地址：[https://github.com/CoderWanFeng/popdf](https://github.com/CoderWanFeng/popdf)

#### 参数说明

- input_path：输入PDF的路径一般用于批量操作
- output_path：输出PDF的路径，一般用于批量操作
- input_file: 输入PDF的文件名，可以包含路径，一般用于单个文件的操作
- output_file：输出结果的文件名，可以包含路径，一般用于单个文件的操作


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

- [业余爱好者，如何从0开始快速掌握Python？](https://mp.weixin.qq.com/s/ZxJZimZYSvtBSK80tpZbNQ)
- [给小白的《15讲 · Python入门课》](https://mp.weixin.qq.com/s/ZxJZimZYSvtBSK80tpZbNQ)
- [给小白的《50讲 · Python自动化办公》](https://mp.weixin.qq.com/s/lOx4cAp9AllsCrhsUqVn8g)
- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg)
- [给小白的《5讲 · Python实现文字批量识别》](https://mp.weixin.qq.com/s/pGim7ifpgLwYUJ9a-FHvaw)
- [给小白的《6讲 · Python自动收发邮件》](https://mp.weixin.qq.com/s/AeTkloNri7gpk25m50VmTA)
- [给小白的《30讲 · Python + Excel数据分析》](https://www.python-office.com/course-002/30-Excel/30-Excel.html)
- [给小白的《10讲 · Python + PDF 自动化办公》](https://www.python-office.com/course-002/10-popdf/10-popdf.html)
- [Python学习交流群](https://mp.weixin.qq.com/s/NN2pX2bQPpczOeGF4ARNtw)
- [零基础Python自动化办公，一站式搞定！](https://mp.weixin.qq.com/s/XDOMnTISBpglNvSf4R-tmg)


---

<p align="center" id='4套课程'>
    <a target="_blank" href='https://www.python-office.com/guide/allFunc.html'>
    <img src="https://cos.python-office.com/course%2Fall-1.jpg" width="100%"/>
    </a>   
</p>


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


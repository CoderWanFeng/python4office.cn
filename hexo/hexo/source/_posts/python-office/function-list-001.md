---
title: 5个有趣的 Python 自动化办公程序，建议收藏！超实用~
date: 2022-05-06 13:31:42
tags:
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
<a href="https://mp.weixin.qq.com/s/7rH5U6s91hnTKCKZy4BHCg">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>



<div align="center">
    <a href="https://github.com/CoderWanFeng"> <img src="https://badgen.net/badge/Github/%E7%A8%8B%E5%BA%8F%E5%91%98?icon=github&color=red"></a>
    <a href="http://www.python4office.cn/account-display/"> <img src="https://badgen.net/badge/follow/%E5%85%AC%E4%BC%97%E5%8F%B7?icon=rss&color=green"></a>
    <a href="https://space.bilibili.com/259649365"> <img src="https://badgen.net/badge/pick/B%E7%AB%99?icon=dependabot&color=blue"></a>
    <a href="http://www.python4office.cn/wechat-group/"> <img src="https://badgen.net/badge/join/%E4%BA%A4%E6%B5%81%E7%BE%A4?icon=atom&color=yellow"></a>
</div>

<!-- more -->


-------------------------------------------------------------------------------


大家好，我是Python程序员晚枫。

今天，给大家介绍Python一些鲜为人知的操作。

这些操作，并非是炫技，而是真的实用！
## 1. 生成二维码
我们在日常生活中经常看到二维码，QR码节省了很多用户的时间。
我们也可以用python库qrcode为网站或个人资料创建独特的QR码。

安装
```
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```
代码
```
# 导入库
import office
# 执行这行代码，生成链接对应的二维码
office.tools.qrcodetools('http://python4office.cn/python-office/profile/') 
```
## 2. 翻译
我们生活在一个多语言的世界里。
因此，为了理解不同的语言，我们需要一个语言翻译器。
我们可以在python库Translator的帮助下创建我们自己的语言翻译器。

安装
```
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```
代码
```
# 导入这个库
import office  
  
# to_lang，是翻译的结果使用哪种语言，支持全球100多个语言；content，是你想翻译的文本内容
office.tools.transtools(to_lang='Chinese', content='hello world')
```
## 3. 提取音频
在某些情况下，我们有mp4文件，但我们只需要其中的音频，比如用另一个视频的音频制作一个视频。

我们为获得相同的音频文件做了足够的努力，但我们失败了。
这个问题用python库moviepy可以轻而易举的解决。

安装
```

pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```

代码
```
# 导入这个库
import office

# 这里填写你的视频位置
path = r'D:\download\baiduyun\2.mp4'
# path，是你的视频位置；mp3_name，是你的MP3结果文件的名称，可以不填
office.video.video2mp3(path=path, mp3_name='result')
```

## 4.批量重命名文件

有时候我们获得一些网上资源，文件名里全是广告。
用下面这行命令，哪怕有1w个文件，也可以一键去广告~

安装
```
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```
代码

```
import office
path = r'D:\\QMDownload\\'
office.file.replace4filename(
                              path=path,
                              del_content='你要去掉的内容',
                              replace_content='你想替换掉广告的内容，可以不填'
                              )
```

## 5.图片加水印
有时候我们好不容易P好了一张精美的图片，发出去分分钟就被别人给盗版了。
使用Python，加上图片水印吧~

安装
```
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```
代码
```
import office

office.image.add_watermark(file='你的图片', mark='你的水印')
```
本文就是抛砖引玉一下，希望大家能够寻找到更多有趣的Python玩法！

![](https://cos.python-office.com/course/50%E8%AE%B2%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8A%9E%E5%85%AC/free-link.jpg)

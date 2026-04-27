---
title: 用腾讯云 AI 录音文件识别 实现短视频字幕批量处理
date: 2022-09-29 14:22:18
tags: python-office
---

<!-- more -->
<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="https://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
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
<a href="https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>


大家好，我是在重庆的Python程序员晚枫，全网同名。

经常遇到身边的朋友，想从视频中提取出文字，尤其是自媒体博主，如果能直接把视频转换成文章，那可太省时间了。

通过一阵检索，发现网上有很多付费软件可以提供视频提取语音的功能，但是价格都不低。

作为程序员，肯定不满足于付费工具的东西，正好看到腾讯云AI平台正在搞活动，1元即可购买60个小时的录音文件识别时长，另外还有多种福利的赠送，于是果断购买。[福利传送门](https://url.cn/7DV7SNid)

我们来一起看一下是怎么使用的~

## 0、前置操作

从视频转为文字，我这里分成了2步：视频→音频→文字。

> 之前给大家开发了：视频提取语音的方法，代码如下，不懂的可以翻看我之前的文章。这里就不再多介绍了。
```
# pip install povideo
import povideo

povideo.video2mp3(path=r'your_video_path', mp3_name='result')
```

接下来我们看一下，⭐如何使用腾讯云AI的录音识别功能，把提取出来的语音，转换成文字吧。

## 1、安装

这个录音识别的功能，腾讯云已经为我们写好了文档和代码，我根据这些资料，把这个转换功能，同样封装进了第三方库：``povideo``。所以首先需要安装这个库：

```
pip install povideo -U
```

## 2、使用

安装成功后，可以直接1行代码进行调用：
```
import povideo

povideo.audio2txt(audio_path=r"your_audio_path",
                  appid='your_appid',
                  secret_id='your_secret_id',
                  secret_key='your_secret_key')

```

## 3、参数说明
参数主要分为2部分：语音路径和app配置,
- 语音路径：填写你语音文件的路径，本地语音文件不能大于5MB。
  - audio_path
- app配置：需要到这个网址进行注册：[https://console.cloud.tencent.com/cam/capi](https://console.cloud.tencent.com/cam/capi)
  - appid
  - secret_id
  - secret_key


## 4、参考资料
- povideo的源码仓库：[https://github.com/CoderWanFeng/povideo](https://github.com/CoderWanFeng/povideo)
- 录音识别，官方说明文档：[https://cloud.tencent.com/document/product/1093/37823](https://cloud.tencent.com/document/product/1093/37823)
- 录音识别，腾讯提供的代码：[https://github.com/TencentCloud/tencentcloud-sdk-python](https://github.com/TencentCloud/tencentcloud-sdk-python)



程序员晚枫专注AI编程培训，小白看完他和图灵社区合作的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)就能上手做AI项目。


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


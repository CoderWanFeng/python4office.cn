---
title: 用腾讯云 AI 录音文件识别 实现短视频字幕批量处理
date: 2022-09-29 14:22:18
tags: python-office
---


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


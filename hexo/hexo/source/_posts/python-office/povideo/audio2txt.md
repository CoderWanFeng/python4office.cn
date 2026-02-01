---
title: 音视频转文字不求人， 腾讯云AI来帮您
date: 2024-05-23 13:00:35
tags: 开源项目
---

被抓过小三的朋友都知道，神探在搜集证据的时候一定要带一只永远不停机的录音笔。

如何把录音快速转成文字呢？

今天我们看看**如何用1行Python代码实现录音转文字**


## 上代码

首先下载一个开源第三方库：povideo

```shell
pip install povideo
```

然后通过1行代码，调用录音转文字的功能。

```python
import povideo

povideo.audio2txt(audio_path=r"your_audio_path",
                  appid='your_appid',
                  secret_id='your_secret_id',
                  secret_key='your_secret_key')
```

参数主要分为2部分：语音路径和app配置,

语音路径：填写你语音文件的路径，本地语音文件不能大于5MB。
audio_path
app配置：开通语音识别功能后，去到这个👉[链接](https://curl.qcloud.com/fuOGcm2R)👈进行获取：appid、secret_id、secret_key

> 友情提示：我们之前的OCR视频教程里使用的发票批量识别功能，也来自腾讯云AI哟~入门案例！批量识别发票自动保存为Excel文件，1行Python代码实现（支持PDF]([https://cloud.tencent.com/developer/video/80321](https://cloud.tencent.com/developer/video/80321))

## 读者福利

新用户专享一句话识别5000次免费调用，免费实时语音识别5小时时长，免费录音文件识别10小时时长，免费语音流异步识别5小时时长。

- 领取地址：[点我直达](https://curl.qcloud.com/rKrZxb82)




---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)就能上手做AI项目。
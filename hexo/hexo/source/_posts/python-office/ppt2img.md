---
title: 1行Python代码，把PPT转成图片
date: 2023-03-05 22:25:14
tags: python-office
---




大家好，这里是程序员晚枫。

今天给大家分享一个Python自动化办公的专用库python-office的最新功能：1行代码，实现PPT转为图片。

更多功能，请见官网：[开源中国推荐：python-office自动化办公，每个功能只需一行代码，做到了真正的开箱即用。](https://www.python-office.com/)

## 1、上代码


首先，下载python-office，下载教程之前录制过了，大家可以去看看~

[点我直达](https://www.bilibili.com/video/BV1pT4y1k7FH)


其次，1行代码调用ppt转图片的功能。
```python
import office

office.ppt.ppt2img(input_path=r'D:\test\py310\ppt_test\程序员晚枫的文档.pptx',
                   output_path=r'D:\test\py310\ppt_test',
                   img_type='png')
```

## 2、参数说明

一共有3个参数，作用分别如下：

- input_path：必填，待转换ppt的存放位置和名称
- output_path：选填，转换后的图片存储的位置，会自动生成一个和ppt同名的文件夹。可以不填，默认值：‘./’
- img_type：转换的图片类型，可以填：jpg或者png，可以不填，默认值：jpg

## 更多功能

- [后厂村：中国“硅谷”，遍地985，天天996](https://mp.weixin.qq.com/s/MSJ3t1hC3JmuGAorbkJyog)
- [普通人如何追上ChatGPT的风口？](https://mp.weixin.qq.com/s/uBqSV1QkX9JrvIkYexQy6A)
- [天呐！1行Python代码，收集微信群信息，聊天机器人太简单了~](https://mp.weixin.qq.com/s/t3TEkwR_MMaKmetSL1jsAA)


---
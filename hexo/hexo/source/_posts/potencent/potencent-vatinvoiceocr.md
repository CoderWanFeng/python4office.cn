---
title: 实战案例！用1行Python代码识别增值税发票，然后用爬虫将数据自动录入系统
date: 2023-01-25 01:18:40
tags: [potencent,AI]
---


![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/potencent%2FVatInvoiceOCR%2Fcover.jpg)

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。

录入发票是一件繁琐的工作，如果可以自动识别并且录入系统，那可真是太好了。

今天我们就来学习一下，如何自动识别增值税发票并且录入系统~



## 第一步：识别发票 - 人工智能

识别发票的代码最简单，只需要1行代码，如下所示。👇

```python
# 导入potencent这个库，下载命令：pip install potencent
import potencent

# 调用增值税识别的功能
potencent.ocr.VatInvoiceOCR(img_path=r'C:\vx_CoderWanFeng\your_img.jpg')
```

识别后的返回结果，包含发票信息如下，几乎涵盖所有发票上肉眼可见的内容。👇
![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/potencent%2FVatInvoiceOCR%2F003.jpg)
![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/potencent%2FVatInvoiceOCR%2F004.jpg)
面对这个返回数据，你当然可以使用之前推荐过的``B站：Python自动化办公社区``里播放第一的Excel自动化办公课程，把它转换到Excel里，这里不再重复。传送门：[https://mp.weixin.qq.com/s/waAgnrK_RFIQnUss998vnA](https://mp.weixin.qq.com/s/waAgnrK_RFIQnUss998vnA)

### 注意事项

该功能的实现，依托于腾讯云的发票识别，所以在同级目录下，需要配置一个``potencent-config.toml``文件。文件位置和内容如下图所示。👇
![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/potencent%2FVatInvoiceOCR%2F002.jpg)

```python
[tencent-ai]
TENCENTCLOUD_SECRET_ID = '你的 SecretId'     # 建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参考https://cloud.tencent.com/document/product/598/37140
TENCENTCLOUD_SECRET_KEY = '你的 SecretKey'   # 建议使用子账号密钥，授权遵循最小权限指引，降低使用风险。子账号密钥获取可参考https://cloud.tencent.com/document/product/598/37140
```

另外，如果需要自定义配置文件名称和位置，可以使用``configPath``参数，具体使用请看GitHub源码。




## 第二步：自动化录入系统 - 爬虫

光把发票信息识别出来还不够，如果能自动录入系统，那就完美了。

在编程语言中，把从网站下载数据和将信息录入网页的操作，统称为**爬虫**。更直白的理解，所有人类可以对网站进行的操作，Python都可以做，而且可以更快速更准确。而这一部分爬虫方面的知识，直接看Python爬虫大神崔老师的课程就可以一站式搞定了：[http://gk.link/a/11erO](http://gk.link/a/11erO)

这套课程的知识非常实用，不论是工作还是学习，都是不错的选择。赶紧学起来吧~

---

大家在阅读本文和使用代码中有任何问题，欢迎在评论区进行交流~
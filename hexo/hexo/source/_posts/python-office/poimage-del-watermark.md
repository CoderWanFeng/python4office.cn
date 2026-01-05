---
title: 1行Python代码去除图片水印，网友：一干二净！
date: 2023-02-12 20:43:55
tags: 自动化办公
---



![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poimage/%E5%9B%BE%E7%89%87%E5%8E%BB%E6%B0%B4%E5%8D%B0/cover.jpg)

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/h0MExYJag6hLnQg26yx98w)。

最近小明在开淘宝店（淘宝店名：``爱吃火锅的少女``），需要给自己的原创图片加水印，于是我上次给她开发了增加水印的功能：[图片加水印，保护原创图片，一行Python代码搞定](https://www.bilibili.com/video/BV1jT411T7n9)。

今天在后台收到读者提问：如何去除公众号文章图片上自带的水印？这个功能也早就开发好了！

接下来我们一起看一下，如何用1行Python代码，去除图片水印吧~

## 一、代码运行，效果演示

举个例子，在阅读公众号文章的时候，经常会看到下图所示的水印，这个是公众号系统自带的。


```python

# pip install poimage
import poimage

# 支持jpg、png等所有图片格式
poimage.del_watermark(
    input_image=r"D:\test\程序员晚枫\加了水印的图片.jpg",
    output_image=r'D:\test\程序员晚枫\保存为去除了水印的图片.jpg')

```

实现的效果如下：
![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poimage/%E5%9B%BE%E7%89%87%E5%8E%BB%E6%B0%B4%E5%8D%B0/water001.png)


![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/poimage/%E5%9B%BE%E7%89%87%E5%8E%BB%E6%B0%B4%E5%8D%B0/water002.png)
是不是很简单？赶紧去试试吧~



> 源码地址：https://github.com/CoderWanFeng/poimage/blob/main/demo/del_watermark_demo.py



## 二、已有功能
截止发布本文的时间，``poimage``库除了去除水印外，共有以下功能：


| 1行代码的功能   | 点击看代码    | 
| :---------| :---------| 
| add_watermark | [图片加水印](https://mp.weixin.qq.com/s/Z_RcTRYxUFpCQBGpShO0ig) | 
| down4img | [下载图片](https://mp.weixin.qq.com/s/H9NVBxwo_po8WsqsIRJ7YQ) | 
| txt2wordcloud | [生成词云图片](https://mp.weixin.qq.com/s/ifmt7MDleACNQKxk77EeNA) | 
| pencil4img | [人像转素描](https://mp.weixin.qq.com/s/8qBytOyIANmpI5Thqo2zmw) | 
| image2gif | 图片转Gif |


## 三、相关阅读


- [1行Python代码实现AI换脸，真假难辨！网友：细思极恐](https://mp.weixin.qq.com/s/D0Mp_CjbOlNsUbfL9fBSTw)

- [你家停车场的秘密，被1行Python代码发现了，车牌识别YYDS](https://mp.weixin.qq.com/s/owXyC5DjbOwrcHpTGjMbJA)

- [用1行Python代码识别增值税发票，YYDS](https://mp.weixin.qq.com/s/agsF8ttwxOiZyizsTKBxMQ)



---

代码使用中有任何疑问，欢迎大家在评论区交流~


---
title: 减小20M！PDF自动化办公专用库：popdf，发布1.0.0版本
date: 2024-12-08 10:16:17
tags: [ 第三方库,自动化办公,pdf ]
---

大家好，这里是程序员晚枫，今天给大家分享一个Python自动化办公的新功能：分割PDF。

## 需求说明

上次在小破站给大家录制的原创课程：[《给小白的50讲Python自动化办公》](https://mp.weixin.qq.com/s/lOx4cAp9AllsCrhsUqVn8g)
，里面有一讲是关于PDF转Word的特别热门。

但是那个功能有一个缺点：不能转换扫描件，最近在录制另一套新课程发现了一个值得尝试的解决办法，于是就想找一个扫描版的PDF试一下。

在50讲自动化办公的课程群里一问，热心的学员马上就发出来了。但是这个PDF文件太大了，做测试不方便，我就想把它拆分一下，比如：只要前3页，或者取第10-第30页。

搜了一下已有的PDF自动化办公的库，没找到这个功能，所以就有了今天的代码。

## 上代码

首先，下载一个PDF自动化办公的专用库：``popdf``，命令如下，👇

```
pip install popdf
```

然后直接1行代码搞定，👇

```
# pip install popdf
import popdf

popdf.split_pdf(input_path=r'D:\程序员晚枫的文件夹\原始.pdf',
                output_path=r'D:\程序员晚枫的文件夹\切割后的.pdf',
                from_page=0, to_page=4)
```

#### 参数说明

- input_path：输入PDF的路径一般用于批量操作
- output_path：输出PDF的路径，一般用于批量操作
- input_file: 输入PDF的文件名，可以包含路径，一般用于单个文件的操作
- output_file：输出结果的文件名，可以包含路径，一般用于单个文件的操作
- input_file_list: 输入PDF的文件列表，一般用于批量操作，例如：合并2个pdf文件

## 相关课程

- [给小白的《50讲 · Python自动化办公》（完结）](https://mp.weixin.qq.com/s/lOx4cAp9AllsCrhsUqVn8g)
- [给小白的《10讲 · Python微信机器人》（完结）](https://mp.weixin.qq.com/s/-oR2dUakXEY3vmPbzVtrnA)
- [给小白的《Python实现OCR自动批量识别》](https://mp.weixin.qq.com/s/pGim7ifpgLwYUJ9a-FHvaw)

---


交流群：[http://www.python4office.cn/wechat-group/](http://www.python4office.cn/wechat-group/)
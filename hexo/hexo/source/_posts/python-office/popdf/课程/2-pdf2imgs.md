---
title: PDF转图片，1行代码搞定
date: 2024-12-08 10:16:17
tags: [ 第三方库,自动化办公,pdf ]
---

<p align="center" id='进群-banner'>
    <a target="_blank" href='http://www.python4office.cn/wechat-group/'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2F%E6%8A%80%E6%9C%AF%E7%BE%A4.jpg" width="100%"/>
    </a>   
</p>

大家好，这里是程序员晚枫，今天给大家分享一个Python自动化办公的第三方库：popdf，专门用来处理PDF文件。

> 源码地址：https://github.com/CoderWanFeng/popdf

## 需求说明



## 上代码

首先，下载一个PDF自动化办公的专用库：``popdf``，命令如下，??

```
pip install popdf
```

然后直接1行代码搞定，??

```
# pip install popdf
import popdf

popdf.pdf2imgs(
            input_file=r'test_files/pdf/程序员晚枫.pdf',
            output_path='./test_files/img/')
```

#### 参数说明

- input_path：输入PDF的路径一般用于批量操作
- output_path：输出PDF的路径，一般用于批量操作
- input_file: 输入PDF的文件名，可以包含路径，一般用于单个文件的操作
- output_file：输出结果的文件名，可以包含路径，一般用于单个文件的操作
- input_file_list: 输入PDF的文件列表，一般用于批量操作，例如：合并2个pdf文件

## 相关课程

- [给小白的《50讲 · Python自动化办公》](https://www.bilibili.com/opus/857901377884520482?spm_id_from=333.999.0.0)
- [给小白的《10讲 · Python微信机器人》](https://www.bilibili.com/video/BV1S84y1m7xd/?spm_id_from=333.999.0.0)
- [给小白的《5讲 · Python实现OCR自动批量识别》](https://www.bilibili.com/video/BV13J4m1s7L7/?spm_id_from=333.999.0.0)
- [给小白的《6讲 · Python自动收发邮件》](https://www.bilibili.com/video/BV1pQ4y177nV/)

---



![](https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/ads/gzh/sub-py.jpg)


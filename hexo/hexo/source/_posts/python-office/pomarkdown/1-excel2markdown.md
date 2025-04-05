---
title: Excel转Markdown，1行代码搞定
date: 2024-12-08 10:16:17
tags: [ 第三方库,自动化办公,markdown ]
---

<p align="center" id='进群-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/0GrWWSQ8sKs-WA8WoN3Ztg'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2F%E6%8A%80%E6%9C%AF%E7%BE%A4.jpg" width="100%"/>
    </a>   
</p>

大家好，这里是程序员晚枫，今天给大家分享一个Python自动化办公的第三方库：``pomarkdown``，专门用来处理markdown文件。

> 源码地址：https://github.com/CoderWanFeng/pomarkdown

本文是该库的第1个功能：1行代码将Excel转成Markdown。

## 需求说明

我最近在出一套课程：Python + Excel，实现自动化办公。

其中写文档的过程中需要用到到Excel转成Markdown，方便我在文档中插入表格数据。

所以我就开发了这个功能：可以实现整个Excel的转换，也可以只转换其中的1个sheet。

## 上代码

首先，下载一个Markdown自动化办公的专用库：``pomarkdown``，命令如下，👇

```
pip install pomarkdown
```

然后直接1行代码搞定，👇

```
# pip install pomarkdown
import pomarkdown

pomarkdown.excel2markdown(
            input_file=r"./teset_files/test.xlsx",
            output_file=r"./teset_files/test.md",
            sheet_name='Sheet1'
        )
```

#### 参数说明

- input_file: 输入PDF的文件名，可以包含路径，一般用于单个文件的操作
- output_file：输出结果的文件名，可以包含路径，一般用于单个文件的操作
- input_path：输入PDF的路径一般用于批量操作，选填
- output_path：输出PDF的路径，一般用于批量操作，选填
- sheet_name：工作表名称，可以不填，默认是所有的sheet

## 相关课程

- [给小白的《50讲 · Python自动化办公》](https://www.bilibili.com/opus/857901377884520482?spm_id_from=333.999.0.0)
- [给小白的《10讲 · Python微信机器人》](https://www.bilibili.com/video/BV1S84y1m7xd/?spm_id_from=333.999.0.0)
- [给小白的《5讲 · Python实现OCR自动批量识别》](https://www.bilibili.com/video/BV13J4m1s7L7/?spm_id_from=333.999.0.0)
- [给小白的《6讲 · Python自动收发邮件》](https://www.bilibili.com/video/BV1pQ4y177nV/)

---



![](https://cos.python-office.com/ads/gzh/sub-py.jpg)


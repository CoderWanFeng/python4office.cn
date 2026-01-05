---
title: Python0基础，如何识别照片信息并且保存在Excel中？
date: 2023-04-25 22:32:02
tags: 1对1咨询
---

学习Python知识，实现：识别照片中的数字和姓名，保存到Excel中。

**类似功能演示，建议先看一下**：[发票识别，点我直达](https://www.bilibili.com/video/BV1eM411V7kL/?spm_id_from=333.999.0.0&vd_source=ca20bb8763fcb18660aa74d7a87234fa)


<!-- more -->

# 1、学习资料

学习分3步：
- [基础](https://www.bilibili.com/video/BV1MM4y1G76j/?spm_id_from=333.999.0.0)
- [pandas处理Excel](https://www.bilibili.com/video/BV1hk4y1C73S/?spm_id_from=333.999.0.0)
- [正则表达式](http://gk.link/a/113MD)


# 2、下载地址/文档

＞python &pycharm下载和安装：

- [视频教程](https://www.bilibili.com/video/BV1Q44y1u7rV/?spm_id_from=333.999.0.0)

- [下载地址](https://mp.weixin.qq.com/s/ktmQafdstwep_A5vae_Ymw)

# 3、代码Demo

所有ocr功能的python代码，见👉[https://www.python-office.com/video/poocr.html](https://www.python-office.com/video/poocr.html)

```
import poocr

poocr.ocr.GeneralAccurateOCR(img_path=r'd://你照片的存储位置//学生1的照片.jpg')

```
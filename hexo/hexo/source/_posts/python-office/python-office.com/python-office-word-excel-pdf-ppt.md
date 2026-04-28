---
title: 熬了个通宵，整理了22个Python自动化办公项目
date: 2023-08-07 00:12:40
tags: python-office
---



<!-- more -->
大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)，读者群👉[点我直达](https://www.python4office.cn/wechat-group/)

按照惯例，这个周末还是又是周六加班，周天更文。

这次给大家整理了22个Python自动化办公的功能，内容包含：word、excel、ppt、pdf这些主要的办公软件。




## 一、Word + 自动化办公 = poword

 | 序号 | 方法名            | 功能                | 视频（文档）                                        | 演示代码                                                                                                            |
 | ---- | ----------------- | ------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
 | 1    | merge4docx        | 合并Word文档        | [视频](https://www.bilibili.com/video/BV1Vo4y1q7i3) | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poword/%E5%90%88%E5%B9%B6word.py)             |
 | 2    | docx2doc/doc2docx | doc和docx，互相转换 | [视频](https://www.bilibili.com/video/BV1so4y1H7rj) | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poword/doc%E5%92%8Cdocx%E4%BA%92%E8%BD%AC.py) |
 | 3    | docx2pdf          | word 转 pdf         | [视频](https://www.bilibili.com/video/BV1pT4y1k7FH) | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poword/word%E8%BD%ACPDF.py)                   |

## 2、Excel + 自动化办公 = poexcel

| 序号 | 方法名          | 功能                                            | 视频（文档）                                                            | 演示代码                                                                                                                                                                                                                                          |
| ---- | --------------- | ----------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | fake2excel      | 批量生成Excel数据                               | [视频](https://www.bilibili.com/video/BV1wr4y1b7uk)                     | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poexcel/%E6%89%B9%E9%87%8F%E6%A8%A1%E6%8B%9F%E6%95%B0%E6%8D%AE.py)                                                                                                          |
| 2    | merge2excel     | 合并多个Excel到一个Excel的不同sheet中           | [视频](https://www.bilibili.com/video/BV1714y147Ao)                     | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poexcel/%E5%90%88%E5%B9%B6%E5%A4%9A%E4%B8%AAExcel%E5%88%B0%E4%B8%80%E4%B8%AAExcel%E7%9A%84%E4%B8%8D%E5%90%8Csheet%E4%B8%AD.py)                                              |
| 3    | sheet2excel     | 同一个excel里的不同sheet，拆分为不同的excel文件 | [视频](https://www.bilibili.com/video/BV1714y147Ao)                     | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poexcel/%E5%90%8C%E4%B8%80%E4%B8%AAexcel%E9%87%8C%E7%9A%84%E4%B8%8D%E5%90%8Csheet%EF%BC%8C%E6%8B%86%E5%88%86%E4%B8%BA%E4%B8%8D%E5%90%8C%E7%9A%84excel%E6%96%87%E4%BB%B6.py) |
| 4    | find_excel_data | 根据内容查询Excel                               | [视频](https://www.bilibili.com/video/BV1Bd4y1B7yr)                     | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poexcel/%E6%A0%B9%E6%8D%AE%E5%86%85%E5%AE%B9%EF%BC%8C%E6%9F%A5%E8%AF%A2Excel.py)                                                                                            |
| 5   | excel2pdf       | Excel转PDF                                      | [视频](https://www.bilibili.com/video/BV1A84y1N7or)                     | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poexcel/Excel%E8%BD%ACPDF.py)                                                                                                                                               |
| 6    | query4excel     | 把100个Excel中符合条件的数据，汇总到1个Excel里  | [视频](https://www.bilibili.com/video/BV1Hs4y1S7TT)                     | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poexcel/%E6%8A%8A100%E4%B8%AAExcel%E4%B8%AD%E7%AC%A6%E5%90%88%E6%9D%A1%E4%BB%B6%E7%9A%84%E6%95%B0%E6%8D%AE%EF%BC%8C%E6%B1%87%E6%80%BB%E5%88%B01%E4%B8%AAExcel%E9%87%8C.py)  |
| 7    | count4page      | 统计Excel打印出来有多少页                       | [文档](https://blog.csdn.net/weixin_42321517/article/details/131218163) | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poexcel/%E7%BB%9F%E8%AE%A1Excel%E6%89%93%E5%8D%B0%E5%87%BA%E6%9D%A5%E6%9C%89%E5%A4%9A%E5%B0%91%E9%A1%B5.py)                                                                 |
| 8  | merge2sheet      | 统计Excel打印出来有多少页                 | [文档](https://blog.csdn.net/weixin_42321517/article/details/131218163) | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poexcel/合并2个Excel的内容到一个sheet中.py)                                                                 |
| 9  | split_excel_by_column      | 根据指定的列，拆分Excel到不同的sheet         | [文档](https://blog.csdn.net/weixin_42321517/article/details/131218163) | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poexcel/根据指定的列，拆分excel.py)                                                                 |


## 3、PDF + 自动化办公

| 序号 | 方法名        | 功能         | 视频（文档）                                                            | 演示代码                                                                                                       |
| ---- | ------------- | ------------ | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 1    | add_watermark | PDF加水印    | [视频](https://www.bilibili.com/video/BV1Se411T7au)                     | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/popdf/PDF%E5%8A%A0%E6%B0%B4%E5%8D%B0.py) |
| 2    | txt2pdf       | TXT转PDF     | [文档](https://blog.csdn.net/weixin_42321517/article/details/130612189) | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/popdf/TXT%E8%BD%ACPDF.py)                |
| 3    | encrypt4pdf   | PDF加密      | [文档](https://blog.csdn.net/weixin_42321517/article/details/129963432) | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/popdf/PDF%E5%8A%A0%E5%AF%86.py)          |
| 4    | decrypt4pdf   | PDF解密      | [文档](https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA)               | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/popdf/PDF%E8%A7%A3%E5%AF%86.py)          |
| 5    | merge2pdf     | 合并PDF      | [文档](https://baijiahao.baidu.com/s?id=1733062611567959337)            | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/popdf/%E5%90%88%E5%B9%B6PDF.py)          |
| 6    | pdf2docx      | 💻PDF 转 Word | 💻[视频](https://www.bilibili.com/video/BV19D4y1i7Eu)                    | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/popdf/pdf%E8%BD%ACword.py)               |
| 7    | pdf2imgs      | PDF 转 图片  | 💻[文档](https://mp.weixin.qq.com/s/Ve5FH6q6ZqNbhUUG9RR8aw)              | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/popdf/pdf%E8%BD%AC%E5%9B%BE%E7%89%87.py) |

## 4、PPT + 自动化办公

| 序号 | 方法名    | 功能      | 视频（文档）                                                            | 演示代码                                                                                  |
| ---- | --------- | --------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 1    | ppt2pdf   | PPT转PDF  | [视频](https://www.bilibili.com/video/BV17Y411c792)                     | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poppt/ppt2pdf.py)   |
| 2    | ppt2img   | PPT转图片 | [视频](https://www.bilibili.com/video/BV1pu411Y7zz/)                    | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poppt/ppt2img.py)   |
| 3    | merge4ppt | 合并PPT   | [文档](https://blog.csdn.net/weixin_42321517/article/details/130877688) | [源码](https://github.com/CoderWanFeng/python-office/blob/master/demo/poppt/merge4ppt.py) |

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


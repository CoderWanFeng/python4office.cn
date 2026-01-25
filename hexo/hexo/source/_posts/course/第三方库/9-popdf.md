---
title: 减小20M！PDF自动化办公专用库：popdf，发布1.0.0版本
date: 2024-12-08 10:16:17
tags: [ 第三方库,自动化办公,pdf ]
---

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，今天给大家分享一个PDF自动化办公的第三方库：popdf。

> 源码地址：[https://github.com/CoderWanFeng/popdf](https://github.com/CoderWanFeng/popdf)

popdf 是一个 Python 自动化办公之 Excel 操作的第三方库，它来自于开源项目 python-office。

以下是 popdf 的一些基本使用方法：

### 安装 popdf

你可以通过 pip 命令来安装 popdf：

```bash
pip install -i https://mirrors.aliyun.com/pypi/simple/ popdf -U
```
## 更新说明

本次popdf 发布了1.0.0版本：重点有以下几个方面的更新：

- 精简了依赖库：重点封装了PyMuPDF和PyPDF2这2个库，去掉了其它处理PDF的库，减小了20M的存储空间。
- 精简了代码：删除了不必要的代码和注释，优化了代码结构。
- 统一了参数的命名方式：input_path、output_path、input_file、output_file...，下文有详细的介绍
- 完善了配套的课程，这部分课程会发布到B站：Python自动化办公社区，大家敬请期待~


## popdf 的功能

popdf 提供了多种功能，包括但不限于：

1. `add_text_watermark`：给 PDF 添加文本类型的水印。
2. `txt2pdf`：将 TXT 文件转换为 PDF。
3. `encrypt4pdf`：对 PDF 文件进行加密。
4. `decrypt4pdf`：对 PDF 文件进行解密。
5. `merge2pdf`：合并多个 PDF 文件。
6. `pdf2docx`：将 PDF 转换为 Word 文档。
7. `pdf2imgs`：将 PDF 转换为图片。
8. `split4pdf`：将 PDF 按指定页数拆分。

## 使用示例

以下是一些 popdf 功能的使用示例：

### PDF 转 Word

```python
import popdf

popdf.pdf2docx(input_file='程序员晚枫.pdf', output_path='输出的Word文件路径')
```

### 添加水印

```python
import popdf

popdf.add_text_watermark(input_file='你的PDF文件路径.pdf', point=(50, 50), text='水印内容')
```

请注意，具体的使用方法和参数可能会根据 popdf 的版本更新而有所变化，建议查看官方文档或 GitHub 仓库以获取最新的使用指南和示例代码。

### 参数说明

本次更新，还统一了参数的命名方式：

- input_path：输入PDF的路径一般用于批量操作
- output_path：输出PDF的路径，一般用于批量操作
- input_file: 输入PDF的文件名，可以包含路径，一般用于单个文件的操作
- output_file：输出结果的文件名，可以包含路径，一般用于单个文件的操作
- input_file_list: 输入PDF的文件列表，一般用于批量操作，例如：合并2个pdf文件

## 相关课程

- [给小白的《50讲 · Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)
- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg)
- [给小白的《5讲 · Python实现OCR自动批量识别》](https://www.python-office.com/course-002/5-poocr/5-poocr.html)

---




![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')




程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg)就能上手做AI项目。
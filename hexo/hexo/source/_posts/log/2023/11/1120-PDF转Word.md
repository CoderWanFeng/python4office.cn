---
title: PDF转Word，1行Python代码就够了，免费用
date: 2023-11-20 10:16:17
tags: 自动化办公
---

大家好，这里是程序员晚枫。

今年十一假期没出去旅游，在家里更新一套原创课程，点击查看👉[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/lOx4cAp9AllsCrhsUqVn8g)。

所有功能，都只需要1行代码，非常适合非程序员入门Python使用。

目前全网播放量直逼100w+，其中第4讲：PDF转Word，在百度的播放量已经达到了30w+。

**今天就免费给大家分享一下这一讲的代码。**



## 代码

PDF换Word功能，来自第三方库：``python-office``，免费下载命令：

```python
pip install python-office
```

下载之前，你需要安装Python和PyCharm，教程我也给大家准备好了：

- Python安装：https://www.python-office.com/course/docs/50-01-python.html
- PyCharm安装：https://www.python-office.com/course/docs/50-02-pycharm.html
- pip使用：https://www.python-office.com/course/docs/50-03-pip.html

```python
## Win用户
import office

office.pdf.pdf2docx(file_path=r'd://程序员晚枫的文件夹/小破站也叫程序员晚枫.pdf')

## Mac用户 & Linux用户
import popdf

popdf.pdf2docx(file_path=r'd://程序员晚枫的文件夹/小红薯也叫程序员晚枫.pdf')
```

## 注意事项

使用过程中，看到大家在视频评论区有一些问题，这里统一回复一下：

- 安全吗？这个代码没有任何联网功能，如果不放心，你甚至可以断网使用，代码不会上传你的文件。
- 扫描件PDF可以转换吗？不支持。
- 代码使用免费吗？你直接复制这篇文章的代码就行了，免费。

----


大家在使用代码过程中有任何问题，都欢迎在评论区和我交流哟~👇


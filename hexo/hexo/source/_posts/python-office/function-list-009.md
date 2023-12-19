---
title: 5个常用的Python第三方库，小白也能用
date: 2023-10-31 01:25:17
tags: 第三方库
---


## pathlib
## uiautomation
## poocr
## pandas

经常有小伙伴问我学Python数据分析应该学习哪个库，我的回复里一定会有``pandas``这个库。

pandas，官方解释，这个名字是**pandas - Python Data Analysis Library**的缩写。

里面集成了

## PIL
PIL，全称 Python Imaging Library，是 Python 平台一个功能非常强大而且简单易用的图像处理库。但是，由于 PIL 仅支持到Python 2.7，加上年久失修，于是一群志愿者在 PIL 的基础上创建了兼容 Python 3 的版本，名字叫 Pillow ，我们可以通过安装 Pillow 来使用 PIL。 
```python
打开、保存、显示图片
from PIL import Image

image = Image.open('2092.jpg')
image.show()
image.save('1.jpg')
print(image.mode, image.size, image.format)
# RGB (481, 321) JPEG
# mode 属性为图片的模式，RGB 代表彩色图像，L 代表光照图像也即灰度图像等
# size 属性为图片的大小(宽度，长度)
```




-------

以上所有仓库的功能介绍，我都加入了原创课程:[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/tKlzVee4kmJk4dGfKvVnFQ)都是1行Python代码就能实现的，适合纯小白的课程，需要可以加入学习哟~

- 加入学习👉[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/tKlzVee4kmJk4dGfKvVnFQ)

大家学习 或 使用代码过程中，有任何问题，都可以加入读者群交流哟~👇


![](https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/0816.jpg)

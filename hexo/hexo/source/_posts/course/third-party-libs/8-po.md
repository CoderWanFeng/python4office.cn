---
title: 26.7万下载！Python自动化办公专用库：python-office，发布1.0.0版本
date: "2024-12-4 00:41:49"
tags: ["第三方库", "pip"]
cover: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop"
---




<!-- more -->

![26.7万下载！Python自动化办公专用库：python-office，发布1.0.0版本](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)



![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93/%E5%B0%81%E9%9D%A2/%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93.jpg)

大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)。

今天给大家分享的第三方库是**Python自动化办公的专用库**：python-office。

> 从2022年发布到现在，经过40多个版本的迭代，这个库的下载量已经超过26.7万次，并且在2024年12月4日终于发布了1.0.0版本。

我们一起来看一下它的高频使用案例。

## 下载

作为一个为Python新人开发的第三方库，它的下载方式非常简单，只需要在命令行中输入以下命令即可：

```python
pip install python-office==1.0.0
```

> 这里要说一下，本次发布的1.0.0版本，和上一个版本相比，最大的区别就是它去掉了所有运行时的广告。以前版本刚发布的时候需要一些广告来更好的推广这个库，现在有越来越多的人使用它，就不再需要广告了，非常的清爽。





## 高频使用案例

python-office里的功能非常丰富，这里给大家介绍几个常用的功能。



### PDF转Word
```python
import office

office.pdf.pdf2word('test.pdf', 'test.docx')

```

### 图片加水印

```python
import office

office.image.add_watermark(file='./test_files/add_watermark/程序员晚枫-2.jpg',
                           mark='程序员晚枫',
                           output_path=r'./test_files/add_watermark/mark_img')
```

### 从视频里提取音频

```python
import office

office.video.mark2video(video_path=r'D:\download\baiduyun\图片添加水印.mp4', output_path=r'D:\download\baiduyun\out')

```

## ToDoList

2024年的最后一个月，本仓库也加入了atomgit的G-Star毕业项目，这意味着这个库的维护将会更加的完善。

接下来除了继续开发新的功能外，还会重点在以下几个方面进行优化：

- 写出所有功能的演示代码和单元测试。开发了3年，这个库的代码量已经非常大了，但是没有单元测试和演示代码，这对后续的维护和扩展都是非常不利的。
- 优化文件的处理方式，提高性能。例如有些依赖库的函数名已经变了，这就需要我们及时更新代码。
- 增加exe版本里的功能，之前做了一个exe的测试版本，但是没有时间和精力去完善它。

大家在使用这个库的过程中，有什么问题或者建议，欢迎在评论区留言。

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


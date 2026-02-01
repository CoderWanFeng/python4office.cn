---
title: 用Python模拟海量Excel数据，你的数据分析工作任务有救了
date: 2025-07-27 23:41:49
tags: [50讲Python自动化办公]
---
[![14块读者交流群.png](https://raw.atomgit.com/user-images/assets/5027920/48edc8fa-6d2e-4eca-9e14-d71638eadb55/14块读者交流群.png '14块读者交流群.png')](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502200&idx=1&sn=7e543675545ac6622123af6009fdebce&scene=21#wechat_redirect)

大家好，我是晚枫，用通俗易懂的方式，教小白学python。


前几年我还在努力学习爬虫的时候，我的培训老师给我们实操的练手项目就有自动将爬取到的数据存储到Excel表格中。

也是从那个时候开始，我就觉得用Python实现办公自动化真的太牛逼了。

不过那个时候我没想过去系统学习一下Python办公自动化。

时隔几年，命运仿佛给我开了一个玩笑——我学爬虫没找到工作，但是我又一次和晚枫老师合作起来做起了销售和课程研发。

而晚枫老师就是Python自动化办公领域的头部编程博主。

他真的很厉害，白天上班，晚上抽空做自媒体，6年以来没怎么休息过，所以我真的很赞叹他开发的办公自动化的课程。



## -01-


以前学爬虫，是为了获取数据，有些公司的爬虫还是专门为了给数据分析做准备。

你们可以想象一下这样的一个场景：

程序员用爬虫去网页上爬取数据，然后将是否爬取到结果的状态发送到邮件中，除此之外还能将爬取到的结果数据格式化之后存储到Excel表格中。

这其实就是办公自动化呀，难道不是很省心省力嘛！

所以，我们认为用Python创建Excel表格这个场景需求还是蛮大的。

那今天我们就讲一下怎么实现用Python的方式创建Excel表格，并且用一行代码模拟真实数据。

即使是模拟10w+的数据也只需要一行代码就能实现。

首先，我想需要给大家明确的一点是，为什么要用Python技术模拟出大量真实度很高的数据呢？

我想聪明的小伙伴肯定能想到，没错，就是数据分析。

其实，我们不管是用爬虫爬取数据或者用Python模拟数据，最终的目的都是为了获取大量的数据。

那有了数据我们就可以进行数据分析！

所以，今天这篇内容对于想做数据分析的小伙伴来说很重要，希望大家保持专注，我马上就给大家看一下具体该如何用代码创建Excel表格以及模拟大量数据。



## -02-


**代码实现如下：**
```
import office

# 代码、文档，见置顶评论
# 能模拟的数据有哪些？http://python4office.cn/python-office/fake2excel/

# 普通
office.excel.fake2excel(columns=['name', 'company', 'phone_number'],
                        rows=10,
                        path=r'./test_files/50-07-fake2excel/中文-1.xlsx')

```
参数解释：
```
columns: 列名。可以模拟的列有：http://python4office.cn/python-office/fake2excel/
rows: 生成多少行数据。默认值：1
path: 生成的Excel的位置和名称。
language: 数据用什么语言，默认是中文，可以填english
```

说句实话，今天这个代码的参数部分有些复杂，其实也不算是复杂吧，就是可选参数比较多，也因此它更灵活一些。

大家有时间可以去研究一下所有的参数，尤其是columns这个参数，这样对你模拟数据会有很大的帮助。



## -03-


我相信如果你有能力将这个代码中的参数熟练掌握，那你应对一些简单的数据分析任务会信手拈来。

不过，数据分析的一个最大的原则就是数据要保证真实性，所以仅仅靠Python模拟数据还差点意思。

但这个问题不在我们的讨论范围之内，如果你感兴趣可以去学下爬虫。

像上面介绍的Python创建Excel表格和模拟数据的需求开发就来源于《50讲Python自动化办公》这门课程。

现在课程已经更新完毕了，但是我们仍然在开发更多的功能，只要有用户提需求，我们就开发和实现。

而且，这门课程的每一节课都包含：视频、文档、代码、软件和答疑群。

晚枫老师的课程体系和交付真的很完善了，大家可以放心跟着学习。



## 写在最后：



我们这套课程具备以下3个特点：

第一，这门课程适合小白学习，不需要学习复杂的编程知识，拿来就用。

第二，内容很丰富，涵盖热门的自动化办公需求。

第三，所有功能只需要一行代码就能实现问题的解决。

所以，如果你对这门[《给小白的50讲 · Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)感兴趣，可以点击左边蓝字报名咨询。

![image.png](https://raw.atomgit.com/user-images/assets/5027920/df7121f7-192b-42e5-a627-fbe859fa12d2/image.png 'image.png')


如果你对这门课程还有想了解的，或者购买后有问题，可以加我微信咨询，**wfdev7**，备注**888**。

<center>

[一个Python小白的学习之路，附入门课程](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502329&idx=1&sn=d8ffdbd41689302b30fa4b1f985f23cc&scene=21#wechat_redirect)

[Python的包管理：为什么第三方包会安装失败](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502378&idx=1&sn=c370c6fa85ab74560d3d01917fc28535&scene=21#wechat_redirect)

[一行代码教你白嫖PDF和Word文件相互转换](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502407&idx=1&sn=4b375aaa3f71d008d7a2879be02951cc&scene=21#wechat_redirect)

[还在使用PPT插件转长图吗？今天教你一行代码解决这个转换的问题](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502431&idx=1&sn=0636d23d00ccea1f1ee2f2f495e876cf&scene=21#wechat_redirect)
  
<center>

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)就能上手做AI项目。
---
title: 小白神器：复制粘贴这行Python，你的PDF立刻加密无人能开
date: 2025-07-29 23:41:49
tags: [50讲Python自动化办公]
---
[![14块读者交流群.png](https://raw.atomgit.com/user-images/assets/5027920/48edc8fa-6d2e-4eca-9e14-d71638eadb55/14块读者交流群.png '14块读者交流群.png')](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502200&idx=1&sn=7e543675545ac6622123af6009fdebce&scene=21#wechat_redirect)

大家好，我是晚枫，用通俗易懂的方式，教小白学python。

今天，我们一起来聊一聊如何用Python技术的手段，一行代码实现给PDF文件加密。

可能大部分小伙伴遇到给PDF文件加密的问题时，都是选择下载一个PDF编辑器的软件来实现该功能。

但是，这个功能对于软件来说，很有可能是收费才能用的，因此很多人都不喜欢用这个软件来加密。

那今天我要给大家讲的实现该功能的方法是离线在本地且免费使用的加密方法，而且只需要一行代码就能实现哦。

怎么样，是不是很好奇我们这个一行代码是如何写的呢？

别急，下面我们会给你娓娓道来。

## 01

虽然，我们这个功能的需求很好理解，就是给PDF文件加密，但是关键是我们如何用Python代码来实现。

好吧，这里就不给大家卖关子了，我们直接看代码吧。

代码演示：
```
import office

# 将pdf文件加密
# path：待加密pdf文件路径
# password：输出pdf文件
# output_path：输出pdf文件路径
office.pdf.encrypt4pdf(
    path=r"E:\program\python-office\pdf",
    password="123@#",
)
```
参数解释：
```
path：待加密pdf文件路径
password：输出pdf文件
```
好的，通过代码演示和参数解释，我相信你一定已经学会了该如何使用我们这个脚本。

如果你还没有学会，那就照着我们的代码去手动敲一遍，感受一下敲代码的美妙，等你敲个几遍，相信你就一定能记住这一行代码了。

但是，这里我还是要提醒一下：

要想让这一行代码正常运行，你们需要把运行代码的环境给安装配置好。

不知道如何配置环境的可以看——给小白的《50讲Python自动化办公》的前面3讲内容，我们真的是手把手地教你如何配置环境的，相信我，一点都不难哈。

## 02

OK，到这里我要告诉大家的是，今天这篇文章教给大家的代码的视频讲解都在给小白的《50讲Python自动化办公》这套课程的第38讲内容中了，对讲解视频感兴趣的可以去本套课程中学习一下。

这里不得不说的一点是，我们这个课程每一讲都是独立的案例讲解。

所以，你们完全可以根据自己的兴趣找到自己感兴趣的内容优先学习，这个不会影响学习效果的。

当然了，我们这门课程的每一节课都包含：视频、文档、代码、软件和答疑群。

所以你们完全不用担心学不会的问题，可以说，只要你认真跟着学习，认真练习敲代码，没有学不会的可能。

## 写在最后：

我们这套给小白的《50讲Python自动化办公》课程具备以下3个特点：

第一，这门课程适合小白学习，不需要学习复杂的编程知识，拿来就用。
第二，内容很丰富，涵盖热门的自动化办公需求。

第三，所有功能只需要一行代码就能实现问题的解决。

所以，如果你对这门[《给小白的50讲 · Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)感兴趣，可以点击左边蓝字报名咨询。

![image.png](https://raw.atomgit.com/user-images/assets/5027920/df7121f7-192b-42e5-a627-fbe859fa12d2/image.png 'image.png')
如果你对这门课程还有想了解的，或者购买后有问题，可以加我微信咨询，**wfdev7**，备注**888**。

<center>

[一行代码教你白嫖PDF和Word文件相互转换](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502407&idx=1&sn=4b375aaa3f71d008d7a2879be02951cc&scene=21#wechat_redirect)

[还在使用PPT插件转长图吗？今天教你一行代码解决这个转换的问题](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502431&idx=1&sn=0636d23d00ccea1f1ee2f2f495e876cf&scene=21#wechat_redirect)
  
[用Python模拟海量Excel数据，你的数据分析工作任务有救了](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502439&idx=1&sn=a9c1308bbcfd2ac39fbabab4bacded74&scene=21#wechat_redirect)

[群太多管理不过来？试试这个微信机器人的智能回复功能](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502446&idx=1&sn=05ddaf0b55ccb2a35cc89120b4032a43&scene=21#wechat_redirect)

[你忘记了文件名称？那我来教你用内容搜索来找到目标文件](https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&mid=2247502454&idx=1&sn=0473e26f4a63d132b0a61c1211bce497&scene=21#wechat_redirect)

  
<center>


## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
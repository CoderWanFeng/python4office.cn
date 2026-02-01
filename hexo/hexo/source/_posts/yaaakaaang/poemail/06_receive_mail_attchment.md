---
title: 批量下载邮件的附件
date: 2025-05-14 12:50:32
tags: [poemail]
---

<span style="font-size:20px;"><span style="color:#66a3e0;">如果你是教师或培训师，会收到大量学生提交的作业或项目文件； </span></span>

<span style="font-size:20px;"><span style="color:#66a3e0;">如果你参与了一个项目，团队成员会给你发送大量设计稿、文档等； </span></span>

<span style="font-size:20px;"><span style="color:#66a3e0;">如果你是一家公司的财务，会收到大量包含发票、财务报表的邮件； </span></span>

<span style="font-size:20px;"><span style="color:#66a3e0;">无论是什么职业，如果你有大量的邮件附件需要下载，那么这篇文章会为你节省大把的时间去做你想做的事！ </span></span>

#  一、打开文件

双击鼠标左键第六个文件

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747197779534.jpg)

#  二、修改授权码和qq邮箱

打开文件后，把这两行分别改为你的授权码和qq邮箱

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747197845098.jpg)

就像这样

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747197942432(1).jpg)

#  三、指定下载位置

接下来就是指定把附件下载到哪了，比如你要下载到 `E:\poemail\tests`这个文件夹下

你就把 ` output_path=`的后面修改为 `r'E:\poemail\tests'`，注意仍然是用英文引号

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747198100502.jpg)

#  四、指定下载未读邮件的附件，还是全部邮件的附件

如果是要下载未读邮件的附件

就把 ` status=`的后面修改为 `"UNSEEN"`，就像这样

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747198289009.jpg)

如果是要下载全部邮件的附件
就把 ` status=`的后面修改为 `"ALL"`，就像这样

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747198428116.jpg)

#  五、运行代码

鼠标移到第六个文件，然后鼠标右键单击

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747198529061.jpg)

找到有三角形这行，鼠标左键单击它就可以了。

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747198578410.jpg)

#  六、运行效果

首先可以看到我这里有两封未读邮件

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747206494057.jpg)

我们在这里设置为  UNSEEN，然后日志显示成功

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747206720575.jpg)

接下来打开 E:\poemail\tests 这个文件夹，会看见有以  序号 + 发送人的邮箱地址命名的文件夹

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747206818413.jpg)

打开文件夹能看见附件被正确的下载下来了

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747206935914.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)就能上手做AI项目。
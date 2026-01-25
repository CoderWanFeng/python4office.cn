---
title: 收集微信群指定成员消息
date: 2025-05-22 13:05:32
tags: [PyOfficeRobot]
---


#  一、填写微信群名称

找到左边【收集群指定人发的消息】，鼠标左键双击它

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1748242121861.jpg)

然后在这里填写微信群的名字

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747990880948.jpg)

# 二、填写好友备注

收集指定成员的聊天记录，这里面就填上你对他的备注

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747991158807.jpg)

多个成员之间用英文逗号隔开，比如

`names=['张三',  '李四',  '王五']`

#  三、填写收集量

这个数字表示在微信群的聊天界面，鼠标向上滚动的次数

滚动的越多，收集的聊天记录越多

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747991485141.jpg)

注意：在运行代码前最好在要收集的群里发一条消息，让这个群位于消息列表前面

因为如果这个群聊在消息列表的靠后处，鼠标有可能移不到有效地点

就会导致不能向上滚动滑轮，加载更多聊天记录。（置顶群消息也不行）

#  四、运行代码

单击鼠标右键左边第九个文件

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747997572191.jpg)

然后找到有三角形这行，鼠标左键单击它

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747995241986.jpg)

#  五、运行效果

日志显示运行成功

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747997401583.jpg)

这里也多了一个文件

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747997458920.jpg)

打开可以看到收集的聊天记录

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747997532252.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg)就能上手做AI项目。
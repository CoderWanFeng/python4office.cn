---
title: 自定义功能
date: 2025-05-26 13:05:32
tags: [PyOfficeRobot]
---

#  一、自定义功能

找到左边第六个文件，鼠标左键双击它

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1748237589574.jpg)

自定义功能，比如当别人发送“来个密码”时，我们给他生成一个密码

我们就在 keywords 的括号里面新增一行  `"来个密码": office.tools.passwordtools(),`

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1748237799119.jpg)

我们要自动回复谁的微信，就在这里填写谁的微信昵称

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1748238461852.jpg)

#  二、安装库

我们可以看到这里有一个红色的下划线，代表我们还没有安装 office 这个库

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/04646e6e64c36be832730c446fbd86b.png)

生成密码这个功能需要先安装 office

点击左下角这个矩形 

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1748237742514.jpg)

然后输入 `pip install python-office`  接着按下回车

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1748240131828.jpg)

可能会安装得有点久。出现 Successfully 就表示安装成功了

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1748240298919.jpg)

然后就可以把这个关闭了

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1748240333734.jpg)

#  三、运行代码

找到左边第六个文件，鼠标右键单击它

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1748238549821.jpg)

然后找到有三角形这行，鼠标左键单击它

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1748238592073.jpg)

# 四、运行效果

这时候  Yaaakaaang 给我发 “来个密码”

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1748240455187.png)

我就会自动随机生成一个密码，并且回复

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)就能上手做AI项目。
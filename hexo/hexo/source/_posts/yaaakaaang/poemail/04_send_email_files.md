---
title: 发送带有附件的邮件
date: 2025-05-13 20:50:32
tags: [poemail]
---

#  一、打开文件

双击鼠标左键第四个文件

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747139002082.jpg)

#  二、修改授权码和qq邮箱

打开文件后，前面这4行还是按照上一章的方法修改

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747139243114.jpg)

#  三、指定要发送的附件

重点是这里，把这里改为你要发送的附件

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747139378466.jpg)

比如要发送的附件在 E:\poemail\tests\test_files，文件名+后缀名 是[ 测试附件.docx]

那么就写成 `r'E:\poemail\tests\test_files\测试附件.docx'`

就像这样

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747139670589.jpg)

如果有多个附件，比如第二个附件在 E:\poemail\tests\test_files，文件名+后缀名 是[ 程序员晚枫.doc]

就把鼠标移到反中括号 ] 的前一位，输入 `, r'E:\poemail\tests\test_files\程序员晚枫.doc'`

注意，r 前面那个符号是英文的逗号

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747140018401.jpg)

#  四、运行代码

鼠标移到第四个文件，然后鼠标右键单击

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747140169981.jpg)

找到有三角形这行，鼠标左键单击它就可以了。

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747140201231.jpg)

#  五、运行效果
运行日志显示成功

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747204448394.jpg)

然后我们再看网页邮箱有一封带附件的未读邮件

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747204569143(1).jpg)

点开查看详细信息

![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1747204667553.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
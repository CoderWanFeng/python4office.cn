---
title: 发送纯文字邮件
date: 2025-05-13 19:50:32
tags: [poemail]
---

#  一、填写qq邮箱授权码
打开文件 poemail/course/code/test_files/3-send_mail_content.py

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747137158510.jpg)

鼠标移到这个括号后面，然后按下键盘的删除键，一直删到 “=”后面。

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747137516383(1).jpg)

然后你们把上一章得到的qq邮箱授权码，用英文的引号包裹住，写在后面，就像这样。

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747137790647.jpg)


#  二、填写你的qq邮箱授

用刚才的方法，把这里改成你的 qq邮箱

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747137890748(1).jpg)

就像这样

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747138008245.jpg)

#  三、填写收件人qq邮箱授

还是老方法修改第三行

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747138071396.jpg)

比如

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747138211124(1).jpg)

#  四、填写抄送人qq邮箱授

正文和主题不用多说了，不过这里的抄送人还是要多提一嘴

这里框起来的就是抄送人的qq邮箱

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747138306004.jpg)

如果需要抄送人的话，我们还需要做一点修改。

首先把鼠标移到反括号 )  的前一位，然后输入 `, msg_cc=msg_cc`  

注意，有一个逗号

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747138471730.jpg)

就像这样

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747138616552.jpg)

#  五、运行代码

鼠标移到第三个文件，然后鼠标右键单击

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747138727482.jpg)

找到有三角形这行，鼠标左键单击它就可以了。

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747138812298.jpg)
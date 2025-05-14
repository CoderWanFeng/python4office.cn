---
title: 批量发送带附件邮件
date: 2025-05-14 10:50:32
tags: [poemail]
---

<span style="font-size:20px;"><span style="color:#66a3e0;">昨天收到一个客户的咨询，可以群发邮件吗？而且还要发送附件。 </span></span>

<span style="font-size:20px;"><span style="color:#66a3e0;">我就想到一定还有很多人被这事困扰着，所以我今天写了这篇文章。下面就让我们从既费时，又容易出错的重复性工作中解脱出来吧！ </span></span>


#  一、打开文件
双击鼠标左键第五个文件

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747191490267.jpg)

#  二、修改授权码和qq邮箱

前面这两行改成你的授权码和qq邮箱

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747191574272.jpg)

#  三、批量发送给多个收件人

下面就是实现批量发送的关键步骤了

如果有多个收件人，比如 `123...456@qq.com` 和 `123...789@qq.com`

就要修改第三行，首先用英文的引号将所有邮箱包裹，然后用英文分号分隔

`"123...456@qq.com; 123...789@qq.com"`

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747192704157.jpg)

#  四、发送时指定多个抄送人

如果有多个抄送人，比如 `456...456@qq.com` 和 `456...789@qq.com`

也是一样的操作修改第四行

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747192940607.png)

#  五、运行代码

鼠标移到第五个文件，然后鼠标右键单击

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747193030052.jpg)

找到有三角形这行，鼠标左键单击它就可以了。

![](https://raw.gitcode.com/yaaakaaang/pic/raw/main/1747193113909.jpg)

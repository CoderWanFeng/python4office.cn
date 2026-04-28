---
title: C语言学习笔记
date: 2025-06-29 8:56:36
tags: [wwp,c语言]
---

<!-- more -->
# 内存对齐
本质：用空间换时间

![image.png](https://raw.atomgit.com/user-images/assets/5027920/73fa2315-5683-4c70-8109-8fd8cedb1dcd/image.png)
![image.png](https://raw.atomgit.com/user-images/assets/5027920/8c94445b-4d76-4e95-a2c1-e06f4e48adc4/image.png)
**eg：该结构体中最大的数据类型是double 8个字节 目前算完以后占20个字节，做偏移，距离20最近的8的整数倍就是24**

备注：对齐模数可以改为2的n次方

# 光标
![image.png](https://raw.atomgit.com/user-images/assets/5027920/12cbde89-8a83-4c40-bcc8-81196e54e24f/image.png)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


---
title: C语言学习笔记
date: 2025-06-29 8:56:36
tags: [wwp,c语言]
---

# 内存对齐
本质：用空间换时间

![image.png](https://raw.atomgit.com/user-images/assets/5027920/73fa2315-5683-4c70-8109-8fd8cedb1dcd/image.png 'image.png')
![image.png](https://raw.atomgit.com/user-images/assets/5027920/8c94445b-4d76-4e95-a2c1-e06f4e48adc4/image.png 'image.png')
**eg：该结构体中最大的数据类型是double 8个字节 目前算完以后占20个字节，做偏移，距离20最近的8的整数倍就是24**

备注：对齐模数可以改为2的n次方

# 光标
![image.png](https://raw.atomgit.com/user-images/assets/5027920/12cbde89-8a83-4c40-bcc8-81196e54e24f/image.png 'image.png')

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)就能上手做AI项目。
---
title: C语言学习笔记
date: 2025-06-25 5:56:36
tags: [wwp,C语言]
---

# 一维数组数组名
取地址
1. 对数组名取地址 步长 整个数组长度
2.对数组名sizeof
3.除啦以上两个情况，其他情况都是都是指向一个元素的指针

指针常量
int * const p 类型
数组下标可以是负数

![image.png](https://raw.atomgit.com/user-images/assets/5027920/fb190a0e-8501-4a5f-bf20-49b9575cd3b4/image.png 'image.png')

本质   *（p-1）

![image.png](https://raw.atomgit.com/user-images/assets/5027920/afe84b5b-4d90-4f5e-bb73-2b1504fce7d5/image.png 'image.png')

# 二维数组
![image.png](https://raw.atomgit.com/user-images/assets/5027920/6d4dd182-28f5-46fe-8e88-237e7928c530/image.png 'image.png')


![image.png](https://raw.atomgit.com/user-images/assets/5027920/73b546d5-3815-4a4d-918c-825bc214a7a5/image.png 'image.png')
备注：在栈区开辟空间并赋值不会出现这种问题
在堆区开辟空间 并赋值 在释放空间的时候会造成内容泄露和内存空间重复释放
这是因为 p1=p2 是浅拷贝 又叫逐字节拷贝 需要解决就要手动赋值 在创建一个新的空间 并进行赋值操作

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
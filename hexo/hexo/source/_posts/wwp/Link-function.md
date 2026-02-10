---
title: c语言学习笔记
date: 2025-07-01 9:00:00
tags: [wwp,c语言]
---


# 链表
分类：单向链表 双向链表 循环链表（单向 双向）
按内存分类： 静态链表（分配在栈区）   动态链表（分配在堆区） 

定义一个链表的结构体

**备注：链表的增删改查的操作几乎都是用两个指针来实现，有时还用会用到第三个指针充当中间变量来完成**
~~~
struct LinkNode 
{
		int num; //数据域
        struct LinkNode * next; //指针域
}
~~~
![image.png](https://raw.atomgit.com/user-images/assets/5027920/def16d0a-765b-4fef-b2ed-a3c85d27eed6/image.png 'image.png')

**清空链表**
![image.png](https://raw.atomgit.com/user-images/assets/5027920/06ea1861-da91-4013-8009-a2e23a08a5cb/image.png 'image.png')

# 函数指针的定义
![image.png](https://raw.atomgit.com/user-images/assets/5027920/20fc133f-f60e-4e7d-bd95-bfb20255874e/image.png 'image.png')
备注： func 是自定义的函数名字

![image.png](https://raw.atomgit.com/user-images/assets/5027920/41d82ad5-364a-4b43-a503-ffc1f1db6c89/image.png 'image.png')

![image.png](https://raw.atomgit.com/user-images/assets/5027920/77392c1e-c863-408f-bfc9-2f9f0020bcc1/image.png 'image.png')

# 函数指针数组的定义
![image.png](https://raw.atomgit.com/user-images/assets/5027920/22d0250f-9f15-417f-83d3-88b762a12e48/image.png 'image.png')

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)
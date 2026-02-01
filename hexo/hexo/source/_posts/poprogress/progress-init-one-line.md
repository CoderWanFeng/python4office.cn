---
title: 给程序加个进度条吧！1行Python代码，快速搞定~
date: 2023-03-23 22:11:12
tags: 开源
---



![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/progress/1/cover.jpg)


大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。

你在写代码的过程中，有没有遇到过以下问题？

- 已经写好的程序，想看看程序执行的进度？

- 在写代码批量处理文件的时候，如何显示现在处理到第几个文件了？

👆如上图所示的进度条是一个最好的解决方法，怎么在不修改原来代码的情况下，快速给程序加一个进度条呢？

今天我们来学习一个最简单的方法~

## 1、先上代码

下载进度条的第三方库。

```python
pip install poprogress
```

使用这个库，快速制作进度条

```python
from poprogress import simple_progress

a_list = [1, 2, 3, 4, 5, 6, 7, 8]*100000000

for a in simple_progress(a_list。desc='这个参数是进度条的说明，可以不填'):
    pass
```

效果如下👇。

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/progress/1/Snipaste_2023-03-23_20-29-28.jpg)

## 2、使用说明

细心的你一定发现，这个进度条代码，对我们平时写的代码没有伤害。

平时我们可能会直接循环``list``，而进度条是把这个``list``用``simple_progress()``包起来，在进行循环。

```python
# 平时的代码：
for i in list:
  pass
  
# 加了进度条的代码
for i in simple_progress(list):
  pass
```

所以如果你已经写好的代码，想加上一个进度条，也直接把``for``循环后面的内容，直接用``simple_progress()``包起来就行了~程序员不需要做任何改变。

是不是非常简单？

## 3、实现原理

想进一步了解的同学，可以看一下源码，研究一下它的实现原理：

- ⭐GitHub：https://github.com/CoderWanFeng/poprogress

---




## 说干就干

接下来我的账号会转向**以AI编程为中心，分享和AI有关的内容**。

和2019年做自动化办公，录制了一套自动化办公的教程，并且围绕这套教程更新了接近5年类似。我也在整理了自己的经验后，打造了一套全新的课程：**给小白的《30讲 · AI编程训练营》**。

- 面向小白：不需要会编程，因为AI本来就是为了解放大脑，加入以后，我会循序渐进的带大家学习AI编程
- 项目为主：这也是我一直以来的风格，**大家都不是深入研究大模型的，用的溜更重要，对吧？**
- 内容详实：从必备的原理到实践，从文档到视频、软件，有关AI编程有关的，我能接触到的所有内容，我都会制作分享
- 特色内容：**BAT的合作资源，各家大厂的AI福利，我作为一个编程博主都能拿到的**，作为这套核心课程的学员，我也会毫无保留的分享

以下是这次课程的目录（只展示主干必学部分）：



<p align="center" id='AI编程训练营'>
    <a target="_blank" href='https://www.python-office.com/course-002/AICoding/version-001/all.html'>
    <img src="https://raw.gitcode.com/user-images/assets/5027920/1f021b1e-f401-4afa-bfa5-f1b289d351a7/599.jpg" />
    </a>   
</p>




目前计划的课程价格是299元。预售留的50个名额已经秒空了30个。

这也是我接下来的重点破局项目，现在价格是**199元**，最后再剩下的20个名额，满人后就恢复原价299了。大家想学习就加直接我微信：**wfdev7**，备注：AI编程

<p align="center" id='30个名额'>
    <a target="_blank" href='http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/71bd2ff3-ac85-43a4-8288-164cc66e119d/image.png" width="350" height='600'/>
    </a>   
</p>


<p align="center" id='老粉的认可'>
    <a target="_blank" href='http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/6d5a3b73-0367-455a-ab69-4b47ca2646af/image.png" width="350" height='600'/>
    </a>   
</p>

<p align="center" id='学习群的氛围'>
    <a target="_blank" href='http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/b89b206c-8f44-4e1b-a9e3-4f168531b9da/image.png" width="350" height='600'/>
    </a>   
</p>

## 常见问题

Q：不会编程可以学吗？
<br/>A：可以学习，我的粉丝大多是编程小白。

Q：学习形式是什么？
<br/>A：按顺序看视频，边学边练。文档用来扩展知识，课程群用来分享资料和答疑。

Q：老粉丝有其他优惠吗？
<br/>A：我所有付过费的老粉丝，都有额外的降价优惠，最低我也会送一本书，作为再次支持的感谢。如果是已经购买了这套课程，再想学其它课程，也会有专属的优惠。

Q：有其他更高级的课程吗？
<br/>A：我后续打算还会出：AI编程出海、智能体、工作流、AI创作营，都会以本次的AI编程为基础。





程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)就能上手做AI项目。
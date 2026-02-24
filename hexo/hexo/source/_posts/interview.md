---
title: Python面试题
date: 2021-12-28 10:40:08
tags: [程序员,面试]
---


<p align="center">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://raw.atomgit.com/CoderWanFeng1/website/raw/main/github-nav.jpg" alt="github license"/>
    </a>   
</p>
<p align="center">
	<strong>🍬python for office</strong>
</p>
<p align="center">
	👉 <a href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>


<p align="center" name="图标-github">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/contributors/CoderWanFeng/python-office" alt="github contributors"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/forks/CoderWanFeng/python-office" alt="github forks"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues/CoderWanFeng/python-office" alt="github issues"/>
    </a>	
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues-pr/CoderWanFeng/python-office" alt="github license"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/license/CoderWanFeng/python-office" alt="github license"/>
    </a>   
</p>

<p align="center" name="gitee">
	<a target="_blank" href='https://gitee.com/CoderWanFeng/python-office/'>
		<img src='https://gitee.com/CoderWanFeng/python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
		<img src="https://gitee.com/CoderWanFeng/python-office/badge/fork.svg?theme=white" alt="gitee fork"/>
	</a>
	<a href="https://mp.weixin.qq.com/s/yaSmFKO3RrBpyanW3nvRAQ">
	<img src="https://img.shields.io/badge/QQ-163434413-orange"/></a>
</p>



最近在面试Python程序员的工作，顺手把自己在学习和面试过程中遇到的问题，整理在这里。
内容种类比较多，我把它们分为5大类：Python、算法和数据结构、数据库和调优、前端、职业规划。
> 内容持续更新中，如需深入沟通，请添加我的微信：[python-office](http://www.python4office.cn/wechat-qrcode/)，备注：面试

### Python

<!-- more -->

- Python里有哪些基本数据类型？
    - https://www.runoob.com/python3/python3-data-type.html
- Python中进程、线程、协程
    - Python中多线程的情况下，因为有GIL的存在，所以实际上是单线程的效果，并不能加快速度。
    - 协程yield能有效的应对这个问题
    - 多进程和多线程的应用场景
        - 多进程（multiprocessing）适合执行计算密集型任务（如：视频编码解码、数据处理、科学计算等）、可以分解为多个并行子任务并能合并子任务执行结果的任务以及在内存使用方面没有任何限制且不强依赖于I/O操作的任务。
        - 多线程（threading）适合那些会花费大量时间在I/O操作上，但没有太多并行计算需求且不需占用太多内存的I/O密集型应用。
- 列表和字典的底层实现？
- django的中间件？
    - 类似java里的servlet，在请求和相应的中间进行一些操作，例如：拦截器
- 列表排序算法的实现
- django中get和filter的区别？
    - get：返回的是model对象，只能获取到为一只的对象结果，查询更准确，但查询不到数据就会报错
    - filter：返回的是Queryset，可以返回空的[]
- django中函数f和q的区别？
    - https://www.cnblogs.com/wdliu/p/7977504.html
- 深拷贝和浅拷贝的区别？
    - 浅拷贝：拷贝内存地址，速度快,原数据变化，拷贝后的数据会变化，
    - 深拷贝：拷贝的是全部数据。
- 用过celery吗？
    - 分布式异步消息任务队列
- django和flask的区别？
    - https://www.cnblogs.com/wdliu/p/7977504.html
- 如果让你来写一个Web框架，你需要考虑哪些方面？
    - orm（待完善）
- 钉钉里面打开微信支付
    - 用钉钉小程序，启动一个微信的网页，唤起支付页面


### 算法和数据结构
-  常见的排序算法及其实现？
    - https://www.cnblogs.com/yocichen/p/10457067.html
- struct和class的区别？
    - 不只是

### 数据库和调优
- MySQL的数据库引擎里，MyISAM和InnoDB的区别？
    - https://blog.csdn.net/qq_35642036/article/details/82820178
- 主键和唯一键的区别？
    - https://www.jb51.net/article/155930.htm
- redis有哪几种数据类型？
    - https://www.cnblogs.com/a609251438/p/12075181.html

### 前端
- 你常用的框架有哪些？
- 你用过哪些ECharts的图表？有没有对它做过二次开发？


## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)就能上手做AI项目。
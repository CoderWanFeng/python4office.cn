---
title: 帮师姐把100个Excel中符合条件的数据，汇总到1个Excel里
date: 2023-03-25 16:32:08
tags: 自动化办公
---



<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='http://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>



<p align="center" name="atomgit">
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>	
	    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>




大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)，B站也叫这个名~

后台收到一个读者需求：

>人事部门有最近3年每个月全公司的工资Excel文件，一共500多个。现在和1位员工有一件劳动纠纷，**需要把这1位员工散落在500多个Excel中的所有工资信息，都汇总到一个Excel中**。


简单来说，就是从500多个Excel文件里，把符合条件的数据汇总到一个Excel里。

这个需求，如果只用Excel，应该如何实现呢？请Excel大佬分享一下~

我们今天来一起看一下，如果用1行Python代码来实现！

## 1、上代码

首先下载这个库：

```python
pip install poexcel
```

然后调用这个库：

（左右滑动，查看代码）


```python
# 导入这个库
import poexcel

poexcel.query4excel(query_content='必填，需要查询的内容',
                    query_path=r'必填，放Excel文件的位置',
                    output_path=r'选填，输出查询结果Excel的位置，默认是query_path的位置',
                    output_name='选填，输出的文件名字，默认是：query4excel.xlsx')
```

## 2、建议和需求

功能刚刚上线，大家赶紧去试用一下吧~

如果大家对这个功能有更多需求和建议，可以在评论区告诉我

也欢迎大家加入项目的开发：
- ⭐GitHub：https://github.com/CoderWanFeng/poexcel


-----


---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
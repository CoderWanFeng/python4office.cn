---
title: 如何用Python创建1个空白的Excel文件？
date: 2024-01-09 16:32:08
tags: 自动化办公
---



<p align="center" id='进群-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/dfdNNrlnxGCOsDHV4fq6iQ'>
    <img src="https://raw.gitcode.com/user-images/assets/5027920/d78ad96d-6a5e-49fa-9a6d-ba98ec1a1293/image.png" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>



<p align="center" name="gitcode">
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
		<img src='https://gitcode.com/CoderWanFeng1/python-office/star/badge.svg?theme=dark' alt='gitcode star'/>
	</a>	
	    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
	<img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E4%BA%A4%E6%B5%81%E7%BE%A4-brightgreen"/>
  </a>

</p>




大家好，这里是程序员晚枫，元旦假期给大家更新了一套课程：[给小白的《6讲 · Python自动收发邮件》（完结）](https://mp.weixin.qq.com/s/XYIVihTmBUtxGha24QJ-yg)。

今天继续给大家分享**Excel自动化办公**的内容：**如何用Python创建一个空白的Excel文件？**

## 前文回顾

在去年发布的课程：[给小白的《50讲 · Python自动化办公》（完结）](https://www.python-office.com/course/50-python-office.html)中，分享过**自动创建带模拟数据的Excel文件**。👇

- [是真的！Python可以创建Excel了，1行代码就能模拟真实数据，AI办公还会远吗？](https://www.bilibili.com/video/BV18m4y1u7Kq/?buvid=&is_story_h5=false&mid=qMItlNpUNhCu1MnTH%2FJ7Ew%3D%3D&share_medium=iphone&share_pattern=placard&share_plat=ios&share_session_id=D4F498EB-69F0-47F6-987B-8B2E41BC59E9&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1704814497&unique_k=lYda8Fz&vd_source=dcea3feb81b702defb6006f671564224)

然而这个功能有一个我不满意的地方：没法生成空白的Excel，但因为需求不紧急，所以我一直没有优化。

最近我想出一套新的课程：Python + Excel自动化办公，其中第一讲就是自动创建一个空白的Excel文件，所以就必须优化一下了。

优化后的使用方法如下。


## 上代码

自动创建空白Excel文件的功能，依然来自第三方库：poexcel，下载命令如下，👇

```shell
pip install poexcel -U
```

创建空白Excel，只需要1行代码，👇。

```python
import poexcel

poexcel.fake2excel(rows=0, path='./test/test.xlsx')
```

## 相关课程

- [2G资料，Pandas处理Excel配套代码，来啦~](https://mp.weixin.qq.com/s/n5b-C4ZhkhfZmlCTvepM4A)
- [给小白的《10讲 · Python微信机器人》（完结）](https://www.python-office.com/course-002/10-PyOfficeRobot/10-PyOfficeRobot.html)
- [给小白的《6讲 · Python自动收发邮件》（完结）](https://mp.weixin.qq.com/s/XYIVihTmBUtxGha24QJ-yg)

-----





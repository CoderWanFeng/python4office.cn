---
title: 分享10个免费的Python代码仓库，轻松实现自动化办公（上）
date: 2023-10-19 01:25:17
tags: python-office
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
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>	
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
<a href="https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>



大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，小红书/小破站都叫这个名。

作为一个程序员，在工作之余我给大家（非程序员）搜集了很多实用的自动化办公代码：**可以用1行代码，帮助编程小白解决复杂的办公问题。**

下面给大家分享其中的10个常用第3方库和对应的代码，相关的演示视频，都在我的小破站账号：**Python自动化办公社区**里。👇

> 上一篇给大家分享的是前5个：excel、pdf、ppt、文件管理和图片：[分享10个免费的Python代码仓库，轻松实现自动化办公（上）](https://mp.weixin.qq.com/s/3eKDWOiJv5CCiMliCDtAWA)
> 这一篇给大家分享剩下的5个，大家可以关注我的主页查看更新。

## 1、Python + 微信 = PyOfficeRobot

微信如何自动化回复？你可以看一下poexcel这个库。

全部功能 &　下载链接：``https://pypi.org/project/PyOfficeRobot/``


> 功能举例：自动给好友发送消息
```python

# 首先，将PyOfficeRobot模块导入到我们的代码块中。
import PyOfficeRobot

# PyOfficeRobot.chat.send_message(who='程序员晚枫', message='你好，我是xxx')
# who:发给谁
# message:发送的内容
# 其中，发消息如何换行？


PyOfficeRobot.chat.send_message(who='程序员晚枫', message='你好' + '{ctrl}{ENTER}' + '点赞有好运哟~'+ '{ctrl}{ENTER}' +'python-office.com')

```


## 2、Python + 视频 = povideo

批量剪辑视频，也可以用``povideo``这个库，1行代码搞定！

全部功能 &　下载链接：``https://pypi.org/project/povideo/``


> 功能举例：从视频里，自动提取音频。

```python
# pip install povideo
import povideo

povideo.video2mp3(path=r'D:\download\baiduyun\小破站：50讲自动化办公\程序员晚枫.mp4', mp3_name='44',output_path=r'./test_files/50-47-video2mp3/')
```


## 3、Python + 工具 = wftools

很多实用的办公工具，都集成在``wftools``这个库里了。

全部功能 &　下载链接：``https://pypi.org/project/wftools/``


> 功能举例：测试网速

```python
# pip install wftools
import wftools

wftools.net_speed_test()
```


## 4、Python + AI = porobot

最近AI很火，用``porobot``试试免费的AI工具吧！

全部功能 &　下载链接：``https://pypi.org/project/porobot/``


> 功能举例：智能聊天


```python
# pip install porobot
import porobot

reply_msg = porobot.normal.chat('你好，我是程序员晚枫')
print(reply_msg)
```


## 5、Python + 金融 = pofinance

最近A股，让大家惊喜还是惊吓？

全部功能 &　下载链接：``https://pypi.org/project/pofinance/``


> 功能举例：单次做T


```python
import pofinance as pf

money = pf.t0(buy_price=9.9, sale_price=10, num=6000, w_rate=2.5 / 10000, min_rate=5, stamp_tax=0.5 / 1000)
print(money)

"""
计算做T的收益
Args:
    buy_price: 买入成本
    sale_price: 卖出价格
    num: 单笔数量
    w_rate: 手续费，默认万2.5
    min_rate: 单笔最低手续费，默认5元
    stamp_tax: 印花税，默认千0.5

Returns: 做T后的收益金额

"""
```




-------

以上所有仓库的功能介绍，我都加入了原创课程:[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)都是1行Python代码就能实现的，适合纯小白的课程，需要可以加入学习哟~

- 加入学习👉[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)

大家学习 或 使用代码过程中，有任何问题，都可以加入读者群交流哟~👇


![](https://cos.python-office.com/group/0816.jpg)

![](https://cos.python-office.com/course/50%E8%AE%B2%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8A%9E%E5%85%AC/free-link.jpg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg)就能上手做AI项目。
---
title: 用Python破解WiFi密码，只需要1行代码，太刺激了！
date: 2022-09-03 15:18:25
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
<a href="http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>


大家好，这里是在重庆的Python程序员晚枫。

今天给大家分享一个超级实用的功能：**1行代码，破解wifi密码**！！！


>最近在紧锣密鼓的给python-office增加实用功能，全部功能汇总网站：[https://www.python-office.com](https://mp.weixin.qq.com/s/n9aq6QvkFq-FsheDQaIhFg)


## 1、先上代码

因为代码实在太简单，所以直接上代码。

```
# 导入库：python-office，简写为：office
import office

# 1行代码实现
office.tools.pwd4wifi(len_pwd=8, pwd_list=['12345678', 'v-x-CoderWanFeng'])
```

## 2、注意事项

### 参数说明
破解方法在tools方法下，有2个可以选填的参数:
- ``len_pwd``，可以不填，含义是：你猜测的密码位数，默认是8位。
- ``pwd_list``，可以不填，含义是：可能的密码，有时候你可能知道几个密码，但是不确定是哪一个了，你可以把预期的密码，写在这里面，让程序自己去试验。**我个人最常用这个功能，尤其是在切换不同wifi的时候**

如果你完全不知道密码有多少位,可能的值是什么，怎么办？运行以下代码，从8位开始到20位，让程序自己去试验吧。

```
import office

for len_pwd in range(8, 21):
    office.tools.pwd4wifi(len_pwd)
```
### 密码组成
限于破解速度，目前只支持破解密码组成为：数字 + 大小写字母。

如果对方密码含有符号，目前的代码不能破解，未来会持续开发。

### 破解速度

很慢，因为是功能的第一版，目前先实现了：可用。

至于速度问题，还需要各位开发大佬，尤其是对算法、速度优化感兴趣的朋友，参与我们的项目中，一起进行优化。

源码地址：``https://github.com/CoderWanFeng/python-office``

## 3、更多功能

关于python-office，近期开发的功能有：
- [超详细！python-office自动化办公的18个功能汇总](https://mp.weixin.qq.com/s/QhaUoB7Q4CJHR29uD6JSHQ)
- [下载B站视频？1行命令搞定，悄悄用](https://mp.weixin.qq.com/s/sFdZnhkxiBxNE7C3_ciT8w)
- [【Python助力疫情】100+不同格式的Excel、100w+数据，1秒找出1个人的信息，怎么做到的？](https://mp.weixin.qq.com/s/NAfh6ooO_9haALMsF8Jf5w)

----


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)就能上手做AI项目。
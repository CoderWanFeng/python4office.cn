---
title: 【DNS 解析】使用腾讯云DNS解析 + Github Pages，免费搭建个人网站 （给小白的保姆级教程）
date: 2022-06-09 16:43:24
tags: [DNS,腾讯云,GitHub]
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
<a href="https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>




大家好，这里是Python程序员晚枫。

​``每位程序员和技术爱好者，想必都想搭建一个属于自己的个人网站吧？``

我自己使用【腾讯云DNS解析 + GitHub Pages】，免费创建了一个个人网站：[www.python-office.com](https://www.python-office.com)
今天我就给大家分享一下，我的具体操作步骤，小白也能看得懂~

<!-- more -->

## 打开Github仓库的Pages功能


![开通Github Pages](https://img-blog.csdnimg.cn/eacc77ac6d214138899f0811303d3235.png#pic_center)


打开Pages功能的步骤如上图所示，每一步的具体内容是：
1. 打开自己的任意一个GitHub仓库，例如我自己的是：[python-office](https://github.com/CoderWanFeng/python-office)
2. 点击右侧的settings
3. 点击侧边栏的Pages
4. 选择存放个人网站代码的分支和文件夹，建议：gh-pages分支的docs文件夹（便于区分源代码和打包的代码）
5. 在custom domin这里，填写接下来要通过【DNS解析】的域名，点击Save保存即可。例如我的是：[www.python-office.com](www.python-office.com)


## 配置腾讯云DNS解析

这里是非常关键但又简单的一步啦~如下图所示：


![配置腾讯云DNS解析](https://img-blog.csdnimg.cn/15fe9ca3ab4c49248f1f68817ba5211c.png#pic_center)

本来配置DNS解析是一个复杂的过程，但是腾讯DNS解析帮我们简化了配置步骤。你只需要：

1. 打开DNS解析的官网：[传送门](https://console.cloud.tencent.com/cns/detail/python-office.com/records/0)，选择蓝色按钮：添加记录
2. 按照图中内容，填写一模一样的2条解析记录
3. 记录类型选择CNAME
4. 注意：记录值这里，填写你的GitHub用户名.github.io，例如我的GitHub用户名是CoderWanFeng，所以我这里填写的是coderwanfeng.github.io（填写保存后，系统可能会自动给末尾加个.，不影响解析）

## 小结

到这里，你自己免费的个人网站就搭建完成，可以正常访问了。是不是非常简单？

``赶紧去试试！``如有疑问，欢迎在评论区和我交流~
 




程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。
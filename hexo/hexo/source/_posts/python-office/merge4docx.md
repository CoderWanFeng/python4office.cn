---
title: 1行代码，帮小明合并了162个Word文件
date: 2023-03-17 22:11:21
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
<a href="https://mp.weixin.qq.com/s/7rH5U6s91hnTKCKZy4BHCg">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>


大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。

终于周末了，我和小明又开始了疯狂的考证学习，昨晚通过合法的手段获取了一套学习资料，却遇到了一个问题：

> 一套完整的资料，被机构拆分成了162个word文件，不方便看。

小明想让我写一段代码，把它们合并成一个word文件，我果断拒绝了。

原因很简单：有现成的付费工具，何必自己重写？能花钱解决的事，绝对不要花时间自己去试错。比如：找我咨询如何学习Python，很实惠，但很高效！我的微信👉**CoderWanFeng**

但话说回来，有没有免费的Python方法呢？肯定有的，本文我们一起来看一下~

## 1、上代码

其实，不论合并多少个Word文件，1行代码就够了。👇左右滑动，查看代码。

```
# 下载方式：pip install python-office
import office

office.word.merge4docx(input_path=r'D:\程序员晚枫的文件夹\word-in', 
                        output_path=r'D:\程序员晚枫的文件夹\word-out')
```

## 2、相关功能

如果是打印需要，还可以合并后，把Word转为PDF。

```
import office

office.word.docx2pdf(path=r'D:\程序员晚枫的文件夹\word-out')
```
## 3、Python自动化办公，免费学习

所有学习资源，我都放在官网里了~

💻 ``www.python-office.com``


---


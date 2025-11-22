---
title: 1行Python代码，把PPT转成图片
date: 2023-03-05 22:25:14
tags: python-office
---


<p align="center" id='进群-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/0GrWWSQ8sKs-WA8WoN3Ztg?payreadticket=HPsk3SM42QLKkwlPgzoQN00eTUDy7x7I70-jcY9jIG2bWFmjZvB7r1mF10OiNSkxknfiN08&scene=1&click_id=1'>
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
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
		<img src='https://gitcode.com/CoderWanFeng1/python-office/star/badge.svg?theme=dark' alt='gitcode star'/>
	</a>	
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
<a href="https://mp.weixin.qq.com/s/4Szn7qE3YkBU66amRgmAEw">
  <img src="https://img.shields.io/badge/加入-AI编程训练营-red" alt="AI编程训练营">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
	<img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E4%BA%A4%E6%B5%81%E7%BE%A4-brightgreen"/>
  </a>

</p>


大家好，这里是程序员晚枫，正在all in [AI编程](https://mp.weixin.qq.com/s/4Szn7qE3YkBU66amRgmAEw)。

今天给大家分享一个Python自动化办公的专用库python-office的最新功能：1行代码，实现PPT转为图片。

更多功能，请见官网：[开源中国推荐：python-office自动化办公，每个功能只需一行代码，做到了真正的开箱即用。](https://www.python-office.com/)

## 1、上代码


首先，下载python-office，下载教程之前录制过了，大家可以去看看~

[点我直达](https://www.bilibili.com/video/BV1pT4y1k7FH)


其次，1行代码调用ppt转图片的功能。
```python
import office

office.ppt.ppt2img(input_path=r'D:\test\py310\ppt_test\程序员晚枫的文档.pptx',
                   output_path=r'D:\test\py310\ppt_test',
                   img_type='png')
```

## 2、参数说明

一共有3个参数，作用分别如下：

- input_path：必填，待转换ppt的存放位置和名称
- output_path：选填，转换后的图片存储的位置，会自动生成一个和ppt同名的文件夹。可以不填，默认值：‘./’
- img_type：转换的图片类型，可以填：jpg或者png，可以不填，默认值：jpg

## 更多功能

- [后厂村：中国“硅谷”，遍地985，天天996](https://mp.weixin.qq.com/s/MSJ3t1hC3JmuGAorbkJyog)
- [普通人如何追上ChatGPT的风口？](https://mp.weixin.qq.com/s/uBqSV1QkX9JrvIkYexQy6A)
- [天呐！1行Python代码，收集微信群信息，聊天机器人太简单了~](https://mp.weixin.qq.com/s/t3TEkwR_MMaKmetSL1jsAA)


---
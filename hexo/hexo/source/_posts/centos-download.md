---
title: CentOS 官方下载地址
date: 2022-02-07 15:30:09
tags: [CentOS,Linux]
---


<p align="center" id='进群-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/0GrWWSQ8sKs-WA8WoN3Ztg?payreadticket=HOM_f1W8Dyy1cX9yLlSj9TUoJEXFC4p5UHj4IjbEYOGs2CdefJeSCX4kmmGM6iXpka9eo0c'>
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
  	<a href="https://mp.weixin.qq.com/s/yaSmFKO3RrBpyanW3nvRAQ">
	<img src="https://img.shields.io/badge/QQ-163434413-orange"/>
  </a>
    	<a href="http://www.python4office.cn/wechat-group/">
	<img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E4%BA%A4%E6%B5%81%E7%BE%A4-brightgreen"/>
  </a>

</p>





<p align="center" id='支付宝-banner'>
    <a target="_blank" href='http://www.python4office.cn/fuli/zhifubao-0923/'>
    <img src="https://ads-1300615378.cos.ap-guangzhou.myqcloud.com/alipay/hong-3.jpg" width="100%"/>
    </a>   
</p>


<p align="center" id='外卖-banner'>
    <a target="_blank" href='https://kzurl19.cn/7CAHjq'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2F%E5%A4%96%E5%8D%96-1040-100.jpg" width="100%"/>
    </a>   
</p>


1. 官方下载地址，包含不同架构和镜像
    > [https://www.centos.org/download/](https://www.centos.org/download/)
    下载之后，如果是win10系统，可以直接使用hyper功能安装本地虚拟机
    CentOS8自带Python3.6.8
<!-- more -->


2. 修复yum
    最近项目使用的服务器系统是CentOS8，在使用yum安装redis时发现yum已经不能用了。
    > 修复方式，来自阿里云 · 开发者社区：[https://developer.aliyun.com/mirror/centos?spm=a2c6h.13651102.0.0.2ab21b11a5xMh1](https://developer.aliyun.com/mirror/centos?spm=a2c6h.13651102.0.0.2ab21b11a5xMh1)
    更新所有的软件包
    yum update -y

3. 通过Hyper方式安装的虚拟机，默认是动态IP，需要自己设置固定IP
    > https://www.cnblogs.com/wswind/p/11007613.html
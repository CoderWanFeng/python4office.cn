---
title: win10-docker-install
date: 2022-09-05 23:35:24
tags:
---


<p align="center" id='支付宝-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/UsFs6ooDspyhhKMleKTVpw'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2Falipay.jpg" width="100%"/>
    </a>   
</p>


<p align="center" id='外卖-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/fdQ0TbTocPvw-DAMsFUlVg'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2F%E5%A4%96%E5%8D%96-1040-100.jpg" width="100%"/>
    </a>   
</p>

## docker下载和安装
docker下载：https://www.docker.com/

docker engine 国内源：

```
{
  "registry-mirrors": [  
    "https://registry.docker-cn.com",
    "http://hub-mirror.c.163.com",
    "https://docker.mirrors.ustc.edu.cn"
  ],
  "insecure-registries": [],
  "debug": false,
  "experimental": false,
  "features": {
    "buildkit": true
  }
}
```
参考链接：https://blog.csdn.net/sinat_29217765/article/details/114888396

-----

## docker知识点

1、3要素
- 容器：根据镜像，生成的环境
- 镜像：一个模板
- 仓库：存放镜像的地方

2、编写dockerfile
可以打包一个镜像

docker是分层生成的

3、docker-compose
对于大量的镜像运行，已经运行顺序，进行编排

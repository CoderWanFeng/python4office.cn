---
title: win10-docker-install
date: 2022-09-05 23:35:24
tags:
---


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

---

title: win10-docker-install
date: 2022-09-05 23:35:24
tags: [部署, Docker]

---



<!-- more -->
<p align="center" id='支付宝-banner'>
    <a target="_blank" href='https://www.python4office.cn/fuli/zhifubao-0923/'>
    <img src="https://ads-1300615378.cos.ap-guangzhou.myqcloud.com/alipay/hong-3.jpg" width="100%"/>
    </a>   
</p>


<p align="center" id='外卖-banner'>
    <a target="_blank" href='https://kzurl19.cn/7CAHjq'>
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



---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


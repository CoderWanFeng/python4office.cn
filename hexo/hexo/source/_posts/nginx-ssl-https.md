---
title: 【DNS 解析】Nginx+SSL+DNS解析+腾讯云服务器，免费给自己的个人网站开启HTTPS防护
date: 2022-06-17 17:25:33
tags:
---

​


大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/h0MExYJag6hLnQg26yx98w)。
之前给大家介绍了[如何通过DNS解析把自己的域名绑定到腾讯云服务器上](https://cloud.tencent.com/developer/article/2021770)，在使用的过程中我发现了一个问题：
> <br/>域名的访问协议有http和https（更加安全）。
> <br/>我现在有2个域名：python-office.com 和 python4office.cn，在不开启https的情况下，以<br/>① .cn为结尾的python4office.cn所有的浏览器都可以打开；
<br/>② 但是以.com结尾的python-office.com则存在：**部分浏览器默认使用https进行访问导致打不开网页的问题。**

在这种情况下，就必须给python-office.com加上ssl证书，这样就可以对[https://python-office.com](https://python-office.com)进行访问了。

**我们一起操作一下~**

<!-- more -->

## 一、使用的设备的技术

- 设备：[腾讯云服务器](https://curl.qcloud.com/l7IdTQv0)
- 技术：vuepress（网站编写）、nginx（反向代理）、[cdn（图床）](https://curl.qcloud.com/gohfFwWN)、[dns解析（配置ssl证书）](https://curl.qcloud.com/ou6k5Dfv)

## 实现步骤

### 1、购买ssl证书（免费）
因为我这里搭建的是个人网站，所以我选择的是域名型免费版。

![1-ssl证书-免费.jpg](https://ask8088-private-1251520898.cn-south.myqcloud.com/developer-images/article/6652786/3ng9rrvocn.jpg?q-sign-algorithm=sha1&q-ak=AKID2uZ1FGBdx1pNgjE3KK4YliPpzyjLZvug&q-sign-time=1655472629;1655479829&q-key-time=1655472629;1655479829&q-header-list=&q-url-param-list=&q-signature=92a89e5d8fab8a88ff0b782979dcce8fe130f8ab)

### 2、绑定域名 & 配置DNS解析 & 打开443端口
如果你的域名、云服务器、SSL证书都是在腾讯云购买的，这一步会自动设置。

![2-绑定域名-1.jpg](https://ask8088-private-1251520898.cn-south.myqcloud.com/developer-images/article/6652786/bheum51u8z.jpg?q-sign-algorithm=sha1&q-ak=AKID2uZ1FGBdx1pNgjE3KK4YliPpzyjLZvug&q-sign-time=1655472643;1655479843&q-key-time=1655472643;1655479843&q-header-list=&q-url-param-list=&q-signature=6c590bcdc270426c59d50190889d5138ae41be57)

### 3、下载证书到云服务器
下载证书，解压后有4个文件,其中你需要上传到服务器的有2个：
- www.python-office.com_bundle.crt
- www.python-office.com.key

![5-下载证书.jpg](https://ask8088-private-1251520898.cn-south.myqcloud.com/developer-images/article/6652786/hk09kl23jr.jpg?q-sign-algorithm=sha1&q-ak=AKID2uZ1FGBdx1pNgjE3KK4YliPpzyjLZvug&q-sign-time=1655472670;1655479870&q-key-time=1655472670;1655479870&q-header-list=&q-url-param-list=&q-signature=44c23b6cffefe862d239b29e26de71778686670d)
### 4、配置nginx.conf
```
server {
        #SSL 访问端口号为 443
        listen 443 ssl; 
        #填写绑定证书的域名
        server_name www.python-office.com; 
        #证书文件名称
        ssl_certificate www.python-office.com_bundle.crt; 
        #私钥文件名称
        ssl_certificate_key www.python-office.com.key; 
        ssl_session_timeout 5m;
        #请按照以下协议配置
        ssl_protocols TLSv1.2 TLSv1.3; 
        #请按照以下套件配置，配置加密套件，写法遵循 openssl 标准。
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE; 
        ssl_prefer_server_ciphers on;
        location / {
           #网站主页路径。此路径仅供参考，具体请您按照实际目录操作。
           #例如，您的网站运行目录在/etc/www下，则填写/etc/www。
            root html; 
            index  index.html index.htm;
        }
    }
```
### 5、重启nginx服务
重启命令：nginx -s reload
在这里有一个特殊情况需要注意，如果原生的nginx没有配置ssl，需要自己编译一下。
```
1.看一下自己的nginx是不是没有配置ssl
nginx -V

2.进入nginx源码目录执行
./configure --prefix=/usr/local/nginx --with-http_ssl_module
3. 执行 make（切记不能 make install 会覆盖安装目录）

4.将新的 nginx 覆盖旧安装目录
cp objs/nginx /usr/local/nginx/sbin/ngin

5.测试nginx是否正确
/usr/local/nginx/sbin/nginx -t 
```
## 三、写在最后
完成以上步骤，个人网站的https访问就全部成功了。
> 在安装过程中有任何问题，欢迎大家在评论区和我讨论~

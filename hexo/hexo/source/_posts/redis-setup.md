---
title: CentOS8下Redis的安装
date: 2022-02-07 14:11:29
tags: [CentOS,Linux,Redis]
---

<div align="center">
    <a href="https://github.com/CoderWanFeng"> <img src="https://badgen.net/badge/Github/%E7%A8%8B%E5%BA%8F%E5%91%98?icon=github&color=red"></a>
    <a href="http://www.python4office.cn/account-display/"> <img src="https://badgen.net/badge/follow/%E5%85%AC%E4%BC%97%E5%8F%B7?icon=rss&color=green"></a>
    <a href="https://space.bilibili.com/259649365"> <img src="https://badgen.net/badge/pick/B%E7%AB%99?icon=dependabot&color=blue"></a>
    <a href="https://mp.weixin.qq.com/s/6cR5fMSCtdI5sJdWiDwhOA"> <img src="https://badgen.net/badge/join/%E4%BA%A4%E6%B5%81%E7%BE%A4?icon=atom&color=yellow"></a>
</div>

redis可以使用yum安装，也可以使用源码的方式安装
本次使用yum安装。
> 源码安装教程：[https://www.runoob.com/redis/redis-install.html](https://www.runoob.com/redis/redis-install.html)
<!-- more -->

1. 首先修复yum
最近项目使用的服务器系统是CentOS8，在使用yum安装redis时发现yum已经不能用了。
> 修复方式，来自阿里云 · 开发者社区：[https://developer.aliyun.com/mirror/centos?spm=a2c6h.13651102.0.0.2ab21b11a5xMh1](https://developer.aliyun.com/mirror/centos?spm=a2c6h.13651102.0.0.2ab21b11a5xMh1)

2. 然后安装redis
```python
yum install redis
```

3. 启动
```python
cd /usr/bin #进入redis的安装目录
./redis-server /etc/redis.conf #启动redis
./redis-cli #进入redis的命令行界面
```

4. 配置redis的密码
因为项目安全检查的需要，所以这里给redis配置一个密码。
```shell
CONFIG get requirepass #查看密码
CONFIG set requirepass "runoob" #设置密码
AUTH password #使用密码登录
```

5. redis链接方式
```shell
redis://[:password]@host:port/db
```

6. 远程连接redis的几个问题
```shell
bind 0.0.0.0 #设置host为所有ip
requirepass yourpassword #这里的注释去掉，否则redis虽然正常可用，但是pycharm链接不上。
```

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。
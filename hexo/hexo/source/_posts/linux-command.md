---
title: Linux的常用命令
date: 2022-01-05 22:30:46
tags: Linux
---



<p align="center">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://raw.atomgit.com/CoderWanFeng1/website/raw/main/github-nav.jpg" alt="github license"/>
    </a>   
</p>
<p align="center">
	<strong>🍬python for office</strong>
</p>
<p align="center">
	👉 <a href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>


<p align="center" name="图标-github">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/contributors/CoderWanFeng/python-office" alt="github contributors"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/forks/CoderWanFeng/python-office" alt="github forks"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues/CoderWanFeng/python-office" alt="github issues"/>
    </a>	
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues-pr/CoderWanFeng/python-office" alt="github license"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/license/CoderWanFeng/python-office" alt="github license"/>
    </a>   
</p>

<p align="center" name="gitee">
	<a target="_blank" href='https://gitee.com/CoderWanFeng/python-office/'>
		<img src='https://gitee.com/CoderWanFeng/python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
		<img src="https://gitee.com/CoderWanFeng/python-office/badge/fork.svg?theme=white" alt="gitee fork"/>
	</a>
	<a href="https://mp.weixin.qq.com/s/yaSmFKO3RrBpyanW3nvRAQ">
	<img src="https://img.shields.io/badge/QQ-163434413-orange"/></a>
</p>



对于习惯了 Windows、macOS 等图形界面的用户来说，Linux 以命令行为主的操作方式导致它刚开始的学习曲线还是很陡峭的。
别无他法，多看书，多练习。于是我把自己在[腾讯云服务器](https://curl.qcloud.com/PHemptia)里常用的命令，记录在这里，常看常新。

### 查看存储大小
    
```shell
du -sh file、dir 查看文件、文件夹大小

df -h 查看每个根路径的分区大小
df -hl 查看磁盘剩余空间

du -sm [文件夹] 返回该文件夹总M数
```

### 文件操作

<!-- more -->

- 查看文件&显示行号
    - cat -n file
- 清空指定文件
    - truncated -s 0 filename
### 查看系统版本
- 这种方法只适合Redhat系的Linux
    - at /etc/redhat-release

### 防火墙相关命令
- 查看防火墙状态
    - systemctl status firewalld

- 临时关闭防火墙
    - systemctl stop firewalld

- 停止并禁用开启启动防火墙
    - systemctl disable firewalld

- 启动防火墙
    - systemctl start firewalld
    
- 设置开机启动防火墙
    - systemctl enable firewalld

- 查看防火墙开启的端口
    - firewall-cmd --list-ports
### 查看端口被哪个项目占用
- 分2步
    - 先看一下占用端口的进程：netstat -apn | grep 8080 #假如结果显示：占用端口的进程是17997
    - 再找出占用对应进程的项目：ps -ef | grep 17997

> 参考：[Linux实战技能100讲](http://gk.link/a/111MW)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)就能上手做AI项目。
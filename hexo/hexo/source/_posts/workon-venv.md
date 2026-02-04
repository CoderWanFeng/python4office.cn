---
title: 使用virtualenvwrapper搭建Linux虚拟环境，并用workon命令启动
date: 2022-01-23 15:58:41
tags: [Linux,Python]
---


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




## 目标说明

<!-- more -->


最近在负责部署flask项目，需要在Linux上建立独立的虚拟环境。

以前我一直使用的是使用virtualenv新建一个虚拟环境文件夹的方法，这种方式的缺点是：

1. 需要在项目里创建venv虚拟环境的文件夹，让项目变得很大；
2. 需要同一环境的不同项目之间，不方便共同使用同一个虚拟环境，需要创建多个相同的虚拟环境的文件夹，浪费空间；
3. 最后一个，也是我最讨厌的缺点，是每次启动虚拟环境，都要进入venv虚拟环境的目录里，专门启动activate命令，没有全局启动命令，非常麻烦。

为了解决这些问题，我发现了virtualenvwrapper这个库，它可以统一安装虚拟环境在一个相同的文件夹里，并且使用workon命令一键启动指定的虚拟环境。



## 安装和配置步骤



##### 1、查询python解释器所在路径

以下查询py3和py2的目录：

```shell
which python3
/usr/bin/python3

which python2
/usr/bin/python2
```

##### 2、安装python虚拟运行环境
```shell
pip install virtualenvwrapper
```



##### 3、添加环境变量

新建virtualenvwrapper文件夹，来到你习惯的Linux软件目录下

```shell
mkdir virtualenvwrapper
```

在/etc/profile的末尾添加：

> 也有的教程，建议加载~/.bashrc文件里，两种都可以。这两个文件是父子关系（profile是父级文件），我习惯放在profile文件中。

```shell
export WORKON_HOME=/opt/software/virtualenvs
VIRTUALENVWRAPPER_PYTHON=/usr/local/python3/bin/python3
source /usr/local/python3/bin/virtualenvwrapper.sh
```

运行以下命令，加载配置好的环境变量

```shell
source /etc/profile
```

如果报错

```shell
-bash: /../../../virtualenvwrapper.sh: No such file or directory
```

说明文件没在这个路径下

可以通过which 命令查看（which是用来查看当前要执行的命令所在的路径）

```shell
which virtualenvwrapper.sh
```


## 创建并使用python虚拟环境
当你需要Python3开发时：

```shell
mkvirtualenv -p /usr/bin/python3 your_venv_name
```

然后可以随时切换不同的虚拟环境：

```shell
workon your_venv_name
```

不仅可以自由切换py2和py3，同一个版本下还可以配置不同的依赖，pip不同的包，来适应不同项目的需求。

更爽的是，你可以在进入虚拟环境的同时切换到项目目录，只需要编辑 $your_venv_name/bin/postactivate 这个文件即可：

在文件中添加切换目录的命令：

```shell
cd /path/to/your/project
```

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)就能上手做AI项目。
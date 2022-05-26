---
title: 电脑没有联网，怎么用pip安装依赖的第三方库？
date: 2022-02-11 10:31:00
tags: [Linux,Python,pip]
---

1、下载第三方库

首先找一台环境相同的机器，生成项目对应的requirements.txt
👉[生成requirements.txt的方法](http://www.python4office.cn/create-requeriments/)

然后使用download命令，下载第三方库到指定文件夹
```python
pip download -r requirements.txt -d /tmp/pip
```

2、压缩并下载所有第三方库，并上传到目标机器

<!-- more -->

```shell
zip -q -r res.zip *  #压缩
sz res.zip #下载到本地
rz #上传到目标机器
```

3、解压，安装
```shell
unzip #解压
```
安装包分为2中类型：tar.gz 和 whl
tar.gz的安装：
```shell
gar -zxvf pip-module.tar.gz
cd pip-module
python setup.py install
```
whl的安装
```shell
pip install *.whl
```

4、报错
因为测试机器和目标机器可能存在版本问题或者环境问题，所以这样下载的第三方库，直接移植过去可能会有问题。
todo：找到更简便的移植方法


5、pip删除所有库
pip freeze > allpackages.txt
pip uninstall -r allpackages.txt -y

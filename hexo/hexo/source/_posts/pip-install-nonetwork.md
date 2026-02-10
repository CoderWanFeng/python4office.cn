---
title: 电脑没有联网，怎么用pip安装依赖的第三方库？
date: 2022-02-11 10:31:00
tags: [Linux,Python,pip]
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

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。
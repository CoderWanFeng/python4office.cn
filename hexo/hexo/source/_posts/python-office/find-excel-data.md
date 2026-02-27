---
title: 【Python助力疫情】100+不同格式的Excel、100w+数据，1秒找出1个人的信息，怎么做到的？
date: 2022-08-26 11:16:31
tags: python-office
---



![](https://www.python-office.com/api/img-cdn/python-office/find_excel_data/cover.jpg)


大家好，我是在重庆奋斗的Python程序员晚枫。

最近开源中国的推荐项目，Python自动化办公专用的👉[python-office库](https://mp.weixin.qq.com/s/d2m7xYCLXF8QUlr-5sSuPA)，更新了一个和疫情管控有关的功能。

今天我们一起来学习一下，**1行代码就能解决问题**，真的很实用！

> python-office的项目官网：``https://www.python-office.com``


## 0. 功能说明

这次发布的功能，来自核酸检测中，对Excel数据的查询。详情如下👇

疫情以来，各地经常会进行全员检测。

以一个100w+人口的县城举例，每次检测完，汇总到有关部门的就是：100个左右的Excel表格，里面零零总总100w+条数据，而且每个Excel表格的格式（列的个数和名称），可能还不一样。
![](https://www.python-office.com/api/img-cdn/python-office/find_excel_data/qa.jpg)

>这时候，如果你想**根据姓名从中查找出某1个人的信息**，或者**根据检测时间查找出某一类人的数据**，怎么办？

- 一个个的翻，一页页的看，不仅慢，而且可能会遗漏。

- 即使把数据全部汇总到一个表格里进行查询，速度也很慢，
- 而且超过100w条数据，性能差的电脑，可能连Excel都打不开了。

本次发布的功能，针对本需求，让你仅仅使用**1行Python代码**，就可以**快速**查找出指定的条件的：**文件位置和名称、sheet名称、所在行数、具体信息。**
![](https://www.python-office.com/api/img-cdn/python-office/find_excel_data/demo.jpg)
``本功能的作者：bulabean``

``相关PR：https://gitee.com/CoderWanFeng/python-office/pulls/10``

而且不需要你学习Python这门技术，跟着下文操作，就可以轻松实现，快去试试吧~





## 1. 安装python-office
第一步的安装很简单，在有python环境的电脑上，只需要执行下面这一行命令。
> 如果你之前使用过python-office这个库，也需要执行一下，可以下载到最新版本~

安装
```
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```
如果你的电脑里还没有安装python环境，可以在下列公众号的后台发送：**安装教程**，获取一个6分钟的傻瓜式安装教程，有电脑就能跟着完成操作~



## 2. 代码
直接上代码！

代码
```
# 导入库：python-office，简写为：office
import office

# 1行代码，查出内容即可
office.excel.find_excel_data(search_key='刘家站垦殖场',target_dir=r'D:\workplace\')

# 你需要填写的内容：
# search_key：你的查询条件，比如我要查询的内容里，包含：刘家站垦殖场
# target_dir：你那100个Excel文件，存放的位置。比如我放在了D盘下的workplace文件夹里，我就写：r'D:\workplace\'

```


## 3. 使用说明
0. 直接把上面代码复制到Pycharm里即可，⭐按要求填写你需要的内容。
1. 支持xls和xlsx，所有的Excel文件格式。📕
2. 如果使用中有问题，可以加入python-office的**交流群**，进行讨论。🏠

![](https://www.python-office.com/api/img-cdn/python-office/find_excel_data/group.jpg)
## 4.提交需求
1行代码实现复杂功能，是不是很简单？目前python-office这个自动化办公的第三方库正在持续开发中。
目前已经发布了20+功能：

- [超详细！python-office自动化办公的18个功能汇总](https://mp.weixin.qq.com/s/QhaUoB7Q4CJHR29uD6JSHQ)
- [用Python下载B站视频？1行命令搞定，悄悄用](https://mp.weixin.qq.com/s/sFdZnhkxiBxNE7C3_ciT8w)
- [用Python自动生成 图文并茂的数据分析 报告](https://mp.weixin.qq.com/s/STSRuN9Q9NpETKdYQBmxqQ)

也欢迎有技术开发能力的同学，一起来丰富这个项目：
> - 欢迎大家的star & fork & pr！⭐
> - 国内仓库：https://gitee.com/CoderWanFeng/python-office
> - Github：https://github.com/CoderWanFeng/python-office

## 5. 相关阅读

- [超详细！python-office自动化办公的18个功能汇总](https://mp.weixin.qq.com/s/QhaUoB7Q4CJHR29uD6JSHQ)
- [用Python下载B站视频？1行命令搞定，悄悄用](https://mp.weixin.qq.com/s/sFdZnhkxiBxNE7C3_ciT8w)
- [用Python自动生成 图文并茂的数据分析 报告](https://mp.weixin.qq.com/s/STSRuN9Q9NpETKdYQBmxqQ)




----

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。
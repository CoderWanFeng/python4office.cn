---
title: Python 生成requirements.txt文件的两种方式以及使用
date: 2022-01-24 08:48:39
tags: [Linux,Python,pip]
---



<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='http://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>




<p align="center" name="atomgit">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>	
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
<a href="https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>



为了便于新环境部署，python项目中需要包含一个 requirements.txt 文件，用于记录所有依赖包及其精确的版本号
requirements.txt可以通过pip命令自动生成和安装
```shell
pip install -r requirements.txt
```
### 方式一：freeze命令

<!-- more -->

- 应用场景：在单一虚拟环境下，可以使用这种方式。
- 优点：这种方式会把当前环境下的所有依赖包都整理出来。
- 缺点：不是针对某个项目生成，如果当前环境下有多个项目，那么会生成大量无关的依赖信息。
```python
pip freeze > requirements.txt
```
但是用这个方法，可以实现一个功能：删除当前环境的所有python依赖。

```python
pip uninstall -r requirements.txt -y
```



### 方式二：pipreqs（推荐）

- 应用场景：针对单个项目生成 requirements.txt
- 优点：使用 pipreqs 可以自动检索到当前项目下的所有组件及其版本，并生成 requirements.txt 文件，极大方便了项目迁移和部署的包管理。
- 缺点：相比直接用 freeze 命令，能直接隔离其它项目的包生成。
```shell
pipreqs ./ --encoding=utf-8
#强制执行命令 --force ，覆盖原有的 requirements.txt 文件
pipreqs ./ --encoding=utf-8 --force
```

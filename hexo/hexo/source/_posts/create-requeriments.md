---
title: Python 生成requirements.txt文件的两种方式以及使用
date: 2022-01-24 08:48:39
tags: [Linux,Python,pip]
---
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

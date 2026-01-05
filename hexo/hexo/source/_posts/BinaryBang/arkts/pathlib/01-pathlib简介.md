---
title: 鸿蒙ArkUI开发|文件路径管理好帮手pathlib
date: 2025-07-05 23:46:00 
tags: [鸿蒙开发,pathlib,文件管理]
---

![image.png](https://raw.atomgit.com/user-images/assets/5027920/5e8c4bf3-f19b-42c0-a06c-5ca0191bfc7f/image.png 'image.png')
# 前言
在鸿蒙开发中,避免不了对沙盒中的文件进行操作.最近遇到的一个问题是,将一个目录下的所有文件和文件夹全部删除,但是系统提供的fs对象只能删除一个空目录,对于非空目录进行处理,就会比较棘手.

# 解决方案
为了解决此类痛点,我们参考了Python中的pathlib的核心思想,在arkts中,实现了一套更加方便的处理文件管理的工具类`pathlib`.

上述问题在pathlib的加持下,只需要两步:
```
import { Path } from 'pathlib'

const dir = new Path("xxxx");
dir.rmdir();
```
Path中,自动处理了目录非空的情况下,先递归删除所有子文件夹和子文件的操作.

在pathlib中,我们处理了这些文件管理的细枝末节,让您在开发中更加关注与业务逻辑,事半功倍!

# pathlib简介

`pathlib`提供一套简洁的,面向对象的api调用来操作文件.

仓库地址: [pathlib](https://atomgit.com/python4office/pathlib.git)

## 创建方式
```
// 从字符串创建
const path = Path('folder/file.txt');

// 从多个部分创建
const path2 = Path('folder', 'file.txt');

// 用join运算符连接
const path3 = Path('folder').join('file.txt');


//使用静态方法创建目录对象的时候,需要先初始化Path类,一般在Ability/onWindowStageCreate中初始化

const context = getContext();
Path.initClass(context);

// 从cache目录创建 data/storage/el2/base/haps/demo/cache
const cache = Path.cache()

// 从temp目录创建 data/storage/el2/base/haps/demo/temp
const temp = Path.temp()

// 从files目录创建 data/storage/el2/base/haps/demo/files
const files = Path.files()
```

## 常用对象和方法:

### 通用方法
`exists() 判断路径对象是否存在`

### 文件夹操作
`subPaths() 获取所有的子路径对象`

`rmdir() 删除文件夹递归删除所有子文件和子文件夹`

### 文件操作
`touch() 创建文件`

`unlink() 删除文件`

`rename() 重命名文件`

### 静态方法
`files() 获取沙箱files目录`

`temp() 获取沙箱temp目录`

`cache() 获取沙箱cache目录`

## pathlib的优势:

1.  面向对象的API,更符合使用习惯

2.  自动处理不同系统的路径差异

3.  提供丰富的路径操作方法

4.  代码更简洁易读

## 建议:

1.  新项目优先使用pathlib

2.  路径处理统一使用Path对象

3.  注意正确处理异常情况

4.  考虑文件编码问题




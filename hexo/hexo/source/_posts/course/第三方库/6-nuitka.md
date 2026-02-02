---
title: Nuitka 入门指南：将 Python 代码打包为 exe 文件
date: 2024-11-29 00:41:49
tags: [第三方库,pip]
---


<p align="center" id='腾讯云-banner'>
    <a target="_blank" href='https://curl.qcloud.com/3csDz9jU'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F1040x100-tencent.jpg" width="100%"/>
    </a>   
</p>

> 这是专栏[优秀的第三方库](http://www.python4office.cn/course/%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93/all/)的第6篇原创文章。

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。

今天给大家分享一个可以把Python程序员打包 成exe程序的库——Nuitka。

Nuitka 是一个 Python 编译器，它可以将 Python 代码编译成可执行文件或扩展模块。以下是如何使用 Nuitka 的基本步骤和视频：

## 视频教程

- [初二学生的Python水平，让我震惊！把python-office打包成exe软件，你看完也会喊666](https://www.bilibili.com/video/BV1RG4y1M7uX/?buvid=&is_story_h5=false&mid=qMItlNpUNhCu1MnTH%2FJ7Ew%3D%3D&share_medium=iphone&share_pattern=placard&share_plat=ios&share_session_id=B108129F-613C-474A-94B3-A105CA9CD95B&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1732806036&unique_k=xF8K2Q9)

## 安装 Nuitka
你可以通过 pip 来安装 Nuitk<br/>A：
```bash
pip install nuitka -i https://mirrors.aliyun.com/pypi/simple//
```
确保你使用的是 Python 3.6 或更高版本。

## 编译 Python 代码
使用 Nuitka 编译 Python 代码的基本命令是：
```bash
nuitka --python python_script.py
```
这将编译 `python_script.py` 文件。

## 生成可执行文件
要生成一个独立的可执行文件，可以使用以下命令：
```bash
nuitka --standalone python_script.py
```
这将生成一个包含所有依赖的可执行文件。

## 编译选项
Nuitka 提供了多种编译选项，以下是一些常用的选项：

- `--show-progress`：在编译过程中显示进度条。
- `--enable-plugin=插件名称`：启用指定的 Nuitka 插件。
- `--disable-plugin=插件名称`：禁用指定的 Nuitka 插件。
- `--verbose`：输出详细的编译信息。
- `--assume-yes`：在提示时自动回答“是”。

## 优化选项
Nuitka 还提供了一些优化选项来提升打包程序的性能和体积：

- `--lto`：启用链接时优化（Link Time Optimization），进一步优化二进制文件体积和性能。
- `--nofollow-imports`：避免跟踪不必要的模块依赖导入，减少可执行文件的体积。
- `--remove-output`：在每次构建完成后，删除临时的构建文件，节省磁盘空间。

## 处理第三方依赖
如果 Nuitka 无法自动检测到所有第三方依赖，你可以使用 `--include-data-dir` 选项来指定静态资源或依赖的路径：
```bash
nuitka --onefile --standalone --include-data-dir=./data=./data pdf_extract_tool.py
```
这样可以将项目中的 `data` 文件夹一并打包。

## 高级功能
Nuitka 支持多线程和多进程，并且可以使用 C 编译器的优化选项（如 `-O3`）来加速运行速度：
```bash
nuitka --standalone --onefile --optimize=2 pdf_extract_tool.py
```
`--optimize=2` 选项表示使用 C 编译器的最高优化等级。

这些是 Nuitka 的基本使用方法和一些高级特性。你可以根据项目的具体需求来选择合适的选项进行编译。


> 大家在阅读过程中有任何问题，或者觉得有收获的话，欢迎点赞、评论和收藏。



![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')


## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)就能上手做AI项目。
---
title: 写好的Python程序怎么分享给别人？PyInstaller打包教程
date: 2026-04-17 22:10:00
tags: [PyInstaller, Python, 打包, exe, 分发]
categories: PyInstaller打包
---

## 一个让很多Python开发者头疼的问题

你花了一个周末，写了一个超好用的Python小工具。

运行效果完美，代码也很优雅。你兴冲冲地把代码分享给同事，结果同事回了一句：

> "怎么运行？我没装Python啊。"

你："你安装一下Python呗。"

同事："装完Python还要装一堆库？太麻烦了吧……"

你："……"

然后这个工具就再也没有第二个人用过。

**这就是Python开发者最常遇到的分发问题。**

## 💡 解决方案：PyInstaller

PyInstaller可以把你的Python程序打包成一个独立的可执行文件（Windows上是.exe，Mac上是.app），对方不需要安装Python，也不需要安装任何依赖库，双击就能运行。

就像你给别人发一个安装包，他下载下来直接就能用。

### 安装PyInstaller

```bash
pip install pyinstaller
```

一行命令，搞定。

### 最简单的打包

```bash
pyinstaller your_script.py
```

运行完之后，在dist目录下就能找到打包好的可执行文件。

就这么简单——**你写的Python脚本，变成了一个独立程序。**

## 🔧 实际打包中的一些细节

当然，实际项目中你会遇到更复杂的情况。让我分享一下我打包python-office时的经验：

### 1. 单文件模式

默认PyInstaller会生成一个文件夹（里面有很多文件），你想打包成一个单独的文件：

```bash
pyinstaller -F your_script.py
```

加一个`-F`参数就行。

### 2. 添加图标

一个没有图标的程序看起来太low了：

```bash
pyinstaller -F -i your_icon.ico your_script.py
```

Mac上用`.icns`格式，Windows上用`.ico`格式。

### 3. 隐藏控制台窗口

如果你的程序有图形界面，不希望弹出一个黑色的命令行窗口：

```bash
pyinstaller -F -w your_script.py
```

`-w`参数就是no window的意思。

### 4. 打包数据文件

如果你的程序需要读取配置文件、图片等资源：

```bash
pyinstaller -F --add-data "config.json;." your_script.py
```

Windows用分号`;`，Mac/Linux用冒号`:`。

## 📦 打包后的文件太大怎么办？

这是很多人反馈的问题——PyInstaller打包出来的文件动辄几十MB，甚至上百MB。

这是因为PyInstaller会把Python解释器和所有用到的库都打包进去。

**解决办法：**
1. 创建虚拟环境，只安装必要的库，然后在虚拟环境里打包
2. 使用`--exclude-module`排除不需要的模块
3. 使用UPX压缩打包后的文件

```bash
# 在干净的虚拟环境中打包
python -m venv pack_env
source pack_env/bin/activate  # Windows: pack_env\Scripts\activate
pip install pyinstaller
pip install -r requirements.txt  # 只装你需要的
pyinstaller -F your_script.py
```

## 🎯 我的PyInstaller课程

如果你在打包过程中遇到了各种奇怪的问题——缺少模块、路径错误、文件太大、打包后运行报错……别慌，我专门做了一门PyInstaller打包教程。

课程内容包括：
- ✅ 从安装到打包的完整流程
- ✅ 单文件/单目录/自定义打包模式
- ✅ 数据文件、资源文件的打包处理
- ✅ 常见报错的排查和解决
- ✅ 文件体积优化技巧
- ✅ 实际项目的打包案例

👇 扫码添加微信，咨询课程详情
微信号：python-office

## 相关阅读
- [用PyInstaller打包Python程序，踩过的10个坑和解决方案](02-用PyInstaller打包Python程序踩过的10个坑和解决方案.md)
- [一个Python脚本变成独立exe，只需要这3步](03-一个Python脚本变成独立exe只需要这3步.md)

程序员晚枫专注Python自动化办公和AI编程实战教学，github 1000+ star开源项目python-office作者。

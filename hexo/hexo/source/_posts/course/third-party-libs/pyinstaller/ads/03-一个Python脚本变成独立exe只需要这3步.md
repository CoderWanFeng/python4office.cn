---
title: 一个Python脚本变成独立exe，只需要这3步
date: 2026-04-17 22:30:00
tags: [PyInstaller, Python, exe, 打包, 新手教程]
categories: PyInstaller打包
---

## 最简单的PyInstaller打包教程

网上搜PyInstaller教程，动辄几千字，看得人头大。

今天我给你一个**最简版的打包教程**——只需要3步，你的Python脚本就能变成独立的exe文件。

是的，3步就够了。

## 📋 准备工作

在开始之前，确保你有一份能正常运行的Python脚本。

我们以一个简单的示例为例：

```python
# hello.py
print("Hello, 程序员晚枫！")
name = input("请输入你的名字：")
print(f"你好，{name}！欢迎使用Python自动化办公工具。")
input("按回车键退出...")
```

这个脚本功能很简单：打印欢迎语，输入名字，再打招呼。但不管多简单的脚本，打包流程都是一样的。

## 第一步：安装PyInstaller

打开终端（Windows上是cmd或PowerShell），输入：

```bash
pip install pyinstaller
```

看到"Successfully installed pyinstaller"就说明安装成功了。

**小建议**：建议在一个新的虚拟环境中安装，避免打包进去不必要的依赖。

## 第二步：执行打包命令

在脚本所在的目录下，运行：

```bash
pyinstaller -F -i icon.ico hello.py
```

参数说明：
- `-F`：打包成单个exe文件
- `-i icon.ico`：设置程序图标（如果你没有图标文件，去掉这个参数就行）
- `hello.py`：你的脚本文件名

运行过程中你会看到一堆输出信息，不用担心，让它跑完就行。

大约10-30秒后（取决于项目大小），你会看到：

```
Building EXE from EXE-00.toc completed successfully.
```

**打包成功！**

## 第三步：找到你的exe

打开dist目录，里面就有你的exe文件了。

把它发给任何人，对方双击就能运行——不需要安装Python，不需要安装任何依赖。

> 💡 **注意**：打包过程中生成的build目录和.spec文件可以删掉，你只需要保留dist目录里的exe。

## 🎉 就是这么简单

总结一下，3步流程：

```
第一步：pip install pyinstaller
第二步：pyinstaller -F your_script.py
第三步：去dist目录拿exe
```

**连一个Python新手都能在5分钟内完成。**

## 🔧 进阶：常见需求

如果你有更多需求，这里也给你列出来了：

**需要控制台窗口**（默认就有，不用加参数）

**不需要控制台窗口**（比如GUI程序）：
```bash
pyinstaller -F -w hello.py
```

**需要包含数据文件**：
```bash
pyinstaller -F --add-data "config.json;." hello.py
```

**想要自定义程序名称**：
```bash
pyinstaller -F -n "我的工具" hello.py
```

## ⚠️ 几个注意事项

1. **打包前先在本地测试通过**——确保你的脚本能正常运行
2. **尽量不要打包太大的项目**——如果项目依赖很多库，打包后的文件会很大
3. **杀毒软件可能误报**——这是PyInstaller的通病，可以忽略
4. **第一次打包建议用最简单的命令**——先确保能成功，再慢慢加参数

## 📚 更多PyInstaller教程

如果你在实际打包中遇到了问题，或者想要学习更高级的打包技巧，欢迎查看我的完整PyInstaller课程：

- ✅ 从零开始的打包教程
- ✅ 10个常见报错的解决方案
- ✅ 打包体积优化技巧
- ✅ 实际项目打包案例

👇 扫码添加微信，咨询课程详情
微信号：aiwf365

## 相关阅读
- [写好的Python程序怎么分享给别人？PyInstaller打包教程](01-写好的Python程序怎么分享给别人PyInstaller打包教程.md)
- [用PyInstaller打包Python程序，踩过的10个坑和解决方案](02-用PyInstaller打包Python程序踩过的10个坑和解决方案.md)

程序员晚枫专注Python自动化办公和AI编程实战教学，github 1000+ star开源项目python-office作者。


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



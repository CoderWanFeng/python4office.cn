---
title: 第1讲 搭建开发环境与HelloWorld
date: "2026-04-28 23:54:00"
tags: ["python", "入门", "课程", "第1讲"]
cover: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=1200&auto=format&fit=crop"
---


<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<!-- more -->
<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/a8bdeb7d-f6a8-4ad5-8020-e206055dd039/Python编程：从入门到实践_第3版__.png" alt="Python编程：从入门到实践（第3版）" width="400"/>
</p>
> 📖 **一起读书吧！** 加入《Python编程：从入门到实践》共读营 👉 [点击参加](https://mp.weixin.qq.com/s/ehe2vMrfAFscRLqbM9TF-g)



## 本讲内容

- 安装Python（Windows / macOS / Linux）
- 安装代码编辑器 VS Code（第3版推荐）
- 运行Hello World的3种方式
- 从终端运行Python程序
- 解决常见安装问题

## 学习目标

在电脑上跑通第一个Python程序 🎉

---

## 1. 安装Python

去官网下载最新版：[https://www.python.org/downloads/](https://www.python.org/downloads/)

> 官方文档：[Using Python on Windows](https://docs.python.org/3/using/windows.html)、[Using Python on macOS](https://docs.python.org/3/using/mac.html)、[Using Python on Unix](https://docs.python.org/3/using/unix.html)

### Windows用户

安装时务必勾选 **✅ Add Python to PATH**（最重要！）

### macOS用户

建议用 Homebrew 安装：
```bash
brew install python
```

### Linux用户

通常已预装，检查版本：
```bash
python3 --version
```

### 验证安装

```bash
python --version
# 或
python3 --version
# 输出：Python 3.x.x
```

## 2. 安装VS Code（第3版推荐编辑器）

《Python编程从入门到实践》第3版推荐使用 **VS Code**，免费、轻量、跨平台。

下载地址：[https://code.visualstudio.com/](https://code.visualstudio.com/)

安装Python扩展：
1. 打开VS Code
2. 按 `Ctrl+Shift+X`（Windows）或 `Cmd+Shift+X`（Mac）打开扩展
3. 搜索 **Python**，安装微软官方扩展

## 3. 运行Hello World的3种方式

### 方式一：交互式解释器（适合尝鲜）

命令行输入 `python`（Windows）或 `python3`（Linux/Mac）：

```python
>>> print("Hello, World!")
Hello, World!
>>> 2 + 2
4
>>> exit()  # 退出交互模式
```

> 官方文档：[1. Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
>
> 交互模式有两个提示符：
> - `>>>` — 主提示符，等待输入
> - `...` — 次提示符，用于多行语句（如 for 循环、函数定义）

### 方式二：一行命令（适合快速计算）

```bash
python -c "print('Hello, World!')"
python3 -c "print(2**10)"
```

### 方式三：写脚本文件（实际开发用）

新建文件 `hello.py`，写入：

```python
# hello.py
print("Hello, World!")
```

VS Code中按 `F5` 运行，或命令行运行：

```bash
python hello.py
# 或
python3 hello.py
```

## 4. 从终端运行Python程序

### Windows

```bash
# 打开命令提示符（Win+R → 输入cmd）
cd Desktop
python hello.py
```

### macOS / Linux

```bash
# 打开终端（Cmd+Space → 搜索"Terminal"）
cd ~/Desktop
python3 hello.py
```

## 5. 常见安装问题

| 问题 | 解决方法 |
|------|---------|
| `python` 找不到 | Windows重新安装，勾选Add to PATH；Linux用 `python3` |
| 终端乱码 | 文件保存为UTF-8编码（VS Code右下角点击UTF-8） |
| 安装被杀毒拦截 | 允许Python通过防火墙 |

> 官方文档：[A.1.2. Troubleshooting Installation](https://docs.python.org/3/using/windows.html#installer-repair) — Windows安装问题排查。

---

## 📚 官方文档参考

- [Using Python](https://docs.python.org/3/using/index.html) — 跨平台安装配置
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) — 官方入门教程
- [Installing Python Modules](https://docs.python.org/3/installing/index.html) — 第三方模块安装
- [1. Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)

---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲](https://www.bilibili.com/cheese/play/ss982042944)
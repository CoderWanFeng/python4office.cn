---
title: Python程序打包后从700MB瘦身到50MB的完整方案
date: 2026-04-17 10:00:00
tags: [PyInstaller, Python打包, 优化, 虚拟环境]
---

大家好，这里是程序员晚枫，正在all in AI编程实战。

第一次用PyInstaller打包的人，大概率会崩溃：

**一个10行的Python脚本，打包后700MB？？？**

---

## 为什么这么大？

PyInstaller默认会把Python解释器和所有依赖都打包进去。

但你可以通过以下方法瘦身：

### 1. 使用虚拟环境（最关键）

```bash
python -m venv venv
source venv/bin/activate  # 激活
pip install -r requirements.txt  # 只装必要的包
pyinstaller --onefile app.py
```

**只用虚拟环境里的包，别用全局Python的200个包！**

### 2. 排除不需要的模块

```bash
pyinstaller --onefile --exclude-module matplotlib app.py
```

### 3. 使用UPX压缩

```bash
pip install pyinstaller[upx]
```

---

## 详细教程

👉 [PyInstaller瘦身教程](/course/third-party-libs/pyinstaller/7-瘦身/)

我的13讲教程覆盖了打包的所有坑：

- 环境隔离 → 核心概念 → 命令行参数
- spec文件 → 图形化 → 瘦身优化
- 问题定位 → 专业实践 → 综合实战

**从700MB到50MB，就差一个教程的距离。**

---

程序员晚枫专注AI编程培训，小白看完他和图灵社区合作的教程[《30讲·AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)就能上手做AI项目。

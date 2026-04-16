---
title: Python实战项目：我写了50行代码，自动整理乱糟糟的下载文件夹
date: 2026-02-28 21:09:00
tags: [Python实战, 自动化, 文件整理]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://www.bilibili.com/cheese/play/ss982042944'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
    </a>   
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
<a href="https://www.bilibili.com/cheese/play/ss982042944">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

前面我们学习了Python的基础知识。今天开始**实战项目**，把学到的知识用起来。

第一个项目：**自动整理下载文件夹**。只需要50行代码，就能让你的Downloads文件夹井井有条。

---

## 项目需求分析

### 问题
下载文件夹通常很乱：文档、图片、视频混在一起，找文件很困难。

> 💡 **场景**：你下载了一堆东西，有PDF报告、照片、压缩包，每次要找某个文件都要翻半天。

### 解决方案
按文件类型自动分类：
- 图片 → Images/
- 文档 → Documents/
- 视频 → Videos/
- 压缩包 → Archives/
- 代码 → Code/

---

## 完整代码

```python
import os
import shutil
from pathlib import Path

def organize_downloads(download_path=None):
    """自动整理下载文件夹"""
    
    # 如果没有指定路径，使用默认下载文件夹
    if download_path is None:
        download_path = Path.home() / "Downloads"
    else:
        download_path = Path(download_path)
    
    # 文件类型映射（按后缀分类）
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c']
    }
    
    # 创建分类文件夹
    for folder in file_types.keys():
        folder_path = download_path / folder
        folder_path.mkdir(exist_ok=True)
    
    # 统计信息
    stats = {key: 0 for key in file_types.keys()}
    stats['Others'] = 0
    
    # 遍历文件
    for item in download_path.iterdir():
        # 跳过文件夹和本脚本
        if not item.is_file() or item.name == os.path.basename(__file__):
            continue
        
        # 获取文件扩展名
        ext = item.suffix.lower()
        
        # 确定目标文件夹
        moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                target = download_path / folder / item.name
                
                # 如果文件已存在，添加序号
                counter = 1
                original_target = target
                while target.exists():
                    stem = original_target.stem
                    suffix = original_target.suffix
                    target = original_target.with_name(f"{stem}_{counter}{suffix}")
                    counter += 1
                
                shutil.move(str(item), str(target))
                stats[folder] += 1
                moved = True
                print(f"移动: {item.name} -> {folder}/")
                break
        
        if not moved:
            stats['Others'] += 1
    
    # 打印统计
    print("\n" + "="*30)
    print("整理完成！统计信息：")
    for category, count in stats.items():
        if count > 0:
            print(f"  {category}: {count}个文件")
    print("="*30)

# 运行
if __name__ == "__main__":
    organize_downloads()
```

---

## 运行效果

**运行前，下载文件夹是这样的：**

```
Downloads/
  ├── 报告.pdf
  ├── 照片.jpg
  ├── 视频.mp4
  ├── 小说.txt
  ├── 资料.zip
  ├── 论文.docx
  └── 代码.py
```

**运行程序：**

```bash
python organize_downloads.py
```

**运行后：**

```
移动: 报告.pdf -> Documents/
移动: 照片.jpg -> Images/
移动: 视频.mp4 -> Videos/
移动: 小说.txt -> Documents/
移动: 资料.zip -> Archives/
移动: 论文.docx -> Documents/
移动: 代码.py -> Code/

==============================
整理完成！统计信息：
  Images: 1个文件
  Documents: 3个文件
  Videos: 1个文件
  Audio: 0个文件
  Archives: 1个文件
  Code: 1个文件
==============================
```

**最终目录结构：**

```
Downloads/
  ├── Images/
  │   └── 照片.jpg
  ├── Documents/
  │   ├── 报告.pdf
  │   ├── 小说.txt
  │   └── 论文.docx
  ├── Videos/
  │   └── 视频.mp4
  ├── Audio/
  ├── Archives/
  │   └── 资料.zip
  ├── Code/
  │   └── 代码.py
  └── organize_downloads.py
```

---

## 代码关键点解析

### 1. pathlib.Path - 优雅的路径操作

```python
from pathlib import Path

# 拼接路径
path = Path.home() / "Downloads" / "Images"

# 获取后缀
ext = "报告.pdf".suffix  # ".pdf"

# 检查存在
path.exists()
```

### 2. 处理重名文件

如果目标文件夹已有同名文件，自动加序号：

```
报告.pdf → 报告_1.pdf → 报告_2.pdf
```

### 3. 跳过正在运行的脚本

```python
if item.name == os.path.basename(__file__):
    continue  # 不要把自己也移动了！
```

---

## 进阶功能

### 按日期分类

```python
from datetime import datetime

# 获取文件修改时间
mtime = datetime.fromtimestamp(item.stat().st_mtime)
date_folder = mtime.strftime('%Y-%m')  # 2024-01

target = download_path / date_folder / folder / item.name
```

### 添加更多文件类型

```python
file_types['Ebooks'] = ['.epub', '.mobi', '.azw3']
file_types['Data'] = ['.csv', '.json', '.xml']
```

---


---

## 📚 推荐：Python 零基础实战营

**系统学习Python，推荐这个免费入门课程 👇**

| 特点 | 说明 |
|-----|------|
| 🎯 专为0基础设计 | 门槛低，上手快 |
| 📹 配套视频讲解 | 配合文章学习效果更好 |
| 💬 专属答疑群 | 遇到问题有人带 |
| 🎁 实体书赠送 | 优秀学员送《Python编程从入门到实践》 |

👉 **[点击免费领取 Python 零基础实战营](https://appycyfaqcq1951.pc.xiaoe-tech.com/p/t_pc/goods_pc_detail/goods_detail/course_38vSeD9XU0XdsWnT6jLTaDeRxjT?channel_id=1515397)**


## 本讲小结

用到的知识：

| 知识 | 用途 |
|-----|------|
| `pathlib.Path` | 路径操作 |
| `os.listdir` / `iterdir` | 遍历文件 |
| `dict` 字典 | 文件类型映射 |
| `for` 循环 | 遍历每个文件 |
| `if` 条件判断 | 判断文件类型 |
| `shutil.move` | 移动文件 |

---

## 下节预告

第二个实战项目是**自动发送邮件报告**——每天自动生成数据报告发给老板！

👉 **[继续阅读：Python实战项目-自动发送邮件报告](./21-Python实战项目-自动发送邮件报告.md)**

---

## 课程导航

**上一篇：** [Python常用标准库](./19-Python常用标准库.md)

**下一篇：** [Python实战项目-自动发送邮件报告](./21-Python实战项目-自动发送邮件报告.md)

---

*PS：文件自动化整理是每个程序员都应该会的技能。学会这个，节省大量找文件的时间！*


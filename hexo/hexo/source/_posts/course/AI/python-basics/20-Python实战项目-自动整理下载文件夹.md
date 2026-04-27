---
title: Python实战项目：我写了50行代码，自动整理乱糟糟的下载文件夹
date: 2026-02-28 21:09:00
tags: [Python实战, 自动化, 文件整理]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw'>
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
<a href="https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

你有没有这样的经历？打开下载文件夹，里面几百个文件乱七八糟地堆在一起——PDF报告、微信图片、安装包、压缩包……找一个文件要翻半天，强迫症看了简直受不了。

> 💡 **场景**：你下载了一堆东西，有PDF报告、照片、压缩包，每次要找某个文件都要翻半天。更烦的是，同一个文件下载了好几次，重名的到处都是。

以前我每个月都要手动整理一次，费时费力。后来我花了一个下午写了50行Python代码，从此下载文件夹自动分类，再也不用操心了。

今天这个实战项目，就是**自动整理下载文件夹**。只需要50行代码，就能让你的Downloads文件夹井井有条。

---

## 项目需求分析

### 问题
下载文件夹通常很乱：文档、图片、视频混在一起，找文件很困难。

### 解决方案
按文件类型自动分类：
- 图片 → Images/
- 文档 → Documents/
- 视频 → Videos/
- 压缩包 → Archives/
- 代码 → Code/
- 音频 → Audio/

### 技术选型

| 方案 | 优点 | 缺点 |
|-----|------|------|
| os + shutil | 不用装第三方库 | API不够优雅 |
| pathlib + shutil | 代码简洁，推荐 | Python 3.4+ |
| 第三方库send2trash | 误删可恢复 | 需要安装 |

> 💡 **我的选择**：用pathlib + shutil，纯标准库，零依赖。

---

## 完整代码

```python
import os
import shutil
from pathlib import Path
from datetime import datetime

def organize_downloads(download_path=None, dry_run=False):
    """自动整理下载文件夹
    
    Args:
        download_path: 目标路径，默认为系统下载文件夹
        dry_run: 试运行模式，只打印不实际移动文件
    """
    
    # 如果没有指定路径，使用默认下载文件夹
    if download_path is None:
        download_path = Path.home() / "Downloads"
    else:
        download_path = Path(download_path)
    
    # 检查目录是否存在
    if not download_path.exists():
        print(f"❌ 目录不存在：{download_path}")
        return
    
    # 文件类型映射（按后缀分类）
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.md', '.rtf', '.odt'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.go', '.rs', '.ts', '.vue'],
        'Executables': ['.exe', '.dmg', '.msi', '.deb', '.rpm', '.app'],
        'Data': ['.csv', '.json', '.xml', '.yaml', '.yml', '.sql', '.db']
    }
    
    # 创建分类文件夹
    for folder in file_types.keys():
        folder_path = download_path / folder
        folder_path.mkdir(exist_ok=True)
    
    # 统计信息
    stats = {key: 0 for key in file_types.keys()}
    stats['Others'] = 0
    total_size = 0
    
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
                
                # 获取文件大小
                file_size = item.stat().st_size
                total_size += file_size
                
                if dry_run:
                    print(f"[试运行] 移动: {item.name} -> {folder}/ ({format_size(file_size)})")
                else:
                    shutil.move(str(item), str(target))
                    print(f"移动: {item.name} -> {folder}/ ({format_size(file_size)})")
                
                stats[folder] += 1
                moved = True
                break
        
        if not moved:
            stats['Others'] += 1
    
    # 打印统计
    print("\n" + "="*40)
    print("📊 整理完成！统计信息：")
    for category, count in stats.items():
        if count > 0:
            print(f"  {category}: {count}个文件")
    print(f"  总计处理：{sum(stats.values())}个文件")
    print(f"  总大小：{format_size(total_size)}")
    if dry_run:
        print("  ⚠️ 以上为试运行，未实际移动文件")
    print("="*40)

def format_size(size_bytes):
    """将字节数格式化为可读大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f}TB"

# 运行
if __name__ == "__main__":
    # 先试运行看看效果
    print("🔍 试运行模式（不会实际移动文件）\n")
    organize_downloads(dry_run=True)
    
    # 确认后再真正运行
    # input("\n确认整理？(y/n): ")
    # organize_downloads()
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
  ├── 代码.py
  ├── 音乐.mp3
  ├── 安装包.exe
  └── 数据.csv
```

**运行程序：**

```bash
python organize_downloads.py
```

**试运行输出：**

```
🔍 试运行模式（不会实际移动文件）

[试运行] 移动: 报告.pdf -> Documents/ (1.2MB)
[试运行] 移动: 照片.jpg -> Images/ (3.4MB)
[试运行] 移动: 视频.mp4 -> Videos/ (156.8MB)
[试运行] 移动: 小说.txt -> Documents/ (45.2KB)
[试运行] 移动: 资料.zip -> Archives/ (23.5MB)
[试运行] 移动: 论文.docx -> Documents/ (890.3KB)
[试运行] 移动: 代码.py -> Code/ (2.1KB)
[试运行] 移动: 音乐.mp3 -> Audio/ (5.6MB)
[试运行] 移动: 安装包.exe -> Executables/ (89.2MB)
[试运行] 移动: 数据.csv -> Data/ (12.3KB)

========================================
📊 整理完成！统计信息：
  Images: 1个文件
  Documents: 3个文件
  Videos: 1个文件
  Audio: 1个文件
  Archives: 1个文件
  Code: 1个文件
  Executables: 1个文件
  Data: 1个文件
  总计处理：10个文件
  总大小：280.7MB
  ⚠️ 以上为试运行，未实际移动文件
========================================
```

**正式运行后，最终目录结构：**

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
  │   └── 音乐.mp3
  ├── Archives/
  │   └── 资料.zip
  ├── Code/
  │   └── 代码.py
  ├── Executables/
  │   └── 安装包.exe
  ├── Data/
  │   └── 数据.csv
  └── organize_downloads.py
```

---

## 代码关键点解析

### 1. pathlib.Path - 优雅的路径操作

```python
from pathlib import Path

# 拼接路径（比os.path.join好看多了）
path = Path.home() / "Downloads" / "Images"

# 获取文件信息
item = Path("报告.pdf")
print(item.stem)   # "报告"（文件名，不含扩展名）
print(item.suffix)  # ".pdf"（扩展名）
print(item.name)    # "报告.pdf"（完整文件名）
print(item.parent)  # 所在目录

# 检查存在
path.exists()

# 获取文件大小
path.stat().st_size
```

### 2. 处理重名文件

如果目标文件夹已有同名文件，自动加序号，不会覆盖：

```python
# 重名处理逻辑
counter = 1
original_target = target
while target.exists():
    stem = original_target.stem
    suffix = original_target.suffix
    target = original_target.with_name(f"{stem}_{counter}{suffix}")
    counter += 1

# 效果：
# 报告.pdf → 报告_1.pdf → 报告_2.pdf
```

### 3. 试运行模式（dry_run）

这是我自己踩坑后加的功能。一开始直接运行，结果把不该移动的文件也移了，后悔都来不及。

```python
if dry_run:
    print(f"[试运行] 移动: {item.name} -> {folder}/")
else:
    shutil.move(str(item), str(target))
    print(f"移动: {item.name} -> {folder}/")
```

> 💡 **强烈建议**：先跑一遍`dry_run=True`，确认没问题再正式运行。

### 4. 文件大小格式化

```python
def format_size(size_bytes):
    """将字节数格式化为可读大小"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f}TB"

# 1024 → "1.0KB"
# 1048576 → "1.0MB"
```

---

## 进阶功能

### 按日期分类

```python
from datetime import datetime

def organize_by_date(download_path):
    """按日期+类型双层分类"""
    download_path = Path(download_path)
    
    for item in download_path.iterdir():
        if not item.is_file():
            continue
        
        # 获取文件修改时间
        mtime = datetime.fromtimestamp(item.stat().st_mtime)
        date_folder = mtime.strftime('%Y-%m')  # 按月份分组
        
        # 按类型分组
        ext = item.suffix.lower()
        type_folder = get_type_folder(ext)
        
        # 目标路径：日期/类型/文件
        target = download_path / date_folder / type_folder / item.name
        target.parent.mkdir(parents=True, exist_ok=True)
        
        shutil.move(str(item), str(target))
        print(f"移动: {item.name} -> {date_folder}/{type_folder}/")
```

**按日期分类后的目录结构：**

```
Downloads/
  ├── 2026-03/
  │   ├── Documents/
  │   │   └── 季度报告.pdf
  │   └── Images/
  │       └── 团建照片.jpg
  ├── 2026-04/
  │   ├── Documents/
  │   │   └── 月度总结.docx
  │   └── Archives/
  │       └── 项目备份.zip
```

### 查找重复文件

```python
import hashlib

def find_duplicates(directory):
    """查找重复文件（基于文件内容的MD5）"""
    directory = Path(directory)
    hash_map = {}  # {md5: [file1, file2, ...]}
    
    for item in directory.rglob("*"):
        if not item.is_file():
            continue
        
        # 计算文件MD5
        md5 = hashlib.md5(item.read_bytes()).hexdigest()
        
        if md5 not in hash_map:
            hash_map[md5] = []
        hash_map[md5].append(item)
    
    # 输出重复文件
    print("🔍 重复文件：")
    total_wasted = 0
    for md5, files in hash_map.items():
        if len(files) > 1:
            size = files[0].stat().st_size
            wasted = size * (len(files) - 1)
            total_wasted += wasted
            print(f"\n  相同文件（{format_size(size)} 每个）：")
            for f in files:
                print(f"    - {f}")
    
    print(f"\n💾 重复文件浪费空间：{format_size(total_wasted)}")

find_duplicates(Path.home() / "Downloads")
```

### 清理大文件

```python
def find_large_files(directory, threshold_mb=100):
    """查找超过指定大小的大文件"""
    directory = Path(directory)
    threshold = threshold_mb * 1024 * 1024  # 转为字节
    
    large_files = []
    for item in directory.rglob("*"):
        if item.is_file() and item.stat().st_size > threshold:
            large_files.append((item, item.stat().st_size))
    
    # 按大小排序
    large_files.sort(key=lambda x: x[1], reverse=True)
    
    print(f"🔍 超过 {threshold_mb}MB 的大文件：")
    for f, size in large_files:
        mtime = datetime.fromtimestamp(f.stat().st_mtime).strftime('%Y-%m-%d')
        print(f"  {format_size(size):>10}  {mtime}  {f}")

find_large_files(Path.home() / "Downloads", threshold_mb=50)
```

---

## 避坑指南

### 1. 文件被占用

```python
# ❌ 问题：文件正在被其他程序使用，移动会失败
# ✅ 解决：加异常处理
try:
    shutil.move(str(item), str(target))
except PermissionError:
    print(f"⚠️ 文件被占用，跳过：{item.name}")
except OSError as e:
    print(f"⚠️ 移动失败：{item.name}，原因：{e}")
```

### 2. 中文文件名乱码

```python
# ❌ 问题：Windows下中文路径可能乱码
# ✅ 解决：使用pathlib，它对Unicode支持更好
from pathlib import Path
# pathlib天然支持中文路径，不用额外处理
```

### 3. 符号链接和快捷方式

```python
# ❌ 问题：误移动快捷方式
# ✅ 解决：检查是否为符号链接
if item.is_symlink():
    continue  # 跳过符号链接
```

### 4. 不要移动正在运行的脚本

```python
# ❌ 危险：脚本把自己移动了，程序直接崩
# ✅ 正确：跳过自身
if item.name == os.path.basename(__file__):
    continue
```

---

## 🔥 进阶：定时自动整理

用schedule库实现定时自动整理，每天自动跑一次：

```python
import schedule
import time
from pathlib import Path

def auto_organize():
    """定时自动整理"""
    print(f"\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M')} 开始自动整理...")
    organize_downloads(dry_run=False)
    print("✅ 整理完成！\n")

# 每天晚上11点自动整理
schedule.every().day.at("23:00").do(auto_organize)

print("🤖 自动整理服务已启动，每天23:00整理下载文件夹")
while True:
    schedule.run_pending()
    time.sleep(60)
```

---

## 性能优化

如果你的下载文件夹有上万个文件，可以考虑这些优化：

```python
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

def move_file(item, target_folder, file_types):
    """移动单个文件（线程安全版本）"""
    ext = item.suffix.lower()
    for folder, extensions in file_types.items():
        if ext in extensions:
            target = target_folder / folder / item.name
            counter = 1
            while target.exists():
                stem = target.stem
                suffix = target.suffix
                target = target.with_name(f"{stem}_{counter}{suffix}")
                counter += 1
            shutil.move(str(item), str(target))
            return folder
    return 'Others'

# 多线程版本（大量文件时更快）
def organize_fast(download_path):
    download_path = Path(download_path)
    files = [f for f in download_path.iterdir() if f.is_file()]
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(
            lambda f: move_file(f, download_path, file_types),
            files
        ))
    
    print(f"处理了 {len(results)} 个文件")
```

> 💡 **但是**：文件操作通常不是CPU密集型，大多数情况下单线程就够了。只有上千个文件时才需要考虑多线程。

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
| `pathlib.Path` | 路径操作、文件遍历 |
| `os.listdir` / `iterdir` | 遍历文件 |
| `dict` 字典 | 文件类型映射 |
| `for` 循环 | 遍历每个文件 |
| `if` 条件判断 | 判断文件类型 |
| `shutil.move` | 移动文件 |
| `hashlib` | 计算文件MD5（查重） |
| `datetime` | 获取文件修改时间 |

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


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



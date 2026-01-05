---
title: 《Python绘图必备！Matplotlib超全入门教程，看完秒变数据可视化大神！》
date: 2025-01-29 16:24:04
tags: 第三方库
---


Matplotlib 是 Python 中一个非常强大的绘图库，广泛用于数据可视化，能够生成各种静态、动画和交互式图表。以下是关于如何使用 Matplotlib 的一些基础内容和示例。
## 1、安装 Matplotlib
如果你还没有安装 Matplotlib，可以通过 pip 命令安装：

```python
pip install matplotlib
```

## 2、基本用法
```
导入库
Python复制
import matplotlib.pyplot as plt
```
pyplot 是 Matplotlib 中最常用的模块，提供了类似于 MATLAB 的绘图接口。
绘制简单的折线图
```
import matplotlib.pyplot as plt

### 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

### 创建图形
plt.plot(x, y, label="Line 1", color="blue", linestyle="--", marker="o")
plt.title("CoderWanFeng Line Plot")  # 添加标题
plt.xlabel("X-axis")  # 添加X轴标签
plt.ylabel("Y-axis")  # 添加Y轴标签
plt.legend()  # 添加图例
plt.grid(True)  # 添加网格
plt.show()  # 显示图形
```
绘制散点图
```
import matplotlib.pyplot as plt

### 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

### 创建图形
plt.scatter(x, y, color="red", marker="*", s=100)  # s是点的大小
plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
```
## 3、多图绘制

可以使用 plt.subplots() 创建多个子图。
```
import matplotlib.pyplot as plt

### 数据
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 9, 16, 25]

### 创建2x1的子图布局
fig, axs = plt.subplots(2, 1, figsize=(6, 8))  # figsize设置图形大小

### 在第一个子图中绘制折线图
axs[0].plot(x, y1, label="Line 1", color="blue")
axs[0].set_title("Line Plot")
axs[0].set_xlabel("X-axis")
axs[0].set_ylabel("Y-axis")
axs[0].legend()

### 在第二个子图中绘制散点图
axs[1].scatter(x, y2, color="red", marker="o", s=100)
axs[1].set_title("Scatter Plot")
axs[1].set_xlabel("X-axis")
axs[1].set_ylabel("Y-axis")

### 调整子图之间的间距
plt.tight_layout()
plt.show()
```

## 4、自定义样式
Matplotlib 提供了丰富的样式选项，可以通过 plt.style.use() 应用预定义的样式。
```
import matplotlib.pyplot as plt

### 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

### 应用样式
plt.style.use("seaborn-darkgrid")

### 绘图
plt.plot(x, y, label="Line 1", color="green", linestyle="-.")
plt.title("Styled Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

```

## 5、保存图形

可以使用 plt.savefig() 将图形保存为文件。
```
import matplotlib.pyplot as plt

### 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

### 绘图
plt.plot(x, y, label="Line 1", color="blue")
plt.title("Saved Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

### 保存图形
plt.savefig("my_plot.png")  # 保存为PNG格式
plt.show()
```
## 6、绘制柱状图

```
import matplotlib.pyplot as plt

# 数据
categories = ["A", "B", "C", "D", "E"]
values = [10, 15, 7, 5, 9]

# 绘制柱状图
plt.bar(categories, values, color=["red", "green", "blue", "yellow", "purple"])
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
```

## 7、绘制饼图

```
import matplotlib.pyplot as plt

# 数据
categories = ["A", "B", "C", "D", "E"]
values = [10, 15, 7, 5, 9]

# 绘制饼图
plt.pie(values, labels=categories, autopct="%1.1f%%", startangle=140)
plt.title("Pie Chart")
plt.show()
```

## 8、绘制直方图
```
import matplotlib.pyplot as plt
import numpy as np

# 数据
data = np.random.randn(1000)  # 生成随机数据

# 绘制直方图
plt.hist(data, bins=30, color="skyblue", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
```

## 9、总结
Matplotlib 是一个功能强大的绘图库，通过简单的代码可以生成各种类型的图表。你可以通过调整参数来自定义图表的样式、颜色、标签等，以满足不同的可视化需求。




![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')


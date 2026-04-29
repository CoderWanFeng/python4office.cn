---
title: 项目二 数据可视化
date: 2026-04-28 23:54:00
tags: [python,入门,课程,项目实战,数据可视化]
cover: https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop
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



## 项目介绍

用Python处理真实数据，生成可视化图表！用 **Matplotlib** 静态图、**Plotly** 交互图、**Pygal** 世界地图。

## 你将学会

- ✅ 随机漫步数据可视化
- ✅ 掷骰子概率分布（Matplotlib）
- ✅ CSV天气数据读取与分析
- ✅ Plotly交互式世界地图（**第2版新增**）
- ✅ GitHub活跃度数据可视化
- ✅ API数据获取（**第2版新增**）

**原书对应章节：第15-17章**

---

## 第1步：安装依赖

```bash
pip install matplotlib plotly pygal
```

## 第2步：Matplotlib 折线图

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, linewidth=3)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
```

## 第3步：Matplotlib 散点图

```python
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values,
            c=y_values, cmap=plt.cm.Blues,
            s=10)
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')
```

## 第4步：随机漫步

```python
from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = choice([1, -1]) * choice(range(0, 5))
            y_step = choice([1, -1]) * choice(range(0, 5))
            if x_step == 0 and y_step == 0:
                continue
            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)
```

## 第5步：掷骰子可视化

```python
from die import Die
import matplotlib.pyplot as plt

die = Die()
results = [die.roll() for _ in range(1000)]
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

plt.bar(range(1, 7), frequencies)
plt.show()
```

## 第6步：读取CSV数据

```python
import csv
from datetime import datetime

filename = 'sitka_weather_2018_simple.csv'
with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[5]))
        lows.append(int(row[6]))

fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.show()
```

## 第7步：Plotly交互式图表（第2版新增）

```python
import plotly.express as px

# 交互式散点图
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="petal_width",
                 color="species", title="Iris数据集")
fig.show()

# 绘制地图
import plotly.graph_objects as go

fig = go.Figure(data=go.Choropleth(
    locations=["CHN", "USA", "IND"],
    z=[1400, 330, 1380],
    text=["China", "United States", "India"],
    colorscale="Blues",
    autocolorscale=False
))
fig.show()
```

## 项目文件结构

```
data_visualization/
├── die.py                 # 骰子类
├── die_visual.py          # 骰子可视化
├── random_walk.py         # 随机漫步类
├── rw_visual.py           # 随机漫步可视化
├── weather_data/
│   └── sitka_weather_2018_simple.csv
├── earthquake_reader.py   # CSV地震数据
├── world_population.py    # Plotly世界地图
├── github_api.py          # API数据获取
└── matplotlib_plots/
    ├── squares_plot.png
    └── rw_visual.png
```

---

## 📚 官方文档参考

- [matplotlib 官方文档](https://matplotlib.org/stable/index.html)
- [plotly Python 文档](https://plotly.com/python/)
- [pygal 文档](https://pygal.readthedocs.io/en/stable/)
- [csv — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
- [json — JSON encoder and decoder](https://docs.python.org/3/library/json.html) — API数据读取

---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲](https://www.bilibili.com/cheese/play/ss982042944)
---
title: "用 Trae 做了一个爬虫：真实记录全过程"
date: 2026-04-12 00:00:00
categories:
- AI工具评测
tags:
- Trae
- Python自动化
- AI编程
- Python爬虫
- AI工具
- 爬虫
- 实战
description: "用 Trae AI 编程做了一个爬虫，记录全过程和真实感受"
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---



<!-- more -->

![用 Trae 做了一个爬虫：真实记录全过程 - 配图1](https://images.unsplash.com/photo-1677443994799-97b6aae1?w=800&h=400&fit=crop)
![用 Trae 做了一个爬虫：真实记录全过程 - 配图2](https://images.unsplash.com/photo-1518709268805-4e6709f4?w=800&h=400&fit=crop)

# 用 Trae 做了一个爬虫：真实记录全过程

## 先说结论

用 Trae 做一个简单爬虫，大概花了 **15 分钟**。

全程我没写一行代码，都是和 AI 对话让它完成的。

下面详细说说过程，有图有真相。

---

## 实验背景

我一直想做一个爬虫，爬取某个网站的文章标题和链接。

需求很简单：
- 输入一个网址
- 自动爬取页面标题和链接
- 保存到本地 txt 文件

这个需求用传统方式写，大概 50 行 Python 代码。

今天试试用 Trae，看 AI 能不能帮我搞定。

---

## 开始操作

### 第一步：打开 Trae，创建新项目

打开 Trae，新建一个 Python 项目。

界面很简洁，左边是文件列表，右边是代码编辑区。

底部有一个 AI 对话窗口，这个就是今天的主角。

### 第二步：告诉 AI 我要做什么

我在底部的对话框输入：

> "帮我写一个爬虫，爬取网页的标题和链接，保存到 result.txt"

AI 立刻开始响应。

---

## AI 的表现

### 第一轮：生成基础代码

AI 给出了一段完整的爬虫代码：

```python
import requests
from bs4 import BeautifulSoup

def crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = []
    links = []

    for item in soup.find_all('a'):
        title = item.get_text(strip=True)
        link = item.get('href')
        if title and link:
            titles.append(title)
            links.append(link)

    with open('result.txt', 'w', encoding='utf-8') as f:
        for i in range(len(titles)):
            f.write(f"{titles[i]} - {links[i]}\n")

    print(f"爬取完成，共 {len(titles)} 条数据")

if __name__ == "__main__":
    url = input("请输入网址：")
    crawl(url)
```

看起来不错，但我注意到几个问题：
1. 缺少错误处理（网站打不开怎么办？）
2. 没有处理相对链接
3. 只爬取了 `<a>` 标签

### 第三轮：让 AI 优化

我继续对话：

> "加上错误处理，还有相对链接转绝对链接"

AI 很快更新了代码：

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        results = []

        for item in soup.find_all('a'):
            title = item.get_text(strip=True)
            link = item.get('href')
            if title and link:
                # 相对链接转绝对链接
                full_link = urljoin(url, link)
                results.append(f"{title} | {full_link}")

        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(f"来源：{url}\n")
            f.write("=" * 50 + "\n")
            for line in results:
                f.write(line + "\n")

        print(f"爬取完成，共 {len(results)} 条数据，已保存到 result.txt")

    except requests.exceptions.RequestException as e:
        print(f"请求失败：{e}")

if __name__ == "__main__":
    url = input("请输入网址：")
    crawl(url)
```

这次好多了。

### 第四轮：添加批量爬取

我又加了个需求：

> "再加个功能，可以批量爬取多个页面"

AI 再次响应，给出了批量爬取的版本。

整个过程就是这样：**提需求 → 看结果 → 提新需求 → 看结果**。

---

## 真实感受

### ✅ 做得好的地方

1. **响应速度快**：基本秒回
2. **代码质量还行**：基础功能都能实现
3. **愿意改代码**：多轮对话很顺畅
4. **免费**：不用花钱

### ❌ 做得不好的地方

1. **有时会"失忆"**：聊久了忘记前面的需求
2. **复杂逻辑容易出错**：比如正则表达式
3. **需要人工检查**：AI 写的代码还是要自己跑一遍确认

---

## 用时统计

| 环节 | 用时 |
|------|------|
| 新建项目 | 1 分钟 |
| 描述需求 | 1 分钟 |
| 看第一版代码 | 2 分钟 |
| 优化3次 | 8 分钟 |
| 测试运行 | 3 分钟 |
| **总计** | **15 分钟** |

---

## 适合谁 / 不适合谁

**适合：**
- 刚学编程的新手
- 简单重复性任务
- 想快速验证想法的人

**不适合：**
- 需要复杂逻辑的项目
- 对代码质量要求高的
- 需要深度定制的

---

## 我的评分

| 维度 | 评分 | 说明 |
|------|------|------|
| 易用性 | ⭐⭐⭐⭐⭐ | 对话式操作，零门槛 |
| 功能强 | ⭐⭐⭐ | 简单任务够用，复杂的不行 |
| 性价比 | ⭐⭐⭐⭐⭐ | 免费，真香 |
| 稳定性 | ⭐⭐⭐ | 偶有小bug |

---

## 总结

**Trae 做简单任务，真的可以。**

15 分钟，一个爬虫搞定。

如果是专业开发，可能觉得差点意思。但对于新手，或者日常小工具来说，Trae 完全够用。

关键是——**免费**。

---

> 📌 **提示**：AI 写的代码，记得自己跑一遍测试。有些边界情况 AI 可能没考虑到。
>
> 如果你也有想做的自动化小工具，评论区说说，下期可以帮你用 Trae 做。

## 更新记录

- 2026-04-12：初稿发布


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



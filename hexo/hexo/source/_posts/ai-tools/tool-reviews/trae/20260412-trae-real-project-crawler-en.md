---
title: "Built a Crawler with Trae: Real Record of the Whole Process"
date: 2026-04-12 00:00:00
categories:
- AI Tools Review
tags:
- Trae
- AI工具
- AI编程
- AI Coding
- Crawler
- Practice
description: "Used Trae AI coding to build a crawler, recording the whole process and real impressions"
cover: https://images.unsplash.com/photo-1518709268805-4e6709f4?w=800&h=400&fit=crop
---




<!-- more -->

![Built a Crawler with Trae: Real Record of the Whole Process](https://images.unsplash.com/photo-1677443994799-97b6aae1?w=800&h=400&fit=crop)
![Built a Crawler with Trae: Real Record of the Whole Process](https://images.unsplash.com/photo-1518709268805-4e6709f4?w=800&h=400&fit=crop)

# Built a Crawler with Trae: Real Record of the Whole Process

## TL;DR

Building a simple crawler with Trae took about **15 minutes**.

I didn't write a single line of code the whole time, just chatted with AI to get it done.

Below is a detailed walkthrough of the process, with pictures and truth.

---

## Experiment Background

I've always wanted to build a crawler to scrape article titles and links from a website.

Requirements were simple:
- Input a URL
- Automatically scrape page titles and links
- Save to local txt file

This requirement would traditionally take about 50 lines of Python code.

Today I tried Trae, to see if AI could handle it.

---

## Starting the Operation

### Step 1: Open Trae, Create New Project

Open Trae, create a new Python project.

The interface is very clean, file list on the left, code editor on the right.

There's an AI chat window at the bottom, that's today's star.

### Step 2: Tell AI What I Want to Do

I typed in the bottom dialog:

> "Help me write a crawler to scrape webpage titles and links, save to result.txt"

AI immediately started responding.

---

## AI's Performance

### Round 1: Generate Basic Code

AI provided a complete crawler code:

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

    print(f"Crawling complete, {len(titles)} items")

if __name__ == "__main__":
    url = input("Please enter URL: ")
    crawl(url)
```

Looks good, but I noticed several issues:
1. Missing error handling (what if website doesn't open?)
2. No relative link handling
3. Only scraped `<a>` tags

### Round 3: Let AI Optimize

I continued the conversation:

> "Add error handling, and convert relative links to absolute links"

AI quickly updated the code:

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
                # Convert relative links to absolute links
                full_link = urljoin(url, link)
                results.append(f"{title} | {full_link}")

        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(f"Source: {url}\n")
            f.write("=" * 50 + "\n")
            for line in results:
                f.write(line + "\n")

        print(f"Crawling complete, {len(results)} items, saved to result.txt")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    url = input("Please enter URL: ")
    crawl(url)
```

Much better this time.
```

### Round 4: Add Batch Scraping

I added another requirement:

> "Add a feature to batch scrape multiple pages"

AI responded again with a batch scraping version.

The whole process was like this: **State requirement → Check result → State new requirement → Check result**.

---

## Real Impressions

### ✅ What It Did Well

1. **Fast response**: Basically instant replies
2. **Decent code quality**: Basic features all implemented
3. **Willing to modify code**: Multi-turn conversation very smooth
4. **Free**: No money needed

### ❌ What It Didn't Do Well

1. **Sometimes "forgets"**: After chatting for a while, forgets earlier requirements
2. **Complex logic prone to errors**: Like regular expressions
3. **Needs manual check**: Run AI-written code yourself to confirm

---

## Time Statistics

| Step | Time |
|------|------|
| Create new project | 1 minute |
| Describe requirements | 1 minute |
| Review first version code | 2 minutes |
| Optimize 3 times | 8 minutes |
| Test run | 3 minutes |
| **Total** | **15 minutes** |

---

## Who It's For / Not For

**For:**
- Beginners learning to code
- Simple repetitive tasks
- People who want to quickly verify ideas

**Not for:**
- Projects requiring complex logic
- High code quality requirements
- Deep customization needed

---

## My Ratings

| Dimension | Rating | Description |
|------|------|------|
| Ease of use | ⭐⭐⭐⭐⭐ | Conversational operation, zero threshold |
| Features | ⭐⭐⭐ | Enough for simple tasks, not for complex ones |
| Cost performance | ⭐⭐⭐⭐⭐ | Free, truly awesome |
| Stability | ⭐⭐⭐ | Occasional small bugs |

---

## Summary

**Trae really can do simple tasks.**

15 minutes, crawler done.

For professional development, might feel lacking. But for beginners or daily small tools, Trae is completely sufficient.

The key is — **it's free**.

---

> 📌 **Tip**: Remember to run test AI-written code yourself. Some edge cases AI might not have considered.
>
> If you also have small automation tools you want to make, tell me in comments, next issue can help you build with Trae.

## Update History

- 2026-04-12: Initial release


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



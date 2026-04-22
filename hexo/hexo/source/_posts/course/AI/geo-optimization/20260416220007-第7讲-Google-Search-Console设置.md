---
title: 第 7 讲：Google Search Console 设置
date: 2026-04-16 22:06:00
tags: [GEO优化, SEO, Google Search Console, 网站管理]
---

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

大家好，我是正在实战各种<a href="https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw" target="_blank">AI 项目</a>的程序员晚枫。

上一讲我们讲了技术层面的 GEO 优化，这一讲我们聚焦最重要的工具：

**Google Search Console（GSC）如何配置和使用？**

GSC 是 Google 官方提供的免费工具，是 SEO 必备。对于 GEO 优化，GSC 更是核心工具。

---

## 什么是 Google Search Console？

### 功能概览

Google Search Console 是 Google 提供的免费工具，帮助你：

1. **监控网站在 Google 搜索中的表现**
2. **发现和修复问题**
3. **提交网站地图**
4. **设置地理定位**
5. **查看搜索流量数据**

### 为什么 GEO 优化需要 GSC？

| GEO 相关功能 | 说明 |
|--------------|------|
| 地理定位 | 设置子域名/子目录的目标国家 |
| hreflang 监控 | 查看 hreflang 配置问题 |
| 国际定位问题 | 发现多语言网站的问题 |
| 地区流量分析 | 查看不同国家的流量数据 |

---

## GSC 注册与验证

### 第一步：访问 GSC

**网址**：https://search.google.com/search-console

**前提**：
- 有 Google 账号
- 网站已上线

### 第二步：添加网站

选择资源类型：

| 类型 | 适用场景 |
|------|----------|
| 网域 | 整个域名（推荐） |
| 网址前缀 | 特定子目录或子域名 |

**推荐**：选择"网域"，可以覆盖所有子域名。

### 第三步：验证网站

#### 方式一：DNS 验证（推荐）

1. 复制 TXT 记录值
2. 登录域名 DNS 管理面板
3. 添加 TXT 记录
4. 等待验证（可能需要几分钟到几小时）

**Cloudflare 配置示例**：
```
类型：TXT
名称：@（或留空）
内容：google-site-verification=XXXXXXXXXX
```

#### 方式二：HTML 文件验证

1. 下载验证文件
2. 上传到网站根目录
3. 点击验证

**文件位置**：
```
https://example.com/googleXXXXXX.html
```

#### 方式三：HTML 标签验证

在首页 `<head>` 中添加：
```html
<meta name="google-site-verification" content="XXXXXX" />
```

---

## 地理定位设置

### 什么是地理定位？

告诉 Google：某个子域名或子目录主要面向哪个国家/地区。

### 适用场景

| 架构 | 是否支持地理定位 |
|------|------------------|
| 子目录 | ✅ 支持 |
| 子域名 | ✅ 支持 |
| 独立域名 | ❌ 不需要（ccTLD 本身就是地理信号） |

### 设置步骤

1. 登录 GSC
2. 选择要设置的网站（子域名或子目录）
3. 点击"索引" → "地理位置"
4. 选择目标国家
5. 保存

**示例**：

```
网站：cn.example.com
地理位置：中国

网站：example.com/cn/
地理位置：中国
```

### 注意事项

1. **独立域名无需设置**
   
   .cn、.jp、.de 等国家域名本身就是地理信号

2. **设置后需要时间生效**
   
   通常需要几周到几个月

3. **不要过度限制**
   
   设置地理定位后，其他国家可能很难获得排名

---

## hreflang 问题监控

### 查看 hreflang 问题

GSC → 索引 → 国际定位

**常见问题**：

| 问题 | 原因 |
|------|------|
| 缺少返回链接 | 对方页面没有链接回来 |
| hreflang 值错误 | 语言或地区代码格式错误 |
| 重复的 hreflang | 多个页面使用相同的 hreflang 值 |

### 修复示例

**问题**：缺少返回链接

```
页面 A 链接到页面 B
但页面 B 没有链接回页面 A
```

**修复**：
```html
<!-- 页面 A -->
<link rel="alternate" hreflang="zh-CN" href="https://example.com/cn/" />

<!-- 页面 B（添加返回链接） -->
<link rel="alternate" hreflang="en" href="https://example.com/" />
```

---

## 搜索流量分析

### 查看地区流量

GSC → 效果 → 国家/地区

可以看到：
- 不同国家的点击次数
- 不同国家的展示次数
- 不同国家的点击率
- 不同国家的平均排名

### 地区流量对比

```
国家         点击次数    展示次数    CTR     排名
美国         1,200      50,000     2.4%    15.3
中国         800        30,000     2.7%    12.1
日本         400        15,000     2.7%    18.5
英国         300        12,000     2.5%    20.2
```

### 发现问题

通过地区流量分析发现：

```
问题：中国流量突然下降

可能原因：
1. 服务器访问速度问题
2. 搜索算法更新
3. 竞争对手优化
4. 内容质量问题
```

---

## 网站地图提交

### 什么是网站地图？

网站地图是列出网站所有页面的文件，帮助搜索引擎更快发现内容。

### 创建网站地图

**格式**：XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2024-01-01</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://example.com/cn/</loc>
    <lastmod>2024-01-01</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>
```

### 多语言网站地图

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://example.com/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://example.com/" />
    <xhtml:link rel="alternate" hreflang="zh-CN" href="https://example.com/cn/" />
  </url>
</urlset>
```

### 提交网站地图

1. GSC → 索引 → 网站地图
2. 输入网站地图 URL
3. 点击提交

**常见位置**：
```
https://example.com/sitemap.xml
https://example.com/sitemap_index.xml
```

---

## 索引覆盖率

### 查看索引状态

GSC → 索引 → 网页

可以看到：
- 已编入索引的页面数量
- 未编入索引的页面及原因

### 常见索引问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 已抓取，尚未编入索引 | 内容质量不足 | 提升内容质量 |
| 重复网页 | 内容重复 | 使用 canonical 或 hreflang |
| 已重定向 | 页面被重定向 | 检查重定向是否正确 |
| 找不到（404） | 页面不存在 | 修复链接或创建页面 |

### 请求编入索引

对于重要页面：
1. GSC → URL 检查
2. 输入页面 URL
3. 点击"请求编入索引"

---

## GSC 使用技巧

### 技巧一：定期检查

**每周检查**：
- 效果报告（点击、展示、排名）
- 索引覆盖率
- 移动设备易用性

**每月检查**：
- 国际定位问题
- hreflang 问题
- 结构化数据错误

### 技巧二：对比分析

使用"对比"功能：
- 对比不同时间段
- 对比不同国家
- 对比不同页面类型

### 技巧三：导出数据

点击"导出"可以：
- 导出为 CSV
- 导出为 Google Sheets
- 用于进一步分析

### 技巧四：邮件提醒

在 GSC 设置中开启邮件提醒：
- 关键问题通知
- 摘要报告

---

## GSC 与 GEO 优化工作流

### 初始设置

```
第 1 步：验证网站
第 2 步：提交网站地图
第 3 步：设置地理定位（如适用）
第 4 步：检查 hreflang 配置
```

### 每周工作流

```
周一：查看效果报告
  - 点击次数变化
  - 排名变化
  - 新获得排名的关键词

周三：检查索引状态
  - 新页面是否被索引
  - 是否有错误

周五：分析地区数据
  - 各地区流量变化
  - 发现问题和机会
```

### 每月工作流

```
第一周：全面数据回顾
  - 导出月度数据
  - 分析趋势

第二周：问题修复
  - 处理 GSC 报告的问题
  - 优化表现不佳的页面

第三周：竞品对比
  - 对比竞争对手表现
  - 发现差距和机会

第四周：策略调整
  - 根据数据调整策略
  - 制定下月计划
```

---

## 下一步

👉 **[第八讲：GEO 优化工具箱](/course/AI/geo-optimization/20260416220008-第8讲-GEO优化工具箱/)**

下一讲我们会介绍更多实用的 GEO 优化工具。

---

## 💬 加入学习交流群

👉 **[点击加入交流群](https://www.python4office.cn/wechat-group/)**

---

## 推荐：AI Python 编程实战营

如果你想系统学习 AI 开发：

🎁 **限时福利**：送《利用 Python 进行数据分析》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

*PS：GSC 是 GEO 优化的核心工具，一定要用好它。建议每周至少登录一次查看数据。*

---

## 💬 联系我

| 平台 | 账号/链接 |
|------|----------|
| 微信 | [扫码加好友](https://www.python4office.cn/wechat-qrcode/) |
| 微博 | [@程序员晚枫](https://weibo.com/u/7726957925) |
| 知乎 | [@程序员晚枫](https://www.zhihu.com/people/CoderWanFeng) |
| 抖音 | [@程序员晚枫](https://www.douyin.com/user/MS4wLjABAAAA259649365) |
| 小红书 | [@程序员晚枫](https://xhslink.com/m/4i8OhkfTvW3) |
| B 站 | [Python 自动化办公社区](https://space.bilibili.com/259649365) |

**主营业务**：AI 编程培训、企业内训、技术咨询

---

![AI搭建个人网站课程](https://raw.atomgit.com/user-images/assets/5027920/4990131c-9e94-46d4-9d48-ef645525c9ee/02-AI编程系列-AI搭建个人网站课程海报-晚枫.png)
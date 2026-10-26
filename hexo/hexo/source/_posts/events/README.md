---
title: 活动总索引
date: 2026-10-26 14:30:00
tags: [活动, 索引]
categories: [活动]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---

# 活动总索引

本目录是「程序员晚枫」所有活动的**文章归档区**。每场活动一个独立子目录，目录下放该活动的预告、总结、报道等系列文章。

---

## 目录规范

```
events/
├── README.md                          ← 本文件（总索引）
├── YYYYMMDD-活动名称-地点/              ← 每场活动一个目录
│   ├── README.md                      ← 活动简介 + 系列文章规划（可选）
│   ├── 01-文章标题.md
│   ├── 02-文章标题.md
│   └── imgs/                          ← 该活动专属图片（可选）
├── YYYYMMDD-活动名称-地点/单篇.md       ← 单篇文章型活动（无系列）
└── 系列名-年份/                        ← 同一系列的多场活动
```

**命名规则**：

| 项目 | 规则 |
|------|------|
| 目录名 | `YYYYMMDD-活动名称-地点`，中横线分隔，全小写不强制但保持一致 |
| 目录内文章 | `NN-文章标题.md`，两位序号表示发布顺序 |
| 标点 | 一律用英文中横线 `-`，禁止中文标点（URL 安全） |
| 活动独有图片 | 放该活动目录下的 `imgs/`，其他活动不引用 |

---

## 活动分类

按活动性质分为四类，与「参加过的活动」文档中的分类保持一致。

### 一、峰会与大会（Summit）

面向行业的大规模会议，通常担任嘉宾、圆桌或分会场主持。

| 时间 | 活动 | 地点 | 角色 |
|------|------|------|------|
| 2026-10-24 | [2026 腾讯云西部架构师峰会](https://www.python4office.cn/events/20261024-腾讯云西部架构师峰会-成都/01-我主持的少年游会场-孩子上台讲AI/) | 成都 | 分会场主持 |

**该场系列文章**：

| 序号 | 文章 | 视角 |
|------|------|------|
| 01 | [我主持的少年游会场-孩子上台讲AI](https://www.python4office.cn/events/20261024-腾讯云西部架构师峰会-成都/01-我主持的少年游会场-孩子上台讲AI/) | 主持视角：孩子在台上讲自己做的 AI 游戏 |
| 02 | [月薪 3 万的 FDE 岗位，腾讯免费培训教你入行，到底图什么？](https://www.python4office.cn/events/20261024-腾讯云西部架构师峰会-成都/02-腾讯云FDE人才培养计划-免费培训到底图什么/) | 延展视角：FDE 人才培养计划的商业逻辑 |

### 二、开发者沙龙与线下活动（Meetup / Workshop）

以动手实操为主的小型活动，通常是主办方。

| 时间 | 活动 | 地点 | 角色 |
|------|------|------|------|
| 2026-10-17 | [WorkBuddy 开发者沙龙·重庆站](https://www.python4office.cn/events/ai-offline-events/20261017-WorkBuddy开发者沙龙-重庆站/) | 重庆 | 主办 |
| 2026-04-08 | [AtomGit AI 龙虾挑战赛·重庆站](https://www.python4office.cn/events/chongqing-lobster-contest-2026/) | 重庆 | 主办 |

### 三、系列活动（Series）

同一品牌、跨多场次的活动，每场一个子目录。

| 活动 | 说明 |
|------|------|
| [AtomGit AI 龙虾挑战赛 2026](https://www.python4office.cn/events/atomgit-lobster-2026/) | 比赛宣传系列文，01-07 编号 |

### 四、直播与线上活动（Online）

以直播形式开展的活动，单独成系列。

| 时间 | 活动 | 平台 |
|------|------|------|
| 2025-12-06 | [我是怎么用AI自动化写文章、剪视频的？](https://www.python4office.cn/course/ai-related/AI编程训练营/others/events/直播/251206-工作流/) | — |
| 2025-12-07 | [Qoder 入门](https://www.python4office.cn/course/ai-related/AI编程训练营/others/events/直播/251207-qoder入门/) | — |
| 2025-12-27 | [AI 开源](https://www.python4office.cn/course/ai-related/AI编程训练营/others/events/直播/251227-AI开源/) | — |

---

## 全部活动总表

含高校讲座、大厂分享、媒体采访、直播、获奖等完整记录，跨年份统一维护在：

👉 [程序员晚枫 · 主办、参与的活动](https://www.python4office.cn/course/程序员晚枫/events/20251123-参加过的活动/)

该文档按年份倒序组织，含以下附录：

- 高校讲座（4 场）
- 科技大厂分享（阿里、腾讯等）
- 媒体采访（AtomGit、脉脉、GitCode）
- 线上直播（6 场）
- 身份与认证（PSF Member、腾讯云架构师名人堂专家等）
- 百科词条（微信百科、百度百科）

---

## 写作规范

活动类文章遵循 [普通文章写作指南](../../../../../guide/普通文章写作指南.md)：

- front-matter 必填 `title` / `date` / `tags` / `categories` / `cover`
- `date` 与当前系统时间一致，精确到分钟
- `tags` 至少 2 个，第一个用 `线下活动` 或 `线上活动`
- `categories` 用 `[线下活动, AI活动]` 或 `[线上活动, AI活动]`
- 正文图片统一使用 GitHub Raw 图床：`https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/xxx.png`
- 文末使用标准 Slogan：「科技不高冷，AI 很好用。」
- 活动类文章必须有「参考链接」（≥ 3 条，格式 `[标题：URL](URL)`）+「相关阅读」（2-4 篇）

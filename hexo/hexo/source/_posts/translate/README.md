---
title: 多语言内容策略与执行手册（内部文档）
date: 2026-06-14 10:00:00
published: false
hidden: true
tags: [internal, 翻译策略, 海外SEO, AdSense]
categories: [内部文档]
description: 内部文档，不对外发布。本指南记录站点多语言扩展的真实策略、踩坑认知和阶段性执行计划。
---

> ⚠️ **本文件不部署**：`published: false` + `_config.yml` 中已配置 `skip_render: source/**/README.md`，本文件不会出现在线上站点。
>
> **文件定位**：本站多语言扩展的**内部策略文档**，记录"为什么做、做什么、不做什么"的决策依据。
>
> **更新原则**：每次跑完一轮验证，把数据写进来，**用数据修正策略**，不要拍脑袋扩规模。

---

## 0. 先承认一件事：之前的方案有方向性错误

最初版本的 README（v1，2026-06-14 上午）写了一套很完整的：

- 8 种语言并行
- AI 批量翻译流水线
- 三级审核流程
- 每日 Cron 同步
- 月度报告

**但它解决的是"如何整齐地翻译"，没解决"如何赚到海外美元"。**

经过复盘，发现 4 个关键认知错误：

| 错误认知 | 真实情况 |
|---------|---------|
| "AdSense 给美元 = 赚海外用户的钱" | AdSense 全球都用美元结算，币种 ≠ 流量来源 |
| ".cn 域名做英文站只是慢一点" | `.cn` 是 ccTLD，Google 默认地理定位中国，英文 SEO 天花板极低 |
| "翻译中文存量就能拿到英文流量" | 90% 的中文选题在英文世界搜索量为 0 |
| "AI 批量翻译质量足够发布" | Google Helpful Content 明确打击未经人工增值的机翻内容 |

**这份 v2 文档就是基于这 4 个修正写的。**

---

## 1. 核心目标重新定义

### 1.1 真实目标（不是"翻译"）

```text
让站点产生有意义的海外 AdSense 收入
≠ 把中文文章翻译成 N 种语言
```

**目标拆解**：

- 海外用户能在 Google 搜到我们 → **国际 SEO 问题**
- 搜到之后愿意点 → **标题 / Meta 描述问题**
- 点进来之后愿意停留 → **内容质量与本地化问题**
- 看到广告且广告匹配高 CPC 关键词 → **eCPM 问题**

**翻译只是其中一环，且不是最重要的一环。**

### 1.2 eCPM 现实数据（决定收益天花板）

| 访客来源 | eCPM 大概范围 | 备注 |
|---------|--------------|------|
| 中国大陆 | $0.3 - $1.5 | 当前主要流量 |
| 印度 / 东南亚 | $0.5 - $2 | 价值低 |
| 欧洲西部 | $3 - $10 | 中等价值 |
| **美国 / 英国 / 加拿大 / 澳洲** | **$5 - $30+** | **真正目标用户** |

**结论**：1 个美国访客 ≈ 10-30 个中国访客的广告价值。

### 1.3 当前基线（持续更新）

| 指标 | 2026-06 | 目标 |
|------|---------|------|
| 月度 AdSense 收入 | $0.42 | 先到 $5，再谈 $50 |
| 月度 PV | 待补 | — |
| 海外流量占比 | 待补（Search Console 查） | 30%+ |
| eCPM | 待补 | $2+ |

> ⚠️ **行动项**：下一步打开 [Google Search Console](https://search.google.com/search-console) 把"Performance → Countries"的数据填到这里。**没有这个数据，所有策略都是猜的。**

---

## 2. 阶段性执行策略

### 2.1 总原则：先验证，再扩大

```text
小步快跑：5 篇 → 看数据 → 决定下一步
不要一次铺 8 种语言 100 篇
不要建复杂流程之前没有任何数据支撑
```

### 2.2 三个阶段

| 阶段 | 时间 | 投入 | 目标 |
|------|------|------|------|
| **Phase 1：MVP 验证** | 1 个月 | 5 篇英文 | 验证 `.cn` 域名能不能拿到海外曝光 |
| **Phase 2：选题与渠道优化** | 2-3 个月 | 累计 20-30 篇 | 找到能持续带来海外流量的选题方向 |
| **Phase 3：独立域名 / 多语言扩展** | 6 个月+ | 视数据投入 | 验证有效后才考虑搬 `.com` 或扩语种 |

**关键原则**：**Phase 1 跑通之前，不进入 Phase 2。**

---

## 3. Phase 1：MVP 验证清单（当前阶段）

### 3.1 选题筛选标准

只挑同时满足下面 3 个条件的选题：

| 条件 | 检查方法 | 通过线 |
|------|---------|--------|
| **英文用户真的会搜** | Google Keyword Planner 查搜索量 | 月搜索量 ≥ 100 |
| **海外用户也关心** | 不能是"腾讯云/支付宝/公众号"这类纯中国语境 | 删掉本地化术语后仍成立 |
| **CPC 不太低** | Keyword Planner 看出价范围 | CPC ≥ $0.5 |

**优先方向**：

- AI 编程工具评测（Cursor、Claude Code、Codex、Copilot）
- 通用 AI 工具教程（ChatGPT prompts、Claude tips）
- 程序员效率技巧（不依赖中国语境）
- 跨平台软件对比（VS Code vs Cursor 等）

**禁止方向**：

- 微信公众号 / 知识星球 / 支付宝相关
- 国产云对比（腾讯云 / 阿里云 / 火山）
- 中国法规 / 政策类内容
- 中文 SEO 技巧

### 3.2 翻译工作流（精翻，非批量）

```text
[选定中文文章]
   ↓
[关键词调研：英文 keyword + CPC + 竞争度]
   ↓
[AI 初稿翻译（GPT-4 / Claude）]
   ↓
[人工改写：标题、开头、案例本地化]
   ↓
[加 hreflang 和 canonical 标签]
   ↓
[发布 + Search Console 提交]
   ↓
[等 2-4 周看曝光数据]
```

**重点**：**人工改写不可省**。完全 AI 直出的内容是被 Google 打击的对象。

### 3.3 5 篇验证清单

| # | 中文原文 | 英文选题方向 | 目标关键词 | 状态 |
|---|---------|------------|-----------|------|
| 1 | （待填） | （待填） | （待填） | pending |
| 2 | | | | pending |
| 3 | | | | pending |
| 4 | | | | pending |
| 5 | | | | pending |

> ⚠️ **行动项**：填完这 5 篇清单，再开始翻译。**不要边写边想。**

### 3.4 Phase 1 成功判定

跑完 1 个月后，检查 Search Console 数据：

| 指标 | 通过线 | 不通过 → 怎么办 |
|------|--------|---------------|
| 5 篇文章是否有海外国家曝光 | 至少 3 篇有 US/UK/CA 曝光 | 域名问题，考虑独立 `.com` |
| 海外曝光总量 | ≥ 500 次/月 | 选题问题，重新挑关键词 |
| 海外点击 | ≥ 20 次/月 | 标题/Meta 问题，优化 SERP |
| 是否带来 AdSense 收入变化 | 月收入 ≥ $1 | 数据太小，再观察 1 个月 |

**任一条不通过，立即停止扩规模，回到根因分析。**

---

## 4. 不要做的事（红线）

| 红线 | 原因 |
|------|------|
| ❌ 一次性翻译 50+ 篇 | 触发 Google Helpful Content 降权信号 |
| ❌ AI 翻译直接发布（无人工改写） | 同上，质量风险 + 降权风险 |
| ❌ 8 种语言并行 | Phase 1 没验证，多语言只会扩大错误 |
| ❌ 在 `.cn` 域名下做大规模英文 | 域名信号本身限制英文排名 |
| ❌ 把"翻译完成率"当 KPI | 真正 KPI 是海外流量和广告收入，不是翻译数量 |
| ❌ 没有数据支撑就建复杂自动化流程 | 流程不创造价值，数据才创造价值 |

---

## 5. 技术执行规范（保留 v1 中仍有效的部分）

> 下面是技术层面的规范，**不变的**继续用，**该修正的**已经修正。

### 5.1 目录结构

```
source/_posts/
├── ads/, ai/, article/...        # 中文主目录
└── translate/                     # 多语言镜像
    ├── README.md                  # 本文档（不部署）
    ├── en/                        # 英文版本
    │   ├── _terminology.md
    │   ├── _style-guide.md
    │   ├── _translation-status.md
    │   └── [镜像子目录]/
    └── （其他语言：Phase 1 验证通过后再加）
```

**Phase 1 阶段只建 `en/` 一个语言目录，其他语言全部冻结。**

### 5.2 文件命名

| 规则 | 示例 |
|------|------|
| 与中文原文同名 | `20241229-xxx.md` → `translate/en/.../20241229-xxx.md` |
| 不加语言后缀 | ❌ `xxx-en.md` |
| 小写 + 连字符 | ✅ `ai-tools-2026.md` |

### 5.3 译文 Front-matter（精简版）

```yaml
---
title: English Title Here
date: 2026-06-14 10:00:00
tags: [tag1, tag2]
categories: [English]
translation:
  source: source/_posts/path/to/original.md
  source_sha: a1b2c3d4...          # 用于检测原文是否更新
  translator: human-edited          # human-edited / ai-only
  reviewed: true
  target_keyword: "main english keyword"
  target_cpc: 1.20                  # 用于事后复盘
canonical_url: https://python4office.cn/en/...
hreflang:
  - lang: zh-CN
    url: https://python4office.cn/...
  - lang: en
    url: https://python4office.cn/en/...
---
```

**重要**：必须配 `canonical_url` 和 `hreflang`，否则 Google 会判定为重复内容。

### 5.4 国际 SEO 必做项

- [ ] 在 Hexo 主题里配置 `hreflang` 标签输出（Butterfly 主题需要改模板）
- [ ] 多语言 sitemap：分别提交 sitemap-zh.xml 和 sitemap-en.xml
- [ ] Google Search Console 国际定位：暂不限定（让 Google 自己判断）
- [ ] 英文文章 Meta description 单独写，**不要直接翻译中文 description**
- [ ] 英文文章 URL slug 用英文（不要中文拼音）

---

## 6. 决策树：什么时候进入下一阶段

```
Phase 1 跑 1 个月
  ↓
检查 Search Console 海外曝光数据
  ↓
  ├─ 海外曝光 ≥ 500/月 且有 US/UK 流量
  │     ↓
  │   进入 Phase 2：扩到 20-30 篇精翻
  │
  ├─ 海外曝光 < 500/月，但选题数据可改进
  │     ↓
  │   留在 Phase 1：换 5 个新选题再试
  │
  └─ 海外曝光极低，明显是域名问题
        ↓
      跳过 Phase 2，直接做 Phase 3 域名决策：
      买 .com / 用子域名 / 暂停海外计划
```

---

## 7. 工具与资源清单

### 7.1 关键词调研

- [Google Keyword Planner](https://ads.google.com/intl/zh-CN_cn/home/tools/keyword-planner/)（免费）
- [Ahrefs Free Keyword Generator](https://ahrefs.com/keyword-generator)（免费版够用）
- [Ubersuggest](https://neilpatel.com/ubersuggest/)（免费每天 3 次）

### 7.2 SEO 检查

- [Google Search Console](https://search.google.com/search-console)
- [Bing Webmaster Tools](https://www.bing.com/webmasters)
- [hreflang 标签生成器](https://www.aleydasolis.com/english/international-seo-tools/hreflang-tags-generator/)

### 7.3 翻译辅助

- Claude / GPT-4：初稿翻译 + 改写建议
- DeepL：欧洲语言对照
- Grammarly：英文语法/拼写检查

### 7.4 数据复盘

- AdSense 后台：eCPM、国家收入分布
- Google Analytics 4：访客地理分布、停留时长

---

## 8. 更新记录

| 日期 | 版本 | 更新内容 | 更新人 |
|------|------|---------|--------|
| 2026-06-14 | v1 | 初版：完整的翻译 SOP（8 语言、流水线、三级审核） | AI 起草 |
| 2026-06-14 | **v2** | **方向性重写**：从"翻译 SOP"改为"海外 SEO 验证策略"；冻结 8 语言，先做 English MVP；明确不部署 | 复盘修正 |
| 待更新 | | Phase 1 验证数据回填 | — |

---

## 9. 当前 TODO（按优先级）

**本周必做**：

- [ ] 打开 Search Console 抓现状数据，填到 §1.3
- [ ] 用 Keyword Planner 调研 20 个英文长尾词
- [ ] 从 20 个里挑出 5 个，填到 §3.3 表格
- [ ] 把这 5 篇对应的中文原文找出来

**本月必做**：

- [ ] 完成 5 篇英文精翻（AI 初稿 + 人工改写）
- [ ] 给主题加 hreflang 标签输出
- [ ] 提交 sitemap-en.xml

**Phase 1 结束后再做**：

- [ ] 复盘 5 篇数据，按 §6 决策树决定下一步
- [ ] 把决策结果写进本文档 §8 更新记录

---

**最后一句话**：

**翻译数量不等于收入。**
**数据验证 > 流程设计 > 翻译速度。**
**Phase 1 没跑通之前，所有"批量翻译""多语言扩展""自动化流水线"的想法全部冻结。**

—— 内部策略组

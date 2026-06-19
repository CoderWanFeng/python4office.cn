# AIHOT API 字段参考

> 数据源：卡兹克维护的 AI 热点监控平台 aihot.virxact.com
> 接口状态：测试版（2026-05-08 公开）
> 鉴权：❌ 无需 API Key
> 必需 Header：**浏览器 User-Agent**（否则 nginx 直接 403）

## Item 完整字段

```json
{
  "id": "cmqlaf27b00wusl2sfbraxwid",
  "title": "baoyu-design Skill迭代：修复导出样式与渐变丢失问题",
  "title_en": "Skill 和软件一样，需要不断迭代的……",
  "url": "https://x.com/dotey/status/...",
  "source": "X：宝玉 (@dotey)",
  "publishedAt": "2026-06-19T18:43:30.000Z",   // 注意驼峰
  "summary": "宝玉分享 baoyu-design Skill 的迭代过程……",
  "category": "tip",                              // 英文枚举
  "score": 75,                                    // 0-100 整数
  "selected": true                                // 是否进入精选
}
```

## 顶层响应

`/api/public/items` 返回：

```json
{
  "count": 50,                  // 满足条件的总条目数
  "hasNext": true,              // 是否还有下一页
  "nextCursor": "eyJhIjox...",  // 下一页 cursor，传给 ?cursor=
  "items": [...]
}
```

## 端点详解

### 1. 精选条目（默认推荐）

```http
GET /api/public/items?mode=selected
```

参数：
- `since`：ISO-8601 时间戳（如 `2026-06-18T00:00:00Z`），只返回该时间之后
- `category`：英文枚举之一（见下表）
- `q`：关键词搜索（PostgreSQL pg_trgm 模糊搜索）
- `cursor`：分页 cursor（从上次响应的 `nextCursor` 拿）

### 2. 全量条目

```http
GET /api/public/items?mode=all
```

返回：所有抓取到的条目（含未评分通过的）

### 3. 关键词搜索

```http
GET /api/public/items?q=Python+自动化
```

⚠️ **空格用 `+`**，不要用 `%20` 或空格。

### 4. 分类筛选

```http
GET /api/public/items?mode=selected&category=ai-models
```

| 枚举值 | 中文名 | 含义 |
|---|---|---|
| `ai-models` | 模型 | 新模型发布 / 权重更新 |
| `ai-products` | 产品 | AI 产品功能更新 / 新工具 |
| `industry` | 行业 | 公司动态 / 融资 / 收购 |
| `paper` | 论文 | 学术论文 |
| `tip` | 技巧 | 教程 / 经验分享 / 观点 |

### 5. 今日日报

```http
GET /api/public/daily
```

返回结构（注意是**嵌套 sections**）：

```json
{
  "date": "2026-06-19",
  "generatedAt": "2026-06-19T00:00:03.961Z",
  "windowStart": "2026-06-18T00:00:00.000Z",
  "windowEnd":   "2026-06-19T00:00:00.000Z",
  "lead": null,
  "sections": [
    {
      "label": "模型发布",
      "items": [/* item 结构同上 */]
    },
    {
      "label": "产品发布",
      "items": [...]
    }
  ],
  "flashes": []
}
```

### 6. 指定日期日报

```http
GET /api/public/daily/2026-06-17
```

### 7. 日报列表（discovery）

```http
GET /api/public/dailies?take=30
```

返回：

```json
{
  "count": 5,
  "items": [
    {
      "date": "2026-06-19",
      "generatedAt": "2026-06-19T00:00:03.961Z",
      "leadTitle": "首个统一科学大模型 LOGOS 正式开源",
      "leadParagraph": null
    }
  ]
}
```

## 字段取值约定

| 字段 | 注意事项 |
|---|---|
| `publishedAt` | **UTC 时间**，注意驼峰命名；展示给用户前转 `+8` |
| `summary` | **LLM 生成的摘要**，引用具体数据请用 `url` 回原文核对 |
| `score` | 0-100 整数，**仅精选条目**有，全量条目可能为 null |
| `category` | **英文枚举**（`ai-models` 等），不是中文 |
| `url` | 唯一可信字段，AIHOT 不缓存原文 |
| `selected` | true = 进入精选，false = 只在全量里 |

## 错误码

| HTTP | 含义 | 怎么办 |
|---|---|---|
| 200 | 正常 | — |
| 400 | 参数错误 | 检查 category 枚举值 |
| 403 | UA 被拒 | 必须用浏览器 User-Agent |
| 429 | 限流 | 降低请求频率 |
| 5xx | 服务端问题 | 重试 |

## 必需 Header

```python
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}
```

无 UA 或非浏览器 UA → 直接 403，nginx 拒绝。

## 限流建议

- 单次会话：≤ 3 次请求
- 间隔：≥ 2 秒
- 定期轮询：用 RSS feed 更友好（见下）

## RSS 替代方案

如果你想做成定时任务（每天早上自动拉日报）：

```bash
# 三种 RSS feed
https://aihot.virxact.com/rss/curated   # 精选
https://aihot.virxact.com/rss/daily     # 日报
https://aihot.virxact.com/rss/all       # 全量
```

RSS 阅读器、Feedly、Inoreader 等都能直接订阅。

## 相关链接

- AIHOT 主页：https://aihot.virxact.com/
- Agent 接入文档：https://aihot.virxact.com/agent
- 官方 Skill 仓库：https://github.com/KKKKhazix/khazix-skills
- 数字生命卡兹克知乎：搜"数字生命卡兹克"
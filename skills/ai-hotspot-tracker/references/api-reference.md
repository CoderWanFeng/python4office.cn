# AIHOT API 字段参考

> 数据源：卡兹克维护的 AI 热点监控平台 aihot.virxact.com
> 接口状态：测试版（2026-05-08 公开）
> 鉴权：❌ 无需 API Key

## 通用响应结构

```json
{
  "items": [
    {
      "id": "string",
      "title": "string",
      "summary": "string",
      "url": "string",          // 原文链接，引用前必须回这里核对
      "category": "string",     // 模型 / 产品 / 行业 / 论文 / 技巧
      "source": "string",       // 信源名（如 "OpenAI Blog"）
      "published_at": "ISO-8601 string (UTC)",
      "score": 0.0-1.0,         // AI 评分
      "tags": ["string"]
    }
  ],
  "total": 100,
  "fetched_at": "ISO-8601"
}
```

## 端点详解

### 1. 精选条目（默认推荐）

```http
GET /api/public/items?mode=selected
```

可选参数：
- `since`：ISO-8601 时间戳，只返回该时间之后
- `category`：5 大分类之一
- `q`：关键词（PostgreSQL pg_trgm 模糊搜索）

返回：精选候选池（已去噪 + 评分排序）

### 2. 全量条目

```http
GET /api/public/items?mode=all
```

返回：所有抓取到的条目（含未评分通过的）

### 3. 关键词搜索

```http
GET /api/public/items?q=Python+自动化
```

注意：**用 `+` 不用空格**（API 文档明确说明），空格在 URL 里会被编码。

### 4. 分类筛选

```http
GET /api/public/items?mode=selected&category=模型
```

5 个可选值：`模型 / 产品 / 行业 / 论文 / 技巧`

### 5. 今日日报

```http
GET /api/public/daily
```

返回结构：

```json
{
  "date": "2026-06-18",
  "generated_at": "ISO-8601",
  "items": [...]   // 同 items 端点的单条结构
}
```

### 6. 指定日期日报

```http
GET /api/public/daily/2026-06-17
```

### 7. 日报列表（发现）

```http
GET /api/public/dailies?take=30
```

返回最近 N 天有日报的日期列表。

## 字段取值约定

| 字段 | 注意事项 |
|---|---|
| `published_at` | **UTC 时间**，不是北京时间；展示给用户前必须转 `+8` |
| `summary` | **LLM 生成的摘要**，引用具体数据前请用 `url` 回原文核对 |
| `score` | 仅精选条目有，全量条目可能为 null |
| `category` | 中文枚举，不是英文 |
| `url` | 唯一可信字段，AIHOT 不缓存原文 |

## 错误码

| HTTP | 含义 |
|---|---|
| 200 | 正常 |
| 429 | 限流（默认足够，正式业务会被限） |
| 5xx | 服务端问题，AIHOT 测试期常见，重试即可 |

## 限流建议

- 单次会话：≤ 3 次请求
- 间隔：≥ 2 秒
- RSS 替代方案：如果要做定时拉取，用 RSS feed 更友好（见 `references/rss-feeds.md`）

## 相关链接

- AIHOT 主页：https://aihot.virxact.com/
- Agent 接入文档：https://aihot.virxact.com/agent
- 官方 Skill 仓库：https://github.com/KKKKhazix/khazix-skills
- 数字生命卡兹克知乎：搜"数字生命卡兹克"
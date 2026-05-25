# python4office.cn AI-First API 服务

为 AI Agents 提供的博客文章和 Python 工具推荐 API 服务。

## 🌟 功能特性

- **博客文章 API** - AI 可读的博客文章查询接口
- **Python 工具推荐** - 精选 Python AI 工具和库
- **MCP Tools** - Model Context Protocol 接口支持
- **AI 友好格式** - 简化的 JSON 响应，专为 AI 设计

---

## 🚀 快速开始

### 1. 安装依赖

```bash
cd api
npm install
```

### 2. 启动服务

```bash
npm run dev
# 或使用预览脚本
./preview.sh
```

服务将在 http://localhost:3001 启动

---

## 📡 API 端点

### 📚 博客文章 API

#### 获取文章列表
```
GET /api/posts
```

**参数：**
- `query` - 搜索关键词
- `tags` - 标签筛选（逗号分隔）
- `featured` - 只返回精选文章
- `page` - 页码
- `limit` - 每页数量

**示例：**
```bash
curl "http://localhost:3001/api/posts?limit=5"
```

#### AI 友好接口
```
GET /api/posts/ai-friendly
```

专为 AI agents 设计的简化格式：

```bash
curl "http://localhost:3001/api/posts/ai-friendly?q=Python&limit=3"
```

**响应：**
```json
{
  "posts": [
    {
      "slug": "python-ai-tools-2024",
      "title": "2024年最好用的Python AI工具推荐",
      "summary": "本文推荐2024年最实用的Python AI开发工具...",
      "tags": ["AI编程", "Python", "工具推荐"],
      "date": "2024-03-15",
      "url": "https://www.python4office.cn/python-ai-tools-2024",
      "reading_time_minutes": 15
    }
  ],
  "count": 1,
  "purpose": "提供给AI Agent使用的文章列表"
}
```

#### 搜索文章
```
GET /api/posts/search?q=<关键词>
```

---

### 🛠️ Python 工具 API

#### 获取工具列表
```
GET /api/tools
```

**示例：**
```bash
curl "http://localhost:3001/api/tools?category=text-generation&freeOnly=true"
```

#### AI 友好接口
```
GET /api/tools/ai-friendly
```

```bash
curl "http://localhost:3001/api/tools/ai-friendly?q=NLP&limit=5"
```

**响应：**
```json
{
  "tools": [
    {
      "id": "transformers",
      "name": "Hugging Face Transformers",
      "description": "Transformers是Hugging Face的核心库...",
      "usage_example": "from transformers import pipeline",
      "capabilities": ["text-classification", "named-entity-recognition"],
      "registration_required": false,
      "free_tier": true,
      "openclaw_config": {
        "model": "distilbert-base-uncased-finetuned-sst-2-english"
      }
    }
  ],
  "count": 1
}
```

#### 搜索工具
```
GET /api/tools/search?q=<关键词>
```

---

### 🤖 MCP Tools

#### 服务信息
```
GET /api/mcp
```

返回 MCP 服务信息和可用工具列表。

#### 调用 MCP 工具
```
POST /api/mcp
```

**示例：**
```bash
curl -X POST http://localhost:3001/api/mcp \
  -H "Content-Type: application/json" \
  -d '{"name":"search_python_tools","arguments":{"query":"NLP","free_only":true}}'
```

**可用工具：**

| 工具名称 | 描述 | 参数 |
|---------|------|------|
| `search_python_tools` | 搜索 Python 工具 | query, category, free_only |
| `get_tool_details` | 获取工具详情 | tool_id |
| `get_blog_posts` | 获取博客文章 | query, tags, limit |
| `search_posts` | 搜索文章 | query |
| `get_post_details` | 获取文章详情 | slug |
| `list_categories` | 列出分类和标签 | 无 |

---

## 📊 已收录内容

### 博客文章
- 10+ 篇精选技术文章
- 覆盖 AI 编程、工具配置等主题
- 支持标签和分类筛选

### Python 工具
- OpenAI Whisper - 语音识别
- LangChain - LLM 应用框架
- Hugging Face Transformers - NLP 模型库
- Gradio - Web 界面构建
- OpenAI API - GPT 模型

---

## 🎯 使用场景

### 场景 1：AI 查找教程
```
用户：帮我找一些关于 Python 代码助手的文章

AI：
GET /api/posts/ai-friendly?q=代码助手
返回相关文章列表和链接
```

### 场景 2：AI 推荐工具
```
用户：我想用 Python 做语音识别，有什么好用的库？

AI：
GET /api/tools/ai-friendly?q=语音识别
返回 Whisper 等工具的详细信息和安装方式
```

### 场景 3：AI 回答问题
```
用户：LangChain 如何安装和使用？

AI：
GET /api/tools/transformers
GET /api/posts/search?q=LangChain
综合工具文档和博客文章回答问题
```

---

## 🔧 配置

### 环境变量（可选）

```env
# API 服务端口
PORT=3001

# 缓存配置
CACHE_TTL=3600
```

---

## 📦 项目结构

```
api/
├── src/
│   ├── app/                    # Next.js App Router
│   │   ├── api/
│   │   │   ├── posts/         # 文章 API
│   │   │   │   ├── route.ts
│   │   │   │   ├── [slug]/
│   │   │   │   ├── search/
│   │   │   │   └── ai-friendly/
│   │   │   ├── tools/         # 工具 API
│   │   │   │   ├── route.ts
│   │   │   │   ├── [id]/
│   │   │   │   ├── search/
│   │   │   │   └── ai-friendly/
│   │   │   └── mcp/           # MCP 服务
│   │   │       └── route.ts
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── lib/
│   │   ├── posts-types.ts     # 文章类型定义
│   │   ├── posts-data.ts      # 示例文章数据
│   │   ├── tools-registry.ts  # 工具类型定义
│   │   └── tools-data.ts      # 工具数据
│   └── mcp/
│       └── server.ts          # MCP 服务器
├── package.json
├── tsconfig.json
├── next.config.ts
└── README.md
```

---

## 🚀 部署

### 开发环境
```bash
npm run dev
```

### 生产环境
```bash
npm run build
npm start
```

### Docker（可选）
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3001
CMD ["npm", "start"]
```

---

## 🔗 集成指南

### 与 OpenClaw 集成

```json
{
  "mcpServers": {
    "python4office": {
      "command": "curl",
      "args": ["-X", "POST", "http://localhost:3001/api/mcp", "-H", "Content-Type: application/json", "-d", '{"name":"${tool}","arguments":${args}}'],
      "description": "程序员晚枫的Python工具和博客API"
    }
  }
}
```

### 与其他 AI Agents 集成

所有 API 都返回标准 JSON 格式，易于解析和使用：

```javascript
// 示例：获取 Python NLP 工具
const response = await fetch('http://localhost:3001/api/tools/ai-friendly?q=NLP');
const data = await response.json();
console.log(data.tools);
```

---

## 📈 扩展内容

### 添加新文章

在 `src/lib/posts-data.ts` 中添加：

```typescript
{
  slug: 'new-post-slug',
  title: '新文章标题',
  date: '2024-01-01',
  tags: ['Python', 'AI'],
  description: '文章描述',
  wordCount: 2000,
  readingTime: 10
}
```

### 添加新工具

在 `src/lib/tools-data.ts` 中添加：

```typescript
{
  id: 'new-tool-id',
  name: '新工具名称',
  description: '工具描述',
  category: 'python-library',
  capabilities: ['feature1', 'feature2'],
  // ... 其他字段
}
```

---

## 📞 支持

- **主站**: https://www.python4office.cn
- **GitHub**: https://github.com/CoderWanFeng/python4office.cn
- **问题反馈**: 通过 GitHub Issues

---

**版本**: 1.0.0  
**更新日期**: 2026-05-20  
**维护者**: 程序员晚枫

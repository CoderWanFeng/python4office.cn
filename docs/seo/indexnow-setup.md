# IndexNow 接入与 SEO 修复文档

> **背景**：2026-07-03 收到 Bing Webmaster Tools 警告，包含 5 条 SEO 优化建议：
> 1. ❌ 部分新页面未通过 IndexNow 提交
> 2. ❌ 部分重要新页面缺失于 sitemap
> 3. ❌ 大量页面 meta description 过短
> 4. ❌ 大量页面 meta description 重复
> 5. ❌ IndexNow 未设置
>
> 本文档说明如何配置、部署、验证这些修复。

---

## 1. 修改清单（已完成）

| 文件 | 操作 | 作用 |
|---|---|---|
| [hexo/hexo/_config.yml](file:///Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/hexo/hexo/_config.yml#L157-L160) | 修改 | 启用 sitemap + baidusitemap 配置 |
| [hexo/hexo/source/a3f8c1d9b7e4f2a6c5d8e1f4a7b2c6d9.txt](file:///Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/hexo/hexo/source/a3f8c1d9b7e4f2a6c5d8e1f4a7b2c6d9.txt) | 新增 | IndexNow API Key 验证文件 |
| [hexo/hexo/scripts/description-generator.js](file:///Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/hexo/hexo/scripts/description-generator.js) | 新增 | 智能生成唯一 description 的 Hexo filter |
| [scripts/indexnow-submit.js](file:///Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/scripts/indexnow-submit.js) | 新增 | IndexNow API 提交脚本 |
| [scripts/seo-audit/scan.js](file:///Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/scripts/seo-audit/scan.js) | 新增 | SEO 现状诊断（前置基线） |
| [scripts/seo-audit/verify.js](file:///Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/scripts/seo-audit/verify.js) | 新增 | SEO 修复后验证 |
| [scripts/deploy/deploy.py](file:///Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/scripts/deploy/deploy.py) | 修改 | 部署末尾自动调用 IndexNow |
| [scripts/.env.example](file:///Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/scripts/.env.example) | 新增 | 环境变量示例 |

---

## 2. IndexNow 是什么

[IndexNow](https://www.indexnow.org/) 是一个让网站即时通知搜索引擎「我有新页面/更新页面」的协议，支持 Bing、Yandex、Seznam.cz 等。Google 不支持，但 Bing 用得很多。

**对比传统 sitemap 收录**：
- sitemap：搜索引擎定期爬取，可能延迟数天到数周
- IndexNow：5-10 分钟内被发现

---

## 3. 配置步骤

### 3.1 生成 API Key

任选一种方式生成 32 位十六进制字符串：

```bash
# 方式 1：openssl（推荐）
openssl rand -hex 16
# 输出：a3f8c1d9b7e4f2a6c5d8e1f4a7b2c6d9

# 方式 2：Node.js
node -e "console.log(require('crypto').randomBytes(16).toString('hex'))"

# 方式 3：手动生成（32 位 hex 即可）
```

### 3.2 创建验证文件

文件名 = 内容 = API Key：

```bash
KEY="a3f8c1d9b7e4f2a6c5d8e1f4a7b2c6d9"
echo "$KEY" > hexo/hexo/source/$KEY.txt
```

部署后，Bing 会访问 `https://www.python4office.cn/<KEY>.txt` 验证文件存在。

### 3.3 部署

```bash
# 部署（自动调用 IndexNow）
python3 scripts/deploy/deploy.py
```

部署流程变成 4 步：构建 → 同步 → CDN 刷新 → **IndexNow 提交**。

---

## 4. 手动触发 IndexNow 提交

```bash
# 提交所有 URL
node scripts/indexnow-submit.js

# 只提交最近 7 天更新过的 URL（推荐）
node scripts/indexnow-submit.js --recent 7

# 只提交最近 30 天
node scripts/indexnow-submit.js --recent 30

# 指定 key（跳过自动发现）
node scripts/indexnow-submit.js --key a3f8c1d9b7e4f2a6c5d8e1f4a7b2c6d9
```

输出示例：

```
📡 IndexNow 提交脚本
===================

✓ API Key: a3f8c1d9...2c6d9
✓ sitemap.xml 共 285 个 URL
✓ 筛选最近 7 天：12 个 URL

🚀 提交中...
✓ HTTP 200
  Body:

🎉 提交成功！
```

---

## 5. 调试与故障排查

### 5.1 返回 403：Key 验证失败

```
❌ Key 验证失败，请检查：
   https://www.python4office.cn/a3f8c1d9...2c6d9.txt 是否可访问
```

**排查步骤**：
1. 部署后访问 `https://www.python4office.cn/<KEY>.txt`，应能看到纯文本的 Key
2. 如果 404：检查 deploy 是否成功，文件是否被 rsync 同步
3. 如果返回 HTML：检查 hexo 是否过滤了 .txt 文件（hexo 默认会把 source/ 下的 .txt 复制到 public/，不需要额外配置）

### 5.2 返回 429：频率限制

IndexNow 限制每天 10,000 个 URL。脚本默认 `--recent 7`，通常远低于上限。

如果超过，临时跳过：

```bash
SKIP_INDEXNOW=true python3 scripts/deploy/deploy.py
```

### 5.3 sitemap.xml 不存在

脚本依赖 `hexo/hexo/public/sitemap.xml`。确认 [_config.yml](file:///Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/hexo/hexo/_config.yml#L157-L160) 中 sitemap 已启用：

```yaml
sitemap:
  path: sitemap.xml
baidusitemap:
  path: baidusitemap.xml
```

---

## 6. SEO 诊断与验证

### 6.1 修复前基线

```bash
cd /Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn
node scripts/seo-audit/scan.js
```

输出：
- sitemap 中 URL 数 vs 源 .md 文件数
- description 过短/重复统计
- IndexNow key 文件是否存在
- 保存详细报告到 `scripts/seo-audit/scan-report.json`

### 6.2 修复后验证

```bash
node scripts/seo-audit/verify.js
```

输出对比修复前后的所有指标：

```
【sitemap 完整性】
  源文件数：285
  sitemap URL 数：285
  缺失：0
  ✅ 所有源文件都在 sitemap 中

【description 质量】
  过短 (<60)：0
  智能生成：268
  去重处理：42
  重复项：0
  ✅ 所有 description 唯一

【IndexNow】
  ✅ 验证文件存在：a3f8c1d9b7e4f2a6c5d8e1f4a7b2c6d9.txt
     部署后 URL：https://www.python4office.cn/a3f8c1d9b7e4f2a6c5d8e1f4a7b2c6d9.txt

🎉 全部修复通过！可以部署到生产环境。
```

---

## 7. description 生成策略

[description-generator.js](file:///Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/hexo/hexo/scripts/description-generator.js) 在 `before_generate` 阶段对每篇文章注入 description：

1. **优先使用 frontmatter 中的 description**：尊重人工撰写
2. **缺失或 <60 字符时自动生成**：
   - 模板：`{标题}。本文围绕{Tag1、Tag2、Tag3}：{正文首段前 80 字}...`
   - 保证长度 60-160 字符
3. **去重**：用 Set 哈希去重，重复时追加"（第 N 篇）"
4. **截断**：超过 160 字符加 `…`

**示例**：
```markdown
---
title: 我做了个「开源搭子」skill
tags: [开源, GitHub, 零基础]
---
```

生成：
> 我做了个「开源搭子」skill。本文围绕开源、GitHub、零基础：兄弟们，我又被"自己用得很爽"的东西感动到了...

---

## 8. 部署时间线

| 步骤 | 耗时 | 说明 |
|---|---|---|
| hexo generate | 30-60s | 现在多了 description 生成，+1-2s |
| rsync 同步 | 10-30s | 取决于文件量 |
| CDN 刷新 | 5-15s | 调腾讯云 API |
| **IndexNow 提交** | **2-5s** | 新增步骤 |
| **总耗时** | **50-110s** | 几乎无影响 |

---

## 9. 引用

- [IndexNow 官方文档](https://www.indexnow.org/)
- [IndexNow API 参考](https://www.indexnow.org/documentation)
- [Bing Webmaster Tools](https://www.bing.com/webmasters)
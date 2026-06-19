# ai-hotspot-tracker

> AI 热点 → 公众号选题，一句话搞定。

**python4office.cn 定制版 AI 资讯追踪 Skill**，基于卡兹克的 [AIHOT](https://aihot.virxact.com) 公开 API，专门为「Python 办公自动化 / AI 工具 / 教程创作」场景优化。

## 跟官方 AIHOT Skill 的区别

| 维度 | 官方 AIHOT Skill | 本 Skill |
|---|---|---|
| 数据源 | AIHOT | AIHOT |
| 输出风格 | 通用中文简报 | 公众号选题简报 |
| 相关性过滤 | 无 | ✅ Python 办公 / AI 工具向 |
| 选题建议 | 无 | ✅ 每条带"是否值得写教程"判断 |
| 标题生成 | 无 | ✅ 每条 3 个候选标题 |
| 限流 | 默认 | 3 次/会话 |

## 一句话安装

在你的 AI Agent（Claude Code / Cursor / Codex / OpenCode 等）里说：

```
帮我安装这个 skill：file:///Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/skills/ai-hotspot-tracker/
```

或者直接告诉 Agent 本 Skill 的 `SKILL.md` 路径：

```
请阅读 /Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/skills/ai-hotspot-tracker/SKILL.md 并加载这个 Skill
```

## 触发示例

安装后，对 Agent 说这些就能用：

- "今天 AI 圈有什么新东西"
- "看一下 AI 日报"
- "最近一周的 AI 论文"
- "OpenAI 最近发了啥"
- "**帮我找 python4office.cn 教程选题**" ← 重点
- "最近 3 天 AI 模型发布"

## 目录结构

```
ai-hotspot-tracker/
├── SKILL.md                          # Skill 主文件（Agent 必读）
├── README.md                         # 本文件
├── scripts/
│   └── fetch_aihot.py                # 命令行调用脚本（Python 3.8+，零依赖）
└── references/
    ├── api-reference.md              # API 字段详解
    └── output-template.md            # 公众号选题简报模板
```

## 手动测试

不装 Skill，也能用脚本直接拉数据：

```bash
# 今日日报
python3 scripts/fetch_aihot.py daily

# 指定日期日报
python3 scripts/fetch_aihot.py daily --date 2026-06-17

# 精选条目（最近 24h）
python3 scripts/fetch_aihot.py items --mode selected --since 24h

# 按分类（最近 7 天）
python3 scripts/fetch_aihot.py items --category 模型 --since 7d

# 关键词搜索
python3 scripts/fetch_aihot.py items --q "Python 自动化"

# 列出最近 30 天日报
python3 scripts/fetch_aihot.py dailies --take 30
```

## 兼容性

- ✅ Claude Code
- ✅ Cursor
- ✅ Codex CLI
- ✅ OpenCode
- ✅ Gemini CLI
- ✅ GitHub Copilot
- ✅ Cline
- ✅ Windsurf

遵循 Agent Skills 开放标准（SKILL.md）。

## 数据源

- 平台：[AIHOT](https://aihot.virxact.com/) by 数字生命卡兹克
- API 文档：https://aihot.virxact.com/agent
- 官方 Skill：[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)

## License

MIT

---

**科技不高冷，AI 很好用。** —— 程序员晚枫
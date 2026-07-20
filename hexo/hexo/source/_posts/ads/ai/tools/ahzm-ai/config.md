---
title: Claude Code 接入第三方中转站 · 配置速记
date: 2026-07-19 09:00:00
tags:
  - AI工具
  - Claude Code
  - 中转站
  - 配置
categories: [ai工具]
---

# Claude Code 接入第三方中转站 · 配置速记

> 适用：把 `claude` CLI 接到 one-api / new-api 类中转站（如 ai.ahzm.top）。
> 复制前把 `<YOUR_KEY>` 换成你自己的 Key。

**一定要走我的链接注册，不然没法享受优惠**：https://ai.ahzm.top/sign-up?aff=wanfeng

## 配置文件位置

| 系统 | 路径 |
|------|------|
| macOS / Linux | `~/.claude/settings.json` |
| Windows | `%USERPROFILE%\.claude\settings.json` |

没有就新建，整段覆盖写入。

## 推荐配置（按模型档次分配槽位）

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "<YOUR_KEY>",
    "ANTHROPIC_BASE_URL": "https://ai.ahzm.top",
    "ANTHROPIC_MODEL": "claude-sonnet-5",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-haiku-4-5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-sonnet-5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "claude-opus-4-8",
    "CLAUDE_CODE_SUBAGENT_MODEL": "claude-sonnet-5"
  },
  "model": "claude-sonnet-5"
}

```

### 槽位作用

| 字段 | 用途 | 建议填 |
|------|------|--------|
| `ANTHROPIC_MODEL` | 前台主力 | sonnet-5 |
| `..._HAIKU_MODEL` | 后台杂活（起标题/补全） | haiku-4-5（最省） |
| `..._SONNET_MODEL` | 中等任务 | sonnet-5 |
| `..._OPUS_MODEL` | 复杂推理/重构 | opus-4-8 |
| `..._SUBAGENT_MODEL` | 子代理 | sonnet-5 |

> 填模型前看模型卡片的状态灯：绿灯才填，红灯/灰灯别填（如 opus-4-7 故障，用 opus-4-8 代替）。

## 三条铁律

1. **BASE_URL 不带 `/v1`**：Anthropic 协议会自动拼 `/v1/messages`（与 OpenAI 格式相反）。
2. **鉴权二选一**：默认用 `ANTHROPIC_AUTH_TOKEN`；若启动报 401/403，把键名换成 `ANTHROPIC_API_KEY`，值不变。
3. **改完完全关掉终端再重开**：配置才会重新加载。

## 切换模型

```bash
/model claude-sonnet-5      # 会话内手敲（列表选不到自定义名时直接敲 ID）
/model                      # 看可选列表
/status                     # 确认当前 Model / Base URL

claude --model claude-sonnet-5   # 启动时指定，单次会话最稳
```

## 故障速查

| 现象 | 含义 | 处理 |
|------|------|------|
| 401 / 403 | 鉴权头不对 | AUTH_TOKEN ↔ API_KEY 互换 |
| 404 / model not found | 模型名拼错 | 去详情页复制完整 ID |
| 503 No available…（耗时 0.0s、token 为 –） | 中转站该模型渠道没货，非你配置问题 | 临时 `/model` 绕到绿灯模型（如 opus-4-8），稍后重试 |
| 切了模型却像没切 | shell 里残留旧 `ANTHROPIC_*` 变量 | `unset ANTHROPIC_*` 或重开终端；检查 `~/.zshrc` 有无写死 |

> 判断 503 不是你的锅：只要日志里任一模型成功扣费，就证明 key / 地址 / 鉴权全对，503 纯属供给侧，等站长补渠道即可。

## 安全提醒

- Key 一旦在聊天/截图里明文出现，视为泄露 → 去平台轮换 Key，旧 Key 作废。
- `settings.json` 含 Key，不要提交到 Git（加进 `.gitignore`）。
- 验证：重开终端 → `claude` → 问一句能正常回复即成功。

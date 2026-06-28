---
title: "Claude Code加入国产大模型 + 白嫖OpenCode"
date: 2026-06-27 22:12:36
tags: ["Claude", "Claude Code", "npm", "Node.js", "教程", "AI工具"]
categories: ["AI工具", "教程"]
description: "零基础教程：用 npm 安装 Claude Code（@anthropic-ai/claude-code），全程 4 步：装 Node → 装 Claude Code → 打开 → 配置大模型"
cover: https://images.unsplash.com/photo-1629654297299-c8506221a04b?q=80&w=1200&auto=format&fit=crop
---


视频中提到的几个链接，直接复制即可：

## 1、下载node（npm）
- https://nodejs.org/en/

## 2、安装Claude Code：

```bash
npm install -g @anthropic-ai/claude-code
```

### 配置
通过我给你的文件，补充这部分内容

## 配置步骤

完成Claude Code安装后，如果想配置国产大模型，直接编辑配置文件

编辑或新增 `settings.json` 文件，替换以下占位符：

- `<ARK_API_KEY>`：替换为你的 API Key
- `<Model_Name>`：替换为要使用的模型 ID

### 配置文件路径

不同系统的配置文件路径不同：

- **macOS & Linux**：`~/.claude/settings.json`
- **Windows**：`C:\Users\<用户名>\.claude\settings.json`

> 如果你用的是阿里、腾讯大模型，直接移步以下链接看文档：

- [阿里云大模型](https://help.aliyun.com/zh/model-studio/claude-code?scm=20140722.H_2949529._.OR_help-T_cn~zh-V_1&source=5176.29345612&userCode=t6duaoe1)
- [腾讯云大模型](https://curl.qcloud.com/VKPNg7bb)

我直播里，是以[火山AI大模型](https://volcengine.com/L/yJQuaxEAtM8)的配置举例：

```json
{
    "env": {
        "ANTHROPIC_AUTH_TOKEN": "<ARK_API_KEY>",
        "ANTHROPIC_BASE_URL": "https://ark.cn-beijing.volces.com/api/compatible",
        "ANTHROPIC_MODEL": "doubao-seed-2-1-pro-260628",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "doubao-seed-2-0-lite-260428",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "doubao-seed-2-1-pro-260628",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "doubao-seed-2-1-pro-260628",
        "CLAUDE_CODE_SUBAGENT_MODEL": "doubao-seed-2-1-pro-260628"
    }
}
```



## 3、安装OpenCode
```bash
npm install -g opencode-ai
```
安装后这么白嫖大模型，直接看群里的视频。

这里我写几个自己常用的命令：
- /models：查看所有可用的大模型
- /connect：连接到自定义的大模型
- /quit：退出当前对话
- /help：查看帮助
- /compact：压缩当前对话


## 4、更多免费AI工具

- AI视频：https://libtv.cgref.cn/s/9omkl4jn4d
- AI设计：https://xingliu.cgref.cn/s/1zn5oxmeqm
- AI写软件：https://atoms.cgref.cn/s/qmnog4ze29
- AI助理：https://volcengine.cgref.cn/s/omklvl7n4d
- AI写剧本：https://wawawriter.com/app/?utm_source=aiweb96
- AI生成短剧：https://www.updream.cn/?bsource=xinyan_as


### 参考链接

- https://opencode.ai/docs/zh-cn/
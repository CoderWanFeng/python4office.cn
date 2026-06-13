# English Translation Directory

This directory contains the English (en) version of all Markdown articles in the POS main project (`source/_posts/`). The directory structure mirrors the POS structure exactly.

## Quick Links

- **Translation Guide**: [../README.md](../README.md)
- **Terminology**: [_terminology.md](_terminology.md)
- **Translation Status**: [_translation-status.md](_translation-status.md)
- **Style Guide**: [_style-guide.md](_style-guide.md)

## Directory Map

The directory structure mirrors `source/_posts/`:

```
translate/en/
├── 2026/                          # Recent posts (2026)
├── ads/                           # Sponsored / promotional articles
│   ├── ai/  aliyun/  atomgit/  azure/  baidu-cloud/
│   ├── bd/  bytedance/  cake-growth/  deepseek/  easydoc/
│   ├── guide/  huashu/  huawei/  jd/  kuaiShou/  marscode/
│   ├── minimax/  moonshot/  openai/  openrouter/  tencent/
│   └── unitree/  xiaomi/  xunfei/  yidong/  zhipu/
├── ai/                            # AI topic articles
│   ├── AI口播稿/  news/  openclaw/  豆包/  数字人/
├── ai-skills/                     # AI Skills documentation
├── article/                       # Long-form articles
│   ├── books/  business/  CQ/  大佬/  腾讯云/  麓悦江城/
├── bks-ai/                        # BKS AI project
├── chatgpt/                       # ChatGPT-related
└── course/                        # Course materials
```

## Naming Convention

| Rule | Example |
|------|---------|
| Match POS structure exactly | `translate/en/ads/openai/<file>.md` |
| Use ISO 639-1 code | `en` (NOT `English` or `EN`) |
| Preserve original directory names | `ads`, `ai` (NOT `advertisements`) |
| File name unchanged | `20260428-今天我也有个人网站了.md` → `20260428-today-i-have-my-personal-website.md` (slugs normalized) |

## Maintenance

- **Owner**: English Translation Team
- **Update Frequency**: Daily sync, weekly review
- **Last Updated**: 2026-06-14

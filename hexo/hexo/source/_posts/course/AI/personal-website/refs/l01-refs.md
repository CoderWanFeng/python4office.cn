---
title: 配套开源项目说明与本地运行指南
date: 2026-03-02 14:30:00
permalink: course/AI/personal-website/refs/l01-refs/
tags: [个人网站, 开源项目, Hexo, VuePress, Next.js, 实战教程]
cover: https://images.unsplash.com/photo-1556075798-4825dfaaf498?q=80&w=1200&auto=format&fit=crop
---

# 配套开源项目说明与本地运行指南

> 第 1 讲选型篇里提到的 **3 个真实在线运行的开源项目**——本文给出每个项目的简介、环境要求、克隆命令、安装步骤、本地启动命令，**全部代码块可直接复制运行**。
>
> ⚠️ **前置条件**（3 个项目都需要）：
> 1. 已安装 [Git](https://git-scm.com/downloads) → 终端 `git --version` 能看到版本号
> 2. 已安装 [Node.js 18+](https://nodejs.org/zh-cn/download)（推荐 LTS 20.x）→ 终端 `node -v` 能看到版本号
> 3. 已安装 [VS Code](https://code.visualstudio.com/) 用于编辑代码
>
> 如果 Node.js 没装，请先看本文末尾 **「附录：Node.js / pnpm / yarn 安装」** 再回到这里。

---

## 总览：3 个项目对比

| 项目 | 类型 | 技术栈 | 难度 | 仓库地址 |
|------|------|-------|------|---------|
| ① **python4office.cn** | 个人博客 | Hexo + Butterfly 主题 | ⭐ 最低 | <https://atomgit.com/python4office/python4office.cn> |
| ② **python-office.com** | 知识文档站 | VuePress | ⭐⭐ 偏低 | <https://atomgit.com/python4office/python-office.com> |
| ③ **ai-nav** | AI 工具导航站 | Next.js + Tailwind | ⭐⭐⭐ 中等 | <https://atomgit.com/python4office/ai-nav> |

---

# ① python4office.cn — Hexo 个人博客

## 项目简介

- **在线地址**：<https://www.python4office.cn>
- **用途**：晚枫的个人技术博客，存放技术文章、学习笔记、生活随笔
- **技术栈**：Hexo 7.3.0 + Butterfly 主题 5.5.4 + Yarn 包管理
- **特点**：
  - 静态博客，加载极快，SEO 友好
  - 文章用 Markdown 写，零运维
  - 已上线运行多年，可直接克隆作为你自己博客的起点

## 环境要求

| 软件 | 版本 | 验证命令 |
|------|------|---------|
| Node.js | ≥ 18 (推荐 20.x LTS) | `node -v` |
| Yarn | ≥ 1.22（建议用 corepack 启用） | `yarn -v` |
| Git | 任意版本 | `git --version` |

**Yarn 没装？一行命令开启**（Node.js 16.10+ 自带 corepack）：

```bash
corepack enable
corepack prepare yarn@stable --activate
```

## 本地运行步骤（复制粘贴即可）

```bash
# 1. 克隆项目
git clone https://atomgit.com/python4office/python4office.cn.git

# 2. 进入项目目录（注意是双层 hexo/hexo）
cd python4office.cn/hexo/hexo

# 3. 安装依赖（首次运行，可能需要 3-5 分钟）
yarn install

# 4. 清理缓存（每次切换分支后建议执行）
yarn run clean

# 5. 生成静态文件
yarn run build

# 6. 启动本地预览服务器（默认 http://localhost:4000）
yarn run server
```

✅ **运行成功的标志**：浏览器打开 <http://localhost:4000> 能看到博客首页。

## 常用开发命令

```bash
# 实时预览（边写边看，自动刷新，最常用）
yarn run server

# 新建一篇文章
npx hexo new "我的第一篇文章"
# 文章会生成到 source/_posts/我的第一篇文章.md

# 全量重新构建（修改了主题或配置后）
yarn run clean && yarn run build

# 部署到腾讯云 COS（需配置环境变量，可选）
yarn run deploy
```

## 项目结构速查

```
python4office.cn/hexo/hexo/
├── source/_posts/         # ⭐ 你的所有文章在这里（按目录分类）
├── themes/                # 主题文件（Butterfly）
├── _config.yml            # ⭐ Hexo 主配置（站点标题/描述/导航）
├── _config.butterfly.yml  # ⭐ 主题配置（颜色/侧边栏/插件）
├── public/                # 构建后的静态文件（自动生成，勿改）
└── package.json           # 依赖与脚本
```

## 常见问题

| 问题 | 解决方案 |
|------|---------|
| `yarn install` 卡住 | 切淘宝源：`yarn config set registry https://registry.npmmirror.com` |
| 端口 4000 被占用 | 改端口：`yarn run server -p 5000` |
| 修改文章不更新 | 先 `yarn run clean` 再 `yarn run server` |
| 构建报内存溢出 | package.json 已加 `--max-old-space-size=16384`，应不会报。若报，调更大 |

---

# ② python-office.com — VuePress 知识文档站

## 项目简介

- **在线地址**：<https://www.python-office.com>
- **用途**：晚枫的课程文档与教程体系，承载 python-office 库的完整使用文档
- **技术栈**：VuePress（基于 Vue + Markdown）
- **特点**：
  - 适合做系统化教程、产品文档、知识库
  - 左侧自动生成多级目录导航
  - 内置全文搜索、代码高亮、移动端适配
  - 已上线运行多年

## 环境要求

| 软件 | 版本 | 验证命令 |
|------|------|---------|
| Node.js | ≥ 18 (推荐 20.x LTS) | `node -v` |
| pnpm（首选）或 npm | pnpm ≥ 8 | `pnpm -v` |
| Git | 任意版本 | `git --version` |

**pnpm 没装？一行命令安装**：

```bash
# 通过 npm 安装
npm install -g pnpm

# 或通过 corepack（Node.js 16.10+ 自带）
corepack enable
corepack prepare pnpm@latest --activate
```

## 本地运行步骤（复制粘贴即可）

```bash
# 1. 克隆项目
git clone https://atomgit.com/python4office/python-office.com.git

# 2. 进入项目目录
cd python-office.com

# 3. 安装依赖（首次运行，可能需要 3-5 分钟）
pnpm install
# 没有 pnpm 也可以用 npm：npm install

# 4. 启动开发服务器（默认 http://localhost:8080）
pnpm docs:dev
# 没有 pnpm：npm run docs:dev
```

✅ **运行成功的标志**：浏览器打开 <http://localhost:8080> 能看到文档首页。

> 💡 **提示**：VuePress 项目的具体启动命令以仓库根目录的 `package.json` 中的 `scripts` 字段为准。若 `docs:dev` 不生效，可尝试 `dev` 或 `start`：
>
> ```bash
> # 查看可用命令
> cat package.json | grep -A 20 '"scripts"'
> ```

## 构建生产版本

```bash
# 构建静态文件（输出到 docs/.vuepress/dist 或类似目录）
pnpm docs:build

# 本地预览构建结果（可选）
npx serve docs/.vuepress/dist
```

## 项目结构速查

```
python-office.com/
├── docs/                       # ⭐ 所有文档内容
│   ├── .vuepress/
│   │   ├── config.ts           # ⭐ VuePress 主配置（导航/侧边栏/插件）
│   │   └── dist/               # 构建产物（自动生成）
│   ├── README.md               # 文档首页
│   └── <章节目录>/             # 各个章节的 Markdown 文件
└── package.json
```

## 常见问题

| 问题 | 解决方案 |
|------|---------|
| `pnpm install` 慢 | 换源：`pnpm config set registry https://registry.npmmirror.com` |
| 启动报 `EADDRINUSE` | 端口被占，改端口：`pnpm docs:dev --port 8888` |
| 改了 `config.ts` 不生效 | Ctrl+C 停止，重新 `pnpm docs:dev` |
| 中文搜索不工作 | 检查 `config.ts` 里是否启用了中文搜索插件 |

---

# ③ ai-nav — AI 工具导航站

## 项目简介

- **用途**：聚合各类 AI 工具、常用网址、分类导航的个人专属"AI 工具箱"
- **技术栈**：Next.js + React + Tailwind CSS（modern stack）
- **特点**：
  - 卡片式 UI，分类清晰
  - 服务端渲染（SSR），SEO 友好
  - 可扩展：加新工具只需改配置文件

## 环境要求

| 软件 | 版本 | 验证命令 |
|------|------|---------|
| Node.js | ≥ 18 (推荐 20.x LTS) | `node -v` |
| npm（自带）或 pnpm | npm ≥ 9 | `npm -v` |
| Git | 任意版本 | `git --version` |

## 本地运行步骤（复制粘贴即可）

```bash
# 1. 克隆项目
git clone https://atomgit.com/python4office/ai-nav.git

# 2. 进入项目目录
cd ai-nav

# 3. 安装依赖（首次运行，可能需要 2-4 分钟）
npm install
# 或用 pnpm：pnpm install

# 4. 启动开发服务器（默认 http://localhost:3000）
npm run dev
# 或用 pnpm：pnpm dev
```

✅ **运行成功的标志**：浏览器打开 <http://localhost:3000> 能看到 AI 导航首页。

> 💡 **提示**：上述是 Next.js 项目的标准启动命令。若仓库实际使用了 Vite 或其他框架，请以仓库根目录 `package.json` 的 `scripts` 字段为准：
>
> ```bash
> cat package.json | grep -A 20 '"scripts"'
> ```

## 添加你自己的工具

大多数 AI 导航站会把工具配置放在 `data/` 或 `lib/` 目录下的 JSON / TS 文件里。**典型操作**：

```bash
# 1. 找到工具配置文件（常见路径）
ls -la data/ lib/ 2>/dev/null
# 通常是 data/tools.json 或 lib/tools-data.ts

# 2. 编辑配置，添加一个新工具（示例 JSON）
# {
#   "id": "claude",
#   "name": "Claude",
#   "url": "https://claude.ai",
#   "category": "AI 对话",
#   "description": "Anthropic 出品的 AI 助手",
#   "icon": "/icons/claude.png"
# }

# 3. 保存后开发服务器会自动热更新
```

## 构建生产版本

```bash
# 构建生产版本
npm run build

# 本地启动生产模式（验证构建结果）
npm run start
```

## 部署方式（推荐 Vercel 一键部署）

```bash
# 1. 安装 Vercel CLI
npm i -g vercel

# 2. 在项目根目录执行
vercel

# 3. 跟随交互提示，几分钟后即得到部署 URL
```

或直接到 <https://vercel.com> 网页端 **Import Git Repository** → 粘贴 atomgit 仓库地址 → 一键部署。

## 常见问题

| 问题 | 解决方案 |
|------|---------|
| `npm install` 卡 sharp/canvas | 切淘宝源：`npm config set registry https://registry.npmmirror.com` |
| 端口 3000 被占用 | 改端口：`PORT=3001 npm run dev` |
| 构建报 `Module not found` | 删除 `node_modules` 和 `.next`，重新 `npm install` |
| 图标显示不出来 | 把图标文件放到 `public/icons/`，配置里写相对路径 `/icons/xxx.png` |

---

# 三个项目共同的注意事项

## 1️⃣ 国内访问慢？切淘宝源

```bash
# npm
npm config set registry https://registry.npmmirror.com

# yarn
yarn config set registry https://registry.npmmirror.com

# pnpm
pnpm config set registry https://registry.npmmirror.com

# 验证
npm config get registry
```

## 2️⃣ 把项目改成"你自己的"

克隆下来后，至少要改 4 个地方才能算"你自己的网站"：

| 项目 | 必改文件 | 改什么 |
|------|---------|--------|
| Hexo 博客 | `hexo/hexo/_config.yml` | `title` / `subtitle` / `description` / `author` / `url` |
| Hexo 主题 | `hexo/hexo/_config.butterfly.yml` | 头像、侧边栏、社交链接 |
| VuePress | `docs/.vuepress/config.ts` | `title` / `description` / 导航栏 / 侧边栏 |
| ai-nav | `data/tools.json`（或类似） | 工具列表全部换成你自己收藏的 |

## 3️⃣ 第一次跑起来后做什么？

1. **改一行测试**：在某个文件里改个标题，看浏览器是否实时刷新
2. **看目录结构**：花 10 分钟把每个文件夹都看一遍，知道东西放在哪里
3. **看一个 commit**：用 `git log --oneline | head -20` 看作者最近改了什么
4. **写一篇文章 / 加一个工具**：动手写第一条内容，跑通"编辑 → 预览 → 提交"完整闭环

> ⚠️ **千万别一上来就大改主题/配色** —— 先把内容流程跑通，再美化。**先上线，再优化**。

---

# 附录：Node.js / pnpm / yarn 安装

## macOS

```bash
# 用 Homebrew 装 Node.js（推荐）
brew install node@20

# 或用 nvm 装多版本
brew install nvm
nvm install 20
nvm use 20

# 装 pnpm + yarn（任选）
corepack enable
corepack prepare pnpm@latest --activate
corepack prepare yarn@stable --activate

# 验证
node -v   # 应显示 v20.x.x
pnpm -v   # 应显示 8.x 或 9.x
yarn -v   # 应显示 1.22 或 4.x
```

## Windows

```powershell
# 1. 去官网下载 Node.js LTS：https://nodejs.org/zh-cn/download
#    选 Windows Installer (.msi) 64-bit，一路下一步即可

# 2. 安装完毕后，打开 PowerShell 验证
node -v

# 3. 启用 corepack 装 pnpm/yarn
corepack enable
corepack prepare pnpm@latest --activate
corepack prepare yarn@stable --activate
```

## Linux (Ubuntu/Debian)

```bash
# 用 NodeSource 源安装最新 Node.js LTS
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# 启用 corepack
sudo corepack enable
corepack prepare pnpm@latest --activate
corepack prepare yarn@stable --activate

# 验证
node -v && pnpm -v && yarn -v
```

---

# 下一步

学完本文你应该已经把 3 个项目都在本地跑起来了。**强烈建议**：

1. **先选 Hexo 博客**跑通完整流程（克隆 → 安装 → 启动 → 写一篇文章 → 重新构建）
2. 跑通后再去克隆 VuePress 文档站，对比两者差异
3. 最后再玩 ai-nav，理解 Next.js 现代前端框架的写法

**📎 相关文档**：
- 课程主目录：[第 1 讲：AI 时代，为什么每个人都需要个人网站](../20260302010101-第1讲-AI时代为什么每个人都需要个人网站.md)
- 后续：第 2 讲会讲 **如何把克隆下来的项目改造成你自己的网站**

---

> 有问题在仓库 Issues 区提：
>
> - <https://atomgit.com/python4office/python4office.cn/issues>
> - <https://atomgit.com/python4office/python-office.com/issues>
> - <https://atomgit.com/python4office/ai-nav/issues>

# software 目录迁移说明

> 生成日期：2026-11-16
> 变更范围：`hexo/hexo/source/_posts/` 下新建 `software/` 目录，容纳「软件 / 电脑软件 / 办公效率工具」类文章。

## 一、为什么单独建目录

此前软件类文章散落在 `_posts/` 根目录和 `_posts/ai/` 里，分类混乱：LocalSend（Mac/Windows 传文件）这种通用工具被放进了 `ai/`，而 Files 文件管理器、office 插件、PyCharm 插件这类纯软件分享则直接躺在根目录。

本次统一收拢到 `software/`，判断口径是：**文章主体在讲某个具体软件 / 工具本身**（是什么、怎么装、怎么用、值不值得用），而不是讲编程技术本身。

## 二、迁移清单（14 篇）

| # | 原路径 | 新路径 | URL 是否变化 |
|---|--------|--------|--------------|
| 1 | `_posts/ai/20261115-localsend-mac-windows-file-transfer.md` | `_posts/software/20261115-localsend-mac-windows-file-transfer.md` | ✅ 变为 `/software/20261115-localsend-mac-windows-file-transfer/`（新文未上线，无影响） |
| 2 | `_posts/files-windows.md` | `_posts/software/files-windows.md` | ❌ 保持 `/files-windows/` |
| 3 | `_posts/office-plugin-10.md` | `_posts/software/office-plugin-10.md` | ❌ 保持 `/office-plugin-10/` |
| 4 | `_posts/plugin-pycharm-8.md` | `_posts/software/plugin-pycharm-8.md` | ❌ 保持 `/plugin-pycharm-8/` |
| 5 | `_posts/free-ide.md` | `_posts/software/free-ide.md` | ❌ 保持 `/free-ide/` |
| 6 | `_posts/code-soft-download.md` | `_posts/software/code-soft-download.md` | ❌ 保持 `/code-soft-download/` |
| 7 | `_posts/python-download.md` | `_posts/software/python-download.md` | ❌ 保持 `/python-download/` |
| 8 | `_posts/card-knowledge-manage.md` | `_posts/software/card-knowledge-manage.md` | ❌ 保持 `/card-knowledge-manage/` |
| 9 | `_posts/chatgpt-fudan.md` | `_posts/software/chatgpt-fudan.md` | ❌ 保持 `/chatgpt-fudan/` |
| 10 | `_posts/gui1-5.md` | `_posts/software/gui1-5.md` | ❌ 保持 `/gui1-5/` |
| 11 | `_posts/hexo-setup-config-bug.md` | `_posts/software/hexo-setup-config-bug.md` | ❌ 保持 `/hexo-setup-config-bug/` |
| 12 | `_posts/linux-setup-python.md` | `_posts/software/linux-setup-python.md` | ❌ 保持 `/linux-setup-python/` |
| 13 | `_posts/win10-docker-install.md` | `_posts/software/win10-docker-install.md` | ❌ 保持 `/win10-docker-install/` |
| 14 | `_posts/mac-on-win.md` | `_posts/software/mac-on-win.md` | ❌ 保持 `/mac-on-win/` |

### 有意排除的文件（不属于「软件分享」）

- 资源/导航类：`blacktech-nav.md`、`library-list.md`、`zhiwang-16.md`、`datav-keyword.md`、`datav-upload-web.md`、`short-vedio.md`、`vedio-course.md`
- 服务器与运行环境配置类：`nginx-config.md`、`nginx-ssl-https.md`、`redis-setup.md`、`spark-setup.md`、`install-postgresql-config.md`、`supervisor-config.md`、`pip-install-nonetwork.md`
- 教程/代码类：`pandas-cmd.md`、`sqlalchemy-grammer.md` 等保持原位

## 三、URL 是怎么保住的（重要）

本站 `permalink: :title/`，而 Hexo 的 `:title` 实际取自 **文件所在路径**，即**目录名会进入 URL**：

- 文件在 `_posts/software/foo.md` → URL 形如 `/software/foo/`
- 文件在 `_posts/根目录/foo.md` → URL 形如 `/foo/`

所以「从根目录挪进子目录」本身就等于换 URL。13 篇老文章都是 2022 年上线的老页面，直接移动会让线上链接全部 404。

**处理办法**：给这 13 篇的 front matter 补一行显式 `permalink`，把老 URL 钉死：

```yaml
title: 受够了微软的「下次一定」？让 Files 满足你对 Windows 文件管理器的期待
date: 2022-02-15 09:42:09
permalink: files-windows/
tags: 黑科技导航
cover: https://images.unsplash.com/...
```

构建后已验证：`public/files-windows/index.html` 等 13 个老路径全部照常产出，`sitemap.xml` 同时收录老地址。

> ⚠️ 后续维护注意：**不要删掉这些显式 `permalink` 行**。一旦删掉，URL 会立刻变成 `/software/files-windows/`，老链接全部失效。
> 万一将来确实需要改这批文章的 URL，正确做法是同步补 Nginx 301（格式参考 `docs/url-redirects-side-hustle.md`），而不是直接删 permalink。

## 四、分类页说明

Hexo 未开启 `category_from_folder`，因此：

- 目录 `software/` **不会**自动生成 `/categories/software/` 分类页；
- 13 篇老文章分类归属不变（原本有 `categories` 的仍是「开发工具」「效率工具」，其余走 `default_category`）；
- LocalSend 一篇按公众号规范保持 `categories: [公众号文章]`。

如果希望站点上出现一个「软件」栏目页，可选两种做法（本次未做，等确认）：

1. 给这批文章统一追加 `categories: [软件推荐]` → 生成 `/categories/软件推荐/`；
2. 开启 `category_from_folder: true` → 目录名自动成为分类（会全站生效，影响面大，不推荐）。

## 五、后续写新文章

- 软件/工具类新文章一律放 `hexo/hexo/source/_posts/software/`，URL 自动带 `/software/` 前缀；
- 公众号规范文章（`categories: [公众号文章]`）保持不变，不要往 `categories` 里塞目录名；
- 移动已上线老文章前，先确认是否需要显式 `permalink` 兜底。

## 六、验证记录

```
hexo clean && hexo generate   → 7461 files generated in 53 s
```

- 13 个老 URL 产物齐全：✅
- LocalSend 新地址 `public/software/20261115-localsend-mac-windows-file-transfer/index.html`：✅
  - canonical = `https://www.python4office.cn/software/20261115-localsend-mac-windows-file-transfer/`
- 旧路径 `public/ai/20261115-localsend-mac-windows-file-transfer/` 残留：❌ 无
- `sitemap.xml` 同时含老地址与新地址：✅

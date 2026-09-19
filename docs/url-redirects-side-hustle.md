# side-hustle 专栏 URL 跳转对照表

> 生成日期：2026-09-19

> 背景：本站 `permalink: :title/` 中的 `:title` 取自 **slug = 文件路径（去掉 .md）**，因此**改文件名等于换 URL**。
> 本次整理了重复内容并顺延了项目编号，共 11 个 URL 发生变化。这些旧 URL 在改动前均为线上 200（已实测确认）。

共 11 条重定向。

## 一、对照表

| # | 旧 URL | 新 URL | 变更原因 |
|---|--------|--------|----------|
| 1 | `/course/side-hustle/project-list/douyin-books/250722-赚钱逻辑/` | `/course/side-hustle/project-list/6-在抖音卖书这件事/` | 与 6 号正文字节级完全相同（重复副本） |
| 2 | `/course/side-hustle/project-list/personal-website/20250725-又被刷了/` | `/course/side-hustle/project-list/ai-courses/0-别卷了/` | 正文被误粘贴成「别卷了」那篇 |
| 3 | `/course/side-hustle/project-list/personal-website/250722-怎么被大模型搜到/` | `/course/side-hustle/project-list/ai-courses/0-别卷了/` | 正文被误粘贴成「别卷了」那篇 |
| 4 | `/course/side-hustle/insights/20250724-博主的下一站/` | `/course/side-hustle/insights/8、有了一个新的目标/` | 与 8 号正文字节级完全相同（重复副本） |
| 5 | `/course/side-hustle/project-list/22-副业5年/` | `/course/side-hustle/project-list/21-副业5年/` | 编号断档 21 空缺，22–28 顺延为 21–27 |
| 6 | `/course/side-hustle/project-list/23-第一阶段/` | `/course/side-hustle/project-list/22-第一阶段/` | 编号断档 21 空缺，22–28 顺延为 21–27 |
| 7 | `/course/side-hustle/project-list/24-不想上班/` | `/course/side-hustle/project-list/23-不想上班/` | 编号断档 21 空缺，22–28 顺延为 21–27 |
| 8 | `/course/side-hustle/project-list/25-豆包/` | `/course/side-hustle/project-list/24-豆包/` | 编号断档 21 空缺，22–28 顺延为 21–27 |
| 9 | `/course/side-hustle/project-list/26-第二阶段/` | `/course/side-hustle/project-list/25-第二阶段/` | 编号断档 21 空缺，22–28 顺延为 21–27 |
| 10 | `/course/side-hustle/project-list/27-副业建议/` | `/course/side-hustle/project-list/26-副业建议/` | 编号断档 21 空缺，22–28 顺延为 21–27 |
| 11 | `/course/side-hustle/project-list/28-普通人可以用AI赚钱的项目有哪些/` | `/course/side-hustle/project-list/27-普通人可以用AI赚钱的项目有哪些/` | 编号断档 21 空缺，22–28 顺延为 21–27 |

## 二、Nginx 配置片段（301 永久跳转）

追加到站点 server 块内，`nginx -t` 通过后 reload：

```nginx
location = /course/side-hustle/project-list/douyin-books/250722-赚钱逻辑/ { return 301 /course/side-hustle/project-list/6-在抖音卖书这件事/; }
location = /course/side-hustle/project-list/personal-website/20250725-又被刷了/ { return 301 /course/side-hustle/project-list/ai-courses/0-别卷了/; }
location = /course/side-hustle/project-list/personal-website/250722-怎么被大模型搜到/ { return 301 /course/side-hustle/project-list/ai-courses/0-别卷了/; }
location = /course/side-hustle/insights/20250724-博主的下一站/ { return 301 /course/side-hustle/insights/8、有了一个新的目标/; }
location = /course/side-hustle/project-list/22-副业5年/ { return 301 /course/side-hustle/project-list/21-副业5年/; }
location = /course/side-hustle/project-list/23-第一阶段/ { return 301 /course/side-hustle/project-list/22-第一阶段/; }
location = /course/side-hustle/project-list/24-不想上班/ { return 301 /course/side-hustle/project-list/23-不想上班/; }
location = /course/side-hustle/project-list/25-豆包/ { return 301 /course/side-hustle/project-list/24-豆包/; }
location = /course/side-hustle/project-list/26-第二阶段/ { return 301 /course/side-hustle/project-list/25-第二阶段/; }
location = /course/side-hustle/project-list/27-副业建议/ { return 301 /course/side-hustle/project-list/26-副业建议/; }
location = /course/side-hustle/project-list/28-普通人可以用AI赚钱的项目有哪些/ { return 301 /course/side-hustle/project-list/27-普通人可以用AI赚钱的项目有哪些/; }
```

## 三、说明

- 前 4 条是**删除重复副本**：新地址是与旧地址正文完全一致的那一篇，跳转后内容不丢失。
- 后 7 条是**编号顺延**：内容一字未改，只是文件名里的编号变化。
- 若不方便改 Nginx，可先跳过前 4 条（重复内容本就该收敛），但后 7 条建议配置，避免已分发的链接失效。
- 站点若已提交过百度/Google 站点地图，跳转生效后搜索引擎会自行把权重迁移到新地址。
<div align="center">
    <a href="https://github.com/CoderWanFeng"> <img src="https://badgen.net/badge/Github/%E7%A8%8B%E5%BA%8F%E5%91%98?icon=github&color=red"></a>
    <a href="https://www.python4office.cn/account-display/"> <img src="https://badgen.net/badge/follow/%E5%85%AC%E4%BC%97%E5%8F%B7?icon=rss&color=green"></a>
    <a href="https://space.bilibili.com/259649365"> <img src="https://badgen.net/badge/pick/B%E7%AB%99?icon=dependabot&color=blue"></a>
    <a href="https://mp.weixin.qq.com/s/6cR5fMSCtdI5sJdWiDwhOA"> <img src="https://badgen.net/badge/join/%E4%BA%A4%E6%B5%81%E7%BE%A4?icon=atom&color=yellow"></a>
</div>



## 说明

一个基于hexo搭建的个人网站：[https://www.python4office.cn](https://www.python4office.cn)，用于存放个人技术文章、学习笔记、生活随笔等。

- 另一个存放教程的网站，也开源了：[https://python-office.com](https://python-office.com)


## 快速开始

1. 安装 [Hexo](https://hexo.io/zh-cn/)
2. 克隆项目：`git clone https://atomgit.com/python4office/python4office.cn.git`
3. 本地运行

> cd hexo/hexo &
> yarn install &
> yarn run clean &
> yarn run build &
> yarn run server &


## 项目结构

```
python4office.cn/
├── docs/                    # 文档目录
│   ├── img_stats.txt        # 图片统计信息
│   ├── naming-convention.md # 文件命名规范
│   ├── no_cover_files.txt   # 无封面文件列表
│   └── writing-guidelines.md# 写作指南
├── hexo/                    # Hexo项目主目录
│   └── hexo/                # Hexo核心文件
│       ├── public/          # 生成的静态文件（部署用）
│       │   ├── css/         # 样式文件
│       │   ├── img/         # 图片资源
│       │   ├── js/          # JavaScript文件
│       │   ├── page/        # 分页目录
│       │   ├── tags/        # 标签页
│       │   └── index.html   # 首页
│       ├── records/         # 记录文件
│       ├── scaffolds/       # 文章模板
│       ├── source/          # 源文件
│       │   ├── _posts/      # 文章目录
│       │   │   ├── ads/     # 广告相关文章
│       │   │   └── ...      # 其他文章分类
│       │   ├── projects/    # 项目展示
│       │   └── tags/        # 标签索引
│       ├── themes/          # 主题目录
│       │   ├── butterfly/   # Butterfly主题
│       │   ├── icarus/      # Icarus主题
│       │   ├── next/        # Next主题
│       │   ├── replica/     # Replica主题
│       │   └── yilia/       # Yilia主题
│       └── _config.yml      # Hexo配置文件
├── scripts/                 # 脚本工具
│   ├── add_article_covers.py     # 添加文章封面
│   ├── add_hreflang_seo.py       # 添加Hreflang SEO标签
│   ├── refresh_cdn.py            # 刷新CDN缓存
│   └── translate_50_docs.py      # 文档翻译脚本
├── .gitignore               # Git忽略配置
├── LICENSE                  # 许可证
├── README.md                # 项目说明
└── fix_duplicate_covers.py  # 修复重复封面脚本
```

### 目录说明

| 目录 | 说明 |
|------|------|
| `docs/` | 存放项目文档、写作指南、命名规范等 |
| `hexo/hexo/` | Hexo博客核心目录，包含所有文章和配置 |
| `hexo/hexo/public/` | Hexo生成的静态HTML文件，用于部署 |
| `hexo/hexo/source/_posts/` | 所有Markdown格式的文章源文件 |
| `hexo/hexo/themes/` | Hexo主题目录，支持多种主题切换 |
| `scripts/` | 辅助脚本工具，用于批量处理文章、SEO优化等 |

## 作者

> 请自行添加

- [CoderWanFeng](https://github.com/CoderWanFeng)
- [YaaaKaaang](https://atomgit.com/YaaaKaaang)
- [wzllby](https://atomgit.com/wzllby)

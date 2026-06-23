# AI热点选题脚本

基于《选题.md》指南的自动化创作启动脚本。

## 功能

1. **自动获取AIHOT热点**：从aihot.virxact.com获取今日热点数据
2. **智能筛选**：按"核心2问"（大众能听懂 + 能解释AI知识）筛选合适选题
3. **自动创建目录**：按标准结构创建公众号和口播稿工作目录
4. **生成模板文件**：创建带元数据的Markdown模板文件

## 文件结构

```
scripts/ai-hot/
├── ai-hot-selector.py    # 主Python脚本
├── run.sh                # 启动脚本
└── README.md             # 说明文档
```

## 使用方法

### 方法一：使用启动脚本（推荐）

```bash
cd /Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn
./scripts/ai-hot/run.sh
```

### 方法二：直接运行Python脚本

```bash
cd /Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/scripts/ai-hot
python3 ai-hot-selector.py
```

### 方法三：添加别名到shell配置

在 `~/.zshrc` 或 `~/.bashrc` 中添加：

```bash
alias ai-hot="/Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/scripts/ai-hot/run.sh"
```

然后重新加载配置：

```bash
source ~/.zshrc
```

之后可以直接运行：

```bash
ai-hot
```

## 工作流程

脚本执行以下步骤：

1. **获取数据**：从AIHOT API获取最近30小时的热点
2. **时间过滤**：筛选出今天（北京时间）的条目
3. **质量评估**：按"核心2问"评估每个条目
4. **选题决策**：选择评分最高且符合核心要求的条目
5. **目录创建**：在 `workflow/公众号/task/` 和 `workflow/口播稿/task/` 创建对应目录
6. **模板生成**：创建带元数据的Markdown模板文件

## 输出示例

```
============================================================
AI热点选题脚本 v1.0
============================================================
正在从AIHOT获取数据: https://aihot.virxact.com/api/public/items?mode=all&since=...
获取到 45 条数据
今天有 8 条热点

评估条目...
✓ Netflix开源神器，token直降95% (评分: 85)
✓ 智谱开源744B大模型，100万上下文免费用 (评分: 78)

选中选题: Netflix开源神器，token直降95%
评分: 85
符合核心2问: True
加分项: 代码=True, 免费=True, 大厂=True
生成slug: netflix-headroom-save-token

创建工作目录...
创建公众号文章: .../workflow/公众号/task/netflix-headroom-save-token/20240623-netflix-headroom-save-token.md
创建口播稿文件: .../workflow/口播稿/task/netflix-headroom-save-token/Process/1-准备口播稿/20240623-netflix-headroom-save-token.md
创建分段文件: .../workflow/口播稿/task/netflix-headroom-save-token/Process/1-准备口播稿/segments.txt

============================================================
选题完成！
============================================================
选题标题: Netflix开源神器，token直降95%
Slug: netflix-headroom-save-token
公众号目录: .../workflow/公众号/task/netflix-headroom-save-token
口播稿目录: .../workflow/口播稿/task/netflix-headroom-save-token/Process
公众号文章: .../workflow/公众号/task/netflix-headroom-save-token/20240623-netflix-headroom-save-token.md
口播稿文件: .../workflow/口播稿/task/netflix-headroom-save-token/Process/1-准备口播稿/20240623-netflix-headroom-save-token.md

下一步:
1. 编辑公众号文章: workflow/公众号/task/netflix-headroom-save-token/
2. 编辑口播稿: workflow/口播稿/task/netflix-headroom-save-token/Process/1-准备口播稿/
3. 按各自指南完成创作
============================================================
```

## 模板文件说明

### 公众号文章模板
- 包含标准元数据（选题来源、栏目、目标平台）
- 遵循7段式结构（标题、开头钩子、为什么值得关注、怎么用、晚枫点评、背后AI知识、对比参考）
- 预留了需要填充的部分（用`[ ]`标记）

### 口播稿模板
- 包含标准元数据
- 遵循三段式结构（Hook、正文、结尾）
- 配套segments.txt文件用于TTS分段

## 后续步骤

选题完成后，需要：

1. **公众号文章**：按 `workflow/公众号/guide/公众号内容的创作指南.md` 完善内容
2. **口播稿**：按 `workflow/口播稿/guide/口播稿内容的创作指南.md` 完善内容
3. **排版发布**：按 `workflow/公众号/guide/公众号排版的创作指南.md` 进行排版发布
4. **视频制作**：按 `workflow/口播稿/guide/口播稿视频的创作指南.md` 制作视频

## 注意事项

1. **网络要求**：需要能访问 `aihot.virxact.com`
2. **时间设置**：脚本使用北京时间过滤今天条目
3. **文件权限**：确保有创建目录和文件的权限
4. **模板定制**：可根据需要修改 `ai-hot-selector.py` 中的模板内容

## 故障排除

### 问题：获取数据失败
- 检查网络连接
- 确认 `aihot.virxact.com` 可访问
- 检查API是否变更

### 问题：没有今天的热点
- AIHOT可能今天没有更新
- 可以手动创建目录和文件

### 问题：权限不足
- 确保对项目目录有写权限
- 可尝试使用 `sudo`（不推荐）

## 版本历史

- v1.0 (2026-06-23): 初始版本，基于《选题.md》实现基本功能

## 相关文档

- [选题.md](../../hexo/hexo/source/_posts/workflow/选题.md) - 完整选题指南
- [公众号内容创作指南](../../hexo/hexo/source/_posts/workflow/公众号/guide/公众号内容的创作指南.md)
- [口播稿内容创作指南](../../hexo/hexo/source/_posts/workflow/口播稿/guide/口播稿内容的创作指南.md)
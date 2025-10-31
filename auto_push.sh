#!/bin/bash

# 自动打包、提交和推送脚本
# 根据最近修改的文件生成智能的commit信息

# 参数处理
BUILD_HEXO=false

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        --build-hexo|-b)
            BUILD_HEXO=true
            shift
            ;;
        --help|-h)
            echo "用法: $0 [选项]"
            echo "选项:"
            echo "  -b, --build-hexo    构建Hexo网站"
            echo "  -h, --help         显示帮助信息"
            exit 0
            ;;
        *)
            echo "未知参数: $1"
            echo "使用 --help 查看帮助信息"
            exit 1
            ;;
    esac
done

echo "=== 开始自动打包和推送流程 ==="

# 可选：构建Hexo网站
if [ "$BUILD_HEXO" = true ]; then
    echo "\n=== 构建Hexo网站 ==="
    cd hexo/hexo
    yarn install
    yarn run clean
    yarn run build
    echo "Hexo构建完成！"
    cd ../..
fi

# 1. 检查git状态
echo "检查git状态..."
git status

# 2. 获取最近修改的文件列表
echo "\n=== 分析最近修改的文件 ==="
MODIFIED_FILES=$(git diff --name-only HEAD)
UNTRACKED_FILES=$(git ls-files --others --exclude-standard)

if [ -n "$MODIFIED_FILES" ]; then
    echo "修改的文件:"
    echo "$MODIFIED_FILES"
fi

if [ -n "$UNTRACKED_FILES" ]; then
    echo "新增的文件:"
    echo "$UNTRACKED_FILES"
fi

# 3. 生成智能commit信息
echo "\n=== 生成commit信息 ==="
COMMIT_MSG="更新网站"

# 根据文件类型生成更具体的commit信息
if echo "$MODIFIED_FILES" | grep -q "\.md$"; then
    COMMIT_MSG="更新博客文章"
elif echo "$MODIFIED_FILES" | grep -q "\.yml$"; then
    COMMIT_MSG="更新配置文件"
elif echo "$MODIFIED_FILES" | grep -q "\.js$" || echo "$MODIFIED_FILES" | grep -q "\.css$"; then
    COMMIT_MSG="更新网站代码"
fi

# 如果有Hexo相关的修改，说明是博客更新
if echo "$MODIFIED_FILES" | grep -q "hexo/" || echo "$UNTRACKED_FILES" | grep -q "hexo/"; then
    COMMIT_MSG="更新博客内容"
fi

echo "生成的commit信息: $COMMIT_MSG"

# 4. 添加所有文件到git
echo "\n=== 添加文件到git ==="
git add .

# 5. 提交更改
echo "\n=== 提交更改 ==="
git commit -m "$COMMIT_MSG"

# 6. 推送更改
echo "\n=== 推送更改到远程仓库 ==="
git push

echo "\n=== 流程完成 ==="
echo "自动打包、提交和推送完成！"


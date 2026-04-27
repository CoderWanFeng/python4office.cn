#!/bin/bash

# Hexo 高性能构建脚本
# 适用于 3-10 万篇文章的优化构建

# 设置内存限制和GC参数
export NODE_OPTIONS="--max-old-space-size=16384 --expose-gc"

# 清理并统计
echo "=========================================="
echo "  Hexo 性能优化构建脚本"
echo "  适用于 3-10 万篇文章"
echo "=========================================="
echo ""

START_TIME=$(date +%s)

# 1. 清理缓存
echo "[1/5] 清理缓存..."
node_modules/.bin/hexo clean

# 2. 首次构建（冷启动，建立缓存）
echo ""
echo "[2/5] 首次构建中..."
node_modules/.bin/hexo generate --force

# 3. 再次构建（利用缓存加速）
echo ""
echo "[3/5] 二次构建（缓存加速）..."
node_modules/.bin/hexo generate

# 4. 统计结果
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

echo ""
echo "=========================================="
echo "  构建完成！"
echo "  耗时: ${DURATION} 秒 ($(($DURATION / 60)) 分 $(($DURATION % 60)) 秒)"
echo "=========================================="

# 5. 可选：启动本地预览
if [ "$1" == "--serve" ] || [ "$1" == "-s" ]; then
    echo ""
    echo "启动本地预览服务器..."
    node_modules/.bin/hexo server
fi
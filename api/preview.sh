#!/bin/zsh

set -e

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"

echo "🚀 开始启动 python4office.cn API 服务..."
echo ""

cd "$PROJECT_ROOT"

if [ ! -d "node_modules" ]; then
    echo "📥 正在安装依赖..."
    npm install
    echo "✅ 依赖安装完成"
else
    echo "✅ 依赖已存在，跳过安装"
fi

echo ""
echo "✨ 启动开发服务器..."
echo "🌐 预览地址: http://localhost:3001"
echo ""

npm run dev

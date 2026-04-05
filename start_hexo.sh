#!/bin/bash

# Python4Office Hexo 网站启动脚本

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${CYAN}========================================${NC}"
echo -e "${CYAN}    启动 Hexo 网站${NC}"
echo -e "${CYAN}========================================${NC}"
echo ""

# 进入 Hexo 目录
cd "$SCRIPT_DIR/hexo/hexo" || exit 1

# 检查并安装依赖
if [ ! -d "node_modules" ]; then
    echo -e "${YELLOW}首次运行，正在安装依赖...${NC}"
    yarn install
    echo -e "${GREEN}依赖安装完成！${NC}"
    echo ""
fi

# 启动服务器
echo -e "${YELLOW}正在启动 Hexo 服务器...${NC}"
echo ""
echo -e "${GREEN}网站地址: http://localhost:4000${NC}"
echo -e "${YELLOW}按 Ctrl+C 停止服务器${NC}"
echo ""
echo -e "${CYAN}========================================${NC}"
echo ""

yarn run server

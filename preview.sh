#!/bin/bash

# Python4Office Hexo 网站启动脚本 - 支持热加载

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/preview.log"

# 清空旧日志，重新开始记录
> "$LOG_FILE"

# 日志写入函数
log() {
    echo -e "$1"
    echo -e "$1" | sed 's/\x1b\[[0-9;]*m//g' >> "$LOG_FILE"
}

echo -e "${CYAN}========================================${NC}"
echo -e "${CYAN}    启动 Hexo 网站 (热加载模式)${NC}"
echo -e "${CYAN}========================================${NC}"
echo ""

# 进入 Hexo 目录
cd "$SCRIPT_DIR/hexo/hexo" || exit 1

# 检查并安装依赖
if [ ! -d "node_modules" ]; then
    log "${YELLOW}首次运行，正在安装依赖...${NC}"
    yarn install >> "$LOG_FILE" 2>&1
    log "${GREEN}依赖安装完成！${NC}"
    log ""
fi

# 清理旧的静态文件（确保配置修改生效）
log "${YELLOW}清理旧的静态文件...${NC}"
yarn run clean >> "$LOG_FILE" 2>&1

# 重新生成静态网站（确保配置修改生效）
log "${YELLOW}生成静态网站...${NC}"
yarn run build >> "$LOG_FILE" 2>&1

# 检查是否安装了 hexo-browsersync 插件（实现浏览器自动刷新）
if grep -q "hexo-browsersync" package.json; then
    log "${GREEN}✓ 检测到 browsersync 插件，浏览器将自动刷新${NC}"
    log ""
fi

# 启动服务器（带热加载和调试信息）
log "${YELLOW}正在启动 Hexo 服务器...${NC}"
log "${YELLOW}热加载已启用 - 修改文件后会自动重新生成${NC}"
log ""
log "${GREEN}网站地址: http://localhost:4000${NC}"
log "${YELLOW}按 Ctrl+C 停止服务器${NC}"
log ""
log "${CYAN}========================================${NC}"
log ""

# 启动带监视功能的服务器
yarn run server --watch --debug >> "$LOG_FILE" 2>&1

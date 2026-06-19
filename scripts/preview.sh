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

# 检查并清理过大的旧日志（>5M 或 >7天）
if [ -f "$LOG_FILE" ]; then
    file_size=$(stat -f%z "$LOG_FILE" 2>/dev/null || echo 0)
    file_mtime=$(stat -f%m "$LOG_FILE" 2>/dev/null || echo 0)
    now=$(date +%s)
    size_mb=$((file_size / 1024 / 1024))
    age_days=$(( (now - file_mtime) / 86400 ))

    if [ "$size_mb" -gt 5 ] || [ "$age_days" -gt 7 ]; then
        echo -e "${YELLOW}旧日志清理: ${size_mb}M, ${age_days}天前 -> 删除${NC}"
        rm "$LOG_FILE"
    fi
fi

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
cd "$SCRIPT_DIR/../hexo/hexo" || exit 1

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
log "${CYAN}========================================${NC}"
log ""

# 自动杀掉占用 4000 端口的旧 hexo 进程
if command -v lsof >/dev/null 2>&1; then
  old_pid=$(/usr/sbin/lsof -nP -iTCP:4000 -sTCP:LISTEN -t 2>/dev/null | head -1)
  if [ -n "$old_pid" ]; then
    log "${YELLOW}发现端口 4000 被占用（PID $old_pid），自动清理...${NC}"
    kill "$old_pid" 2>/dev/null
    sleep 1
    if /usr/sbin/lsof -nP -iTCP:4000 -sTCP:LISTEN >/dev/null 2>&1; then
      kill -9 "$old_pid" 2>/dev/null
      sleep 1
    fi
  fi
fi

# 后台启动 server
yarn run server --watch --debug >> "$LOG_FILE" 2>&1 &
SERVER_PID=$!

# Ctrl+C 时一起清理
cleanup_server() {
  if kill -0 "$SERVER_PID" 2>/dev/null; then
    kill -TERM "$SERVER_PID" 2>/dev/null
    sleep 1
    kill -KILL "$SERVER_PID" 2>/dev/null
  fi
}
trap cleanup_server INT TERM EXIT

# 轮询端口 4000 是否就绪
log "${YELLOW}等待服务器就绪...${NC}"
SERVER_READY=0
for i in $(seq 1 180); do
  if /usr/sbin/lsof -nP -iTCP:4000 -sTCP:LISTEN >/dev/null 2>&1; then
    SERVER_READY=1
    log "${GREEN}✓ Hexo 服务器已就绪（${i} 秒）${NC}"
    log ""
    log "${GREEN}网站地址: http://localhost:4000${NC}"
    log "${YELLOW}按 Ctrl+C 停止服务器${NC}"
    log ""
    log "${CYAN}========================================${NC}"
    log ""
    break
  fi
  if ! kill -0 "$SERVER_PID" 2>/dev/null; then
    log "${RED}✗ Hexo 服务器启动失败${NC}"
    log "${YELLOW}preview.log 末尾：${NC}"
    /usr/bin/tail -15 "$LOG_FILE" 2>/dev/null
    exit 1
  fi
  sleep 1
done

if [ "$SERVER_READY" -ne 1 ]; then
  log "${RED}✗ Hexo 服务器 180 秒内未就绪${NC}"
  kill -KILL "$SERVER_PID" 2>/dev/null
  exit 1
fi

# 让 server 跑前台（Ctrl+C 由 trap 处理）
wait "$SERVER_PID"

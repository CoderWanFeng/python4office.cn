#!/bin/bash

# 优化版 Hexo 构建脚本 - 性能优化版本
# 自动检测依赖状态，增量构建，并行处理

set -e  # 遇到错误立即退出

# 颜色定义（可选，用于更好的输出）
if [ -t 1 ]; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    NC='\033[0m' # No Color
else
    RED=''
    GREEN=''
    YELLOW=''
    BLUE=''
    NC=''
fi

# 日志函数
log() {
    echo -e "${BLUE}[$(date +'%H:%M:%S')]${NC} $1"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

log_error() {
    echo -e "${RED}✗${NC} $1"
}

# 检查并进入目录
if [ ! -d "hexo/hexo" ]; then
    log_error "Hexo目录不存在: hexo/hexo"
    exit 1
fi

cd hexo/hexo
log "进入Hexo目录: $(pwd)"

# 1. 智能依赖安装（避免重复安装）
log "检查依赖状态..."
if [ ! -d "node_modules" ] || [ "package.json" -nt "node_modules" ] || [ "yarn.lock" -nt "node_modules" ]; then
    log "检测到依赖需要更新，开始安装..."
    
    # 使用Yarn的缓存和并行安装优化
    if yarn install --frozen-lockfile --silent --ignore-engines --ignore-optional --non-interactive 2>&1; then
        log_success "依赖安装完成"
    else
        log_error "依赖安装失败"
        exit 1
    fi
else
    log_success "依赖已是最新，跳过安装"
fi

# 2. 智能清理策略
log "检查是否需要清理..."
if [ ! -d "public" ] || [ "db.json" -nt "public" ] || [ "_config.yml" -nt "public" ]; then
    log "执行Hexo清理..."
    if yarn run clean 2>&1; then
        log_success "清理完成"
    else
        log_warning "清理过程中出现警告，但继续执行"
    fi
else
    log_success "public目录已是最新，跳过清理"
fi

# 3. 并行构建优化（如果支持）
log "开始构建Hexo网站..."

# 设置环境变量优化构建性能
export NODE_ENV=production
export HEXO_GENERATE_CONCURRENCY=4  # 并行生成页面

# 使用Hexo的增量生成和缓存优化
if npx hexo generate --draft --silent 2>&1; then
    log_success "Hexo构建完成"
else
    log_error "Hexo构建失败"
    exit 1
fi

# 4. 构建后优化
log "执行构建后优化..."

# 检查构建结果
if [ -d "public" ]; then
    PUBLIC_SIZE=$(du -sh public | cut -f1)
    FILE_COUNT=$(find public -type f | wc -l)
    log_success "构建完成: ${PUBLIC_SIZE} 大小，${FILE_COUNT} 个文件"
else
    log_error "构建失败：public目录不存在"
    exit 1
fi

# 5. 可选：启动本地服务器（注释状态）
# log "启动本地服务器..."
# yarn run server &
# SERVER_PID=$!
# log_success "服务器已启动 (PID: $SERVER_PID)"

log_success "Hexo构建流程全部完成！"

# 显示构建统计信息
echo ""
echo "=== 构建统计 ==="
echo "- 构建时间: $(date)"
echo "- 输出目录: public/"
echo "- 文件数量: ${FILE_COUNT}"
echo "- 总大小: ${PUBLIC_SIZE}"
echo ""

# 注释掉的Git操作和部署代码（保持原有功能）
# git add .
# git commit -m "更新网站"
# git push
# rm -rf /opt/website/python4office.cn/*
# cp /opt/workplace/pro/python4office.cn/hexo/hexo/public/* /opt/website/python4office.cn/ -R

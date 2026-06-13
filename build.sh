#!/bin/bash

# Nginx 远程部署脚本
# 从 public 仓库同步静态文件并部署

set -e  # 遇到错误立即退出

# 颜色定义
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

# 错误处理函数
handle_error() {
    log_error "操作失败: $1"
    exit 1
}

PUBLIC_REPO="https://atomgit.com/python4office/hexo-public"
PUBLIC_DIR="/opt/workplace/pro/opc-website/python4office.cn/hexo-public"

sync_public_repo() {
    log "开始同步 public 仓库..."

    if [ ! -d "$PUBLIC_DIR/.git" ]; then
        rm -rf "$PUBLIC_DIR"
        git clone "$PUBLIC_REPO" "$PUBLIC_DIR" || handle_error "克隆 public 仓库失败"
    fi

    cd "$PUBLIC_DIR"

    git fetch --prune origin

    if git rev-parse origin/main >/dev/null 2>&1; then
        BRANCH="main"
    elif git rev-parse origin/master >/dev/null 2>&1; then
        BRANCH="master"
    else
        handle_error "无法确定 public 仓库远程主分支名称"
    fi

    git reset --hard "origin/$BRANCH"
    git clean -fdx

    log_success "public 仓库已强制同步到 origin/$BRANCH"
}

# 部署到Nginx目录
deploy_to_nginx() {
    log "开始部署到Nginx目录..."
    
    NGINX_DIR="/opt/website/opc-website/python4office.cn"
    
    # 检查源目录
    if [ ! -d "$PUBLIC_DIR" ]; then
        handle_error "public 目录不存在: $PUBLIC_DIR"
    fi
    
    # 检查Nginx目录
    if [ ! -d "$NGINX_DIR" ]; then
        log_warning "Nginx目录不存在，尝试创建: $NGINX_DIR"
        mkdir -p "$NGINX_DIR" || handle_error "无法创建Nginx目录"
    fi
    
    # 清空Nginx目录
    log "清空Nginx目录..."
    rm -rf "${NGINX_DIR:?}"/*
    
    # 复制 public 仓库文件
    log "复制 public 文件..."
    rsync -a --delete --exclude='.git' "$PUBLIC_DIR"/ "$NGINX_DIR"/
    
    # 设置权限
    log "设置文件权限..."
    chmod -R 755 "$NGINX_DIR"
    
    # 统计部署结果
    FILE_COUNT=$(find "$NGINX_DIR" -type f | wc -l)
    DIR_SIZE=$(du -sh "$NGINX_DIR" | cut -f1)
    
    log_success "部署完成: ${DIR_SIZE} 大小，${FILE_COUNT} 个文件"
}

# 主执行流程
main() {
    log "========== 开始远程部署 =========="
    
    # 1. 同步 public 仓库
    sync_public_repo
    
    # 2. 部署到Nginx
    deploy_to_nginx
    
    log "========== 部署完成 =========="
    
    # 显示最终状态
    echo ""
    echo "=== 部署统计 ==="
    echo "- 完成时间: $(date)"
    echo "- public 提交: $(cd "$PUBLIC_DIR" && git log --oneline -1)"
    echo "- public 提交数量: $(cd "$PUBLIC_DIR" && git rev-list --count HEAD)"
    echo ""
    
    log_success "所有操作已成功完成！"
}

# 执行主函数
main

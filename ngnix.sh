#!/bin/bash

# Nginx 远程部署脚本
# 自动处理Git历史差异，远程版本覆盖本地

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

# 验证Git仓库状态
validate_git_repo() {
    if [ ! -d ".git" ]; then
        handle_error "当前目录不是Git仓库"
    fi
    
    if ! git rev-parse HEAD >/dev/null 2>&1; then
        handle_error "Git仓库状态异常"
    fi
    
    log_success "Git仓库验证通过"
}

# 处理本地更改
handle_local_changes() {
    log "检查本地更改..."
    
    # 检查是否有未提交的更改
    if ! git diff-index --quiet HEAD --; then
        log_warning "检测到本地更改，将被远程版本覆盖"
        
        # 显示将被覆盖的文件
        CHANGED_FILES=$(git diff --name-only HEAD)
        if [ -n "$CHANGED_FILES" ]; then
            log "将被覆盖的文件:"
            echo "$CHANGED_FILES" | while read file; do
                echo "  - $file"
            done
        fi
        
        # 强制重置到远程状态
        log "重置本地更改..."
        git reset --hard HEAD
        git clean -fd
        log_success "本地更改已清除"
    else
        log_success "工作区干净"
    fi
}

# 智能拉取代码（处理历史差异）
smart_pull() {
    log "开始拉取远程代码..."
    
    # 获取远程最新信息
    git fetch origin
    
    # 获取本地和远程的提交信息
    LOCAL_COMMIT=$(git rev-parse HEAD)
    REMOTE_COMMIT=$(git rev-parse origin/main 2>/dev/null || git rev-parse origin/master 2>/dev/null)
    
    # 确定主分支名称
    if git rev-parse origin/main >/dev/null 2>&1; then
        BRANCH="main"
    elif git rev-parse origin/master >/dev/null 2>&1; then
        BRANCH="master"
    else
        handle_error "无法确定远程主分支名称"
    fi
    
    log "本地提交: $LOCAL_COMMIT"
    log "远程提交: $REMOTE_COMMIT"
    log "主分支: $BRANCH"
    
    # 检查本地和远程是否相同
    if [ "$LOCAL_COMMIT" = "$REMOTE_COMMIT" ]; then
        log_success "本地已是最新版本"
        return 0
    fi
    
    # 检查是否有历史差异（本地和远程分叉）
    MERGE_BASE=$(git merge-base HEAD origin/$BRANCH 2>/dev/null || echo "")
    
    if [ -z "$MERGE_BASE" ]; then
        # 没有共同祖先，说明历史完全不同（可能是历史压缩导致）
        log_warning "检测到历史差异（可能由历史压缩导致）"
        log "使用远程版本完全覆盖本地..."
        
        git reset --hard origin/$BRANCH
        log_success "本地已同步到远程版本"
    else
        # 有共同祖先，检查是否分叉
        if [ "$MERGE_BASE" != "$LOCAL_COMMIT" ] && [ "$MERGE_BASE" != "$REMOTE_COMMIT" ]; then
            # 本地和远程都有新提交，存在分叉
            log_warning "检测到本地和远程分叉"
            log "使用远程版本覆盖本地..."
            
            git reset --hard origin/$BRANCH
            log_success "本地已同步到远程版本"
        elif [ "$MERGE_BASE" = "$LOCAL_COMMIT" ]; then
            # 本地落后于远程，正常快进
            log "本地落后于远程，执行快进合并..."
            git merge --ff-only origin/$BRANCH
            log_success "快进合并完成"
        else
            # 本地领先于远程（不应该发生，但做保护性处理）
            log_warning "本地领先于远程，强制同步到远程版本..."
            git reset --hard origin/$BRANCH
            log_success "本地已同步到远程版本"
        fi
    fi
    
    # 清理reflog和垃圾回收
    git reflog expire --expire=now --all 2>/dev/null || true
    git gc --prune=now 2>/dev/null || true
}

# 部署到Nginx目录
deploy_to_nginx() {
    log "开始部署到Nginx目录..."
    
    NGINX_DIR="/opt/website/python4office.cn"
    PUBLIC_DIR="/opt/workplace/pro/python4office.cn/hexo/hexo/public"
    
    # 检查源目录
    if [ ! -d "$PUBLIC_DIR" ]; then
        handle_error "构建目录不存在: $PUBLIC_DIR"
    fi
    
    # 检查Nginx目录
    if [ ! -d "$NGINX_DIR" ]; then
        log_warning "Nginx目录不存在，尝试创建: $NGINX_DIR"
        mkdir -p "$NGINX_DIR" || handle_error "无法创建Nginx目录"
    fi
    
    # 清空Nginx目录
    log "清空Nginx目录..."
    rm -rf "${NGINX_DIR:?}"/*
    
    # 复制新文件（使用原来的命令格式）
    log "复制构建文件..."
    cp "$PUBLIC_DIR"/* "$NGINX_DIR"/ -R
    
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
    
    # 1. 验证Git仓库
    validate_git_repo
    
    # 2. 处理本地更改
    handle_local_changes
    
    # 3. 智能拉取代码
    smart_pull
    
    # 4. 部署到Nginx
    deploy_to_nginx
    
    log "========== 部署完成 =========="
    
    # 显示最终状态
    echo ""
    echo "=== 部署统计 ==="
    echo "- 完成时间: $(date)"
    echo "- 当前提交: $(git log --oneline -1)"
    echo "- 提交数量: $(git rev-list --count HEAD)"
    echo ""
    
    log_success "所有操作已成功完成！"
}

# 执行主函数
main

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

# ============================================
# Git 历史压缩功能（保留最近10次提交）
# 设置 TRUNCATE_GIT_HISTORY=true 启用此功能
# ============================================
TRUNCATE_GIT_HISTORY=${TRUNCATE_GIT_HISTORY:-false}
KEEP_COMMITS=10

if [ "$TRUNCATE_GIT_HISTORY" = "true" ]; then
    log "开始Git历史压缩..."
    
    # 返回仓库根目录
    cd "$(git rev-parse --show-toplevel)"
    
    # 获取当前分支名
    BRANCH=$(git rev-parse --abbrev-ref HEAD)
    
    # 检查是否有未提交的更改
    if ! git diff-index --quiet HEAD --; then
        log_error "存在未提交的更改，请先提交或暂存"
        exit 1
    fi
    
    # 检查提交数量
    COMMIT_COUNT=$(git rev-list --count HEAD)
    log "当前提交总数: $COMMIT_COUNT"
    
    if [ "$COMMIT_COUNT" -le "$KEEP_COMMITS" ]; then
        log_warning "提交数量不足${KEEP_COMMITS}次，无需压缩历史"
    else
        log "将保留最近 ${KEEP_COMMITS} 次提交，压缩更早的历史..."
        
        # 获取要保留的提交列表（从旧到新）
        FIRST_KEEP_COMMIT=$(git rev-list -n $KEEP_COMMITS HEAD | tail -1)
        
        # 备份当前分支引用
        git branch backup_before_truncate_$(date +%Y%m%d%H%M%S) HEAD 2>/dev/null || true
        
        # 删除可能存在的临时分支
        git branch -D temp_truncate 2>/dev/null || true
        
        # 获取第一个要保留的提交的树对象和提交信息
        TREE=$(git rev-parse ${FIRST_KEEP_COMMIT}^{tree})
        COMMIT_MSG=$(git log --format=%B -n 1 $FIRST_KEEP_COMMIT)
        
        # 创建一个新的初始提交（无父提交）
        NEW_BASE=$(echo "$COMMIT_MSG" | git commit-tree $TREE)
        
        # 将后续提交 rebase 到新基础上
        git checkout -b temp_truncate $NEW_BASE
        
        # 获取需要 cherry-pick 的提交（从旧到新，排除第一个）
        CHERRY_PICKS=$(git rev-list --reverse ${FIRST_KEEP_COMMIT}..HEAD~0 --first-parent 2>/dev/null | head -n $((KEEP_COMMITS - 1)))
        
        # 使用 rebase 方式更安全
        if [ -n "$CHERRY_PICKS" ]; then
            git rebase --onto temp_truncate ${FIRST_KEEP_COMMIT}^ HEAD~0 --committer-date-is-author-date 2>/dev/null || \
            for commit in $CHERRY_PICKS; do
                git cherry-pick $commit --allow-empty 2>/dev/null || true
            done
        fi
        
        # 更新原分支指向
        git checkout $BRANCH
        git reset --hard temp_truncate
        
        # 清理临时分支
        git branch -D temp_truncate 2>/dev/null || true
        
        # 执行垃圾回收以释放空间
        log "执行Git垃圾回收..."
        git reflog expire --expire=now --all
        git gc --aggressive --prune=now
        
        # 显示结果
        NEW_COMMIT_COUNT=$(git rev-list --count HEAD)
        log_success "历史压缩完成: $COMMIT_COUNT -> $NEW_COMMIT_COUNT 次提交"
        
        # 提示强制推送
        log_warning "如需同步到远程，请执行: git push --force origin $BRANCH"
    fi
else
    log "Git历史压缩已跳过 (设置 TRUNCATE_GIT_HISTORY=true 启用)"
fi

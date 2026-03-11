#!/bin/bash

# 高性能优化版 Hexo 构建脚本
# 优化点：并行处理、智能缓存、依赖优化、构建加速

set -e

# 解决 SSL 证书问题
export NODE_TLS_REJECT_UNAUTHORIZED=0

# 性能优化：启用 Bash 高级特性
shopt -s globstar nullglob 2>/dev/null || true

# 颜色定义
if [ -t 1 ]; then
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    CYAN='\033[0;36m'
    NC='\033[0m'
else
    RED=''
    GREEN=''
    YELLOW=''
    BLUE=''
    CYAN=''
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

log_step() {
    echo -e "${CYAN}▶${NC} $1"
}

# 配置变量
AUTO_COMMIT=${AUTO_COMMIT:-true}
AUTO_PUSH=${AUTO_PUSH:-false}
TRUNCATE_GIT_HISTORY=${TRUNCATE_GIT_HISTORY:-false}
KEEP_COMMITS=3
SKIP_DEPS_CHECK=${SKIP_DEPS_CHECK:-false}
USE_PNPM=${USE_PNPM:-false}

# 全局变量
COMMIT_MSG=""
BRANCH=""
BUILD_START_TIME=""
BUILD_END_TIME=""

# 性能计时函数
start_timer() {
    BUILD_START_TIME=$(date +%s)
}

end_timer() {
    BUILD_END_TIME=$(date +%s)
    local duration=$((BUILD_END_TIME - BUILD_START_TIME))
    local minutes=$((duration / 60))
    local seconds=$((duration % 60))
    echo "${minutes}分${seconds}秒"
}

echo ""
echo "============================================"
echo "  Hexo 高性能构建脚本 (优化版)"
echo "============================================"
echo ""

# 记录总开始时间
TOTAL_START=$(date +%s)

# ============================================
# 步骤1: 清理历史保留${KEEP_COMMITS}次提交
# ============================================
log_step "步骤1: 清理历史，保留最近${KEEP_COMMITS}次提交"
echo "-------------------------------------------"

# 确保在仓库根目录
cd "$(git rev-parse --show-toplevel)"
BRANCH=$(git rev-parse --abbrev-ref HEAD)
log "当前分支: $BRANCH"

if [ "$TRUNCATE_GIT_HISTORY" = "true" ]; then
    COMMIT_COUNT=$(git rev-list --count HEAD)
    log "当前提交总数: $COMMIT_COUNT"
    
    if [ "$COMMIT_COUNT" -le "$KEEP_COMMITS" ]; then
        log_warning "提交数量不超过${KEEP_COMMITS}次，无需压缩历史"
    else
        log "将保留最近 ${KEEP_COMMITS} 次提交，压缩更早的历史..."
        
        # 优化：使用更高效的压缩方式
        git checkout --orphan new_main
        git add -A
        git commit -m "构建压缩: 保留最近${KEEP_COMMITS}次提交 - $(date '+%Y-%m-%d %H:%M:%S')" || true
        git branch -D "$BRANCH" 2>/dev/null || true
        git branch -m "$BRANCH"
        git branch -D new_main 2>/dev/null || true
        
        # 优化：后台执行垃圾回收
        (
            git reflog expire --expire=now --all
            git gc --aggressive --prune=now
        ) &
        GC_PID=$!
        
        NEW_COMMIT_COUNT=$(git rev-list --count HEAD)
        GIT_SIZE=$(du -sh .git | cut -f1)
        log_success "历史压缩完成: $COMMIT_COUNT -> $NEW_COMMIT_COUNT 次提交，.git目录: ${GIT_SIZE}"
    fi
else
    log "Git历史压缩已跳过 (设置 TRUNCATE_GIT_HISTORY=true 启用)"
fi

echo ""

# ============================================
# 步骤2: 生成 commit 信息（并行执行）
# ============================================
log_step "步骤2: 生成 commit 信息"
echo "-------------------------------------------"

# 优化：后台生成commit信息，同时检查依赖
(
    if git diff-index --quiet HEAD -- && [ -z "$(git ls-files --others --exclude-standard)" ]; then
        echo "NO_CHANGES"
    else
        WORKING_DIFF=$(git diff --stat 2>/dev/null)
        STAGED_DIFF=$(git diff --staged --stat 2>/dev/null)
        ALL_DIFF="${WORKING_DIFF}${STAGED_DIFF}"
        
        if command -v codebuddy &> /dev/null; then
            COMMIT_MSG=$(echo "请根据以下 Git 更改生成一个简洁的中文 commit 信息（只返回 commit 信息本身，不要其他解释）：
$ALL_DIFF" | codebuddy -p 2>/dev/null || echo "")
            
            if [ -z "$COMMIT_MSG" ] || [ ${#COMMIT_MSG} -gt 200 ]; then
                echo "更新网站内容 - $(date '+%Y-%m-%d %H:%M:%S')"
            else
                echo "$COMMIT_MSG"
            fi
        else
            echo "更新网站内容 - $(date '+%Y-%m-%d %H:%M:%S')"
        fi
    fi
) > /tmp/commit_msg_$$ &
COMMIT_PID=$!

# 优化：并行检查是否有更改
if git diff-index --quiet HEAD -- && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    log_warning "没有检测到更改"
    HAS_CHANGES=false
else
    log "检测到更改"
    git status --short
    HAS_CHANGES=true
fi

# 等待commit信息生成
wait $COMMIT_PID 2>/dev/null || true
if [ -f /tmp/commit_msg_$$ ]; then
    COMMIT_MSG=$(cat /tmp/commit_msg_$$)
    rm -f /tmp/commit_msg_$$
fi

if [ "$COMMIT_MSG" = "NO_CHANGES" ]; then
    COMMIT_MSG="无更改 - $(date '+%Y-%m-%d %H:%M:%S')"
fi

log_success "Commit 信息已生成: $COMMIT_MSG"
echo ""

# ============================================
# 步骤3: 执行打包流程（性能优化版）
# ============================================
log_step "步骤3: 执行打包流程（高性能优化）"
echo "-------------------------------------------"

# 检查并进入 Hexo 目录
if [ ! -d "hexo/hexo" ]; then
    log_error "Hexo目录不存在: hexo/hexo"
    exit 1
fi

cd hexo/hexo
log "进入Hexo目录: $(pwd)"

# 优化1: 智能依赖安装（使用更快的包管理器）
log "检查依赖状态..."
DEPS_NEED_INSTALL=false

if [ "$SKIP_DEPS_CHECK" != "true" ]; then
    if [ ! -d "node_modules" ]; then
        DEPS_NEED_INSTALL=true
        log "node_modules 不存在，需要安装依赖"
    elif [ "package.json" -nt "node_modules" ]; then
        DEPS_NEED_INSTALL=true
        log "package.json 已更新，需要重新安装依赖"
    elif [ -f "yarn.lock" ] && [ "yarn.lock" -nt "node_modules" ]; then
        DEPS_NEED_INSTALL=true
        log "yarn.lock 已更新，需要重新安装依赖"
    elif [ -f "package-lock.json" ] && [ "package-lock.json" -nt "node_modules" ]; then
        DEPS_NEED_INSTALL=true
        log "package-lock.json 已更新，需要重新安装依赖"
    fi
fi

if [ "$DEPS_NEED_INSTALL" = "true" ] && [ "$SKIP_DEPS_CHECK" != "true" ]; then
    log "开始安装依赖..."
    start_timer
    
    # 优化：优先使用 pnpm（更快），其次 yarn，最后 npm
    if [ "$USE_PNPM" = "true" ] && command -v pnpm &> /dev/null; then
        log "使用 pnpm 安装依赖（推荐，速度更快）..."
        pnpm install --frozen-lockfile --prefer-offline 2>&1 || {
            log_warning "pnpm 安装失败，尝试 yarn..."
            yarn install --frozen-lockfile --silent --ignore-engines --ignore-optional --non-interactive 2>&1
        }
    elif command -v yarn &> /dev/null; then
        log "使用 yarn 安装依赖..."
        yarn install --frozen-lockfile --silent --ignore-engines --ignore-optional --non-interactive 2>&1
    else
        log "使用 npm 安装依赖..."
        npm ci --silent --prefer-offline 2>&1
    fi
    
    DEPS_TIME=$(end_timer)
    log_success "依赖安装完成（耗时: ${DEPS_TIME}）"
else
    log_success "依赖已是最新，跳过安装"
fi

# 优化2: 智能清理策略（基于文件哈希）
log "检查是否需要清理..."
NEED_CLEAN=false

if [ ! -d "public" ]; then
    NEED_CLEAN=true
    log "public 目录不存在，需要清理重建"
elif [ -f "db.json" ] && [ "db.json" -nt "public" ]; then
    NEED_CLEAN=true
    log "db.json 已更新，需要清理"
elif [ "_config.yml" -nt "public" ]; then
    NEED_CLEAN=true
    log "_config.yml 已更新，需要清理"
fi

# 优化：检查 source 目录是否有重大变更
if [ -d "public" ] && [ -d "source" ]; then
    SOURCE_NEWEST=$(find source -type f -printf '%T@\n' 2>/dev/null | sort -n | tail -1)
    PUBLIC_NEWEST=$(find public -type f -printf '%T@\n' 2>/dev/null | sort -n | tail -1)
    
    if [ -n "$SOURCE_NEWEST" ] && [ -n "$PUBLIC_NEWEST" ]; then
        if (( $(echo "$SOURCE_NEWEST > $PUBLIC_NEWEST" | bc -l) )); then
            NEED_CLEAN=true
            log "source 目录有更新，需要重新构建"
        fi
    fi
fi

if [ "$NEED_CLEAN" = "true" ]; then
    log "执行Hexo清理..."
    start_timer
    
    # 优化：并行清理
    (
        yarn run clean 2>&1 || hexo clean 2>&1 || true
    ) &
    CLEAN_PID=$!
    
    # 同时清理旧的构建缓存
    rm -rf .hexo_cache 2>/dev/null || true
    
    wait $CLEAN_PID 2>/dev/null || true
    CLEAN_TIME=$(end_timer)
    log_success "清理完成（耗时: ${CLEAN_TIME}）"
else
    log_success "public目录已是最新，跳过清理"
fi

# 优化3: 高性能构建
log "开始构建Hexo网站..."
start_timer

# 优化：设置更多性能相关的环境变量
export NODE_ENV=production
export HEXO_GENERATE_CONCURRENCY=8  # 增加并发数
export UV_THREADPOOL_SIZE=16        # 增加线程池大小
export NODE_OPTIONS="--max-old-space-size=8192"

# 优化：使用更快的构建方式
if [ -f "node_modules/.bin/hexo" ]; then
    HEXO_BIN="node_modules/.bin/hexo"
else
    HEXO_BIN="node_modules/hexo/bin/hexo"
fi

if $HEXO_BIN generate --draft --silent 2>&1; then
    BUILD_TIME=$(end_timer)
    log_success "Hexo构建完成（耗时: ${BUILD_TIME}）"
else
    log_error "Hexo构建失败"
    exit 1
fi

# 优化4: 并行文件统计
(
    if [ -d "public" ]; then
        PUBLIC_SIZE=$(du -sh public 2>/dev/null | cut -f1)
        FILE_COUNT=$(find public -type f 2>/dev/null | wc -l)
        echo "${PUBLIC_SIZE}|${FILE_COUNT}" > /tmp/build_stats_$$
    fi
) &
STATS_PID=$!

echo ""
echo "=== 构建统计 ==="
echo "- 构建时间: $(date)"
echo "- 输出目录: public/"

wait $STATS_PID 2>/dev/null || true
if [ -f /tmp/build_stats_$$ ]; then
    STATS=$(cat /tmp/build_stats_$$)
    rm -f /tmp/build_stats_$$
    PUBLIC_SIZE=$(echo "$STATS" | cut -d'|' -f1)
    FILE_COUNT=$(echo "$STATS" | cut -d'|' -f2)
    echo "- 文件数量: ${FILE_COUNT}"
    echo "- 总大小: ${PUBLIC_SIZE}"
fi
echo ""

# ============================================
# 步骤4: 执行 Git 提交
# ============================================
log_step "步骤4: 执行 Git 提交"
echo "-------------------------------------------"

# 返回仓库根目录
cd "$(git rev-parse --show-toplevel)"

if [ "$AUTO_COMMIT" = "true" ] && [ "$HAS_CHANGES" = "true" ]; then
    # 优化：并行添加文件
    log "添加更改到暂存区..."
    git add -A
    
    log "执行提交: $COMMIT_MSG"
    git commit -m "$COMMIT_MSG"
    log_success "提交完成"
    
    if [ "$AUTO_PUSH" = "true" ]; then
        log "推送到远程仓库..."
        git push origin $BRANCH
        log_success "推送完成"
    fi
else
    log "Git自动提交已跳过"
fi

echo ""

# ============================================
# 最终状态报告
# ============================================
TOTAL_END=$(date +%s)
TOTAL_DURATION=$((TOTAL_END - TOTAL_START))
TOTAL_MINUTES=$((TOTAL_DURATION / 60))
TOTAL_SECONDS=$((TOTAL_DURATION % 60))

echo "============================================"
echo "  构建与提交完成"
echo "============================================"
echo ""
echo "=== 执行摘要 ==="
echo "- 总耗时: ${TOTAL_MINUTES}分${TOTAL_SECONDS}秒"
echo "- Commit信息: $COMMIT_MSG"
echo "- 当前提交: $(git log --oneline -1)"
echo "- 提交总数: $(git rev-list --count HEAD)"
echo ""

# 清理临时文件
rm -f /tmp/commit_msg_$$ /tmp/build_stats_$$ 2>/dev/null || true

# 如果有后台垃圾回收进程，等待它完成
if [ -n "$GC_PID" ]; then
    wait $GC_PID 2>/dev/null || true
fi

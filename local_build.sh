#!/bin/bash

# 优化版 Hexo 构建脚本
# 执行顺序：历史压缩 -> 生成commit信息 -> 打包 -> 提交

set -e  # 遇到错误立即退出

# 解决 SSL 证书问题
export NODE_TLS_REJECT_UNAUTHORIZED=0

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
TRUNCATE_GIT_HISTORY=${TRUNCATE_GIT_HISTORY:-true}
KEEP_COMMITS=3

# 全局变量
COMMIT_MSG=""
BRANCH=""

echo ""
echo "============================================"
echo "  Hexo 构建与自动提交脚本"
echo "============================================"
echo ""

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
        
        # 使用 orphan 分支重新创建历史
        git checkout --orphan new_main
        
        # 添加所有文件并提交
        git add -A
        git commit -m "构建压缩: 保留最近${KEEP_COMMITS}次提交 - $(date '+%Y-%m-%d %H:%M:%S')" || true
        
        # 删除旧分支并重命名新分支
        git branch -D "$BRANCH" 2>/dev/null || true
        git branch -m "$BRANCH"
        
        # 清理临时分支
        git branch -D new_main 2>/dev/null || true
        
        # 执行垃圾回收以释放空间
        log "执行Git垃圾回收..."
        git reflog expire --expire=now --all
        git gc --aggressive --prune=now
        
        NEW_COMMIT_COUNT=$(git rev-list --count HEAD)
        GIT_SIZE=$(du -sh .git | cut -f1)
        log_success "历史压缩完成: $COMMIT_COUNT -> $NEW_COMMIT_COUNT 次提交，.git目录: ${GIT_SIZE}"
    fi
else
    log "Git历史压缩已跳过 (设置 TRUNCATE_GIT_HISTORY=true 启用)"
fi

echo ""

# ============================================
# 步骤2: 生成 commit 信息（不执行提交）
# ============================================
log_step "步骤2: 生成 commit 信息"
echo "-------------------------------------------"

# 检查是否有更改
if git diff-index --quiet HEAD -- && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    log_warning "没有检测到更改"
    COMMIT_MSG="无更改 - $(date '+%Y-%m-%d %H:%M:%S')"
else
    log "检测到以下更改:"
    git status --short
    
    # 获取工作区的 diff（未暂存的更改）
    WORKING_DIFF=$(git diff --stat 2>/dev/null)
    STAGED_DIFF=$(git diff --staged --stat 2>/dev/null)
    ALL_DIFF="${WORKING_DIFF}${STAGED_DIFF}"
    
    # 使用 CodeBuddy 生成 commit 信息
    if command -v codebuddy &> /dev/null; then
        log "调用 CodeBuddy 生成 commit 信息..."
        COMMIT_MSG=$(echo "请根据以下 Git 更改生成一个简洁的中文 commit 信息（只返回 commit 信息本身，不要其他解释）：
$ALL_DIFF" | codebuddy -p 2>/dev/null || echo "")
        
        if [ -z "$COMMIT_MSG" ] || [ ${#COMMIT_MSG} -gt 200 ]; then
            log_warning "CodeBuddy 生成失败，使用默认格式"
            COMMIT_MSG="更新网站内容 - $(date '+%Y-%m-%d %H:%M:%S')"
        fi
    else
        log_warning "CodeBuddy 未安装，使用默认格式"
        COMMIT_MSG="更新网站内容 - $(date '+%Y-%m-%d %H:%M:%S')"
    fi
fi

log_success "Commit 信息已生成: $COMMIT_MSG"
echo ""

# ============================================
# 步骤3: 执行打包流程
# ============================================
log_step "步骤3: 执行打包流程"
echo "-------------------------------------------"

# 检查并进入 Hexo 目录
if [ ! -d "hexo/hexo" ]; then
    log_error "Hexo目录不存在: hexo/hexo"
    exit 1
fi

cd hexo/hexo
log "进入Hexo目录: $(pwd)"

# 智能依赖安装
log "检查依赖状态..."
if [ ! -d "node_modules" ] || [ "package.json" -nt "node_modules" ] || [ "yarn.lock" -nt "node_modules" ]; then
    log "检测到依赖需要更新，开始安装..."
    if yarn install --frozen-lockfile --silent --ignore-engines --ignore-optional --non-interactive 2>&1; then
        log_success "依赖安装完成"
    else
        log_error "依赖安装失败"
        exit 1
    fi
else
    log_success "依赖已是最新，跳过安装"
fi

# 智能清理策略
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

# 构建网站
log "开始构建Hexo网站..."
export NODE_ENV=production
export HEXO_GENERATE_CONCURRENCY=4

if node --max-old-space-size=4096 node_modules/.bin/hexo generate --draft --silent 2>&1; then
    log_success "Hexo构建完成"
else
    log_error "Hexo构建失败"
    exit 1
fi

# 检查构建结果
if [ -d "public" ]; then
    PUBLIC_SIZE=$(du -sh public | cut -f1)
    FILE_COUNT=$(find public -type f | wc -l)
    log_success "构建完成: ${PUBLIC_SIZE} 大小，${FILE_COUNT} 个文件"
else
    log_error "构建失败：public目录不存在"
    exit 1
fi

echo ""
echo "=== 构建统计 ==="
echo "- 构建时间: $(date)"
echo "- 输出目录: public/"
echo "- 文件数量: ${FILE_COUNT}"
echo "- 总大小: ${PUBLIC_SIZE}"
echo ""

# ============================================
# 步骤4: 执行 Git 提交
# ============================================
log_step "步骤4: 执行 Git 提交"
echo "-------------------------------------------"

# 返回仓库根目录
cd "$(git rev-parse --show-toplevel)"

if [ "$AUTO_COMMIT" = "true" ]; then
    # 检查是否有更改需要提交
    if git diff-index --quiet HEAD -- && [ -z "$(git ls-files --others --exclude-standard)" ]; then
        log_warning "没有检测到更改，跳过提交"
    else
        # 添加所有更改到暂存区
        log "添加更改到暂存区..."
        git add -A
        
        # 使用之前生成的 commit 信息执行提交
        log "执行提交: $COMMIT_MSG"
        git commit -m "$COMMIT_MSG"
        
        log_success "提交完成"
        
        # 可选：自动推送到远程
        if [ "$AUTO_PUSH" = "true" ]; then
            log "推送到远程仓库..."
            git push origin $BRANCH
            log_success "推送完成"
        fi
    fi
else
    log "Git自动提交已跳过 (设置 AUTO_COMMIT=true 启用)"
fi

echo ""

# ============================================
# 最终状态报告
# ============================================
echo "============================================"
echo "  构建与提交完成"
echo "============================================"
echo ""
echo "=== 执行摘要 ==="
echo "- 完成时间: $(date)"
echo "- Commit信息: $COMMIT_MSG"
echo "- 当前提交: $(git log --oneline -1)"
echo "- 提交总数: $(git rev-list --count HEAD)"
echo ""

#!/bin/bash

# 优化版 Hexo 构建脚本
# 执行顺序：清理历史 -> 生成commit -> Hexo构建 -> 推送public -> 推送源文件
#
# ![流程概览](https://picsum.photos/seed/hexo-build-deploy/800/400)

set -e  # 遇到错误立即退出

# 解决 SSL 证书问题
export NODE_TLS_REJECT_UNAUTHORIZED=0

# 日志函数（极简：步骤 / 状态 / 推送结果）
log()      { echo "[$(date +'%H:%M:%S')] $1"; }
log_sub()  { echo "[$(date +'%H:%M:%S')]    $1"; }
log_ok()   { echo "[$(date +'%H:%M:%S')]    OK $1"; }
log_warn() { echo "[$(date +'%H:%M:%S')]    ! $1"; }
log_err()  { echo "[$(date +'%H:%M:%S')]    FAILED $1" >&2; }

# 配置
AUTO_COMMIT=${AUTO_COMMIT:-true}
AUTO_PUSH=${AUTO_PUSH:-true}
TRUNCATE_GIT_HISTORY=${TRUNCATE_GIT_HISTORY:-false}
KEEP_COMMITS=3
COMMIT_MSG=""
BRANCH=""

# 步骤1: 清理历史
log "步骤1: 清理历史"
cd "$(git rev-parse --show-toplevel)"
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$TRUNCATE_GIT_HISTORY" = "true" ]; then
    COMMIT_COUNT=$(git rev-list --count HEAD)
    if [ "$COMMIT_COUNT" -le "$KEEP_COMMITS" ]; then
        log_sub "提交数 ${COMMIT_COUNT} 不超过 ${KEEP_COMMITS}，跳过"
    else
        git checkout --orphan new_main
        git add -A
        git commit -m "构建压缩: 保留最近${KEEP_COMMITS}次提交 - $(date '+%Y-%m-%d %H:%M:%S')" || true
        git branch -D "$BRANCH" 2>/dev/null || true
        git branch -m "$BRANCH"
        git branch -D new_main 2>/dev/null || true
        git reflog expire --expire=now --all
        git gc --aggressive --prune=now
        log_sub "压缩完成: $COMMIT_COUNT -> $KEEP_COMMITS"
    fi
else
    log_sub "已跳过 (TRUNCATE_GIT_HISTORY=false)"
fi

# 步骤2: 生成 commit 信息
log "步骤2: 生成 commit 信息"
if git diff-index --quiet HEAD -- && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    COMMIT_MSG="无更改 - $(date '+%Y-%m-%d %H:%M:%S')"
    log_warn "无变更"
else
    WORKING_DIFF=$(git diff --stat 2>/dev/null)
    STAGED_DIFF=$(git diff --staged --stat 2>/dev/null)
    ALL_DIFF="${WORKING_DIFF}${STAGED_DIFF}"

    if command -v codebuddy &> /dev/null; then
        COMMIT_MSG=$(echo "请根据以下 Git 更改生成一个简洁的中文 commit 信息（只返回 commit 信息本身，不要其他解释）：$ALL_DIFF" | codebuddy -p 2>/dev/null || echo "")
        if [ -z "$COMMIT_MSG" ] || [ ${#COMMIT_MSG} -gt 200 ]; then
            COMMIT_MSG="更新网站内容 - $(date '+%Y-%m-%d %H:%M:%S')"
            log_warn "codebuddy 失败，使用默认"
        fi
    else
        COMMIT_MSG="更新网站内容 - $(date '+%Y-%m-%d %H:%M:%S')"
    fi
    log_sub "$COMMIT_MSG"
fi

# 步骤3: Hexo 构建
log "步骤3: Hexo 构建"
if [ ! -d "hexo/hexo" ]; then
    log_err "Hexo 目录不存在"
    exit 1
fi
cd hexo/hexo

# 依赖
if [ ! -d "node_modules" ] || [ "package.json" -nt "node_modules" ] || [ "yarn.lock" -nt "node_modules" ]; then
    if yarn install --frozen-lockfile --silent --ignore-engines --ignore-optional --non-interactive 2>&1; then
        log_sub "依赖已安装"
    else
        log_err "依赖安装失败"
        exit 1
    fi
fi

# 清理策略
INCREMENTAL=${INCREMENTAL:-true}
if [ "$INCREMENTAL" != "true" ] || [ ! -d "public" ]; then
    if [ ! -d "public" ] || [ "db.json" -nt "public" ] || [ "_config.yml" -nt "public" ]; then
        yarn run clean 2>&1 || true
    fi
fi

# 构建
export NODE_ENV=production
export HEXO_GENERATE_CONCURRENCY=4
BUILD_CMD="node --max-old-space-size=8192 node_modules/hexo/bin/hexo generate --draft --silent"
if [ "$INCREMENTAL" = "true" ] && [ -d "public" ]; then
    BUILD_CMD="$BUILD_CMD --detect"
fi

if ! $BUILD_CMD 2>&1; then
    yarn run clean 2>&1 || true
    if ! node --max-old-space-size=8192 node_modules/hexo/bin/hexo generate --draft --silent 2>&1; then
        log_err "Hexo 构建失败"
        exit 1
    fi
fi

if [ -d "public" ]; then
    FILE_COUNT=$(find public -type f | wc -l)
    PUBLIC_SIZE=$(du -sh public | cut -f1)
    log_sub "${FILE_COUNT} 个文件, ${PUBLIC_SIZE}"
else
    log_err "public 目录未生成"
    exit 1
fi

# 步骤3.5: 推送 public/ 到 hexo-public
log "步骤3.5: 推送 public/ 到 hexo-public 仓库"
# ![推送 public/ 到 deploy 仓库](https://picsum.photos/seed/push-deploy-public/800/300)
ORIG_CWD="$(pwd)"
HEXO_PUBLIC_DIR="$ORIG_CWD/public"

if [ ! -d "$HEXO_PUBLIC_DIR" ]; then
    log_warn "public 目录不存在"
else
    pushd "$HEXO_PUBLIC_DIR" > /dev/null

    # 🛡️ 自动恢复 .git（hexo clean 会删除）
    if [ ! -d ".git" ]; then
        git init -b main > /dev/null 2>&1
        git remote add deploy https://atomgit.com/python4office/hexo-public.git 2>&1
        cat > .gitignore << 'GITIGNORE_EOF'
.DS_Store
Thumbs.db
*.swp
*.swo
*~
*.log
GITIGNORE_EOF
        git fetch deploy > /dev/null 2>&1
        git reset --hard deploy/main > /dev/null 2>&1
        log_sub ".git 已重建"
    fi

    if ! git remote get-url deploy &>/dev/null; then
        log_warn "deploy remote 不存在，跳过"
    else
        find . -type f -size 0 -delete 2>/dev/null || true
        git add -A

        if ! git diff-index --quiet HEAD --; then
            git commit -m "build: $(date '+%Y-%m-%d %H:%M:%S')" > /dev/null
        fi

        # 强制推送（本地是 single source of truth）
        if git push --force-with-lease deploy main 2>&1; then
            HASH=$(git rev-parse --short HEAD)
            log_ok "atomgit/hexo-public: ${HASH}"
        else
            log_err "atomgit/hexo-public 推送失败"
        fi
    fi

    popd > /dev/null
fi

# 步骤4: 推送主仓库
log "步骤4: 推送主仓库到 origin"
# ![推送源文件到主仓库](https://picsum.photos/seed/push-origin-main/800/300)
cd "$(git rev-parse --show-toplevel)"

if [ "$AUTO_COMMIT" = "true" ]; then
    if git diff-index --quiet HEAD -- && [ -z "$(git ls-files --others --exclude-standard)" ]; then
        log_warn "无变更，跳过"
    else
        git add -A
        git commit -m "$COMMIT_MSG" > /dev/null

        if [ "$AUTO_PUSH" = "true" ]; then
            if git push origin $BRANCH 2>&1; then
                HASH=$(git rev-parse --short HEAD)
                log_ok "atomgit/python4office.cn: ${HASH}"
            else
                log_err "atomgit/python4office.cn 推送失败"
            fi
        else
            log_warn "AUTO_PUSH=false，未推送"
        fi
    fi
else
    log_warn "AUTO_COMMIT=false，跳过"
fi

log "完成"

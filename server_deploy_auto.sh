#!/bin/bash

# Python4Office SCP 部署脚本 (自动输密码版)
# 流程：清理 → hexo 编译 → rsync 同步到服务器
#
# 第一次运行时会提示输入 SSH 密码，输入一次即可。
# 密码仅在当前进程中使用，不会写入文件。
#
# ![流程概览](https://picsum.photos/seed/hexo-build-scp-deploy-auto/800/400)

set -e  # 遇到错误立即退出

# ========== 服务器配置 ==========
SERVER_HOST="119.45.129.198"
SERVER_PORT="22"
SERVER_USER="root"
SERVER_PATH="/opt/website/opc-website/python4office.cn"

# ========== SSH 密钥配置（免密部署）==========
# 专用密钥（已生成，推到服务器后免密）
SERVER_KEY="$HOME/.ssh/server_python4office"

# 推公钥命令（首次部署前手动跑一次，输一次密码即可）：
#   ssh-copy-id -i $SERVER_KEY.pub -p $SERVER_PORT $SERVER_USER@$SERVER_HOST

# ========== 认证方式优先级 ===========
# 1. 专用密钥 SERVER_KEY（推荐，推公钥后完全免密）
# 2. 标准密钥（id_ed25519 / id_rsa / id_ecdsa，需已推公钥）
# 3. sshpass 手动输入密码（brew install sshpass）
# 4. SSHPASS 环境变量
# 5. SSH 弹框（兜底）

# ========== 日志函数 ==========
log()      { echo "[$(date +'%H:%M:%S')] $1"; }
log_sub()  { echo "[$(date +'%H:%M:%S')]    $1"; }
log_ok()   { echo "[$(date +'%H:%M:%S')]    OK $1"; }
log_warn() { echo "[$(date +'%H:%M:%S')]    ! $1"; }
log_err()  { echo "[$(date +'%H:%M:%S')]    FAILED $1" >&2; }

# ========== 0. 准备认证 ==========
log "步骤 0: 准备 SSH 认证"

# 检测 SSH 密钥（优先用 SERVER_KEY）
SSH_KEY=""
if [ -f "$SERVER_KEY" ]; then
    SSH_KEY="$SERVER_KEY"
else
    for k in "$HOME/.ssh/id_ed25519" "$HOME/.ssh/id_rsa" "$HOME/.ssh/id_ecdsa"; do
        if [ -f "$k" ]; then
            SSH_KEY="$k"
            break
        fi
    done
fi

# 决定认证模式
if [ -n "$SSH_KEY" ] && ssh -p $SERVER_PORT -i "$SSH_KEY" \
        -o BatchMode=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null \
        -o ConnectTimeout=5 $SERVER_USER@$SERVER_HOST 'echo ok' 2>/dev/null | grep -q ok; then
    log_ok "使用 SSH 密钥: $SSH_KEY"
    USE_KEY=true
    USE_SSHPASS=false
else
    USE_KEY=false
    if [ -n "$SSHPASS" ]; then
        log_sub "从 SSHPASS 环境变量读取密码"
        USE_SSHPASS=true
    elif command -v sshpass &>/dev/null; then
        echo -n "请输入 SSH 密码（输入隐藏）: "
        read -s SSHPASS
        echo
        if [ -z "$SSHPASS" ]; then
            log_err "密码不能为空"
            exit 1
        fi
        USE_SSHPASS=true
    else
        log_warn "sshpass 未安装，将由 SSH 自己弹密码框（可能弹多次）"
        log_warn "推荐：brew install sshpass"
        USE_SSHPASS=false
    fi
fi

# 包装命令前缀
if [ "$USE_SSHPASS" = "true" ]; then
    SSH_PREFIX="sshpass -e"
    log_ok "认证: sshpass（一次输入，全程免弹）"
elif [ "$USE_KEY" = "true" ]; then
    SSH_PREFIX=""
    log_ok "认证: SSH 密钥"
else
    SSH_PREFIX=""
    log_warn "认证: SSH 弹框（可能需要多次输入）"
fi

# 公共 SSH 选项
SSH_BASE_OPTS=(
    -p "$SERVER_PORT"
    -o "StrictHostKeyChecking=no"
    -o "UserKnownHostsFile=/dev/null"
    -o "ConnectTimeout=10"
)
if [ "$USE_KEY" = "true" ]; then
    SSH_BASE_OPTS+=(-i "$SSH_KEY")
fi

# 包装函数
_ssh() {
    if [ "$USE_SSHPASS" = "true" ]; then
        sshpass -e ssh "${SSH_BASE_OPTS[@]}" "$@"
    else
        ssh "${SSH_BASE_OPTS[@]}" "$@"
    fi
}

_rsync() {
    if [ "$USE_SSHPASS" = "true" ]; then
        # rsync 的 -e 参数是远程 shell 命令，直接用 sshpass -e ssh
        sshpass -e rsync -avz --delete --progress --human-readable \
            --exclude='.DS_Store' --exclude='*.log' --exclude='.git' --exclude='Thumbs.db' \
            -e "ssh ${SSH_BASE_OPTS[*]}" \
            "$@"
    else
        rsync -avz --delete --progress --human-readable \
            --exclude='.DS_Store' --exclude='*.log' --exclude='.git' --exclude='Thumbs.db' \
            -e "ssh ${SSH_BASE_OPTS[*]}" \
            "$@"
    fi
}

# ========== 1. Hexo 编译 ==========
log "步骤 1: Hexo 编译"
cd "$(git rev-parse --show-toplevel)"

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

# 构建
export NODE_ENV=production
export HEXO_GENERATE_CONCURRENCY=4
if ! node --max-old-space-size=8192 node_modules/hexo/bin/hexo generate --draft --silent 2>&1; then
    log_err "Hexo 构建失败"
    exit 1
fi

if [ -d "public" ]; then
    FILE_COUNT=$(find public -type f | wc -l)
    PUBLIC_SIZE=$(du -sh public | cut -f1)
    ZERO_FILES=$(find public -type f -size 0 | wc -l)
    log_sub "${FILE_COUNT} 个文件, ${PUBLIC_SIZE}${ZERO_FILES:+, ${ZERO_FILES} 个 0 字节}"
    if [ "$ZERO_FILES" -gt 0 ]; then
        log_warn "本地有 ${ZERO_FILES} 个 0 字节文件，删除后上传"
        find public -type f -size 0 -delete
    fi
else
    log_err "public 目录未生成"
    exit 1
fi

# ========== 2. 准备 SSH ==========
log "步骤 2: 准备 SSH 连接"

SSH_TARGET="${SERVER_USER}@${SERVER_HOST}"

# 测试连接
log_sub "测试连接"
if ! _ssh "$SSH_TARGET" "echo connected" 2>&1 | grep -q "connected"; then
    log_err "SSH 连接失败"
    exit 1
fi
log_ok "SSH 连接成功"

# 确保服务器端目录存在
log_sub "确保服务器目录存在: $SERVER_PATH"
_ssh "$SSH_TARGET" "mkdir -p '$SERVER_PATH'"

# ========== 3. rsync 同步 ==========
log "步骤 3: rsync 同步 public/ → ${SSH_TARGET}:${SERVER_PATH}/"

if _rsync public/ "${SSH_TARGET}:${SERVER_PATH}/" 2>&1 | tail -10; then
    log_ok "rsync 同步完成"
else
    log_err "rsync 失败"
    exit 1
fi

# ========== 4. 服务器端清理 + 统计 ==========
log "步骤 4: 服务器端清理 + 统计"

REMOTE_DELETED=$(_ssh "$SSH_TARGET" \
    "find '$SERVER_PATH' -type f -size 0 -delete -print | wc -l" 2>/dev/null | tr -d ' ')
if [ -n "$REMOTE_DELETED" ] && [ "$REMOTE_DELETED" -gt 0 ]; then
    log_sub "清理服务器端 ${REMOTE_DELETED} 个 0 字节文件"
fi

REMOTE_COUNT=$(_ssh "$SSH_TARGET" \
    "find '$SERVER_PATH' -type f | wc -l" 2>/dev/null | tr -d ' ')
REMOTE_DIRS=$(_ssh "$SSH_TARGET" \
    "find '$SERVER_PATH' -mindepth 1 -type d | wc -l" 2>/dev/null | tr -d ' ')
log_ok "服务器端: ${REMOTE_COUNT} 个文件, ${REMOTE_DIRS} 个子目录"
log_ok "https://python4office.cn/* → ${SERVER_PATH}"

# 清理敏感变量
unset SSHPASS

log "完成"

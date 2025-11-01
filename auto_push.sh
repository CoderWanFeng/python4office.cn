#!/bin/bash

# 自动打包、提交和推送脚本（详细状态版）
# 根据最近修改的文件生成智能的commit信息

# 参数处理
BUILD_HEXO=false
QUIET=false
VERBOSE=false

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        --build-hexo|-b)
            BUILD_HEXO=true
            shift
            ;;
        --quiet|-q)
            QUIET=true
            shift
            ;;
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        --help|-h)
            echo "用法: $0 [选项]"
            echo "选项:"
            echo "  -b, --build-hexo    构建Hexo网站"
            echo "  -q, --quiet         静默模式，减少输出"
            echo "  -v, --verbose       详细模式，显示所有操作步骤和状态"
            echo "  -h, --help         显示帮助信息"
            exit 0
            ;;
        *)
            echo "未知参数: $1"
            echo "使用 --help 查看帮助信息"
            exit 1
            ;;
    esac
done

# 颜色定义（如果支持）
if [ -t 1 ] && command -v tput >/dev/null 2>&1; then
    RED=$(tput setaf 1)
    GREEN=$(tput setaf 2)
    YELLOW=$(tput setaf 3)
    BLUE=$(tput setaf 4)
    MAGENTA=$(tput setaf 5)
    CYAN=$(tput setaf 6)
    BOLD=$(tput bold)
    RESET=$(tput sgr0)
else
    RED=""
    GREEN=""
    YELLOW=""
    BLUE=""
    MAGENTA=""
    CYAN=""
    BOLD=""
    RESET=""
fi

# 输出控制函数
log() { 
    if ! $QUIET; then
        echo "$@"
    fi
}

# 详细日志函数
log_verbose() {
    if $VERBOSE; then
        echo "${CYAN}[详细]${RESET} $@"
    fi
}

# 状态检查函数
check_status() {
    local step_name="$1"
    local exit_code=$2
    local error_message="$3"
    
    if [ $exit_code -eq 0 ]; then
        echo "${GREEN}✓${RESET} ${BOLD}$step_name${RESET} - 成功"
        return 0
    else
        echo "${RED}✗${RESET} ${BOLD}$step_name${RESET} - 失败"
        if [ -n "$error_message" ]; then
            echo "  ${RED}错误信息: $error_message${RESET}"
        fi
        return 1
    fi
}

# 步骤开始函数
step_start() {
    local step_name="$1"
    echo "${BLUE}▶${RESET} ${BOLD}$step_name${RESET}..."
}

# 错误处理函数
handle_error() {
    local step_name="$1"
    local exit_code=$2
    local error_message="$3"
    
    echo "${RED}❌ 错误: $step_name 执行失败${RESET}"
    echo "${RED}退出码: $exit_code${RESET}"
    if [ -n "$error_message" ]; then
        echo "${RED}错误详情: $error_message${RESET}"
    fi
    echo "${YELLOW}请检查相关配置后重试${RESET}"
    exit $exit_code
}

echo
echo
echo "${MAGENTA}${BOLD}=== 开始自动打包和推送流程 ===${RESET}"

# 1. Hexo构建优化（并行执行）
if [ "$BUILD_HEXO" = true ]; then
    echo
    echo "${MAGENTA}${BOLD}=== 构建Hexo网站 ===${RESET}"
    
    step_start "检查Hexo目录"
    if [ ! -d "hexo/hexo" ]; then
        handle_error "Hexo目录检查" 1 "hexo/hexo 目录不存在"
    fi
    cd hexo/hexo
    check_status "Hexo目录检查" 0
    
    # 检查是否需要重新安装依赖（避免重复安装）
    step_start "检查依赖状态"
    if [ ! -d "node_modules" ] || [ "package.json" -nt "node_modules" ]; then
        log_verbose "需要重新安装依赖"
        step_start "安装依赖"
        if yarn install --silent 2>&1; then
            check_status "依赖安装" 0
        else
            handle_error "依赖安装" $? "yarn install 执行失败"
        fi
    else
        log_verbose "依赖已存在，跳过安装"
        check_status "依赖检查" 0 "依赖已存在"
    fi
    
    # 并行执行清理和构建
    step_start "清理Hexo缓存"
    HEXO_CLEAN_RESULT=$(yarn run clean 2>&1)
    HEXO_CLEAN_EXIT=$?
    if [ $HEXO_CLEAN_EXIT -eq 0 ]; then
        check_status "Hexo清理" 0
        if [ -n "$HEXO_CLEAN_RESULT" ]; then
            log_verbose "Hexo清理输出: $HEXO_CLEAN_RESULT"
        fi
    else
        handle_error "Hexo清理" $HEXO_CLEAN_EXIT "$HEXO_CLEAN_RESULT"
    fi
    
    step_start "构建Hexo网站"
    HEXO_BUILD_RESULT=$(yarn run build 2>&1)
    HEXO_BUILD_EXIT=$?
    if [ $HEXO_BUILD_EXIT -eq 0 ]; then
        check_status "Hexo构建" 0
        if [ -n "$HEXO_BUILD_RESULT" ]; then
            log_verbose "Hexo构建输出: $HEXO_BUILD_RESULT"
        fi
    else
        handle_error "Hexo构建" $HEXO_BUILD_EXIT "$HEXO_BUILD_RESULT"
    fi
    
    cd ../..
    echo "${GREEN}✓ Hexo构建流程完成${RESET}"
fi

# 2. Git状态检查
echo
echo "${MAGENTA}${BOLD}=== Git操作流程 ===${RESET}"

step_start "检查Git仓库状态"
if git diff-index --quiet HEAD -- 2>/dev/null && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    echo "${YELLOW}⚠ 无文件变更，跳过提交${RESET}"
    exit 0
fi
check_status "Git仓库状态检查" 0

# 3. 获取文件变更信息
step_start "分析文件变更"
MODIFIED_FILES=$(git diff --name-only HEAD 2>/dev/null || echo "")
UNTRACKED_FILES=$(git ls-files --others --exclude-standard 2>/dev/null || echo "")

MODIFIED_COUNT=$(echo "$MODIFIED_FILES" | wc -l)
UNTRACKED_COUNT=$(echo "$UNTRACKED_FILES" | wc -l)

if [ -n "$MODIFIED_FILES" ]; then
    log_verbose "修改的文件: $MODIFIED_COUNT 个"
fi
if [ -n "$UNTRACKED_FILES" ]; then
    log_verbose "新增的文件: $UNTRACKED_COUNT 个"
fi
check_status "文件变更分析" 0 "修改: $MODIFIED_COUNT, 新增: $UNTRACKED_COUNT"

# 4. 生成智能commit信息
step_start "生成commit信息"
COMMIT_MSG="更新网站"

# 使用更高效的模式匹配
if [[ "$MODIFIED_FILES" =~ \.md$ ]]; then
    COMMIT_MSG="更新博客文章"
elif [[ "$MODIFIED_FILES" =~ \.(yml|yaml)$ ]]; then
    COMMIT_MSG="更新配置文件"
elif [[ "$MODIFIED_FILES" =~ \.(js|css)$ ]]; then
    COMMIT_MSG="更新网站代码"
fi

# 如果有Hexo相关的修改
if [[ "$MODIFIED_FILES$UNTRACKED_FILES" =~ hexo/ ]]; then
    COMMIT_MSG="更新博客内容"
fi

log_verbose "生成的commit信息: $COMMIT_MSG"
check_status "commit信息生成" 0 "$COMMIT_MSG"

# 5. 批量Git操作
step_start "添加文件到暂存区"
if git add . 2>&1; then
    check_status "文件添加" 0
else
    handle_error "文件添加" $? "git add 执行失败"
fi

step_start "提交变更"
if git commit -m "$COMMIT_MSG" 2>&1; then
    check_status "提交变更" 0
else
    handle_error "提交变更" $? "git commit 执行失败"
fi

step_start "推送到远程仓库"
if git push 2>&1; then
    check_status "推送操作" 0
else
    handle_error "推送操作" $? "git push 执行失败"
fi

echo "${GREEN}✓ Git操作流程完成${RESET}"

# 6. 远程操作优化（条件执行和并行处理）
if [ "$BUILD_HEXO" = true ]; then
    echo
    echo "${MAGENTA}${BOLD}=== 远程部署流程 ===${RESET}"
    
    # 从环境变量获取服务器信息
    LINUX_IP=$linux_ip
    LINUX_USER=$linux_user
    LINUX_PWD=$linux_pwd
    LINUX_P4O=$linux_p4o
    
    # 检查环境变量是否设置
    step_start "检查远程服务器配置"
    if [ -z "$LINUX_IP" ] || [ -z "$LINUX_USER" ] || [ -z "$LINUX_PWD" ] || [ -z "$LINUX_P4O" ]; then
        echo "${YELLOW}⚠ 缺少远程服务器环境变量，跳过远程操作${RESET}"
        echo "${YELLOW}需要设置: linux_ip, linux_user, linux_pwd, linux_p4o${RESET}"
    else
        check_status "服务器配置检查" 0 "IP: $LINUX_IP, 用户: $LINUX_USER"
        
        # 并行执行远程操作和CDN刷新
        step_start "启动远程部署任务"
        
        # 远程服务器操作
        (
            step_start "建立SSH连接"
            SSH_RESULT=""
            SSH_ERROR=""
            
            if command -v sshpass >/dev/null 2>&1; then
                # Linux系统：使用sshpass（最快）
                log_verbose "使用sshpass进行SSH连接"
                SSH_RESULT=$(sshpass -p "$LINUX_PWD" ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no \
                    $LINUX_USER@$LINUX_IP "cd '$LINUX_P4O' && sh ngnix.sh" 2>&1)
                SSH_EXIT=$?
            elif command -v powershell >/dev/null 2>&1; then
                # Windows系统：优化PowerShell调用
                log_verbose "使用PowerShell进行SSH连接"
                SSH_RESULT=$(powershell -Command "
                    \$ErrorActionPreference = 'SilentlyContinue'
                    try {
                        # 直接使用标准ssh命令，避免复杂的PowerShell模块
                        \$process = Start-Process -NoNewWindow -PassThru -Wait ssh -ArgumentList @('-o', 'ConnectTimeout=10', '-o', 'StrictHostKeyChecking=no', \"$LINUX_USER@$LINUX_IP\", \"cd '$LINUX_P4O' && sh ngnix.sh\") -WindowStyle Hidden
                        exit \$process.ExitCode
                    } catch {
                        Write-Error 'PowerShell SSH连接失败'
                        exit 1
                    }
                " 2>&1)
                SSH_EXIT=$?
            else
                # 使用标准ssh（需要密钥认证）
                log_verbose "使用标准SSH连接"
                SSH_RESULT=$(ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no \
                    $LINUX_USER@$LINUX_IP "cd '$LINUX_P4O' && sh ngnix.sh" 2>&1)
                SSH_EXIT=$?
            fi
            
            if [ $SSH_EXIT -eq 0 ]; then
                check_status "SSH连接" 0
                step_start "执行远程部署脚本"
                if [ -n "$SSH_RESULT" ]; then
                    log_verbose "远程脚本输出: $SSH_RESULT"
                fi
                check_status "远程部署" 0 "$SSH_RESULT"
            else
                handle_error "SSH连接" $SSH_EXIT "$SSH_RESULT"
            fi
        ) &
        
        REMOTE_PID=$!
        
        # CDN刷新操作
        (
            step_start "检查CDN刷新脚本"
            if [ ! -f "refresh_cdn.py" ]; then
                echo "${YELLOW}⚠ CDN刷新脚本不存在，跳过CDN刷新${RESET}"
            else
                check_status "CDN脚本检查" 0
                step_start "执行CDN缓存刷新"
                CDN_RESULT=$(python refresh_cdn.py 2>&1)
                CDN_EXIT=$?
                if [ $CDN_EXIT -eq 0 ]; then
                    check_status "CDN刷新" 0 "$CDN_RESULT"
                else
                    handle_error "CDN刷新" $CDN_EXIT "$CDN_RESULT"
                fi
            fi
        ) &
        
        CDN_PID=$!
        
        # 等待所有后台任务完成
        step_start "等待并行任务完成"
        wait $REMOTE_PID $CDN_PID 2>/dev/null
        REMOTE_EXIT=$?
        CDN_EXIT=$?
        
        if [ $REMOTE_EXIT -eq 0 ] && [ $CDN_EXIT -eq 0 ]; then
            check_status "并行任务" 0 "所有任务执行完成"
        else
            if [ $REMOTE_EXIT -ne 0 ]; then
                echo "${RED}✗ 远程部署任务失败${RESET}"
            fi
            if [ $CDN_EXIT -ne 0 ]; then
                echo "${RED}✗ CDN刷新任务失败${RESET}"
            fi
        fi
    fi
fi

echo
echo "${GREEN}${BOLD}=== 流程完成 ===${RESET}"
echo "${GREEN}✓ 自动打包、提交和推送完成！${RESET}"


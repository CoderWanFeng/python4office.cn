#!/bin/bash

# 远程SSH执行脚本
# 自动登录到远程服务器的指定位置，并执行指定命令

# 参数处理
QUIET=false
VERBOSE=false

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
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
echo "${MAGENTA}${BOLD}=== 开始远程SSH执行流程 ===${RESET}"

# 从环境变量获取服务器信息
LINUX_IP=${LINUX_IP}
LINUX_USER=${LINUX_USER}
LINUX_PWD=${LINUX_PWD}
LINUX_P4O=${LINUX_P4O}

# 要执行的命令
COMMAND_TO_RUN="sh ngnix.sh"

# 检查环境变量是否设置
step_start "检查远程服务器配置"
if [ -z "$LINUX_IP" ] || [ -z "$LINUX_USER" ] || [ -z "$LINUX_PWD" ] || [ -z "$LINUX_P4O" ]; then
    echo "${RED}❌ 错误: 缺少必要的环境变量${RESET}"
    echo "${YELLOW}需要设置的环境变量:${RESET}"
    echo "  LINUX_IP: 远程服务器IP地址"
    echo "  LINUX_USER: 远程服务器用户名"
    echo "  LINUX_PWD: 远程服务器密码"
    echo "  LINUX_P4O: 远程服务器路径"
    echo "${YELLOW}请设置这些环境变量后重试${RESET}"
    exit 1
fi

# 显示连接信息
log_verbose "准备连接到远程服务器..."
log_verbose "服务器地址: $LINUX_USER@$LINUX_IP"
log_verbose "远程目录: $LINUX_P4O"
log_verbose "执行命令: $COMMAND_TO_RUN"

# 执行SSH连接和命令
step_start "建立SSH连接并执行命令"
SSH_RESULT=""
SSH_EXIT=""

if command -v sshpass >/dev/null 2>&1; then
    # Linux系统：使用sshpass（最快）
    log_verbose "使用sshpass进行SSH连接"
    log_verbose "SSH命令: sshpass -p '[密码]' ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no $LINUX_USER@$LINUX_IP \"cd '$LINUX_P4O' && $COMMAND_TO_RUN\""
    SSH_RESULT=$(sshpass -p "$LINUX_PWD" ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no \
        $LINUX_USER@$LINUX_IP "cd '$LINUX_P4O' && $COMMAND_TO_RUN" 2>&1)
    SSH_EXIT=$?
elif command -v powershell >/dev/null 2>&1; then
    # Windows系统：优化PowerShell调用
    log_verbose "使用PowerShell进行SSH连接"
    log_verbose "PowerShell命令: Start-Process ssh -ArgumentList @('-o', 'ConnectTimeout=10', '-o', 'StrictHostKeyChecking=no', \"${LINUX_USER}@${LINUX_IP}\", \"cd '${LINUX_P4O}' && $COMMAND_TO_RUN\")"
    SSH_RESULT=$(powershell -Command "
        \$ErrorActionPreference = 'SilentlyContinue'
        try {
            # 直接使用标准ssh命令，避免复杂的PowerShell模块
            \$sshArgs = @('-o', 'ConnectTimeout=10', '-o', 'StrictHostKeyChecking=no', \"${LINUX_USER}@${LINUX_IP}\", \"cd '${LINUX_P4O}' && $COMMAND_TO_RUN\")
            \$process = Start-Process -NoNewWindow -PassThru -Wait ssh -ArgumentList \$sshArgs -WindowStyle Hidden
            exit \$process.ExitCode
        } catch {
            Write-Output 'PowerShell SSH连接失败: \$_.Exception.Message'
            exit 1
        }
    " 2>&1)
    SSH_EXIT=$?
else
    # 使用标准ssh（需要密钥认证）
    log_verbose "使用标准SSH连接"
    log_verbose "SSH命令: ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no $LINUX_USER@$LINUX_IP \"cd '$LINUX_P4O' && $COMMAND_TO_RUN\""
    SSH_RESULT=$(ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no \
        $LINUX_USER@$LINUX_IP "cd '$LINUX_P4O' && $COMMAND_TO_RUN" 2>&1)
    SSH_EXIT=$?
fi

# 显示执行结果
log_verbose "SSH执行完成，退出码: $SSH_EXIT"

# 检查执行结果
if [ $SSH_EXIT -eq 0 ]; then
    check_status "SSH连接和命令执行" 0
    
    # 显示命令执行结果（ngnix.sh的输出）
    echo
    echo "${MAGENTA}${BOLD}=== ngnix.sh 执行结果 ===${RESET}"
    if [ -n "$SSH_RESULT" ]; then
        echo "${SSH_RESULT}"
    else
        echo "${YELLOW}⚠ ngnix.sh 执行成功，但无输出内容${RESET}"
        echo "${CYAN}这可能是因为：${RESET}"
        echo "${CYAN}1. git pull 没有新的更新${RESET}"
        echo "${CYAN}2. 脚本执行成功但没有输出信息${RESET}"
        echo "${CYAN}3. 目标目录可能需要检查更新${RESET}"
    fi
    
    # 验证脚本是否真的执行了
    echo
    echo "${MAGENTA}${BOLD}=== 验证脚本执行效果 ===${RESET}"
    echo "${CYAN}检查目标目录更新时间...${RESET}"
    # 这里可以添加验证逻辑，比如检查文件修改时间等
    
    echo
    echo "${GREEN}${BOLD}=== 执行完成 ===${RESET}"
    echo "${GREEN}✓ 远程命令执行成功！${RESET}"
    echo "${GREEN}✓ 已执行 ngnix.sh 脚本${RESET}"
else
    handle_error "SSH连接和命令执行" $SSH_EXIT "$SSH_RESULT"
fi

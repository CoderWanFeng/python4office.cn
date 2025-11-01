#!/bin/bash

# 自动Git提交、推送和远程部署脚本（详细状态版）
# 根据最近修改的文件生成智能的commit信息，并执行远程部署

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
echo "${MAGENTA}${BOLD}=== 开始自动Git提交和推送流程 ===${RESET}"

# 1. Git状态检查
echo
echo "${MAGENTA}${BOLD}=== Git操作流程 ===${RESET}"

step_start "检查Git仓库状态"
if git diff-index --quiet HEAD -- 2>/dev/null && [ -z "$(git ls-files --others --exclude-standard 2>/dev/null)" ]; then
    echo "${YELLOW}⚠ 无文件变更，跳过提交${RESET}"
    exit 0
fi
check_status "Git仓库状态检查" 0

# 3. 获取文件变更信息
step_start "分析文件变更"
MODIFIED_FILES=$(git diff --name-only HEAD 2>/dev/null || echo "")
UNTRACKED_FILES=$(git ls-files --others --exclude-standard 2>/dev/null || echo "")

# 修复：正确计算文件行数，处理空输入情况
MODIFIED_COUNT=$(echo "$MODIFIED_FILES" | grep -c . || echo "0")
UNTRACKED_COUNT=$(echo "$UNTRACKED_FILES" | grep -c . || echo "0")

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


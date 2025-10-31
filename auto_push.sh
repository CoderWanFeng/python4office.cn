#!/bin/bash

# 自动打包、提交和推送脚本（优化修复版）
# 根据最近修改的文件生成智能的commit信息

# 参数处理
BUILD_HEXO=false
QUIET=false

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
        --help|-h)
            echo "用法: $0 [选项]"
            echo "选项:"
            echo "  -b, --build-hexo    构建Hexo网站"
            echo "  -q, --quiet         静默模式，减少输出"
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

# 输出控制函数
log() { $QUIET || echo "$@"; }

log "=== 开始自动打包和推送流程 ==="

# 1. Hexo构建优化（修复并行执行问题）
if [ "$BUILD_HEXO" = true ]; then
    log "\n=== 构建Hexo网站 ==="
    cd hexo/hexo || { log "错误: 无法进入hexo目录"; exit 1; }
    
    # 检查是否需要重新安装依赖（避免重复安装）
    if [ ! -d "node_modules" ] || [ "package.json" -nt "node_modules" ]; then
        log "安装依赖..."
        yarn install --silent || { log "错误: 依赖安装失败"; exit 1; }
    else
        log "依赖已存在，跳过安装"
    fi
    
    # 修复并行执行问题：先清理再构建
    log "清理..."
    yarn run clean --silent || { log "警告: 清理失败，继续构建"; }
    
    log "构建..."
    yarn run build --silent || { log "错误: Hexo构建失败"; exit 1; }
    
    log "Hexo构建完成！"
    cd ../.. || { log "错误: 无法返回上级目录"; exit 1; }
fi

# 2. 快速Git状态检查（避免不必要的git status输出）
log "\n=== 检查Git状态 ==="
if git diff-index --quiet HEAD -- 2>/dev/null && [ -z "$(git ls-files --others --exclude-standard 2>/dev/null)" ]; then
    log "无文件变更，跳过提交"
    exit 0
fi

# 3. 获取文件变更信息（优化版）
MODIFIED_FILES=$(git diff --name-only HEAD 2>/dev/null || echo "")
UNTRACKED_FILES=$(git ls-files --others --exclude-standard 2>/dev/null || echo "")

if [ -n "$MODIFIED_FILES" ]; then
    log "修改的文件数量: $(echo "$MODIFIED_FILES" | wc -l)"
fi

if [ -n "$UNTRACKED_FILES" ]; then
    log "新增的文件数量: $(echo "$UNTRACKED_FILES" | wc -l)"
fi

# 4. 生成智能commit信息（优化版）
log "\n=== 生成commit信息 ==="
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

log "生成的commit信息: $COMMIT_MSG"

# 5. 批量Git操作（减少命令调用）
log "\n=== 执行Git操作 ==="
git add . >/dev/null 2>&1 || { log "错误: git add失败"; exit 1; }
git commit -m "$COMMIT_MSG" >/dev/null 2>&1 || { log "错误: git commit失败"; exit 1; }
git push >/dev/null 2>&1 || { log "错误: git push失败"; exit 1; }

log "Git操作完成"

# 6. 远程操作优化（修复并行处理和错误处理）
if [ "$BUILD_HEXO" = true ]; then
    log "\n=== 执行远程部署 ==="
    
    # 从环境变量获取服务器信息
    LINUX_IP=$linux_ip
    LINUX_USER=$linux_user
    LINUX_PWD=$linux_pwd
    LINUX_P4O=$linux_p4o
    
    # 检查环境变量是否设置
    if [ -z "$LINUX_IP" ] || [ -z "$LINUX_USER" ] || [ -z "$LINUX_PWD" ] || [ -z "$LINUX_P4O" ]; then
        log "警告：缺少远程服务器环境变量，跳过远程操作"
    else
        # 修复并行处理：使用更稳定的方式
        remote_operation() {
            # SSH远程操作（优化连接）
            if command -v sshpass >/dev/null 2>&1; then
                # Linux系统：使用sshpass（最快）
                sshpass -p "$LINUX_PWD" ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no \
                    $LINUX_USER@$LINUX_IP "cd '$LINUX_P4O' && sh ngnix.sh" 2>/dev/null && \
                    log "远程服务器操作完成" || log "远程服务器操作失败"
            elif command -v powershell >/dev/null 2>&1; then
                # Windows系统：优化PowerShell调用
                powershell -Command "
                    \$ErrorActionPreference = 'SilentlyContinue'
                    try {
                        Import-Module Posh-SSH -ErrorAction Stop
                        \$cred = New-Object System.Management.Automation.PSCredential('$LINUX_USER', (ConvertTo-SecureString '$LINUX_PWD' -AsPlainText -Force))
                        \$session = New-SSHSession -ComputerName '$LINUX_IP' -Credential \$cred -AcceptKey \$true -ConnectionTimeout 10
                        if (\$session.Connected) {
                            Invoke-SSHCommand -SessionId \$session.SessionId -Command 'cd \"$LINUX_P4O\" && sh ngnix.sh' | Out-Null
                            Remove-SSHSession -SessionId \$session.SessionId | Out-Null
                            Write-Host '远程服务器操作完成'
                        } else {
                            Write-Host 'SSH连接失败'
                        }
                    } catch {
                        Write-Host 'PowerShell SSH模块未安装或连接失败'
                    }
                " 2>/dev/null
            else
                log "警告：未找到合适的SSH工具"
            fi
        }
        
        cdn_refresh() {
            python refresh_cdn.py >/dev/null 2>&1 && \
            log "CDN缓存刷新完成" || log "CDN缓存刷新失败"
        }
        
        # 并行执行
        remote_operation &
        REMOTE_PID=$!
        
        cdn_refresh &
        CDN_PID=$!
        
        # 等待所有后台任务完成
        wait $REMOTE_PID $CDN_PID
    fi
fi

log "\n=== 流程完成 ==="
log "自动打包、提交和推送完成！"


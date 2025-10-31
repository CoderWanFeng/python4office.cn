#!/bin/bash

# 自动打包、提交和推送脚本
# 根据最近修改的文件生成智能的commit信息

# 参数处理
BUILD_HEXO=false

# 解析命令行参数
while [[ $# -gt 0 ]]; do
    case $1 in
        --build-hexo|-b)
            BUILD_HEXO=true
            shift
            ;;
        --help|-h)
            echo "用法: $0 [选项]"
            echo "选项:"
            echo "  -b, --build-hexo    构建Hexo网站"
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

echo "=== 开始自动打包和推送流程 ==="

# 可选：构建Hexo网站
if [ "$BUILD_HEXO" = true ]; then
    echo "\n=== 构建Hexo网站 ==="
    cd hexo/hexo
    yarn install
    yarn run clean
    yarn run build
    echo "Hexo构建完成！"
    cd ../..
fi

# 1. 检查git状态
echo "检查git状态..."
git status

# 2. 获取最近修改的文件列表
echo "\n=== 分析最近修改的文件 ==="
MODIFIED_FILES=$(git diff --name-only HEAD)
UNTRACKED_FILES=$(git ls-files --others --exclude-standard)

if [ -n "$MODIFIED_FILES" ]; then
    echo "修改的文件:"
    echo "$MODIFIED_FILES"
fi

if [ -n "$UNTRACKED_FILES" ]; then
    echo "新增的文件:"
    echo "$UNTRACKED_FILES"
fi

# 3. 生成智能commit信息
echo "\n=== 生成commit信息 ==="
COMMIT_MSG="更新网站"

# 根据文件类型生成更具体的commit信息
if echo "$MODIFIED_FILES" | grep -q "\.md$"; then
    COMMIT_MSG="更新博客文章"
elif echo "$MODIFIED_FILES" | grep -q "\.yml$"; then
    COMMIT_MSG="更新配置文件"
elif echo "$MODIFIED_FILES" | grep -q "\.js$" || echo "$MODIFIED_FILES" | grep -q "\.css$"; then
    COMMIT_MSG="更新网站代码"
fi

# 如果有Hexo相关的修改，说明是博客更新
if echo "$MODIFIED_FILES" | grep -q "hexo/" || echo "$UNTRACKED_FILES" | grep -q "hexo/"; then
    COMMIT_MSG="更新博客内容"
fi

echo "生成的commit信息: $COMMIT_MSG"

# 4. 添加所有文件到git
echo "\n=== 添加文件到git ==="
git add .

# 5. 提交更改
echo "\n=== 提交更改 ==="
git commit -m "$COMMIT_MSG"

# 6. 推送更改
echo "\n=== 推送更改到远程仓库 ==="
git push

# 7. 如果构建了Hexo，执行远程服务器操作并刷新CDN缓存
if [ "$BUILD_HEXO" = true ]; then
    echo "\n=== 执行远程服务器操作 ==="
    
    # 从环境变量获取服务器信息
    LINUX_IP=$linux_ip
    LINUX_USER=$linux_user
    LINUX_PWD=$linux_pwd
    LINUX_P4O=$linux_p4o
    
    # 打印环境变量值（用于调试）
    echo "环境变量信息："
    echo "linux_ip: $LINUX_IP"
    echo "linux_user: $LINUX_USER"
    echo "linux_pwd: [已设置]"  # 密码不直接显示
    echo "linux_p4o: $LINUX_P4O"
    
    # 检查环境变量是否设置
    if [ -z "$LINUX_IP" ] || [ -z "$LINUX_USER" ] || [ -z "$LINUX_PWD" ] || [ -z "$LINUX_P4O" ]; then
        echo "警告：缺少远程服务器环境变量，跳过远程操作"
        echo "需要设置的环境变量：linux_ip, linux_user, linux_pwd, linux_p4o"
    else
        echo "登录远程服务器: $LINUX_USER@$LINUX_IP"
        
        # Windows系统SSH自动登录方案
        echo "Windows系统SSH自动登录..."
        
        # 方案1: 使用PowerShell的SSH命令（推荐）
        if command -v powershell >/dev/null 2>&1; then
            echo "使用PowerShell SSH连接..."
            powershell -Command "
                \$session = New-SSHSession -ComputerName $LINUX_IP -Credential (New-Object System.Management.Automation.PSCredential('$LINUX_USER', (ConvertTo-SecureString '$LINUX_PWD' -AsPlainText -Force))) -AcceptKey \$true
                if (\$session.Connected) {
                    Invoke-SSHCommand -SessionId \$session.SessionId -Command 'cd \"$LINUX_P4O\" && sh ngnix.sh'
                    Remove-SSHSession -SessionId \$session.SessionId | Out-Null
                    Write-Host '远程服务器操作完成'
                } else {
                    Write-Host 'SSH连接失败'
                }
            "
        # 方案2: 使用expect工具（如果已安装）
        elif command -v expect >/dev/null 2>&1; then
            echo "使用expect工具..."
            expect << EOF
                spawn ssh -o StrictHostKeyChecking=no $LINUX_USER@$LINUX_IP
                expect "password:"
                send "$LINUX_PWD\r"
                expect "*$"
                send "cd \"$LINUX_P4O\"\r"
                expect "*$"
                send "sh ngnix.sh\r"
                expect "*$"
                send "exit\r"
                expect eof
EOF
            echo "远程服务器操作完成"
        # 方案3: 使用plink（PuTTY工具）
        elif command -v plink >/dev/null 2>&1; then
            echo "使用plink工具..."
            echo "y" | plink -ssh -pw "$LINUX_PWD" $LINUX_USER@$LINUX_IP "cd \"$LINUX_P4O\" && sh ngnix.sh"
            echo "远程服务器操作完成"
        else
            echo "警告：未找到合适的自动登录工具"
            echo "请选择以下方案之一："
            echo "1. 安装PowerShell SSH模块: Install-Module -Name Posh-SSH"
            echo "2. 安装expect工具（Windows版）"
            echo "3. 安装PuTTY工具包（包含plink）"
            echo "4. 手动登录服务器执行: cd $LINUX_P4O && sh ngnix.sh"
        fi
    fi
    
    echo "\n=== 刷新CDN缓存 ==="
    python refresh_cdn.py
fi

echo "\n=== 流程完成 ==="
echo "自动打包、提交和推送完成！"


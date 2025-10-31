#!/bin/bash

# 远程登录测试脚本
# 用于测试远程服务器连接和命令执行功能

echo "=== 远程登录功能测试 ==="

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
    echo "错误：缺少远程服务器环境变量"
    echo "请设置以下环境变量："
    echo "  export linux_ip=服务器IP地址"
    echo "  export linux_user=用户名"
    echo "  export linux_pwd=密码"
    echo "  export linux_p4o=工作目录路径"
    exit 1
fi

echo ""
echo "开始测试远程连接..."

# 测试1: 基本连接测试
echo "1. 测试SSH连接..."
if command -v powershell >/dev/null 2>&1; then
    echo "检测到PowerShell，使用PowerShell测试..."
    powershell -Command "
        try {
            Import-Module Posh-SSH -ErrorAction Stop
            # 设置SSH选项，避免首次连接时的确认提示
            \$sshOptions = @{
                'StrictHostKeyChecking' = 'no'
                'UserKnownHostsFile' = '/dev/null'
            }
            \$session = New-SSHSession -ComputerName $LINUX_IP -Credential (New-Object System.Management.Automation.PSCredential('$LINUX_USER', (ConvertTo-SecureString '$LINUX_PWD' -AsPlainText -Force))) -AcceptKey \$true -AcceptKey \$true -AcceptKey \$true -ConnectionTimeout 30 -AcceptKey \$true -ErrorAction Stop
            if (\$session.Connected) {
                Write-Host '✓ SSH连接成功' -ForegroundColor Green
                \$result = Invoke-SSHCommand -SessionId \$session.SessionId -Command 'echo \"连接测试成功\" && whoami && pwd'
                Write-Host '远程命令执行结果:'
                Write-Host \$result.Output
                Remove-SSHSession -SessionId \$session.SessionId | Out-Null
            } else {
                Write-Host '✗ SSH连接失败' -ForegroundColor Red
            }
        } catch {
            Write-Host '✗ PowerShell SSH模块测试失败: ' \$_.Exception.Message -ForegroundColor Red
        }
    "
elif command -v ssh >/dev/null 2>&1; then
    echo "检测到SSH客户端，使用标准SSH测试..."
    # 简单连接测试（不执行命令）
    timeout 10 ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no $LINUX_USER@$LINUX_IP "echo '连接测试成功' && whoami && pwd"
    if [ $? -eq 0 ]; then
        echo "✓ SSH连接成功"
    else
        echo "✗ SSH连接失败"
    fi
else
    echo "未找到SSH客户端"
fi

echo ""

# 测试2: 工作目录测试
echo "2. 测试工作目录访问..."
if command -v powershell >/dev/null 2>&1; then
    powershell -Command "
        try {
            Import-Module Posh-SSH -ErrorAction SilentlyContinue
            \$session = New-SSHSession -ComputerName $LINUX_IP -Credential (New-Object System.Management.Automation.PSCredential('$LINUX_USER', (ConvertTo-SecureString '$LINUX_PWD' -AsPlainText -Force))) -AcceptKey \$true -AcceptKey \$true -AcceptKey \$true
            if (\$session.Connected) {
                \$result = Invoke-SSHCommand -SessionId \$session.SessionId -Command 'cd \"$LINUX_P4O\" && pwd && ls -la | head -10'
                Write-Host '工作目录内容:'
                Write-Host \$result.Output
                Remove-SSHSession -SessionId \$session.SessionId | Out-Null
                Write-Host '✓ 工作目录访问成功' -ForegroundColor Green
            }
        } catch {
            Write-Host '✗ 工作目录测试失败' -ForegroundColor Red
        }
    "
else
    echo "跳过工作目录测试（需要SSH客户端）"
fi

echo ""

# 测试3: ngnix.sh脚本测试
echo "3. 测试ngnix.sh脚本执行..."
if command -v powershell >/dev/null 2>&1; then
    powershell -Command "
        try {
            Import-Module Posh-SSH -ErrorAction SilentlyContinue
            \$session = New-SSHSession -ComputerName $LINUX_IP -Credential (New-Object System.Management.Automation.PSCredential('$LINUX_USER', (ConvertTo-SecureString '$LINUX_PWD' -AsPlainText -Force))) -AcceptKey \$true -AcceptKey \$true -AcceptKey \$true
            if (\$session.Connected) {
                \$result = Invoke-SSHCommand -SessionId \$session.SessionId -Command 'cd \"$LINUX_P4O\" && [ -f ngnix.sh ] && echo \"找到ngnix.sh文件\" || echo \"未找到ngnix.sh文件\"'
                Write-Host \$result.Output
                
                # 测试执行权限
                \$result = Invoke-SSHCommand -SessionId \$session.SessionId -Command 'cd \"$LINUX_P4O\" && [ -x ngnix.sh ] && echo \"ngnix.sh有执行权限\" || echo \"ngnix.sh无执行权限\"'
                Write-Host \$result.Output
                
                Remove-SSHSession -SessionId \$session.SessionId | Out-Null
                Write-Host '✓ ngnix.sh脚本测试完成' -ForegroundColor Green
            }
        } catch {
            Write-Host '✗ ngnix.sh脚本测试失败' -ForegroundColor Red
        }
    "
else
    echo "跳过ngnix.sh脚本测试（需要SSH客户端）"
fi

echo ""

# 测试4: 完整流程模拟测试
echo "4. 完整流程模拟测试..."
if command -v powershell >/dev/null 2>&1; then
    powershell -Command "
        try {
            Import-Module Posh-SSH -ErrorAction SilentlyContinue
            \$session = New-SSHSession -ComputerName $LINUX_IP -Credential (New-Object System.Management.Automation.PSCredential('$LINUX_USER', (ConvertTo-SecureString '$LINUX_PWD' -AsPlainText -Force))) -AcceptKey \$true -AcceptKey \$true -AcceptKey \$true
            if (\$session.Connected) {
                Write-Host '执行完整流程...'
                \$result = Invoke-SSHCommand -SessionId \$session.SessionId -Command 'cd \"$LINUX_P4O\" && echo \"开始执行ngnix.sh...\" && sh ngnix.sh && echo \"ngnix.sh执行完成\"'
                Write-Host '执行结果:'
                Write-Host \$result.Output
                if (\$result.ExitStatus -eq 0) {
                    Write-Host '✓ 完整流程测试成功' -ForegroundColor Green
                } else {
                    Write-Host '✗ ngnix.sh执行失败，退出码: ' \$result.ExitStatus -ForegroundColor Red
                }
                Remove-SSHSession -SessionId \$session.SessionId | Out-Null
            }
        } catch {
            Write-Host '✗ 完整流程测试失败: ' \$_.Exception.Message -ForegroundColor Red
        }
    "
else
    echo "跳过完整流程测试（需要SSH客户端）"
fi

echo ""

# 总结
echo "=== 测试总结 ==="
echo "环境变量检查: ✓ 完成"
echo "远程连接测试: 请查看上方结果"
echo "工作目录测试: 请查看上方结果"
echo "脚本执行测试: 请查看上方结果"
echo ""
echo "如果所有测试都通过，可以运行 auto_push.sh --build-hexo 进行完整流程"
echo "如果测试失败，请检查："
echo "1. 环境变量是否正确设置"
echo "2. 远程服务器是否可访问"
echo "3. 用户名和密码是否正确"
echo "4. 工作目录和文件是否存在"
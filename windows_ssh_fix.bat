@echo off
REM Windows SSH 自动确认脚本
REM 用于解决首次连接时的确认提示

echo 正在配置SSH自动确认...

REM 方法1: 使用Windows内置的OpenSSH（如果可用）
if exist "%SYSTEMROOT%\System32\OpenSSH\ssh.exe" (
    echo 使用Windows OpenSSH...
    %SYSTEMROOT%\System32\OpenSSH\ssh.exe -o StrictHostKeyChecking=no -o UserKnownHostsFile=NUL %linux_user%@%linux_ip% "echo '测试连接成功'"
    if %errorlevel% equ 0 (
        echo SSH连接配置成功！
    ) else (
        echo SSH连接失败，尝试其他方法...
    )
)

REM 方法2: 使用PowerShell Posh-SSH模块
echo.
echo 方法2: 配置PowerShell SSH模块自动确认...
powershell -Command "
    if (Get-Module -ListAvailable -Name Posh-SSH) {
        Write-Host 'Posh-SSH模块已安装，配置自动确认...' -ForegroundColor Green
        # 首次连接时自动接受密钥
        Import-Module Posh-SSH
        \$session = New-SSHSession -ComputerName %linux_ip% -Credential (New-Object System.Management.Automation.PSCredential('%linux_user%', (ConvertTo-SecureString '%linux_pwd%' -AsPlainText -Force))) -AcceptKey \$true -ConnectionTimeout 10
        if (\$session.Connected) {
            Write-Host '✓ 自动确认配置成功' -ForegroundColor Green
            Remove-SSHSession -SessionId \$session.SessionId
        } else {
            Write-Host '✗ 自动确认配置失败' -ForegroundColor Red
        }
    } else {
        Write-Host 'Posh-SSH模块未安装，跳过此方法' -ForegroundColor Yellow
    }
"

REM 方法3: 手动添加主机密钥到known_hosts
echo.
echo 方法3: 手动添加主机密钥到known_hosts文件...
if exist "%USERPROFILE%\.ssh" (
    echo 找到.ssh目录
) else (
    mkdir "%USERPROFILE%\.ssh"
    echo 创建.ssh目录
)

REM 使用ssh-keyscan获取主机密钥并添加到known_hosts
if exist "%USERPROFILE%\.ssh\known_hosts" (
    echo 检查是否已存在主机密钥...
    findstr /i "%linux_ip%" "%USERPROFILE%\.ssh\known_hosts" >nul
    if errorlevel 1 (
        echo 添加新的主机密钥...
        echo y | ssh-keyscan -H %linux_ip% >> "%USERPROFILE%\.ssh\known_hosts" 2>nul
        if %errorlevel% equ 0 (
            echo ✓ 主机密钥添加成功
        ) else (
            echo ✗ 主机密钥添加失败
        )
    ) else (
        echo ✓ 主机密钥已存在
    )
) else (
    echo 创建新的known_hosts文件...
    echo y | ssh-keyscan -H %linux_ip% > "%USERPROFILE%\.ssh\known_hosts" 2>nul
    if %errorlevel% equ 0 (
        echo ✓ known_hosts文件创建成功
    ) else (
        echo ✗ known_hosts文件创建失败
    )
)

echo.
echo ===========================================
echo SSH自动确认配置完成！
echo 现在可以运行测试脚本：test_remote_login.sh
echo 或完整流程：auto_push.sh --build-hexo
echo ===========================================

pause
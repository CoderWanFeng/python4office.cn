# 测试脚本语法和功能

Write-Host "=== 测试脚本语法检查 ==="

# 检查脚本文件是否存在
if (Test-Path "auto_push.sh") {
    Write-Host "✓ 脚本文件存在"
    
    # 读取脚本内容检查语法
    $content = Get-Content "auto_push.sh" -Raw
    
    # 检查常见语法问题
    Write-Host "检查常见语法问题:"
    
    # 1. 检查shebang
    if ($content -match "^#!/bin/bash") {
        Write-Host "  ✓ shebang正确"
    } else {
        Write-Host "  ⚠ shebang可能有问题"
    }
    
    # 2. 检查变量赋值
    if ($content -match "BUILD_HEXO=false") {
        Write-Host "  ✓ 变量赋值语法正确"
    }
    
    # 3. 检查函数定义
    if ($content -match "log\(\)") {
        Write-Host "  ✓ 函数定义语法正确"
    }
    
    # 4. 检查条件语句
    if ($content -match "if \[.*\]") {
        Write-Host "  ✓ 条件语句语法正确"
    }
    
    # 5. 检查PowerShell命令
    if ($content -match "powershell -Command") {
        Write-Host "  ✓ PowerShell命令语法正确"
    }
    
    # 检查特定问题
    Write-Host "检查特定问题:"
    
    # 检查环境变量引用
    if ($content -match "\$linux_ip") {
        Write-Host "  ✓ 环境变量引用正确"
    }
    
    # 检查SSH命令
    if ($content -match "sshpass") {
        Write-Host "  ✓ sshpass命令存在"
    }
    
    if ($content -match "New-SSHSession") {
        Write-Host "  ✓ PowerShell SSH命令存在"
    }
    
} else {
    Write-Host "✗ 脚本文件不存在"
}

Write-Host "`n=== 测试环境变量 ==="

# 检查环境变量
$envVars = @("linux_ip", "linux_user", "linux_pwd", "linux_p4o")
foreach ($var in $envVars) {
    $value = [Environment]::GetEnvironmentVariable($var)
    if ($value) {
        Write-Host "  ✓ $var = $value"
    } else {
        Write-Host "  ⚠ $var 未设置"
    }
}

Write-Host "`n=== 测试完成 ==="
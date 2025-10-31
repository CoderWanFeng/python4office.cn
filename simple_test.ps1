Write-Host "=== 简单脚本测试 ==="

# 检查脚本文件
if (Test-Path "auto_push.sh") {
    Write-Host "✓ 脚本文件存在"
    
    # 检查文件内容
    $content = Get-Content "auto_push.sh" -Raw
    
    # 检查关键语法
    Write-Host "检查关键语法:"
    
    if ($content -match "^#!/bin/bash") {
        Write-Host "  ✓ shebang正确"
    }
    
    if ($content -match "BUILD_HEXO=false") {
        Write-Host "  ✓ 变量赋值正确"
    }
    
    if ($content -match "log\(\)") {
        Write-Host "  ✓ 函数定义正确"
    }
    
    # 检查PowerShell命令
    if ($content -match "powershell -Command") {
        Write-Host "  ✓ PowerShell命令存在"
        
        # 检查具体的PowerShell命令语法
        $powershellCmds = [regex]::Matches($content, "powershell -Command \"[^\"]*\"")
        foreach ($cmd in $powershellCmds) {
            Write-Host "  - 命令: $($cmd.Value)"
        }
    }
    
} else {
    Write-Host "✗ 脚本文件不存在"
}

Write-Host "=== 测试完成 ==="
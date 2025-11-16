#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
一键打包脚本
用于将所有Python脚本打包为独立的可执行文件
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"当前工作目录: {current_dir}")

# 确保所有必要的目录存在
directories = [
    "excel_tools",
    "word_tools", 
    "pdf_tools",
    "other_tools",
    "common"
]

for dir_name in directories:
    dir_path = os.path.join(current_dir, dir_name)
    if not os.path.exists(dir_path):
        print(f"警告: 目录 {dir_name} 不存在")

# 获取所有Python脚本
script_files = []

# Excel工具
excel_dir = os.path.join(current_dir, "excel_tools")
if os.path.exists(excel_dir):
    for file in os.listdir(excel_dir):
        if file.endswith(".py"):
            script_files.append(os.path.join(excel_dir, file))

# Word工具
word_dir = os.path.join(current_dir, "word_tools")
if os.path.exists(word_dir):
    for file in os.listdir(word_dir):
        if file.endswith(".py"):
            script_files.append(os.path.join(word_dir, file))

# PDF工具
pdf_dir = os.path.join(current_dir, "pdf_tools")
if os.path.exists(pdf_dir):
    for file in os.listdir(pdf_dir):
        if file.endswith(".py"):
            script_files.append(os.path.join(pdf_dir, file))

# 其他工具
other_dir = os.path.join(current_dir, "other_tools")
if os.path.exists(other_dir):
    for file in os.listdir(other_dir):
        if file.endswith(".py"):
            script_files.append(os.path.join(other_dir, file))

print(f"找到 {len(script_files)} 个Python脚本")

# 检查PyInstaller是否安装
try:
    subprocess.run([sys.executable, "-c", "import PyInstaller"], 
                   check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("PyInstaller已安装")
except subprocess.CalledProcessError:
    print("PyInstaller未安装，正在安装...")
    subprocess.run([sys.executable, "-m", "pip", "install", "PyInstaller"], 
                   check=True)
    print("PyInstaller安装完成")

# 为每个脚本创建打包命令
build_commands = []

# 统一输出目录 - 所有可执行文件将放在这里
output_dir = os.path.join(current_dir, "exe")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 按工具类型创建子目录以保持组织结构
tool_subdirs = {
    "excel_tools": "Excel工具",
    "word_tools": "Word工具", 
    "pdf_tools": "PDF工具",
    "other_tools": "其他工具"
}

# 为每个工具类型创建子目录
for subdir, display_name in tool_subdirs.items():
    subdir_path = os.path.join(output_dir, display_name)
    if not os.path.exists(subdir_path):
        os.makedirs(subdir_path)
        print(f"创建目录: {subdir_path}")

spec_dir = os.path.join(current_dir, "build")

for script in script_files:
    script_name = os.path.splitext(os.path.basename(script))[0]
    script_dir = os.path.dirname(script)
    
    # 构建PyInstaller命令
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",  # 打包为单个文件
        "--windowed",  # 使用GUI模式，不显示控制台
        "--noconfirm",  # 覆盖输出目录而不询问
        "--clean",  # 清理临时文件
        "--distpath", output_dir,  # 输出目录
        "--workpath", os.path.join(spec_dir, script_name),  # 工作目录
        "--specpath", spec_dir,  # 规范文件目录
        script
    ]
    
    build_commands.append((script_name, script_dir, cmd))

# 执行打包
total_commands = len(build_commands)
print(f"开始打包 {total_commands} 个脚本...")

for i, (script_name, script_dir, cmd) in enumerate(build_commands):
    print(f"[{i+1}/{total_commands}] 正在打包: {script_name}")
    
    try:
        # 切换到脚本所在目录
        original_dir = os.getcwd()
        os.chdir(script_dir)
        
        # 执行打包命令
        subprocess.run(cmd, check=True)
        
        # 恢复原始目录
        os.chdir(original_dir)
        
        # 确定目标子目录
        tool_type = os.path.basename(script_dir)
        display_subdir = tool_subdirs.get(tool_type, "其他工具")
        target_subdir = os.path.join(output_dir, display_subdir)
        
        # 移动可执行文件到统一的exe目录下的相应子目录
        ext = ".exe" if sys.platform == "win32" else ""
        exe_path = os.path.join(output_dir, f"{script_name}{ext}")
        if os.path.exists(exe_path):
            target_path = os.path.join(target_subdir, f"{script_name}{ext}")
            if os.path.exists(target_path):
                os.remove(target_path)
            shutil.move(exe_path, target_path)
            print(f"  -> 成功: {target_path}")
        else:
            print(f"  -> 错误: 可执行文件未找到")
            
    except subprocess.CalledProcessError as e:
        print(f"  -> 错误: 打包失败 - {e}")
    except Exception as e:
        print(f"  -> 错误: 未知错误 - {e}")

# 清理临时文件
print("清理临时文件...")
if os.path.exists(output_dir) and not os.listdir(output_dir):
    os.rmdir(output_dir)

if os.path.exists(spec_dir):
    shutil.rmtree(spec_dir)

print("所有脚本打包完成！")

# 统计成功和失败的脚本
success_count = 0
fail_count = 0

for script in script_files:
    script_name = os.path.splitext(os.path.basename(script))[0]
    script_dir = os.path.dirname(script)
    tool_type = os.path.basename(script_dir)
    display_subdir = tool_subdirs.get(tool_type, "其他工具")
    
    ext = ".exe" if sys.platform == "win32" else ""
    target_path = os.path.join(output_dir, display_subdir, f"{script_name}{ext}")
    
    if os.path.exists(target_path):
        success_count += 1
    else:
        fail_count += 1

print(f"\n打包结果: 成功 {success_count}, 失败 {fail_count}")

if fail_count > 0:
    print("\n警告: 部分脚本打包失败，请检查错误信息")
else:
    print("\n所有脚本打包成功！")

# 创建运行脚本
if sys.platform == "win32":
    bat_content = "@echo off\n"
    
    # Excel工具
    if os.path.exists(excel_dir):
        bat_content += "echo ===== Excel工具 =====\n"
        for file in os.listdir(excel_dir):
            if file.endswith(".exe"):
                bat_content += f"echo 运行 {file}\n"
                bat_content += f"start \"\" \"{os.path.join(excel_dir, file)}\"\n"
                bat_content += "pause\n"
        bat_content += "\n"
    
    # Word工具
    if os.path.exists(word_dir):
        bat_content += "echo ===== Word工具 =====\n"
        for file in os.listdir(word_dir):
            if file.endswith(".exe"):
                bat_content += f"echo 运行 {file}\n"
                bat_content += f"start \"\" \"{os.path.join(word_dir, file)}\"\n"
                bat_content += "pause\n"
        bat_content += "\n"
    
    # PDF工具
    if os.path.exists(pdf_dir):
        bat_content += "echo ===== PDF工具 =====\n"
        for file in os.listdir(pdf_dir):
            if file.endswith(".exe"):
                bat_content += f"echo 运行 {file}\n"
                bat_content += f"start \"\" \"{os.path.join(pdf_dir, file)}\"\n"
                bat_content += "pause\n"
        bat_content += "\n"
    
    # 其他工具
    if os.path.exists(other_dir):
        bat_content += "echo ===== 其他工具 =====\n"
        for file in os.listdir(other_dir):
            if file.endswith(".exe"):
                bat_content += f"echo 运行 {file}\n"
                bat_content += f"start \"\" \"{os.path.join(other_dir, file)}\"\n"
                bat_content += "pause\n"
    
    bat_content += "echo 所有工具已启动\n"
    bat_content += "pause\n"
    
    with open(os.path.join(current_dir, "run_all.bat"), "w", encoding="gbk") as f:
        f.write(bat_content)
    
    print("\n创建启动脚本: run_all.bat")
    
elif sys.platform == "darwin":  # macOS
    sh_content = "#!/bin/bash\n"
    sh_content += "echo ===== Excel工具 =====\n"
    
    if os.path.exists(excel_dir):
        for file in os.listdir(excel_dir):
            if file.endswith(".app"):
                sh_content += f"echo 运行 {file}\n"
                sh_content += f"open \"{os.path.join(excel_dir, file)}\"\n"
    
    sh_content += "\n"
    
    with open(os.path.join(current_dir, "run_all.sh"), "w") as f:
        f.write(sh_content)
    
    # 设置执行权限
    os.chmod(os.path.join(current_dir, "run_all.sh"), 0o755)
    print("\n创建启动脚本: run_all.sh")
    
else:  # Linux
    sh_content = "#!/bin/bash\n"
    
    if os.path.exists(excel_dir):
        sh_content += "echo ===== Excel工具 =====\n"
        for file in os.listdir(excel_dir):
            if os.path.isfile(os.path.join(excel_dir, file)) and os.access(os.path.join(excel_dir, file), os.X_OK):
                sh_content += f"echo 运行 {file}\n"
                sh_content += f"\"{os.path.join(excel_dir, file)}\" &\n"
    
    # 类似地添加其他工具...
    
    with open(os.path.join(current_dir, "run_all.sh"), "w") as f:
        f.write(sh_content)
    
    # 设置执行权限
    os.chmod(os.path.join(current_dir, "run_all.sh"), 0o755)
    print("\n创建启动脚本: run_all.sh")

print(f"\n打包完成！所有可执行文件已统一保存到: {output_dir}")
print("您可以使用 run_all.bat (Windows) 或 run_all.sh (macOS/Linux) 启动所有工具。")
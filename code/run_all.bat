@echo off
echo ===== 从统一目录启动所有工具 =====
echo 可执行文件位置: %~dp0exe\

echo ===== Excel工具 =====
if exist "%~dp0exe\Excel工具\*.exe" (
    for %%f in ("%~dp0exe\Excel工具\*.exe") do (
        echo 运行 %%~nf
        start "" "%%f"
        pause
    )
)

echo ===== Word工具 =====
if exist "%~dp0exe\Word工具\*.exe" (
    for %%f in ("%~dp0exe\Word工具\*.exe") do (
        echo 运行 %%~nf
        start "" "%%f"
        pause
    )
)

echo ===== PDF工具 =====
if exist "%~dp0exe\PDF工具\*.exe" (
    for %%f in ("%~dp0exe\PDF工具\*.exe") do (
        echo 运行 %%~nf
        start "" "%%f"
        pause
    )
)

echo ===== 其他工具 =====
if exist "%~dp0exe\其他工具\*.exe" (
    for %%f in ("%~dp0exe\其他工具\*.exe") do (
        echo 运行 %%~nf
        start "" "%%f"
        pause
    )
)

echo 所有工具已启动
pause
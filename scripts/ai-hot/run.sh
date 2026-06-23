#!/bin/bash
# AI热点选题启动脚本

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/ai-hot-selector.py"

echo "启动AI热点选题流程..."
echo "脚本目录: $SCRIPT_DIR"

# 检查Python3
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到python3"
    exit 1
fi

# 执行Python脚本
cd "$SCRIPT_DIR" || exit 1
python3 "$PYTHON_SCRIPT"

# 检查执行状态
if [ $? -eq 0 ]; then
    echo ""
    echo "选题流程完成！"
    echo "请按照输出提示进行后续创作。"
else
    echo ""
    echo "选题流程执行失败，请检查错误信息。"
    exit 1
fi
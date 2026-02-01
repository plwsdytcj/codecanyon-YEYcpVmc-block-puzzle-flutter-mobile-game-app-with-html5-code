#!/bin/bash
# 在浏览器中测试 Candy Blocks 游戏

echo "=================================="
echo "🍬 启动 Candy Blocks 游戏测试"
echo "=================================="

# 检查是否有 Python
if command -v python3 &> /dev/null; then
    echo "使用 Python 启动本地服务器..."
    cd vasugame/lib/Game
    echo ""
    echo "✅ 游戏服务器已启动！"
    echo "📱 在浏览器中打开: http://localhost:8000"
    echo ""
    echo "按 Ctrl+C 停止服务器"
    echo ""
    python3 -m http.server 8000
elif command -v python &> /dev/null; then
    echo "使用 Python 启动本地服务器..."
    cd vasugame/lib/Game
    echo ""
    echo "✅ 游戏服务器已启动！"
    echo "📱 在浏览器中打开: http://localhost:8000"
    echo ""
    echo "按 Ctrl+C 停止服务器"
    echo ""
    python -m SimpleHTTPServer 8000
else
    echo "❌ 未找到 Python，尝试直接打开文件..."
    open vasugame/lib/Game/index.html
fi

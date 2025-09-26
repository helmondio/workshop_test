@echo off
echo 正在启动百度千帆API代理服务器...
echo.
echo 请确保已安装Python和所需依赖包
echo 如果没有安装依赖，请先运行: pip install -r requirements.txt
echo.
echo 服务器启动后，请在浏览器中打开 api_caller.html
echo 按 Ctrl+C 停止服务器
echo.
python proxy_server.py
pause

# 百度千帆API调用工具

这是一个用于调用百度千帆API的Web工具，包含HTML前端和Python代理服务器。

## 问题解决

原始HTML页面出现"Failed to fetch"错误是由于浏览器的CORS（跨域资源共享）策略阻止了直接调用外部API。本解决方案通过Python代理服务器解决了这个问题。

## 文件说明

- `api_caller.html` - 前端HTML页面，提供用户界面
- `proxy_server.py` - Python代理服务器，解决CORS问题
- `requirements.txt` - Python依赖包列表
- `start_server.bat` - Windows批处理文件，用于启动服务器

## 使用方法

### 方法1：使用批处理文件（推荐）
1. 双击运行 `start_server.bat`
2. 在浏览器中打开 `api_caller.html`

### 方法2：手动启动
1. 安装Python依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 启动代理服务器：
   ```bash
   python proxy_server.py
   ```

3. 在浏览器中打开 `api_caller.html`

## 功能特性

- ✅ 解决CORS跨域问题
- ✅ 美观的现代化界面
- ✅ 实时状态显示
- ✅ 详细的错误提示
- ✅ 响应式设计
- ✅ JSON结果格式化显示

## 技术栈

- 前端：HTML5, CSS3, JavaScript (ES6+)
- 后端：Python Flask
- 代理：Flask-CORS

## 注意事项

- 确保代理服务器在调用API前已启动
- 请确保授权令牌有效
- 如果遇到连接问题，请检查防火墙设置

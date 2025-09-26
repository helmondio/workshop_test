#!/usr/bin/env python3
"""
简单的代理服务器，用于解决CORS问题
运行此服务器后，HTML页面将通过此代理调用百度千帆API
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # 启用CORS支持

@app.route('/api/trending_lists', methods=['POST'])
def proxy_trending_lists():
    """
    代理百度千帆API调用
    """
    try:
        # 获取请求数据
        data = request.get_json()
        
        # 验证必需参数
        required_params = ['type', 'mediaType', 'timeRange']
        for param in required_params:
            if param not in data:
                return jsonify({'error': f'缺少必需参数: {param}'}), 400
        
        # 百度千帆API URL
        api_url = 'https://qianfan.baidubce.com/v2/tools/trending_lists/vertical'
        
        # 从请求头获取Authorization
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': '缺少Authorization头'}), 400
        
        # 设置请求头
        headers = {
            'Authorization': auth_header,
            'Content-Type': 'application/json'
        }
        
        # 调用百度千帆API
        response = requests.post(api_url, headers=headers, json=data, timeout=30)
        
        # 检查响应状态
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({
                'error': f'API调用失败',
                'status_code': response.status_code,
                'response': response.text
            }), response.status_code
            
    except requests.exceptions.Timeout:
        return jsonify({'error': '请求超时'}), 408
    except requests.exceptions.ConnectionError:
        return jsonify({'error': '连接错误'}), 503
    except Exception as e:
        return jsonify({'error': f'服务器错误: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """健康检查端点"""
    return jsonify({'status': 'ok', 'message': '代理服务器运行正常'})

if __name__ == '__main__':
    print("启动代理服务器...")
    print("服务器地址: http://localhost:5000")
    print("API端点: http://localhost:5000/api/trending_lists")
    print("健康检查: http://localhost:5000/health")
    print("按 Ctrl+C 停止服务器")
    
    app.run(host='0.0.0.0', port=5000, debug=True)

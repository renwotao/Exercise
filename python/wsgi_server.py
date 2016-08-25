#! /user/bin/env python3
# -*- coding: utf-8 -*-

'''
        WSGI 服务器
        
                Python 内置了一个 WSGI 服务器，这个模块叫 wsgiref，它是用纯 Python编写的 WSGI 服务器的参考实现。
                所谓的“参考实现”是指该实现完全符合 WSGI 标准，但是不考虑任何运行
效率，仅供开发和测试使用。
'''

'''
        运行 WSGI 服务器
'''

# 从 swgiref 模块导入
from wsgiref.simple_server import make_server
# 导入自己编写的 application 函数
from wsgi_hello import application

# 创建一个服务器，IP 地址为空，端口是 8000，处理函数是 application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听 HTTP 请求
httpd.serve_forever()

#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
        如何处理 100 个不同的 URL

        一个简单的做法是取出 environ 变量去除 HTTP 请求信息， 逐个判断
def application(environ, start_response):
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        if method == 'GET' and path == '/':
                return handle_home(environ, start_response)
        if method == 'POST' and path == '/signin':
                return handle_signin(environ, start_response)

        只是代码无法维护
'''

'''
        Flask 使用
'''


'''
	GET /: 首先，返回 Home：
	GET /signin： 登陆页，显示登陆表单
	POST /signin: 处理登陆表单，显示登陆结果

	注意：同一个 URL /signin 分别有 GET 和 POST 两种请求，映射到两个处理函数
'''

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
	return '''<form action="/signin" method="post">
		  <p><input name="username"</p>
		  <p><input name="password" type="password"></p>
		  <p><button type="submit">Sign In</button></p>
	          </form>'''
@app.route('/signin', methods=['POST'])
def signin():
	# 需要从 request 对象读取表单内容
	if request.form['username']=='admin' and request.form['password']=='password':
		return '<h3>Hello, admin!</h3>'
	return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
	app.run()



'''


除了Flask，常见的Python Web框架还有：

    Django：全能型Web框架；

    web.py：一个小巧的Web框架；

    Bottle：和Flask类似的Web框架；

    Tornado：Facebook的开源异步Web框架。
'''

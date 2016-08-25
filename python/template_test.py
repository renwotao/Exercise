#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	MVC:Model-View-Controller
	
	C:Controller,Controller 负责业务逻辑，比如检查用户名是否存在，去除用户信息等
	V:View，View 负责显示逻辑，通过简单地替换一些变量，View 最终输出的就是用户看的 HTML
	M:Model，Model 是用来传给 View 的，这样 View 在替换变量的时候，就可以从 Model 中取出相应的数据
'''

'''
	flask template
'''
# Flask 通过 render_template() 函数来实现魔伴的渲 

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()

#! /user/bin/env python3
# -*- coding: utf-8 -*-

'''
	WSGI：Web Server Gateway Interface
'''
'''
	application() 函数就是符合 WSGI 标准的一个 HTTP 处理函数，它接收两个参数：
	environ: 一个包含所有 HTTP 请求信息 dict 对象
	start_response: 一个发送 HTTP 响应的函数
		start_response() 函数接收两个参数，一个 HTTP 响应吗，
		一个是一组 list 表示 HTTP Header,每个 Header 用一个包含两个 str的 tuple 表示。
'''

def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return [b'<h1>Hello, web!</h1>']



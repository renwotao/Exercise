#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	urllib
		urllib 提供一系列用于操作 URL 的功能
'''

'''
	Get
'''
# 对豆瓣的一个 URL 进行抓取，并返回响应
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))

'''
	模拟浏览器发送 GET 请求，就需要使用 Request 对象，
	通过往 Request 对象添加 HTTP头，就可以把请求伪装成浏览器。
'''
from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', f.read().decode('utf-8'))
# 豆瓣会返回适合 iPhone 的移动版网页

'''
	Post
		如果以 POST 发送一个请求，只需要把参数 data 以 bytes 形式传入。
'''

# 模拟一个微博登陆，先读取登陆的邮箱和口令，然后按照 weibo.cn 的登录页的格式以 username=xxx&password=xxx 的编码传入

from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
	('username', email),
	('password', passwd),
	('entry', 'mweibo'),
	('client_id', ''),
	('savestate', '1'),
	('ec', ''),
	('pagerefer', 'https://passport.weibo.cn/signin/welcom?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', f.read().decode('utf-8'))

'''

	Handler
	
		如果需要更复杂的控制，比如通过一个 Proxy 去访问网站，需要利用 ProxyHandler 
'''
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.pen('http://www.example.com/login.html') as f:
	pass


#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	debug
'''

def foo(s):
	n = int(s)
	print('>>> n = %d' % n)
	return 10 / n

def main():
	foo('0')

main()

'''
	assert
'''
def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	return 10 / n

def main():
	foo('0')

# 如果断言失败，assert语句本身就会抛出AssertionError
# 启动Python解释器可以用-o参数来关闭assert

'''
	logging
		指定记录信息的级别：debug，info，warning，error
'''
import logging

s = '0'
n = int(s)
# 和assert比，logging不会抛出错误，而且可以输出到文件
logging.info('n = %d' % n) # 仅输出ZeroDivisionError
print(10 / n)

import logging
logging.basicConfig(level=logging.INFO) # 详细输出
logging.info('n = %d' % n)
print(10 / 0)

'''
	pdb
	启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态

	参数：
		python3 -m pdb xx.py 启动调试，pdb定位执行的代码
			l 查看代码
			n 单步执行
			c 继续运行
			p 变量名 查看变量
			q 退出
'''

s = '0'
n = int(s)
print(10 / n)

'''
	pdb.set_trace()
'''
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停并进入pdb调试环境
print(10 / n)


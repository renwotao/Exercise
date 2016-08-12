#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
	返回函数
'''

# 函数作为返回值
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax
# 不需要立刻求和，可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

'''
	函数lasy_sum中定义了函数sum，并且内部函数sum可以引用外部函数
	lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
	相关参数和变量都保存在返回函数中，这种称为“闭包(Closure)"de 
	程序结构拥有极大的威力
'''
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print('f1 == f2', f1 == f2)


'''
	闭包
'''
def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())

# 返回闭包时牢记的一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量

def count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())


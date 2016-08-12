#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
	匿名函数
'''

L = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(L)

def f(x):
	return x * x

f = lambda x: x * x
print(f)
print(f(5))

def build(x, y):
	return lambda: x * x + y * y


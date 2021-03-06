#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''
	map/reduce
'''

def f(x):
	return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
	L.append(f(n))
print(L)

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8])))

'''
	reduce
		reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
from functools import reduce
def add(x, y):
	return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
	return x * 10 + y
def char2num(s):
	return {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }[s]

print(reduce(fn, map(char2num, '13579')))

'''
	str2int
'''
from functools import reduce
def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }[s]
	return reduce(fn, map(char2num, s))

'''
	lambda
'''
def char2num(s):
	return {'0': 0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }[s]

def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))

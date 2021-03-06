#! /usr/bin/env python3
# -×- coding:utf-8 -*-

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print('my_abs(-100) = %d' % my_abs(-100))

# 占位符 pass, pass 什么也不做
def nop():
	pass
age = 19
if age >= 18:
	pass

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

import math
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi/6)
print(x, y)

r = move(100, 100, 60, math.pi/6)
print(r)

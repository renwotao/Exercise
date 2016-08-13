#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print(type(123))
print(type('str'))
print(type(abs))

print(type(123) == type(456))
print(type('abc') == str)
print(type('abc')== int)

import types

def fun():
	pass

print(type(fun) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

'''
	dir()
		获得一个对象的所有属性和方法
'''

# __len__方法返回长度
# len()函数师徒获取一个对象的长度，实际上，在len()函数内部，
# 它自动去调用该对象的__len__()方法
dir('ABC')
print(len('ABC'))
print('ABC'.__len__())


class MyDog(object):
	def __len__(self):
		return 100
dog = MyDog()
print(len(dog))

class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
print(setattr(obj, 'y', 19))
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

#getattr(obj, 'z')

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
fn
fn()

def readImage(fp):
	if hasattr(fp, 'read'):
		return readData(fp)
	return None


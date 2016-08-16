#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	error handle
'''

# 错误码
def foo():
	r = some_function()
	if r == (-1):
		return (-1)
	return r

def bar():
	r = foo()
	if r == (-1):
		print('Error')
	else:
		pass

'''
	try... except...finally
'''
try:
	print('try...')
	r = 10 / 0
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
print('END')

try:
	print('try...')
	r = 10 / int('a')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
finally:
	print('finally...')
print('END')


# 如果没有错误发生，可以except语句块后面加一个else，
# 当没有错误是，会自动执行else语句

try:
	print('try...')
	r = 10 /int('2')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')

'''
	Python的错误，所有的错误类型都继承自BaseException，
	所有在时候except时需要注意的是，它不但捕获该类型的错误，
	还把其子类也“一网打尽”。
'''
'''
try:
	foo()
except ValueError as e:
	print('ValueError')
except UnicodeError as e:
	print('UnicodeError')
'''

def foo(s):
	return 10 /int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		print('Error:', e)
	finally:
		print('finally...')

'''
	调用堆栈
'''
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	bar('0')

# main()

'''
	记录错误
'''
import logging

def foo(s):
	return 10 /int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)

main()
print('END')

'''
	抛出错误
	因为错误是class，捕获一个错误就是捕获该class的一个实例。
	因此错误并不是凭空产生的，而是有意创建并抛出的。
'''
# 根据需要，定义一个错误class
class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

foo('0')

# 在必要的时候才定义自己的错误类型
# 尽量使用Python的内置的错误类型（比如ValueError，TypeError）

def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError('invalid value: %s' %s)
	return 10 / n

def bar():
	try:
		foo('0')
	except ValueError as e:
		print('ValueError!')
		raise
bar()



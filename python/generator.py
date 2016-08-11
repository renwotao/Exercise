#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''
	generator
'''

L = [x * x for x in range(10)]
print(L)

# generator
g = (x * x for x in range(10))
print('generator: ', g)
print('next(g): ', next(g))
for n in g:
	print(n)
# fibonacci 
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'
'''
	注： 
		a, b = b, a+b 
		相当于
		t = (b, a + b) 
		a = t[0]
		b = t[1] 
'''
print(fib(6))

'''
	把上面的函数变成generator,只需把print(b)改为yield b
'''
def fib2(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
f = fib2(6)
print(f)

'''
	generator和函数的执行流程不一样。
	函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
	而generator的函数，在每次调用next()的时候执行，遇到yield
	语句就返回，再次执行时从上次返回的yield语句处继续执行。
'''

def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)

o = odd()
print(next(o))
print(next(o))
print(next(o))

'''
	无法取得generator的return语句的返回值。
	如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在
	StopIteration的value中
'''
g = fib2(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break


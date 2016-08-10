#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
	 位置参数
'''

def power(x):
	return x*x;

print(power(5))

def power2(x, n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power2(5, 2))

'''
	 默认参数
'''

def power(x, n= 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(5), power(5, 3))

def enroll(name, gender):
	print('name:', name)
	print('gender:', gender)

print(enroll('Sarah', 'F'))

def enroll2(name, gender, age=6, city='Beijing'):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city', city)

print(enroll2('Sarah', 'F'))
print(enroll2('Bob', 'M', 7))
print(enroll2('Adam', 'M', city='Tianjin'))

def add_end(L=[]):
	L.append('END')
	return L

print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end())
print(add_end())
print(add_end())

def add_end2(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

print(add_end2())
print(add_end2())

'''
	可变参数
'''

def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc([1, 2, 3]))

# 定义可变参数，仅仅在参数前面加一个*号
def calc2(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc2(1, 2), calc2())

# 有一个list 或者 tupe，要调用一个可变参数怎么办
nums = [1, 2, 3]
print(calc2(nums[0], nums[1], nums[2]))
# 上面的写法太繁琐
print(calc2(*nums))

'''
 	关键字参数
		可变参数允许传入0个或任意个参数，
		这些可变参数在函数调用时自动组装成为一个tupe。
		
		关键字参数允许传输0个或任意个含参数名的参数，
		这些关键字参数在函数内部组装成一个dict。
'''

def person(name, age, **kw):
	print('name:', name, 'age:', age, 'ohter:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer' }
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

'''
	命令关键字参数
'''

def person2(name, age, **kw):
	if 'city' in kw:
		print(kw['city'])
		pass
	if 'job' in kw:
		print(kw['job'])
		pass
	print('name:', name, 'age:', age, 'other:', kw)

# 调用这仍可以传入不受限制的关键字参数
person2('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 要限制关键字参数的名字，可以用命名关键字参数
def person3(name, age, *, city, job):
	print(name, age, city, job)

# 和关键字**kw不同，命名关键字参数需要一个特殊分隔符×，×后面的参数被视为命名关键字参数

person3('Jack', 24, city='Beijing', job='Engineer')

'''
	如果函数定义中依据能够有了一个可变参数，
	后面跟着命名关键字参数就不在需要一个特殊分隔符*。
'''

def person4(name, age, *args, city, job):
	print(name, age, args, city, job)
person4('Jack', 24, city='Beijing', job='Engineer')

'''
	使用命名关键字参数时要注意，如果没有可变参数，
	就必须加一个*作为特殊分隔符。
	如果缺少*, Python解释器将无法识别位置参数和命名关键字参数
'''
def person5(name, age, *, city='Beijing', job):
	print(name, age, city, job)
person5('Jack', 24, job='Engineer')

'''
	参数组合
'''
def f1(a, b, c=0, *args, **kw):
	print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)

def f2(a, b, c=0, *, d, **kw):
	print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)


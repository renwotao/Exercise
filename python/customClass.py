#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	__str__
'''
class Student(object):
	def __init__(self, name):
		self.name = name
print(Student('Michael'))

class Student1(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name

print(Student('Michael'))

# 不用print
s = Student('Michael')
# 直接显示变量调用的不是__str__()，而是__repr__()
# 两者的区别是__str__()返回用户看到的字符串
# 而__repr__()返回程序开发者看到的字符串，__repr__()是为调试服务的
s
class Student2(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__


'''
	__iter__
'''
'''
	如果一个类想被用于for ... in循环，类似list或tuple
	就必须实现一个__iter__()方法，该方法返回一个迭代对象
	Python的for循环就会不断调用迭代对象的__next__()方法拿到循环的下一个值
	直到遇到StopIteration错误时退出循环
'''

class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a
for n in Fib():
	print(n)


'''
	__getitem__
'''
'''
	Fib实例虽然能作用于for循环，但无法像list一样取指定索引的元素，
	比如，取第5个元素，Fib()[5]
'''
class Fib(object):
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a

f = Fib()
print(f[0])
print(f[100])

# list的切片方法，而Fib无法切片
print(list(range(100))[5:10])


class Fib(object):
	def __getitem__(self, n):
		if isinstance(n, int): # n是索引
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice): # n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b

			return L

f = Fib()
print(f[0:5])
print(f[:10])

'''
	但是Fib没有对step参数作处理
	f[:10:2]
	[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
	也没有对负数作处理
	
	与__getitem__()对应的是__setitem__(),把对象看做list或dict来对集合赋值
	__delitem__()方法，用于删除某个元素
'''

'''
	__getattr__
'''
class Student(object):
	
	def __init__(self):
		self.name = 'Michael'
	
	def __getattr__(self, attr):
		if attr == 'score':
			return 99
s = Student()
print(s.name)
print(s.score)

class Student(object):
	
	def __getattr__(self, attr):
		if attr == 'age':
			return lambda: 25

s = Student()
print(s.age())

'''
	注意：只有在没有找到属性的情况下，才调用__getattr__， 
	已有的属性，比如name，不会在__getattr__中查找
'''

class Student(object):
	
	def __getattr__(self, attr):
		if attr == 'age':
			return lambda: 25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

'''
	例子：
	调用API的URL类似：
		http://api.server/user/friends
		http://api.server/user/timeline/list
	
	如果要写SDK，给每个URL对应的API都写一个方法，API一旦改动，SDK也要改
	
'''
class Chain(object):

	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path
	
	__repr__ = __str__

print(Chain().status.user.timeline.list)

'''
	__call__
	一个对象实例可以又自己的属性和方法，调用实例方法时使用instance.method()
	来调用。
	能不能直接在实例本身上调用呢？
'''
class Student(object):
	
	def __init__(self, name):
		self.name = name
	
	def __call__(self):
		print('My name is %s.' % self.name)

s = Student('Michael')
s() # self参数不要传入

'''
	判断一个变量是对象还是函数？
	更多的时候，判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
'''
print(callable(Student('Michael')))
print(callable(max))
print(callable('abc'))


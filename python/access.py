#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	访问控制
		__xx ：变量名如果以__开头，就变成了一个私有变量
			只有内部可以访问，外部不能访问
'''

class Student(object):
	
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

	
	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self, score):
		self.__score = score


'''
	以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的,
	但是，按照约定，这样的变量表示：
		虽然我可以被访问，但是请把我视为私有变量，不要随意访问
'''
# Python解释器对外把__name 变量改为_Student__name
bart = Student('Bart Simpson', 59)
print(bart._Student__name)

# 不见已这么访问，不同版本的Python 解释器会把 __name改成不同的变量名

print(bart.get_name())

# 在外部设置__name变量，实际上__name变量和class内部的__name变量不是一个变量
# 内部的__name变量被Python解释器自动改成了_Student__name
bart.__name = 'NewName'
print(bart.__name)
print(bart.get_name())

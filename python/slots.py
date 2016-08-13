#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	__slots__
'''

class Student(object):
	pass

# 给实例绑定一个属性
s = Student()
s.name = 'Michael'
print(s.name)

# 给实例绑定一个方法
def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 但是，给一个实例绑定的方法，对另一个实例不起作用
s2 = Student()
# s2.set_age(25)

# 给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
	self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)

'''
	使用__slots__限制实例的属性
'''
class Student(object):
	__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25
# 绑定属性‘score’，得到AttributeError错误
# s.score = 99

# 使用__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类也定义__slots__,子类实例允许定义的属性就是自身__slots__加上父类的__slots__
class GraduateStudent(Student):
	pass
g = GraduateStudent()
g.score = 9999
print(g.score)

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# class Student 继承于 object 类
class Student(object):
	pass

bart = Student()
print(bart)
print(Student)

bart.name = 'Bart Simpson'
print(bart.name)

class Student1(object):

	def __init__(self, name, score):
		self.name = name;
		self.score = score;


b = Student1('b', 59)
print(b.name)
print(b.score)

def print_score(std):
	print('%s: %s' % (std.name, std.score))

print_score(b)

class Student2(object):
	
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))
		
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

s = Student2('renwotao', 22)
s.print_score()
print(s.get_grade())

'''
	Python 允许对实例变量绑定任何数据,
	对于两个实例变量，虽然它们都是同一类的不同实例,
	但拥有的变量名称都可能不同
'''
s.age = 33
print(s.age)

lisa = Student2('lisa', 99)
print(lisa.age)



#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	@property
'''

# 限制score的范围
class Student(object):
	
	def get_score(self):
		return self._score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

s = Student()
s.set_score(60)
print(s.get_score())

s.set_score(9999)

# Python内置@property装饰负责把一个方法变成属性调用
class Student(object):
	
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value


s = Student()
s.score = 60
print(s.score)
s.score = 9999

# 只定义getter方法，不定义setter方法就是一个只读属性
class Student(object):
	
	@property
	def birth(self):
		return self._birth
	
	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2015 - self._birth
# birth是可读写属性，而age就是一个只读属性，age可以根据birth和当前时间计算处理
	

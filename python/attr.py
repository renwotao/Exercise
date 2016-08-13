#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	实例属性和类属性
'''

# Python是动态语言，根据类创建的实例可以任意绑定属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量

class Student(object):
	def __init__(self, name):
		self.name = name;

s = Student('Bob')
s.score = 90

# 如果Student类本身需要绑定一个属性，可以直接在class中定义属性，归Student类所有
class Student(object):
	name = 'Student'

# 创建实例s
s = Student()
# 打印name属性，因为实例并没有name属性，所以会继续需查找class的name属性
print(s.name)
# 打印类的name属性
print(Student.name)
# 给实例绑定name属性
s.name = 'Michael'
# 由于实例属性优先级比类属性高，因此，它会屏蔽掉的name属性
print(s.name)
# 但类属性并未消失，用Student.name仍然可以访问
print(Student.name)
# 删除实例的name属性
del s.name
# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来
print(s.name)


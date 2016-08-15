#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	Enum
		可以把一组相关敞亮定义在一个class中，且class不可变，
		且成员可以直接比较
'''

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
		'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

# value属性自动赋给成员的int敞亮，默认从1开始计数

# 更精确的控制枚举类型，可以从Enum派生出自定义类
from enum import Enum, unique

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Web = 3
	Thu = 4
	Fri = 5
	Sat = 6
# unique 装饰其可以帮助检查保证没有重复值

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(Weekday(1))
print(day1 == Weekday(1))
# weekday(7) # 报错

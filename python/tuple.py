#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	tuple
		tuple和list非常类似，但是tupe初始化就不能修改
'''

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

'''
 定义1个元素的tupe
t = (1) #错误，()既可以表示tupe,又可以表示数学公式中的小括号
	这就产生了歧义，因此Python 规定，这种情况下，按小括号进行计算
	计算结果自然是1
'''
t = (1,)
print(t)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)



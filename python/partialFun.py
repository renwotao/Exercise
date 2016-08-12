#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''
	偏函数
'''

# int()函数可以把字符串转换为整数
print(int('12345'))

# int()函数提供额外的base参数，默认值为10
print(int('12345', base=8))
print(int('12345', 16))

def int2(x, base=2):
	return int(x, base)

print(int2('1000000'))
print(int2('1010101'))

# functools.partial就是创建一个偏函数，不需要自己定义int2()
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))


max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
max2 = functools.partial(max, 2)
print(max2(5, 6, 7))

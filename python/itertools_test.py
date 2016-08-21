#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	itertools
		Python 的内建模块 itertools 提供用于操作迭代对象的函数。
'''
# count() 会创建一个无限的迭代器，无法停止，只能按 Ctrl + c 退出
import itertools
natuals = itertools.count(1)
for n in natuals:
	print(n)
cs = itertools.cycle('ABC') #　注意字符串也是序列的一种
for c in cs:
	print(c)

# 第二个参数就可以限定重复次数
ns = itertools.repeat('A', 3)
for n in ns:
	print(n)

'''
	无限序列只有在 for 迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
	无限序列虽然可以无限迭代下去，但是可以通过 takewhile() 等函数根据条件判断来截取出一个有限的序列
'''
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

'''
	itertools.chain()
		可以把一组迭代对象串联起来，形成一个更大的迭代器
'''
for c in itertools.chain('ABC', 'XYZ'):
	print(c)

'''
	itertools.groupby()
		把迭代器中相邻的重复元素跳出来放在一起
'''
for key, group in itertools.groupby('AAABBBCCAAA'):
	print(key, list(group))


for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
	print(key, list(group))

'''
	itertools 模块提供的全部是处理迭代功能的函数，它们的返回值不是 list，
	而是 Iterator，只有用 for 循环迭代的时候才真正计算。
'''

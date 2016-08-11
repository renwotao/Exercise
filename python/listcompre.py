#! /usr/bin/env python3
# -*- coding:utf-8 -*-

print(list(range(1, 11)))

L = []
for x in range(1, 11):
	L.append(x * x)
print(L)

'''
	List Comperehensions
'''
print([x * x for x in range(1, 11)])

print([m + n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])

d = {'x':'A', 'y':'B', 'z':'C'}
for k, v in d.items():
	print(k, '=', v)
print(d.items())

print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

x = 'abc'
print('abc is str', isinstance(x, str))
y = 123
print('123 is str', isinstance(y, str))

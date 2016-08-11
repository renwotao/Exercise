#!/usr/bin/env python3
# -*- coding:utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print([L[0], L[1], L[2]])

r = []
n = 3
for i in range(n):
	r.append(L[i])
print(r)

'''
	Slice
'''
print(L[0:3])

# 如果第一个索引是0，可以省略
print(L[:3])

print(L[1:3])

# 取倒数第一个元素 L[-1]
print(L[-2:])
print(L[-2:-1])


L = list(range(100))
print(L)
# 前10个数，每两个取一个
print(L[:10:2])

# 每5个取一个
print(L[::5])

print(L[:])

# tuple
print((0, 1, 2, 3, 4, 5)[:3])

print('ABCDEFG'[:3])
print('ABCDEFG'[::2])


#!/usr/bin/env python3
#-*-coding:utf-8-*-

s = set([1, 2, 3])
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)

# 交集并集操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print('s1 & s2: ', s1 & s2)
print('s1 | s2: ', s1 | s2)

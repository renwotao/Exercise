#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0], classmates[1], classmates[1])

# get element from last to first
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

'''
list methods:
	append
	insert
	pop
'''
print(classmates.append('Adam'))
print(classmates.insert(1, 'Jack'))
print(classmates.pop())
# delete i index of list
print(classmates.pop(1))

# assign with "="
classmates[1] = 'Sarah'
print(classmates)

# different element in list
L = ['Apple', 123, True]
print(L)
	# list can contains list
s = ['python', 'java', ['asp', 'php'], 'sheme']
print(len(s))
print(s)

L = []
print(len(L))





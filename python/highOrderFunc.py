#! /usr/bin/env python3
# -*- coding:utf-8 -*-

print(abs(-10))
f = abs
print(f)
print(f(-10))

def add(x, y, f):
	return f(x) + f(y)

print(add(-5, 6, abs))


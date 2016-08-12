#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
	filter
		filter接收一个函数和一个序列
		filter把传入的函数依次作用于每个元素，根据返回值是True还是False
		决定保留还是丢弃该元素
		filter函数返回是一个Iterator，也是一个惰性序列
'''
def is_odd(n):
	return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
	return s and s.strip()

print(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))

'''
	用filter求素数
'''
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter() # 初始序列
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)
# primes()是一个无限序列，设置一个退出循环条件
for n in primes():
	if n < 1000:
		print(n)
	else:
		break

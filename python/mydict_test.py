#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
	单元测试使用来对一个模块，一个函数或这一个类进行正确性检验的测试工作
'''

import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
	
	def setUp(self):
		print('setUp...')

	def tearDown(self):
		print('tearDown...')
	
	def test_init(self):
		d = Dict(a = 1, b ='test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']
	
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

'''
	以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，
	测试的时候不会被执行。
	
	setUp()和tearDown()方法
		这两个方法会分别在每调用一个测试方法的前后分别执行
	作用：
	设想测试需要启动一个数据库，可以在setUp()方法中连接数据库
	在tearDown()方法中关闭数据库，不izaizai每个测试方法中重复相同的代码
'''

if __name__ == '__main___':
	unittest.main()


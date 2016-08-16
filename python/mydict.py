#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
	单元测试使用来对一个模块，一个函数或这一个类进行正确性检验的测试工作
'''
class Dict(dict):
	
	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'"%key)

	def __setattr__(self, key, value):
		self[key] = value


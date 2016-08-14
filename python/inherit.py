#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	pass

class Mammal(Animal):
	pass
class Bird(Animal):
	pass

class Dog(Mammal):
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass


class Runnale(object):
	def run(self):
		print('Running...')

class Flyable(object):
	def fly(self):
		print('Flying...')

class Dog(Mammal, Runnable):
	pass

class Bat(Mammal, Flyable):
	pass

'''
	Mixln 混合类型；混进；糅合
'''
class RunnableMixIn(object):
	def run(self):
		print('Running...')

class FlyableMixIn(object):
	def fly(self):
		print('Flying...')

class CarnivorousMixIn(object):
	def eat(self):
		print('Eat meating...')

class HerbivoresMixIn(object):
	def eat(self):
		print('Eat plants...')

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
	pass


class Dog(Mammal, RunnableMixIn, 

'''
	Python 自带很多库液使用了MixIn
'''

class MyTCPServer(TCPServer, ForkingMixIn):
	pass

class MyUDPServer(UDPServer, ThreadingMixIn):
	pass

class MyTCPServer(TCPServer, CoroutineMixIn):
	pass


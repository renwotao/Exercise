#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	
	def run(self):
		print('Dog is running...')
	
	def eat(self):
		print('Eating meat...')

class Cat(Animal):
	
	def run(self):
		print('Cat is running...')
		

dog = Dog()
dog.run()
cat = Cat()
cat.run()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))


def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Animal())
run_twice(Dog())


class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')

run_twice(Tortoise())



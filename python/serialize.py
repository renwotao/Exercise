#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	serialization
	
	把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling。
	序列化之后就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
	返回过，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpicking
'''

# pickle模块
import pickle
d = dict(name='Bob', age=20,score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后再把bytes写入文件。
print(pickle.dumps(d))

# 或者pickle.dump()直接把对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

'''
	把对象从磁盘读到内存，可以先把内容读到一个bytes，
	然后用pickle.loads()方法反序列化对象，
	也可以直接用pickle.load()方法从一个file-like Object中直接反序列化处对象
	
'''

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)


'''
	JSON
'''
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age":20, "score":88, "name":"Bob"}'
print(json.loads(json_str))

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

s = Student('Bob', 20, 88)

# TypeError
#print(json.dumps(s))

def student2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}
print(json.dumps(s, default=student2dict))

print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
	return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

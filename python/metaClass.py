#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	type
'''
# 动态语言和静态语言最大的不同，就是函数和类的定义，
# 不是编译时定义的，而是运行时动态创建的

# 举例
class Hello(object):
	def hello(self, name='world'):
		print('Hello, %s.' % name)

h = Hello()
# type()函数可以查看一个类型或变量的类型
print(type(Hello)) # Hello是一个class，它的类型就是type
print(type(h))     # h就是一个实例

'''
	class 的定义是运行时动态创建的，创建class的方法就是使用type()函数
	type()函数既可以返回一个对象的类型，有可以创建出新的类型
	例如：通过type()函数创建出Hello类，无需通过class Hello(object)..定义
'''
def fn(self, name='world'):
	print('Hello, %s.' %name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

'''
	要创建一个class对象，type()函数依次传入3个参数：
	1. class的名称
	2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，
	别忘了tuple的单元素写法
	3. class的方法名称与函数绑定，这里把函数fn绑定到方法名hello上
'''

'''
	通过type()函数创建的类和直接写class是完全一样的，
	因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，
	然后调用type()函数创建出class
'''

'''
	正常情况下，我们都用class Xxx...来定义类，但是，
	type()函数也允许我们动态创建出类来。
	动态语言本身支持运行期动态创建类，这个静态语言又非常大的不同，
	要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，
	或者借助一些工具生成字节码，本质上都是动态编译，会非常复杂。
'''

'''
	metaclass
		直译为元类
'''
'''
	定义类之后，根据这个类可以创建实例，所以先定义类，然后创建实例
	如果创建类呢？根据metaclass创建处类，所以先定义metaclass，然后创建类
	
	连接起来就是：先定义metaclass，就可以创建类，最后创建实例
	metaclass允许创建类或者修改类。类可以看成是metaclass穿件出来的“实例”
'''

# metaclass是类的模板，所以必须从'type'类型派生
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self,  value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
	pass

'''
	__new__()方法接收到的参数依次是：
	1.当前准备创建的类的对象；
	2.类的名字；
	3.类继承的父类集合；
	4.类的方法集合。
'''
L = MyList()
L.add(1)
print(L)

L2 = list()
# L2.add(1) # list类没有add()方法

'''	
	ORM全称"Object Relational Mapping",即对象-关系映射，
	就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，
	这样写代码更简单，不用直接操作SQL语句。
'''

class Field(object):
	
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type
	
	def __str___(self):
		return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
	
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
	
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
	
	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print('Found model: %s' % name)
		mappings = dict()
		for k, v in attrs.items():
			if isinstance(v, Field):
				print('Found mapping: %s ==> %s' % (k, v))
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		attrs['__table__'] = name # 假设表名和类名一致
		return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
		
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % str(args))

'''
	在ModelMetaclass中一共做了几件事：
	1. 排除掉对Model类的修改；
	2. 在当前类（比如User）中查找定义的类的所偶属性，如果找到一个Field属性，
	就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，
	否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
	3. 把表名保存在__table__中，这里简化为表明默认为类名
'''

class User(Model):
	# 定义类的属性到列的映射
	id = IntegerField('id')
	name = StringField('username')
	email =  StringField('email')
	password = StringField('password')

# 创建一个实例
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库
u.save()




















































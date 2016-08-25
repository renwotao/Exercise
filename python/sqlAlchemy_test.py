#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	SQLAlchemy
'''

'''
	数据库表是一个二维表，包含多行多列。
	把一个表的内容用Python的数据结构表示的话，可以用一个list表示多行，list 的每一个元素是 tuple，表示一行记录，比如，包含 id 和 name 的 user 表：

[
	('1', 'Michael'),
	('2', 'Bob'),
	('3', 'Adam')
]

	Python 的 DB-API 返回的数据结构就像上面的这样表示。

	但是用 tuple 表示一行很难看出表的结构。如果把一个 tupe 用 class 实例表示，就可以更容易看出表的结构：
	

class User(object):
	def __init__(self, id, name):
		self.id = id;
		self.name = name;
[
	User('1', 'Michael'),
	User('2', 'Bob'),
	User('3', 'Adam')
]

	这就是 ORM 技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。
	所以 ORM 框架应运而生。在 Python中，最有名的 ORM 框架是 SQLAlchemy。
'''

# 导入 SQLAlchemy，并初始化 DBSession
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义 User 对象
class User(Base):
	# 表的名字
	__tablename__ = 'user'

	# 标的结构
	id = Column(String(20), primary_key=True)
	name = Column(String(20))

# 初始化数据库连接
# SQLAlchemy 用字符串表示连接信息：
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# 创建 DBSession 类型
DBSession = sessionmaker(bind=engine)

'''
	添加一行记录
'''
# 创建 session 对象
session = DBSession()
# 创建新 User 对象
new_user = User(id='5', name='Bob')
# 添加到 session
session.add(new_user)
# 提交即保存到数据库
session.commit()
# 关闭 session
session.close()

'''
	从数据库表中查询数据
'''

# 创建 Session
session = DBSession()
# 创建 Query 查询，filter 是 where 条件，最后调用 one() 返回唯一行，如果调用 all() 则返回所有行
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的 name 属性
print('type:', type(user))
print('name:', user.name)
# 关闭 Session
session.close()
# ORM就是把数据库表的行与相应的对象建立关联，互相转换。

'''
	关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，
	ORM框架也可以提供两个对象之间的一对多、多对多等功能。
'''
# 如果一个 User 拥有多个 Book，就可以定义一对多的关系
class User(Base):
	__tablename__ = 'user'
	
	id = Column(String(20), primary_key=True)
	name = Column(String(20))
	
	# 一对多
	books = relationship('Book')

class Book(Base):
	__tablename__ = 'book'
	
	id = Column(String(20), primary_key=True)
	name = Column(String(20))
	# “多” 的一方的 book 表是通过外键关联到 user 表
	user_id = Column(String(20), ForeignKey('user.id'))


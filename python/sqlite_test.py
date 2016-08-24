#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	SQLite
	
	SQLite是一种嵌入式数据库，它的数据库就是一个文件。
	由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，
	甚至在iOS和Android的App中都可以集成。
'''

# Python内置了SQLite3

'''
	操作关系数据库，首先需要连接到数据库，一个数据库连接称为 Connection
	连接到数据库后，需要打开游标，称之为 Cursor，通过 Cursor 执行 SQL语句，获得执行结果。
'''

# 导入 SQLite 驱动
import sqlite3
# 连接到 SQLite3 数据库
# 数据库文件是 test.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')
# 创建一个 Cursor
cursor = conn.cursor()
# 执行一条 SQL 语句，创建 user 表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条 SQL 语句，插入一条记录
cursor.execute('insert into user (id, name) values(\'1\', \'Michael\')')
# 通过 rowcount 获得插入的行数
print(cursor.rowcount)

# 关闭 Cursor
cursor.close()
# 提交事物
conn.commit()
# 关闭连接
conn.close()


'''
	查询记录
'''
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句,使用 ? 占位符，有几个 ? 占位符就必须对应几个参数
cursor.execute('select * from user where id=?', ('1',))
# 获得查询结果集
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()


'''
	要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。

	如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？
	使用try:...except:...finally:...的用法。
'''

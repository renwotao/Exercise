#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	MySQL
	
	MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。
'''

# 导入 MySQL 驱动
import mysql.connector
# 注意把 password 设为你的 root 口令
conn = mysql.connector.connect(user='root', password='123456', database='test')
cursor = conn.cursor()

# 创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意 MySQL 的占位符是 %s
cursor.execute('insert into user (id, name) values(%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)
# 提交事物
conn.commit()
cursor.close()
# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1'))
values = cursor.fetchall()
print(values)
# 关闭 Cursor 和 Connection
cursor.close()
conn.close()

'''
	

    执行INSERT等操作后要调用commit()提交事务；

    MySQL的SQL占位符是%s。

'''



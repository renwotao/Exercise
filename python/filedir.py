#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	操作文件和目录
'''
import os
print(os.name) # posix说明是linux/unix/mac os x，nt就是windows

print(os.uname())

'''
	环境变量
'''
print(os.environ)

print(os.environ.get('PATH'))

'''
	操作文件和目
'''

# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
print(os.path.join('/home/renwotao', 'testdir'))
# '/home/renwotao/testdir'

# 然后创建一个目录
print(os.mkdir('/home/renwotao/testdir'))
# 删掉一个目录
print(os.rmdir('/home/renwotao/testdir'))

'''
	合并路径：
	把两个路径合成一个时，不要直接拼字符串，而是通过os.path.join()函数，
	这样可以正确处理不同操作系统的路径分隔符。

	在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
	part-1/part-2
	
	而Windows下会返回这样的字符串：
	part-1\part-2

	拆分路径：
	要拆分路径时，也不要直接取拆分字符串，而是通过os.path.split()函数，
	这样可以把路ing拆分为两部分，后一部分是最后级别的目录或文件名	
'''
print(os.path.split('/home/renwotao/testdir/file.txt'))
# 得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))

# 对文件重命名
print(os.rename('test.txt', 'test.py'))
print(os.remove('test.py'))

# 复制文件函数不在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用

# shutil模块提供copyfile()函数
# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

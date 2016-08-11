#!/usr/bin/env python3

# 告诉python解释器，按照utf-8编码读取源代码，
# 但源代码保存格式为utf-8 without BOM
# -*- coding: utf-8 -*-

# Unicode 编码
print('包含中文的str')

# ord() 函数获取字符的整数表示
print(ord('A')) # output: 65

# chr() 函数把编码转换为对应的字符
print(chr(66)) # output:'B'
print(chr(25991)) # output: '文'

print('\u4e2d\u6587') # output: 中文

# python的字符串类型是str,在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

x = b'ABC'
print(x) 
# 注意区分'ABC'和b'ABC',前者是str，两者内容显示一样，但bytes的每个字符都只占用一个字节。

# Uicode表示str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii')) # output: b'ABC'

print('中文'.encode('utf-8')) # output: b'\xe4\xb8\xad\xe6\x96\x87'
# print('中文'.encode('ascii') # output: UnicodeEncodeError

# bytes转为str需要使用 decode()
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 计算str包含多少个字符，可以用len()函数
print(len('AB')) # output: 3
print(len('中文')) # output: 2

print(len(b'ABC')) # output: 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87')) # output: 6
print(len('中文'.encode('utf-8'))) # output: 6

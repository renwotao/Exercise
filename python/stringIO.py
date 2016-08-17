#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	StringIO
		顾名思义，在内存中读写str,类似于c++的stringstram
'''

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

f1 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f1.readline()
	if s == '':
		break;
	print(s.strip())

'''
	BytesIO
		StringIO操作只能是str，操作二进制数据就需要BytesIO
'''
from io import BytesIO
f2 = BytesIO()
f2.write('中文'.encode('utf-8'))
print(f2.getvalue())

f3 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f3.read()

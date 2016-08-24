#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	struct
		Python 没有专门处理字节的数据类型。
		但由于 str 既是字符串，有可以表示字节，所以字节数组=str。
		在 C 语言中，可以用 struct，union来处理字节，以及字节和 int，float的转换。
'''

# 把一个 32 位无符号整数变成字节，也就是 4 个长度的 bytes
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)

# struct 模块来解决 bytes 和其他二进制数据类型的转换
import struct
print(struct.pack('>I', 10240099))
'''
	pack 的第一个参数是处理执行，'>I' 的意思是：
	> 表示字节顺序是 big-endian，也就是网络序，I 表示 4 字节无符号整数
	
'''
# >IH 的说明，后面的 bytes 依次变为 I: 4字节无符号整数和 H: 2字节无符号整数
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

'''
	分析 Windows 的位图 bmp 文件
'''
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', s))

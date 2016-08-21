#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	hashlib
		Python的摘要算法，如MD5，SHA1等
		
	什么是摘要算法呢？
	摘要算法又称哈希算法，散列算法。
	它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
'''
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量很大，可以分块多次调用 update(),最后计算的结果是一样的
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

'''
	MD5是最常见的摘要算法，速度很快，生成结果是固定的 128 bit 字节，
	通常用一个 32 位的 16 进制字符串表示。
'''

# 摘要算法 SHA1
import hashlib
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

'''
	SHA1 的结果 160 bit 字节，通常用一个 40 位的 16 进制字符串表示。
	比 SHA1 更安全的算法是 SHA256 和 SHA512，不妥越安全的算法不仅越慢，而且摘要长度更长。

	通过不同摘要算法可能得到相同的摘要！
'''

'''
	摘要的应用：
	
	网站用户数据库存储用户口令摘要，而不是用户口令明文。
	简单使用能摘要得到用户口令摘要，容易被黑客破解（通过预先计算普通密码的摘要进行爆破），
	由于常用口令的 MD5 值很容易被计算出来，可以通过对原始口令加一个复杂字符串来实现，俗称“加盐”。
	经过 Salt 处理的 MD5 口令，只要 Salt 不被黑客知道，即使输入简单口令，也很难通过 MD5 反推明文口令。
'''





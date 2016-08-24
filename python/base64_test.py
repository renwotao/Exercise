#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	Base64
		Base64是一种最常见的二进制编码方法
'''
import base64
encode = base64.b64encode(b'binary\x00string')
print(encode)
decode = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(decode)

'''
	由于标准的Base64编码后可能出现 + 和 /，在 URL 中就不能直接作为参数，
	所以又有一种 "url safe" 的 base64 编码，其实就是把字符 + 和 / 分别变成 -
 和 _
'''
safe_encode = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(safe_encode)
safe_decode = base64.b64decode('abcd--__')

'''
	Base64 是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
	Base64 适用于小段内容的编码，比如数字证书签字,Cookie 的内容。
	由于 = 字符也可能出现在 Base64 编码中，但 = 用在 URL，Cookie里面会造成歧义，
	所以很多 Base64 编码后会把 = 去掉
'''
# 标准 Base64: 'abcd' -> 'YWJjZA=='
# 自动去掉 =: 'abcd' -> 'YWJjZA'

'''
	去掉 = 后怎么解码?
	因为 Base64 是把 3 个字节变为 4 个字节，所以，Base64 编码的长度永远是 4 的倍数，
	因此，需要加上 = 把 Base64 字符串的长度变为 4 的倍数，就可以正常解码。
'''




#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	XML

	操作 XML 有两种方式：DOM vs SAX
	
	DOM 会把整个 XML 读入内存，解析为树，因此占用内存大，解析慢，有点是可以任意遍历树的节点。
	SAX 是流模式，边读边解析，占用内存小，解析快，缺点是需要自己处理事件。

	正常情况，优先考虑 SAX，因为 DOM 实在太占内存。
'''

'''
	Python 中使用 SAX 解析 XML 非常简洁，通常关心的事件是 tart_element, 
	end_element 和 char_data, 准备这3个函数，就可以解析 xml。
'''
'''
	举个例子，当 SAX 解析器读到一个节点时：
	<a href = "/"> python </a>
	会产生 3 个事件：
	1. start_element 事件，在读取 <a href="/"> 时；
	2. char_data 事件，在读取 python 时；
	3. end_element 事件，在读取 </a> 时。
'''

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
	
	def end_element(self, name):
		print('sax:end_element: %s' % name)
	
	def char_data(self, text):
		print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
	<li><a href="/python">Python</a></li>
	<li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 生成 XML
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append('hello')
L.append(r'</root>')
print(L)

'''
	如果要生成复杂的 XML 呢？
	建议不要用 XML，改成 JSON。
'''


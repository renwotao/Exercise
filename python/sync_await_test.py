#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	async 
	await
'''
# 更好的标识异步 IO，Python3.5 引入新的语法
# 1.把 @asyncio.coroutine 替换为 async
# 2.把 yield from 替换为 await

import asyncio

@asyncio.coroutine
def hello():
	print("Hello world!")
	r = yield from asyncio.sleep(1)
	print("Hello again!")

# 新语法重新编写
async def hello():
	print("Hello world!")
	r = await asyncio.sleep(1)
	print("Hello again!")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()

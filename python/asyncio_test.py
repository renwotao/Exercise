#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    asyncio
        asyncio 的编程模型就是一个消息循环。
        从 asyncio 模块中直接获取一个 EventLoop 的引用，然后把需要的执行协程扔到 EventLoop 中执行，就实现了异步 IO。
'''

import asyncio

@asyncio.coroutine
def hello():
        print("Hello world!")
        # 异步调用 asyncio.sleep(1)
        r = yield from asyncio.sleep(1)
        print("Hello again!")

# 获取 EventLoop
loop = asyncio.get_event_loop()
# 执行 coroutine
loop.run_until_complete(hello())
#loop.close()

'''
    @asyncio。corountine 把一个 generator 标记为 coroutine 类型
    yield from 语法可以调用另一个 generator。
    由于 asyncio.sleep() 也是一个 coroutine，所以线程不会等待 asyncio.sleep(),
    而是直接中断并执行下一个消息循环。
    当 asyncio.sleep() 返回时， 线程就可以从 yield from 拿到返回值（此处时 None),然后接着执行下一句。
    把 asyncio.sleep(1) 看成一个耗时 1 秒的 IO 操作，在此期间，主线程并未等待，
    而是去执行 EventLoop 中其他可以执行的 coroutine 了，因此可以实现并发执行。
'''

import threading
import asyncio
@asyncio.coroutine
def hello():
        print('Hello world! (%s)' % threading.currentThread())
        yield from asyncio.sleep(1)
        print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
#loop.close()

'''
    打印的当前线程名称可以看出，两个 coroutine 是由同一个线程并发执行。
    如果把 asyncio.sleep() 换成真正的 IO 操作，则多个coroutine 就可以由一个线程并发执行。
'''

'''
    用 asyncio 的异步网络连接来获取 sina，sohu 和 163 的网站首页。
'''
import asyncio

@asyncio.coroutine
def wget(host):
        print('wget %s...' % host)
        connect = asyncio.open_connection(host, 80)
        reader, writer = yield from connect
        header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
        writer.write(header.encode('utf-8'))
        yield from writer.drain()
        while True:
                line = yield from reader.readline()
                if line == b'\r\n':
                    break;
                print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        # Ignore the body, close the socket
        writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	分布式进程
	distributed processes
'''

'''
	在Thread和Process中，应当优选Process，因为Process更稳定，
	而且Process可以分不到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上
	Python的multiprocess木块不但支持多进程，其中managers子模块还支持把夺金称分不到多台机器上。
	一个服务进程可以作为调度这，将任务分不到其他多个进程中，依靠网络通信。
'''

'''
	实现分布式进程
'''
# task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
	pass

# 把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000，设置验证码'abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去
for i in range(10):
	n = random.randint(0, 10000)
	print('Put task %d...' % n)
	task.put(n)
# 从result队列读取结果
print('Try get result...')
for i in range(10):
	r = result.get(timeout=10)
	print('Result: %s' % r)
# 关闭
manager.shutdown()
print('master exit.')


#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	multithreads
		Python两种模块：_thread和threading
		_thread是低级模块
		threading是高级模块，对_thread进行了封装

'''
import time, threading

# 新线程执行的代码
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('Thread %s ended.', threading.current_thread().name)


'''
	Lock
'''
import time, threading

# 假定这是你的银行存款
balance = 0

def change_it(n):
	# 先存取后取，结果应该为0
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for i in range(100000):
		change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

balance = 0
lock = threading.Lock()

def run_thread1(n):
	for i in range(100000):
		# 先要获取锁
		lock.acquire()
		try:
			# 放心地改
			change_it(n)
		finally:
			# 改完了一定释放锁
			lock.release()

t1 = threading.Thread(target=run_thread1, args=(5,))
t2 = threading.Thread(target=run_thread1, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


'''
	多核CPU
'''

'''
	如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个线程。

	如果写一个死循环的话，会出现什么情况呢？

	打开Mac OS X的Activity Monitor，或者Windows的Task Manager，
	都可以监控某个进程的CPU使用率。

	我们可以监控到一个死循环线程会100%占用一个CPU。

	如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，
	也就是占用两个CPU核心。

	要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。
'''
# 死循环
import threading, multiprocessing

def loop():
	x = 0
	while True:
		x = x^1

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target=loop)
	t.start()

'''
	启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，		也就是仅使用了一核。

	但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，
	4核就跑到400%，8核就跑到800%，为什么Python不行呢？

	因为Python的线程虽然是真正的线程，但解释器执行代码时，
	有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，
	必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，
	让别的线程有机会执行。
	这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
	所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，
	也只能用到1个核。

	GIL是Python解释器设计的历史遗留问题，
	通常我们用的解释器是官方实现的CPython，
	要真正利用多核，除非重写一个不带GIL的解释器。

	所以，在Python中，可以使用多线程，但不要指望能有效利用多核。
	如果一定要通过多线程利用多核，那只能通过C扩展来实现，
	不过这样就失去了Python简单易用的特点。

	不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，
	但可以通过多进程实现多核任务。
	多个Python进程有各自独立的GIL锁，互不影响。
'''

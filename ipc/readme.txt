ipc:
pipe
fifo
semaphore
shared memory ： 访问速度快于其他进程间通信机制，因为shared memory在访问数据时只在进程的用户空间，而不必切换到内核空间调用内核服务。
message queue

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-22 上午9:23

# 进程共享同一块屏幕，打印输出时如果不加锁会穿插打印
from multiprocessing import Process, Lock


def f(lock, i):
	lock.acquire()
	print('hello word', i)
	lock.release()

if __name__ == '__main__':
	lock = Lock()

	for num in range(100):
		p = Process(target=f, args=(lock, num))
		p.start()

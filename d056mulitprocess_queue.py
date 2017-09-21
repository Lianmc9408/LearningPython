#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-21 下午10:22


# 不同进程间内存是不共享的
# 要想实现两个进程间的数据交换，可以用以下方法：
# Queues
# 使用方法跟threading里的queue类似：
from multiprocessing import Process, Queue


def f(q, n):
	q.put([42, n, 'hello'])


if __name__ == '__main__':
	q = Queue()
	p_list = []
	for i in range(3):
		# 共用的变量放进args参数里面
		p = Process(target=f, args=(q, i))
		p_list.append(p)
		p.start()
	print(q.get())
	print(q.get())
	print(q.get())
	for i in p_list:
		i.join()

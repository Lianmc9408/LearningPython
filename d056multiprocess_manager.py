#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-21 下午10:49

# Manager  管理者
from multiprocessing import Process, Manager


def f(d, l, n):
	d[n] = '1'
	d['2'] = 2
	d[0.25] = None
	l.append(n)
	print(l)


if __name__ == '__main__':
	with Manager() as manager:
		# d = {}
		d = manager.dict()

		l = manager.list(range(5))
		p_list = []
		for i in range(10):
			p = Process(target=f, args=(d, l, i))
			p.start()
			p_list.append(p)
		for res in p_list:
			res.join()

		print(d)
		print(l)

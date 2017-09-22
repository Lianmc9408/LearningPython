#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-21 下午6:48

# 参考：http://www.cnblogs.com/yuanchenqi/articles/5745958.html
# http://www.cnblogs.com/alex3714/articles/5230609.html
from multiprocessing import Process
import time


def f(name):
	time.sleep(1)
	print('hello', name, time.ctime())


if __name__ == '__main__':
	p_list = []
	for i in range(3):
		p = Process(target=f, args=('alvin',))
		p_list.append(p)
		p.start()
	for i in p_list:
		i.join()
	print('end')

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-21 下午6:59

# To show the individual process IDs involved
# here is an expanded example


from multiprocessing import Process
import os
import time


def info(title):
	print(title)
	print('module name:', __name__)  # main
	print('parent process:', os.getppid())  # 父进程ID
	print('process id:', os.getpid())  # 进程ID


def f(name):
	info('\033[31;1mfunction f\033[0m')
	print('hello', name)

# windows创建进程必须加__name__ == '__main__，否则报错
# Linux可以不加
if __name__ == '__main__':
	info('\033[32;1mmain process line\033[0m')
	time.sleep(3)
	p = Process(target=info, args=('bob',))
	p.start()
	p.join()

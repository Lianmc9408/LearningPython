#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-22 上午9:28

# 进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，
# 如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。

# 进程池中有两个方法：
# apply  同步执行：串行
# apply_async  异步执行：并行

from multiprocessing import Process, Pool
import time
import os


def Foo(i):
	time.sleep(2)
	print('in the process',os.getpid())
	return i + 100

# callBack时是主进程执行回调函数的
def Bar(arg):
	print('-->exec done:', arg)


if __name__ == '__main__':
	pool = Pool(5)
	for i in range(10):
		# 并行
		pool.apply_async(func=Foo, args=(i,), callback=Bar)
		# 串行
		# pool.apply(func=Foo, args=(i,))
	print('end')
	pool.close()
	pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。

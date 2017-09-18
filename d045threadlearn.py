#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-18 下午6:35'

import time
import threading


def foo(n):
	print('foo%s' % n)
	time.sleep(1)


def bar(n, a):
	print('bar%s,%s' % (n, a))
	time.sleep(2)


# 创建子线程对象，target参数为方法名，args为方法需要的参数组成的元祖
t1 = threading.Thread(target=foo, args=(1,))
t2 = threading.Thread(target=bar, args=(2, 3))

# 开启线程
t1.start()
t2.start()

# 指在一线程里面调用另一线程join方法时，表示将本线程阻塞直至另一线程终止时再执行
t1.join()
t2.join()

# 此行在主线程中
print('.....in the main.......')

# 指在一线程里面调用另一线程join方法时，表示将本线程阻塞直至另一线程终止时再执行
# t1.join()
# t2.join()

# join放在main线程的print()函数前后有不同的效果

# t1,t2,main三个线程在同时执行

# IO密集型任务或函数    计算密集型任务或函数(如计算1到1亿的和)
# 计算密集型任务串行比并行要快，因为线程间的不断切换会浪费大量时间
# 因为Python是全局解释性语言，只能使用到单颗CPU
# 可以使用多进程代替多线程

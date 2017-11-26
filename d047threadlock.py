#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-19 上午10:03

# import time
# import threading
#
# num = 100  # 设定一个共享变量
# thread_list = []
#
#
# def addnum():
# 	global num  # 在每个线程中都获取这个全局变量
# 	# num-=1
#
# 	temp = num
# 	print('--get num:', num)
# 	time.sleep(0.1)  # sleep()前后结果不同
# 	num = temp - 1  # 对此公共变量进行-1操作
#
#
# for i in range(100):
# 	t = threading.Thread(target=addnum)
# 	t.start()
# 	thread_list.append(t)
#
# for t in thread_list:  # 等待所有线程执行完毕
# 	t.join()
#
# print('final num:', num)

# -------------------------------------------------------

import time
import threading

num = 100  # 设定一个共享变量
thread_list = []
lock = threading.Lock()


def addnum():
    global num  # 在每个线程中都获取这个全局变量
    # num-=1

    # 加锁不加锁结果不同
    lock.acquire()  # 加锁，在release()之前不释放，cpu不切换线程，相当于串行了
    temp = num
    print('--get num:', num)
    time.sleep(0.00001)  # sleep()前后结果不同
    num = temp - 1  # 对此公共变量进行-1操作

    lock.release()  # 释放锁，cpu可以切换线程了


for i in range(100):
    t = threading.Thread(target=addnum)
    t.start()
    thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
    t.join()

print('final num:', num)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-19 上午9:48

import threading
import time


class MyThread(threading.Thread):
	def __init__(self, num):
		threading.Thread.__init__(self)
		self.num = num

	def run(self):  # 定义每个线程要运行的函数(执行父类的start方法时会调用这个方法)

		print("running on number:%s" % self.num)

		time.sleep(3)


if __name__ == '__main__':
	t1 = MyThread(1)
	t2 = MyThread(2)
	t1.start()
	t2.start()

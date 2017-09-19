#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-19 上午11:12

# import threading, time
#
#
# class myThread(threading.Thread):
# 	def doA(self):
# 		lockA.acquire()
# 		print(self.name, "gotlockA", time.ctime())
# 		time.sleep(3)
# 		lockB.acquire()
# 		print(self.name, "gotlockB", time.ctime())
# 		lockB.release()
# 		lockA.release()
#
# 	def doB(self):
# 		lockB.acquire()
# 		print(self.name, "gotlockB", time.ctime())
# 		time.sleep(2)
# 		lockA.acquire()
# 		print(self.name, "gotlockA", time.ctime())
# 		lockA.release()
# 		lockB.release()
#
# 	def run(self):
# 		self.doA()
# 		self.doB()
#
# # 造成死锁的程序
# if __name__ == "__main__":
#
# 	# 单独创建的锁
# 	lockA = threading.Lock()
# 	lockB = threading.Lock()
#
# 	# 递归锁
# 	# lock = threading.RLock()
#
# 	threads = []
# 	for i in range(5):
# 		threads.append(myThread())
# 	for t in threads:
# 		t.start()
# 	for t in threads:
# 		t.join()  # 等待线程结束，后面再讲。

# ---------------------------------------------------

import threading, time


class myThread(threading.Thread):
	def doA(self):
		lock.acquire()
		print(self.name, "gotlockA", time.ctime())
		time.sleep(3)
		lock.acquire()
		print(self.name, "gotlockB", time.ctime())
		lock.release()
		lock.release()

	def doB(self):
		lock.acquire()
		print(self.name, "gotlockB", time.ctime())
		time.sleep(2)
		lock.acquire()
		print(self.name, "gotlockA", time.ctime())
		lock.release()
		lock.release()

	def run(self):
		self.doA()
		time.sleep(0.1)  # 用于比较A～B和cpu线程切换的速度快慢
		self.doB()


if __name__ == "__main__":

	# 单独创建的锁
	# lockA = threading.Lock()
	# lockB = threading.Lock()

	# 递归锁
	lock = threading.RLock()

	threads = []
	for i in range(5):
		threads.append(myThread())
	for t in threads:
		t.start()
	for t in threads:
		t.join()  # 等待线程结束，后面再讲。

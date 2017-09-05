#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-5 下午10:34

# 装饰器(decorator)
# 定义：本质还是函数,用于装饰其他函数，为其他函数添加附加功能
# 原则：不能修改被装饰的函数的源代码
# 		不能修改被装饰的函数的调用方式

# 实现装饰器：1、函数即‘变量’
#           2、高阶函数、嵌套函数
#           高阶函数+嵌套函数=》 装饰器
import time


def timmer(func):
	def warpper(*args, **kwargs):
		start_time = time.time()
		func()
		stop_time = time.time()
		print('the func run time is %s ' % (stop_time - start_time))
	return warpper

@timmer
def test1():
	time.sleep(3)
	print('in func test1')

test1()
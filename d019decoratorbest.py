#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-6 上午10:41

# 装饰器(decorator)
# 定义：本质还是函数,用于装饰其他函数，为其他函数添加附加功能
# 原则：不能修改被装饰的函数的源代码
# 		不能修改被装饰的函数的调用方式

# 实现装饰器：1、函数即‘变量’
#           2、高阶函数、嵌套函数
#               高阶函数：把一个函数名当做实参传给另外一个函数
#                       返回值中包含函数名
#           高阶函数+嵌套函数=》 装饰器

import time


# 下面演示带参数的装饰器
def timmer(a):
	def atype(func):
		def wrapper(*args, **kwargs):
			if a == 'a':
				start_time = time.time()
				res = func(*args, **kwargs)
				stop_time = time.time()
				print('has benn load %s' % (stop_time - start_time))
				return res
			elif a == 'b':
				print('a == b')
				return 'xxz'

		return wrapper

	return atype


@timmer(a='a')
def test1(name):
	print(name, 'in the test1')


@timmer(a='b')
def test2(name):
	print(name, 'in the test2')
	return name


a = test2('zzx')
print(a)

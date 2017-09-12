#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-12 下午3:37

# AttributeError    试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
# IOError           输入/输出异常；基本上是无法打开文件
# ImportError       无法引入模块或包；基本上是路径问题或名称错误
# IndentationError  语法错误（的子类） ；代码没有正确对齐
# IndexError        下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
# KeyError          试图访问字典里不存在的键
# KeyboardInterrupt Ctrl+C被按下
# NameError         使用一个还未被赋予对象的变量
# SyntaxError       Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
# TypeError         传入对象类型与要求的不符合
# UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
# ValueError          传入一个调用者不期望的值，即使值的类型是正确的

dic = ["wupeiqi", 'alex']
try:
	dic[10]
except IndexError as e:
	print(e)

dic = {'k1': 'v1'}
try:
	dic['k20']
except KeyError as e:
	print(e)

s1 = 'hello'
try:
	int(s1)
except ValueError as e:
	print(e)
else:
	print('一切正常')
finally:
	print('不管有没有错，都执行')

s1 = 'hello'
try:
	int(s1)
except KeyError as e:
	print('键错误')
except IndexError as e:
	print('索引错误')
except Exception as e:
	print('错误')

# 异常其他结构
try:
	# 主代码块
	pass
except(KeyError) as e:
	# 异常时，执行该块
	pass
else:
	# 主代码块执行完，执行该块
	pass
finally:
	# 无论异常与否，最终执行该块
	pass

# 主动触发异常
try:
	raise Exception('错误了。。。')
except Exception as e:
	print(e)


# 自定义异常
class WupeiqiException(Exception):
	def __init__(self, msg):
		self.message = msg

	def __str__(self):
		return self.message


try:
	raise WupeiqiException('我的异常')
except WupeiqiException as e:
	print(e)

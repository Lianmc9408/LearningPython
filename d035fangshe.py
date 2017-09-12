#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-12 下午2:31

class Foo(object):
	def __init__(self):
		self.name = 'wupeiqi'

	def func(self, abc):
		return 'func'


obj = Foo()

# #### 检查是否含有成员 ####
hasattr(obj, 'name')
hasattr(obj, 'func')

# #### 获取成员 ####
getattr(obj, 'name')
getattr(obj, 'func')
func = getattr(obj, 'func')
func('abc')


# #### 设置成员 ####
setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)

# #### 删除成员 ####
delattr(obj, 'name')
delattr(obj, 'func')

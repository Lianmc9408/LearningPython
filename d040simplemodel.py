#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-14 上午11:23


# 单例模式
class Foo:
	__v = None

	@classmethod
	def get_instance(cls):
		if cls.__v:
			return cls.__v
		else:
			cls.__v = Foo()
			return cls.__v

obj = Foo.get_instance()

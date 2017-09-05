#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-5 下午4:11

# 匿名函数

# 高阶函数例子,f函数作为一个参数传给add


def add(a, b, f):
	return f(a) + f(b)


res = add(3, -6, abs)
print(res)

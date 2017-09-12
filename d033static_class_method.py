#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-11 上午9:30

# @staticmethod
# 静态方法：名义上归类管理的方法，实际上在静态方法里访问不了类或实例中的任何属性
#       可以用于做工具包，如os模块

# @classmethod
# 类方法：只能访问类变量，不能访问实例变量

# @property
# 属性方法：把一个方法变成静态属性
#       如果要添加属性，必须在类里面添加一个同名方法.setter 的装饰器的方法（最好与原函数同名）
#       属性方法无法直接用del删除，必须添加一个同名方法.deleter的装饰器方法
class A:
	def __init__(self):
		self.__food = None

	# 类方法
	@property
	def eat(self):
		print('eat self', self.__food)

	@eat.setter   # 同名方法.setter装饰器
	def Eat(self, food):
		print('eat food:', food)
		self.__food = food

	@eat.deleter
	def eat(self):
		del self.__food
		print('deleter')

a = A()
a.eat
a.Eat = 'foodddd'
a.eat
del a.eat
a.eat
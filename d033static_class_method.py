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

	@eat.setter  # 同名方法.setter装饰器
	def eat(self, food):
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


# 经典类，具有一种@property装饰器
# ############### 定义 ###############
class Goods:
	@property
	def price(self):
		return "wupeiqi"


# ############### 调用 ###############
obj = Goods()
result = obj.price  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值


# ----------------------------------------------------------------------
# 新式类，具有三种@property装饰器

# ############### 定义 ###############
class Goods(object):
	def __init__(self):
		# 原价
		self.original_price = 100
		# 折扣
		self.discount = 0.8

	@property
	def price(self):
		new_price = self.original_price * self.discount
		print('@property')
		return new_price

	@price.setter
	def price(self, value):
		self.original_price = value
		print('@price.setter')

	@price.deleter
	def price(self):
		del self.original_price
		print('@price.deleter')


# ############### 调用 ###############
obj = Goods()

obj.price  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值

obj.price = 123  # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数

del obj.price  # 自动执行 @price.deleter 修饰的 price 方法

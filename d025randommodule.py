#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-8 下午3:12


import random

# 随机返回[0, 1)区间内的浮点数
print(random.random())
# 随机返回[0, 10)区间内的浮点数
print(random.uniform(1, 10))

# 随机返回[1, 5]区间内的整形
print(random.randint(1, 5))

# 参数与range()函数相同，在结果内随机返回一个数
print(random.randrange(10))

# 可传入字符串，列表，随机返回其中的一个值
print(random.choice('asd'))

# 可传入字符串，列表等，随机返回其中3个值
print(random.sample('asdzxcasdasd', 3))

# 洗牌,打乱顺序
items = [1, 2, 3, 4, 5, 6, 7]
print(items)
random.shuffle(items)
print(items)

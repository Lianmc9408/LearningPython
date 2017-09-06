#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-6 下午12:45


# 可直接用for循环直接作用的的数据类型有以下几种
# 一类是集合数据类型，如list，tuple,dict,set,str等
# 一类是generator，包括生成器和带yield的generator function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以使用isinstance(.., Iterable)判断一个对象是否是Iterable对象
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

from collections import Iterable  # 迭代对象

a = isinstance((x for x in range(10)), Iterable)
b = isinstance([], Iterable)
c = isinstance({}, Iterable)
d = isinstance('abc', Iterable)
print(a, b, c, d)  # True True True True

from collections import Iterator  # 迭代器

a = isinstance((x for x in range(10)), Iterator)  # 生成器
b = isinstance([], Iterator)
c = isinstance({}, Iterator)
d = isinstance('abc', Iterator)
print(a, b, c, d)  # True False False False

# 把Iterable 变成Iterator 可以使用iter()函数

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-5 上午11:00

# 集合set  无序
list1 = [1, 3, 4, 5, 6, 7, 9]
list2 = [0, 2, 66, 4, 6, 8, 22]
list_1 = set(list1)
list_2 = set(list2)
print(list_1.intersection(list_2))  # 交集
print(list_1 & list_2)  # 交集
print(list_1.union(list_2))  # 并集
print(list_1 | list_2)  # 并集
print(list_1.difference(list_2))  # 差集，in list_1 but not in list_2
print(list_1 - list_2)  # 差集，in list_1 but not in list_2
print(list_1.issubset(list_2))  # list_1是否是list_2的子集
print(list_1.issuperset(list_2))  # list_1是否是list_2的父集
print(list_1.symmetric_difference(list_2))  # 对称差集，list_1和list_2的并集去除交集
print(list_1 ^ list_2)  # 对称差集，list_1和list_2的并集去除交集
print(list_1.isdisjoint(list_2))  # 判断list_1和list_2有没有交集，有返回False
list_1.add(321)  # 添加元素
print(list_1)  # 添加元素
list_1.update(list_2)  # 用集合更新集合
print(list_1)  # 用集合更新集合
list_1.pop()  # 随机删除一个元素
print(list_1)  # 随机删除一个元素
list_1.remove(3)  # 指定删除一个元素，不存在会报错
print(list_1)  # 指定删除一个元素
list_1.discard(5)  #指定删除一个元素，不存在不会报错
print(list_1)

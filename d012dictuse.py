#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-5 上午9:46


# 字典，无序，键值对
info = {
	'k1': 'v1',
	'k2': 'v2',
	'k3': 'v3'
}
info['k1'] = 'v11'  # 改
info['k4'] = 'v4'  # 增
info.pop('k1')  # 删
info.popitem()  # 随机删除
info.get('s1')  # 查找，若key不存在，会新建
print(info)
's1' in info     # 判断字典是否有s1
info.setdefault('k5', 'v5')  # 查找k5,不存在会创建新的key
b = {
	'k3': 'v33',
	1: 3,
	2: 5
}
info.update(b)  # 用字典b更新字典info，存在交叉的值会使用新字典b的值
info.items()  # 把字典转换成列表，键值对组成元素
c = dict.fromkeys([321,345,456], ['aa','bb'])  # {456: ['aa', 'bb'], 321: ['aa', 'bb'], 345: ['aa', 'bb']}
print(c)  # 新建字典

for i in info:
	print(i, info[i])

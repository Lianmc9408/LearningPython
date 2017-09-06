#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-6 下午10:50

import pickle

info = {
	'age': 22,
	'name': 'lmc'
}

# 把字典序列化成bytes字符
c = pickle.dumps(info)
print(c)
print(type(c))

# 把bytes字符反序列化成字典
info2 = pickle.loads(c)
print(info2)
print(type(info2))

# 把字典序列化成字符串后写进文件
with open('d022json.txt', 'wb') as f:
	pickle.dump(info, f)
	# 相当于：
	# f.write(json.dumps(info))

# 把文件内的信息读出后反序列化
with open('d022json.txt', 'rb') as a:
	info3 = pickle.load(a)
	print(info3)
	# 相当于：
	# json.loads(f.read())

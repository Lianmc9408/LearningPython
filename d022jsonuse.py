#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-6 下午9:54

import json

info = {
	'age': 22,
	'name': 'lmc'
}

# 把字典序列化成字符串
c = json.dumps(info)
print(c)
print(type(c))

# 把字符串反序列化成字典
info2 = json.loads(c)
print(info2)
print(type(info2))

# 把字典序列化成字符串后写进文件
with open('d022json.txt', 'w') as f:
	json.dump(info, f)
	# 相当于：
	# f.write(json.dumps(info))

# 把文件内的信息读出后反序列化
with open('d022json.txt', 'r') as a:
	info3 = json.load(a)
	# 相当于：
	# json.loads(f.read())

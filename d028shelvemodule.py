#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-8 下午6:22


# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块
# 可以持久化任何pickle可支持的python数据格式

import shelve
import datetime

# ----------------写-----------(会生成.bak,.dat,.dir文件)
# d = shelve.open('shelve_test')  # 打开一个文件
# name = ["alex", "rain", "test"]
# info = {'age':22, 'jog':'it'}
# d["test"] = name  # 持久化列表
# d["info"] = info  # 持久化类
# d["t2"] = datetime.datetime.now()
# d.close()
# ---------------读------------

# d = shelve.open('shelve_test')  # 打开一个文件
# print(d.get('test'))
# print(d.get('info'))
# print(d.get('t2'))

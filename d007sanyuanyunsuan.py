#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-4 下午6:43

# 三元运算
a, b, c = 1, 3, 5
result = a if a > b else c

# 编码和解码
msg = '我爱你哦'
# 默认utf—8
print(msg.encode())  # 编码
print(msg.encode().decode())  # 解码



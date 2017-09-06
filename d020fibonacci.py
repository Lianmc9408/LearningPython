#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-6 上午11:33

# 生成器，不怎么算函数
def fib(maxn):
	n, a, b = 0, 0, 1
	while n < maxn:
		yield b  # 生成器
		# print(b)
		a, b = b, a + b
		n += 1
	return '----done----'  # 异常的时候打印的消息


f = fib(10)
print(f)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print('====start loop====')
for i in f:  # f从第5个开始(前面有4个已经用过),生成器会一个一个生成，超出最后一个会报错抛出异常
	print(i)

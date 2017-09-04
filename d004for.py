#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-4 下午2:27


# for i in range(10):
# 	print('loop', i)

age = 56
for i in range(3):
	guess = input('猜年龄(你还有%d次机会)：' % (3-i))
	while not guess.isnumeric():
		guess = input('年龄是数字啊：')
	guess = int(guess)
	if guess == age:
		print('猜中了')
		break
	elif guess > age:
		print('大了')
	else:
		print('小了')
else:
	print('游戏结束,你没有猜对,正确答案是 %d' % age)

# 3是步长
for i in range(0, 10, 3):
	print('loop', i)

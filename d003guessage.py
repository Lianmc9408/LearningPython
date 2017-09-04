#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-4 下午1:41

import random

age = random.randint(0, 10)
count = 3
while count >= 0:
	guess = input('猜年龄(你还有%d次机会)：' % count)
	while not guess.isnumeric():
		guess = input('年龄是数字啊：')
	guess = int(guess)
	if guess == age:
		print('猜中了')
		break
	elif guess > age:
		print('大了')
		count -= 1
	else:
		print('小了')
		count -= 1
else:
	print('游戏结束,你没有猜对,正确答案是 %d' % age)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-5 下午9:11


def hanoi(n, x, y, z):
	if n == 1:
		print(x, '-->', z)
	else:
		hanoi(n - 1, x, z, y)
		print(x, '-->', z)
		hanoi(n - 1, y, x, z)


hanoi(4, 'x', 'y', 'z')

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-16 上午10:01


import socket

# TCP客户端：创建socket--> 连接到指定计算机的端口
sk = socket.socket()

address = ('127.0.0.1', 8000)
sk.connect(address)

# BUG:直接输入回车会卡死
while 1:
	inp = input('>>>')
	if inp == 'exit':
		break
	sk.send(bytes(inp, 'utf-8'))
	# sk.send(bytes('asdasd', 'utf-8'))
	# 1024表示一次可以收到的最大字节数为1024
	data = sk.recv(1024)
	print(str(data, 'utf-8'))

# print(str(data, 'utf-8'))


sk.close()  # 关闭通道
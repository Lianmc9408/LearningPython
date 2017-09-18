#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-16 上午10:01

# 并发聊天
import socket

# TCP客户端：创建socket--> 连接到指定计算机的端口
sk = socket.socket()

address = ('127.0.0.1', 8000)
sk.connect(address)

while 1:
	inp = input('>>>')
	if inp == 'exit':
		break
	sk.send(bytes(inp, 'utf-8'))
	data = sk.recv(1024)
	print(str(data, 'utf-8'))

sk.close()  # 关闭通道

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-18 上午8:41

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8002))
while 1:
	inp = input('..>>>')
	if inp == 'exit':
		break
	sk.send(bytes(inp, 'utf-8'))

	result_len = int(str(sk.recv(1024), 'utf-8'))
	sk.sendall(bytes('ok', 'utf-8'))
	data = bytes()  # 空字节
	while len(data) != result_len:
		result = sk.recv(1024)  # 如果超过1024字节，会无法接收全部数据，需要重复接收数据
		data += result
	print(str(data, 'utf-8'))
sk.close()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-16 上午10:01

import socket

# socket通信流程
# TCP服务端：创建socket--> 为socket绑定IP和端口号--> 监听设置端口的请求 --> Accept阻塞，直到有客户端连接
# TCP客户端：创建socket--> 连接到指定计算机的端口

# server端的方法：
# socket(),bind(),listen(),accept(),send(),sendall(),recv(),close()

# client端的方法：
# socket(),connect(),send(),sendall(),recv(),close()

# socket.socket()有两个参数，family=AF_INET, type=SOCK_STREAM
# family：AF_INET 服务器之间通信，AF_UNIX UNIX进程间通信
# type：SOCK_DGRAM用于UDP，SOCK_STREAM用于TCP
sk = socket.socket()

# 127.0.0.1 回环IP
address = ('127.0.0.1', 8000)

# 绑定IP和端口号
sk.bind(address)

# 为None时表示无排队服务，bakclog为数字时代表最大等待队列数量
sk.listen(3)


# a bytes-like object is required, not 'str'
# 必须传bype类型的数据
# inp = input('....>>')
# conn.send(bytes(inp, 'utf-8'))

# BUG:直接输入回车会卡死

# 第一种写法：
# conn, addr = sk.accept()
# print(conn)
# while 1:
# 	data = conn.recv(1024)
# 	print(',........', str(data, 'utf-8'))
# 	if not data:
# 		# 一个客户端退出后等待下一个客户端连进的情况
# 		conn.close()
# 		conn, addr = sk.accept()
# 		print(addr)
# 		continue
# 		# 1个客户端的情况
# 		# break
# 	inp = input('....>>')
# 	conn.send(bytes(inp, 'utf-8'))

# 第二种写法：
while 1:
	conn, addr = sk.accept()
	while 1:
		try:
			data = conn.recv(1024)   # 等待接收的过程中如果client关闭，会报ConnectionResetError
		except ConnectionResetError:
			break
		if not data:
			break
		print(',........', str(data, 'utf-8'))
		inp = input('....>>')
		conn.send(bytes(inp, 'utf-8'))


conn.close()  # 关闭连接，关闭后相连的对象断开
sk.close()  # 关闭通道，关闭后全部对象都无法连接

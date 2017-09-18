#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-18 上午8:41

#  远程执行命令
import socket
import subprocess

sk = socket.socket()
sk.bind(('127.0.0.1', 8002))
sk.listen(3)
while True:
	conn, addr = sk.accept()
	print(addr)
	while True:
		try:
			data = conn.recv(1024)
		except ConnectionResetError:
			break
		if not data:
			break
		print(str(data, 'utf-8'))

		# 接收到命令后执行命令
		# stdout=subprocess.PIPE 加入这个参数表示把结果添加到obj对象中
		# obj = subprocess.Popen(data, shell=True) 直接输出结果到控制台，不添加到对象中
		obj = subprocess.Popen(str(data, 'utf-8'), shell=True, stdout=subprocess.PIPE)
		cmd_result = obj.stdout.read()  # 无stdout=subprocess.PIPE参数时，无法使用read()方法
		# cmd_result为字节类型
		if not cmd_result:
			conn.send(bytes('无返回值', 'utf-8'))
		result_len = bytes(str(len(cmd_result)), 'utf-8')
		conn.sendall(result_len)
		conn.recv(1024)  # 解决粘包
		conn.sendall(cmd_result)

sk.close()
# 娃娃菜  白萝卜  牛肉  牛百叶  鸡柳  鱿鱼须
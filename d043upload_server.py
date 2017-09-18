#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-18 下午2:25


import socket
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sk = socket.socket()
sk.bind(('127.0.0.1', 8000))
sk.listen(3)
while 1:
	conn, addr = sk.accept()
	while 1:
		# 先接收文件的基本信息
		data = conn.recv(1024)
		if not data:
			break
		cmd, filename, filesize = str(data, 'utf-8').split('|')
		path = os.path.join(BASE_DIR, 'ATM', filename)
		if os.path.exists(path):
			os.remove(path)
			print('删除旧文件')
		filesize = int(filesize)

		conn.sendall(bytes('ok', 'utf-8'))

		with open(path, 'ab') as f:
			has_receive = bytes()
			while len(has_receive) != filesize:
				data = conn.recv(1024)
				f.write(data)
				has_receive += data

sk.close()

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-18 下午2:24


import socket
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sk = socket.socket()
sk.connect(('127.0.0.1', 8000))
while 1:
	inp = input('>>>').strip()  # post|d043upload.jpg
	if not inp:
		break
	cmd, path = inp.split('|')

	# path = '%s/%s' % (BASE_DIR, path)  不建议用此种方式，不同操作系统的分隔符不同
	# win'\'， Linux'/'
	path = os.path.join(BASE_DIR, path)

	# 得到文件名
	filename = os.path.basename(path)

	# 获取文件大小
	filesize = os.stat(path).st_size

	file_info = 'post|%s|%s' % (filename, filesize)

	sk.sendall(bytes(file_info, 'utf-8'))

	sk.recv(1024)
	# 此前为发送文件的基本信息到服务器
	# 开始发送文件
	with open(path, 'rb') as f:
		has_send = bytes()
		while len(has_send) != filesize:
			data = f.read(1024)
			sk.sendall(data)
			has_send += data
	print('上传成功')

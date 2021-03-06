#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-22 下午8:25


# 通过gevent实现单线程下的多socket并发

import socket
import gevent

from gevent import socket, monkey

monkey.patch_all()


def server(port):
	s = socket.socket()
	s.bind(('127.0.0.1', port))
	s.listen(500)
	while True:
		cli, addr = s.accept()
		gevent.spawn(handle_request, cli)


def handle_request(conn):
	try:
		while True:
			data = conn.recv(1024)
			print("recv:", data)
			conn.send(data)
			if not data:
				conn.shutdown(socket.SHUT_WR)

	except Exception as ex:
		print(ex)
	finally:
		conn.close()


if __name__ == '__main__':
	server(8001)

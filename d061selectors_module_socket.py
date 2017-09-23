#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-23 上午10:06

# http://www.cnblogs.com/alex3714/articles/5248247.html

# 默认用epoll,如不支持用epoll，则用select
# 更简单的写select
import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sock, mask):
	conn, addr = sock.accept()  # Should be ready
	print('accepted', conn, 'from', addr)
	conn.setblocking(False)
	# conn活动，调用read()方法读取数据
	sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
	data = conn.recv(1000)  # Should be ready
	if data:
		print('echoing', repr(data), 'to', conn)
		conn.send(data)  # Hope it won't block
	else:
		print('closing', conn)
		sel.unregister(conn)
		conn.close()


sock = socket.socket()
sock.bind(('localhost', 10000))
sock.listen(100)
sock.setblocking(False)
# 只要来一个新活动链接，就调用accept()方法
sel.register(sock, selectors.EVENT_READ, accept)

while True:
	# 系统支持什么就调用什么，不一定是select，默认阻塞，有活动链接就返回活动的链接列表
	events = sel.select()
	for key, mask in events:
		callback = key.data  # accept()方法
		callback(key.fileobj, mask)  # key.fileobj,就是socket链接conn

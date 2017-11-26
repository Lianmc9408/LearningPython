#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-21 下午10:42


from multiprocessing import Process, Pipe

# 进程间一个send对应一个recv（send两次就要recv两次），多的recv会造成阻塞

def f(conn):
	conn.send([42, None, 'hello'])
	conn.close()


if __name__ == '__main__':
	parent_conn, child_conn = Pipe()
	p = Process(target=f, args=(child_conn,))
	p.start()
	print(parent_conn.recv())  # prints "[42, None, 'hello']"
	p.join()
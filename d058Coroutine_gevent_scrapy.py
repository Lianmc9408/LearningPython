#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-22 下午12:04

# 使用携程批量爬取网页

# 给当前程序打补丁，能检测到当前程序所有的IO操作，如urllib的urlopen()操作
from gevent import monkey

monkey.patch_all()  # 把当前所有的IO操作做上标记

import gevent
from urllib.request import urlopen


def f(url):
	print('GET: %s' % url)
	resp = urlopen(url)
	data = resp.read()
	print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
	gevent.spawn(f, 'https://www.python.org/'),
	gevent.spawn(f, 'https://www.yahoo.com/'),
	gevent.spawn(f, 'https://github.com/'),
])

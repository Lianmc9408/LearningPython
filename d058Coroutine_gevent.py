#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-22 上午10:13


# Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，
# 在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。
# Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。
# gevent 可以自动切换
import gevent


def func1():
	print('\033[31;1m李闯在跟海涛搞...\033[0m')
	gevent.sleep(2)
	print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


def func2():
	print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
	gevent.sleep(1)
	print('\033[32;1m李闯搞完了海龙，回来继续跟海涛搞...\033[0m')


def func3():
	print('\033[33;1m李闯切换到了跟海蛇搞...\033[0m')
	gevent.sleep(0)
	print('\033[33;1m李闯搞完了海蛇，回来继续跟海龙搞...\033[0m')


gevent.joinall([
	gevent.spawn(func1),
	gevent.spawn(func2),
	gevent.spawn(func3),
])

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-13 上午10:46


# 另一个模块级别的函数是logging.getLogger([name])
# （返回一个logger对象，如果没有指定名字将返回root logger）
# 使用logger对象更灵活，自定义需要的方式

import logging

logger = logging.getLogger()

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

# logger对象可以添加多个fh和ch对象
logger.addHandler(fh)
logger.addHandler(ch)

# 设置级别
logger.setLevel(logging.DEBUG)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

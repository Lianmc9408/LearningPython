#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-8 上午9:30

# 模块使用
# 导入方法：
# import module_name
# import module_name1,module_name2
# from module_name import *
# from module_name import m1,m2,m3
# from module_name import m1 as m
# from . import m  # 从当前目录导入m

# import 导入模块的本质就是把Python文件解释一遍
# import 导入包的本质就是执行该包下的__init__.py文件
# sys.path  模块一定要在sys.path返回的列表中
# os.path.abspath(__file__) 当前文件的绝对路径
# os.path.dirname() 获取当前路径的上一级路径
# x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.addend(x)

# 模块分类：
#   a.标准库
#   b.开源模块，第三方模块
#   c.自定义模块

# time模块
# 表示时间的方式：
#   a.时间戳 time.time(),1970年到现在经历过的秒数
#   b.元祖   time.localtime() 年、月、日、时、分、秒、本周第几天，本年第几天，时区
#         t = time.localtime(),可以通过t.tm_year,t.tm_mon等方式得到年月日等值
#   c.格式化的时间字符串

#   时间戳和元祖格式互换
#       time.gmtime(time.time())  转换为元祖格式,为标准时间,非时区时间
#       time.mktime(time.localtime())   转换为时间戳格式

#   元祖格式和格式化字符串互换
#    %Y  Year with century as a decimal number.
#    %m  Month as a decimal number [01,12].
#    %d  Day of the month as a decimal number [01,31].
#    %H  Hour (24-hour clock) as a decimal number [00,23].
#    %M  Minute as a decimal number [00,59].
#    %S  Second as a decimal number [00,61].
#    %z  Time zone offset from UTC.
#    %a  Locale's abbreviated weekday name.
#    %A  Locale's full weekday name.
#    %b  Locale's abbreviated month name.
#    %B  Locale's full month name.
#    %c  Locale's appropriate date and time representation.
#    %I  Hour (12-hour clock) as a decimal number [01,12].
#    %p  Locale's equivalent of either AM or PM.
#
#   time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())  格式化成字符串
#   time.strptime('2017-09-08 11:26:34','%Y-%m-%d %H:%M:%S')    格式化成元祖
#   time.asctime([turple])  把元祖格式化成字符串(%a %b %d %H:%M:%S %Y)
# 							元祖为空时，默认格式化time.localtime()
#   time.ctime([second]) 把时间戳转换成字符串(%a %b %d %H:%M:%S %Y)
#                        时间戳为空时默认格式化time.time()

# datetime
#   datetime.date   日期对象
#   datetime.time   时间对象
#   datetime.datetime   日期和时间对象

#   datetime.datetime.now()  返回当前时间的datetime对象
#   两个datetime对象可以直接比较大小,如datetime1 > datetime2 ,返回True或False
#   datetime对象可以加减一个时间间隔，返回一个新的datetime对象
#       如：datetime.datetime.now() + datetime.timedelta(3)    当前时间+3天
#       如：datetime.datetime.now() + datetime.timedelta(-3)   当前时间-3天
#       如：datetime.datetime.now() + datetime.timedelta(hours=3)    当前时间+3小时
#       如：datetime.datetime.now() + datetime.timedelta(mintues=30)    当前时间+30分钟
#   两个datetime对象可以直接相减，返回一个timedelta对象
#       如：datetime.datetime1 - datetime.datetime2
#   时间替换，如：d = datetime.datetime.now()  -->2017-09-08 12:05:08.163213
#       d.replace(minute=3,hour=2)   -->datetime.datetime(2017, 9, 8, 2, 3, 8, 163213)


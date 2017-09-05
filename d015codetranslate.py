#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-5 下午3:31

# utf-8 -- unicode -- gbk
# unicode 可以encode成任何格式的编码形式，所以不同编码形式之间可以通过unicode转换

# 如gbk转换为utf-8形式流程：
# 1、gbk decode 转换成unicode
# 2、unicode encode 转换成utf-8

# 如utf-8转换为gbk形式流程：
# 1、utf-8 decode 转换成unicode
# 2、unicode encode 转换成gbk

s = '你好'
s_to_gbks = s.encode('gbk')
print(s_to_gbks)

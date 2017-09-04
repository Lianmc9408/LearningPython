#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-4 下午1:30
# 使用暗文密码
import getpass

username = input('username:')
password = getpass.getpass('password:')

print(username, password)

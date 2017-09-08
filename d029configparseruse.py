#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-8 下午10:19

# 用于生成和修改常见配置文档
import configparser

# ----------生成---------------------
# config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini', 'w') as configfile:
# 	config.write(configfile)

# --------------读 - ----------
# config = configparser.ConfigParser()
# config.sections()  # -->[]
# config.read('example.ini')  # -->['example.ini']
# config.sections()  # -->['bitbucket.org', 'topsecret.server.com']
# 'bitbucket.org' in config  # -->True
# 'bytebong.com' in config  # -->False
# config['bitbucket.org']['User']  # -->'hg'
# config['DEFAULT']['Compression']  # -->'yes'
# topsecret = config['topsecret.server.com']
# topsecret['ForwardX11']  # -->'no'
# topsecret['Port']  # -->'50022'
# for key in config['bitbucket.org']: print(key)
# # ...
# # user
# # compressionlevel
# # serveraliveinterval
# # compression
# # forwardx11
# config['bitbucket.org']['ForwardX11']  # -->'yes'

# -------------分割线-----------------
# 获取所有节点
# config = configparser.ConfigParser()
# config.read('xxxooo', encoding='utf-8')
# ret = config.sections()
# print(ret)

# 获取指定节点下所有的键值对
# config = configparser.ConfigParser()
# config.read('xxxooo', encoding='utf-8')
# ret = config.items('section1')
# print(ret)

# 获取指定节点下所有的建
# config = configparser.ConfigParser()
# config.read('xxxooo', encoding='utf-8')
# ret = config.options('section1')
# print(ret)

# 获取指定节点下指定key的值
# config = configparser.ConfigParser()
# config.read('xxxooo', encoding='utf-8')
# v = config.get('section1', 'k1')
# # v = config.getint('section1', 'k1')
# # v = config.getfloat('section1', 'k1')
# # v = config.getboolean('section1', 'k1')
# print(v)

# --------------------------------
# 检查、删除、添加节点
# config = configparser.ConfigParser()
# config.read('xxxooo', encoding='utf-8')

# 检查
# has_sec = config.has_section('section1')
# print(has_sec)

# 添加节点
# config.add_section("SEC_1")
# config.write(open('xxxooo', 'w'))

# 删除节点
# config.remove_section("SEC_1")
# config.write(open('xxxooo', 'w'))

# ------------------------------
# 检查、删除、设置指定组内的键值对
# config = configparser.ConfigParser()
# config.read('xxxooo', encoding='utf-8')

# 检查
# has_opt = config.has_option('section1', 'k1')
# print(has_opt)

# 删除
# config.remove_option('section1', 'k1')
# config.write(open('xxxooo', 'w'))

# 设置
# config.set('section1', 'k10', "123")
# config.write(open('xxxooo', 'w'))

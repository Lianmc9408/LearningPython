#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-13 下午1:12


def file_db_handle(conn_parms):
	print('file db:', conn_parms)
	db_path = '%s/%s' % (conn_parms['path'], conn_parms['name'])
	return db_path


def db_handler(conn_parms):
	if conn_parms['engine'] == 'file_storage':
		return file_db_handle(conn_parms)

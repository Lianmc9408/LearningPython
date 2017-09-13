#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-13 下午12:47


import logging
import os

LOG_LEVEL = logging.DEBUG
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
	'engine': 'file_storage',
	'name': 'accounts',
	'path': '%s/db' % BASE_DIR
}

LOG_TYPES = {
	'transaction': 'transactions.log',
	'access': 'access.log'
}

TRANSACTION_TYPE = {
	'repay': {'action': 'plus', 'interset': 0},
	'withdraw': {'action': 'minus', 'interset': 0.05},
	'transfer': {'action': 'minus', 'interset': 0.05},
	'consume': {'action': 'minus', 'interset': 0}
}

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-13 下午2:24

from core import db_handler
from conf import settings
import json


def load_current_balence(account_id):
	db_path = db_handler.db_handler(settings.DATABASE)
	account_file = '%s/%s.json' % (db_path, account_id)
	with open(account_file, 'r') as f:
		acc_data = json.load(f)
		return acc_data


def dump_account(account_data):
	db_path = db_handler.db_handler(settings.DATABASE)
	account_file = '%s/%s.json' % (db_path, account_data['id'])
	with open(account_file, 'w') as f:
		json.dump(account_data, f)
	return True

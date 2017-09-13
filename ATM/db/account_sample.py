#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-13 下午12:26


import json

acc_dic = {
	'id': 1234,
	'password': 'abc',
	'creait': 15000,
	'balence': 15000,
	'enroll_date': '2016-01-02',
	'expire_date': '2021-01-01',
	'pay_day': 22,
	'status': 0
}

print(json.dumps(acc_dic))

with open('accounts/1234.json', 'w', encoding='utf-8') as f:
	f.write(json.dumps(acc_dic))

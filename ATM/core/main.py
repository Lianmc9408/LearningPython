#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-13 下午12:22

from core import logger
from core import auth
from core import accounts
from core import transaction

trans_logger = logger.logger('transaction')

access_logger = logger.logger('access')

# 初始化
user_data = {
	'account_id': None,
	'is_authenticated': False,
	'account_data': None
}


def account_info(acc_data):
	print(acc_data)


# 还款
def repay(acc_data):
	account_data = accounts.load_current_balence(acc_data['account_id'])
	current_balance = '''------BALANCE INFO------
		Credit:\t\t%s
		Balance:\t\t%s
	''' % (account_data['creait'], account_data['balence'])
	print(current_balance)
	back_flag = False
	while not back_flag:
		repay_amount = input('\033[33;1mInput repay amount:\033[0m').strip()
		if len(repay_amount) > 0 and repay_amount.isdigit():
			print('ddd 00')
			new_balance = transaction.make_transaction(trans_logger, account_data, 'repay', repay_amount)
			if new_balance:
				print('''\33[32;1mNew Balance:%s\033[0m''' % (new_balance['balence']))
		else:
			print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)


def withdraw(acc_data):
	pass


def transfer(acc_data):
	pass


def pay_check(acc_data):
	pass


def logout(acc_data):
	pass


def interactive(user_data):
	menu = u'''
	------ ATM Bank ------
	\033[32;1m1.账户信息
	2.还款（finish）
	3.借款（finish）
	4.转账
	5.账单
	6.退出
	\033[0m'''
	menu_dic = {
		'1': account_info,
		'2': repay,
		'3': withdraw,
		'4': transfer,
		'5': pay_check,
		'6': logout
	}
	exit_flag = False
	while not exit_flag:
		print(menu)
		user_option = input('>>>').strip()
		if user_option in menu_dic:
			menu_dic[user_option](user_data)
		else:
			print('\033[31;1mOption doex not exist!\033[0m')


def run():
	acc_data = auth.acc_login(user_data, access_logger)
	if user_data['is_authenticated']:
		user_data['account_data'] = acc_data
		interactive(user_data)
		access_logger.info('main.run() success')

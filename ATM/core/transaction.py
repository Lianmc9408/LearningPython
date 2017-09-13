#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-13 下午1:24


from conf import settings
from core import accounts


def make_transaction(log_obj, acount_data, tran_type, amount, **others):
	amount = float(amount)
	if tran_type in settings.TRANSACTION_TYPE:
		interest = amount * settings.TRANSACTION_TYPE[tran_type]['interset']

		old_balace = acount_data['balence']
		if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
			new_balance = old_balace + amount + interest
		elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
			new_balance = old_balace - amount - interest

			if new_balance < 0:
				print('\033[31;1mYour credit [%s] is not enough for this transaction' % (acount_data['creait']))
				return

		acount_data['balence'] = new_balance
		accounts.dump_account(acount_data)
		log_obj.info('account:%s\taction:%s\tamount:%s\tinterest:%s' % (acount_data['id'], tran_type, amount, interest))
		return acount_data
	else:
		print('\033[31;1mTransaction type [%s] is not exist!\033[0m' % tran_type)

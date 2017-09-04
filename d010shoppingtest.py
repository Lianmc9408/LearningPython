#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-4 下午8:22


temp = input('请输入你的工资：')

while not temp.isnumeric():
	temp = input('请输入你的工资（数字）:')
salary = int(temp)
shoplist = [['Iphone', 5800], ['Mac Pro', 12000], ['StarBuck', 31], ['Alex Python', 81], ['Bike', 800]]
buylist = []
for i in range(len(shoplist)):
	print(i + 1, '.', shoplist[i])
buy = 't'
while buy != 'q':
	buy = input('你想买什么(按q退出):')
	if salary < 31:
		print('死屌丝，没钱食屎啦！')
		break
	if buy == 'q':
		continue
	if int(buy) > len(shoplist):
		print('输入的商品不存在！')
		continue
	want_buy = int(buy)
	if salary < shoplist[want_buy - 1][1]:
		print('余额不足，你还有\033[31;1m%d\033[0m元' % salary)
		continue
	else:
		buylist.append(shoplist[want_buy - 1])
		salary -= shoplist[want_buy - 1][1]
		print('已加入购物车，你还有\033[31;1m%d\033[0m元' % salary)
else:
	#  打印已经购买商品和余额
	if len(buylist) != 0:
		print('---你买了---')
		for i in buylist:
			print(i)
	else:
		print('你什么都没买！')
	print('余额为：', salary)

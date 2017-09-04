#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-4 下午3:28


guangdong = ['gd1', 'gd2', 'gd3']
guangxi = ['gx1', 'gx2', 'gx3']
hunan = ['hn1', 'hn2', 'hn3']
la = ['la1', 'la2', 'la3']
xiusidun = ['xsd1', 'xsd2', 'xsd3']
mia = ['mia1', 'mia2', 'mia3']
el1 = ['el11', 'el12', 'el13']
el2 = ['el21', 'el22', 'el23']
el3 = ['el31', 'el32', 'el33']
china = {'广东': guangdong, '广西': guangxi, '湖南': hunan}
America = {'洛杉矶': la, '休斯顿': xiusidun, '迈阿密': mia}
England = {'英国1': el1, '英国2': el2, '英国3': el3}
country = {'中国': china, '美国': America, '英国': England}

for i in country.keys():
	print(i)
	ii = country.get(i)
	# print(ii)
	for j in ii.keys():
		print('\t' + j)
		jj = ii.get(j)
		for k in jj:
			print('\t\t' + k)
	print('----------------')

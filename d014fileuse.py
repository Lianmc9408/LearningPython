#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-5 上午11:27

# 文件操作
# 'r' 读模式
# 'r+'读和追加模式，读从光标开始读，写从末尾开始写
# 'w' 写模式,会使文件归零,覆盖存在的文件
# 'w+' 写读模式,会先创建文件，覆盖原文件，写从末尾开始追加,(没卵用)
# 'a' append,追加模式,在源文件末尾追加写,不能读
# 'b' 以二进制方式 --'rb'  --'wb',编码方式不能用'utf-8'
# 'U' 读取时，可以将\r、\n、\r\n自动转换成\n --'rU' --'r+U'

# with open('d014file', 'r', encoding='utf-8') as f  安全打开文件的方法，不用时文件会自动关闭
# f.readlines()  # 读全部，返回列表，一行一个元素
# f.read()  # 读全部
# f.readline()  # 读一行
# f.write('..')  # 写入文件
# f.encoding  # 返回文件的编码方式
# f.flush()  # 把内存的信息写到硬盘上
# f.truncate(size)  # 从头开始截断size个字符

with open('d014file', 'r', encoding='utf-8') as f, \
		open('d014newfile', 'w', encoding='utf-8') as nf:
	# readline()适合读小文件
	# print(f.readline())  # 每读一行，游标向下走
	# for i in f.readlines():
	# 	print(i.strip())

	# for line in f:  # 较readline()高效
	# 	print(line)
	# print(f.readline())
	# f.tell()  # 返回光标所在位置
	# f.seek(0)  # 设置光标位置
	# print(f.readline())

	# 修改文件(修改中间部分)[边改边写]
		for line in f:
			if 'if the sky that we look upon' in line:
				line = line.replace('if the sky that we look upon', '-if the sky that we look upon---')
			nf.write(line)

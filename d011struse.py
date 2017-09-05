#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-5 上午8:35

names = 'my name is lmc {a} yes'
print('1', names.capitalize())  # 把字符串的第一个字符改为大写
print('2', names.lower())  # 把整个字符串的所有字符改为小写
print('3', names.center(50))  # 把字符串居中，并使用空格填充至长度width
print('4', names.center(50, '-'))  # 把字符串居中，并使用'-'填充至长度width
print('5', names.count('a'))  # 返回sub在字符串里边 出现的次数，start和end表示范围
print('6', names.endswith('yes'))  # 检查字符串是否以sub子字符串结束，是返回True，参数表示范围
print('7', names.expandtabs(20))  # 把字符串中的tab符号(\t)转换为空格，如不指定参数，默认空格数是8
print('8', names.find('lmc'))  # 检测sub是否包含在子字符串中，有返回索引值，否则返回-1，参数表示范围
print('9', names.format(a=23))  # 把字符串中{a}的值改为23
print('10', names.format_map({'a': 20}))  # 传入字典，把把字符串中{a}的值改为23
print('11', names.isalnum())  # 字符串不为空且所有字符都是字母或者数字返回True
print('12', names.isalpha())  # 字符串不为空且所有字符都是字母返回True
print('13', names.isdecimal())  # 字符串只包含十进制数字则返回True
print('14', names.isdigit())  # 字符串只包含数字则返回True
print('15', names.islower())  # 字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回True
print('16', names.isnumeric())  # 如果字符串中只包含数字字符，则返回True
print('17', names.isspace())  # 字符串中只包含空格，则返回True
print('18', names.istitle())  # 字符串所有的单词都是大写开始，其余字母小写，则返回True
print('19', names.isupper())  # 字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回True
print('20', names.join('123'))  # 以字符串为分隔符，插入到sub所有的字符之间，1asdasd2asdasd3asdasd4
print('21', names.ljust(30))  # 返回一个左对齐的字符串，插入到sub中所有的字符之间
print('21', names.ljust(30, '='))  # 返回一个左对齐的字符串，多余的用'='填充
print('22', names.lstrip())  # 去掉字符串左边的所有空格
print('23', names.partition('name'))  # 找到字符串sub，把字符串分成一个3元祖(pre_sub,sub,fol_sub),如果不包含sub则返回('原字符串',' ',' ')
print('24', names.replace('name', 'naMe'))  # 把字符串中的old字符串替换成new字符串，如果count指定，则替换不超过count次
print('25', names.rfind('lmc'))  # 类似find()方法，不过是从右边开始查找
print('26', names.rindex('lmc'))  # 类似于index，不过是从右边开始
print('27', names.rpartition('name'))  # 返回一个右对齐的字符串，并使用空格填充至长度为width的新字符串
print('28', names.rstrip())  # 删除字符串末尾的空格
print('29', names.split())  # 不带参数默认是以空格为分隔符切片字符串，如果maxsplit设置有参数，则仅分隔maxsplit个子字符串，返回切片后的子字符串拼接的列表
print('30', names.splitlines())  # 按照'\n'分隔，返回一个包含各行作为元素的列表，如果keepends参数指定，则 返回前keepends行
print('31', names.startswith('name'))  # 检查字符串是否以prefix开头，是则返回True，否则返回False。参数指定范围
print('32', names.strip())  # 删除字符串前边和后边所有的空格，chars参数可以定制删除的字符，可选。
print('33', names.title())  # 返回所有单词都是大写开头，其余字母小写的字符串
print('34', names.translate(str.maketrans('a', 'b')))  # 根据table的规则(可以由str.maketrans('a','b')定制)转换字符串中的字符，把字符串中的a变为b
print('35', names.upper())  # 转换字符串中的所有小写字符为大写
print('36', names.zfill(30))  # 返回长度为width的字符串，原字符串右对齐，前边用0填充
print('37', names.swapcase())  # 大小写转换
# capitalize()  把字符串的第一个字符改为大写
#
# casefole()    把整个字符串的所有字符改为小写
#
# center(width) 把字符串居中，并使用空格填充至长度width
#
# count(sub[,start[,end]])  返回sub在字符串里边 出现的次数，start和end表示范围
#
# encode(encodint='utf-8',errors='strict') 以encoding指定的编码格式对字符串编码
#
# endswith(sub[,start[,end]]))  检查字符串是否以sub子字符串结束，是返回True，参数表示范围
#
# expandtabs([tabsize=8]) 把字符串中的tab符号(\t)转换为空格，如不指定参数，默认空格数是8
#
# find(sub[,start[,end]])) 检测sub是否包含在子字符串中，有返回索引值，否则返回-1，参数表示范围
#
# isalnum() 字符串不为空且所有字符都是字母或者数字返回True
#
# isalpha() 字符串不为空且所有字符都是字母返回True
#
# isdecimal() 字符串只包含十进制数字则返回True
#
# isdigit() 字符串只包含数字则返回True
#
# islower() 字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回True
#
# isnumeric() 如果字符串中只包含数字字符，则返回True
#
# isspace() 字符串中只包含空格，则返回True
#
# istitle() 字符串所有的单词都是大写开始，其余字母小写，则返回True
#
# isupper() 字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回True
#
# join(sub) 以字符串为分隔符，插入到sub所有的字符之间，1asdasd2asdasd3asdasd4
#
# ljust(width) 返回一个左对齐的字符串，插入到sub中所有的字符之间
#
# lower() 转换字符串中所有字符为小写
#
# lstrip() 去掉字符串左边的所有空格
#
# partition(sub) 找到字符串sub，把字符串分成一个3元祖(pre_sub,sub,fol_sub),如果不包含sub则返回('原字符串',' ',' ')
#
# replace(old,new[,count]) 把字符串中的old字符串替换成new字符串，如果count指定，则替换不超过count次
#
# rfind(sub[,start[,end]])) 类似find()方法，不过是从右边开始查找
#
# rindex(sub[,start[,end]])) 类似于index，不过是从右边开始
#
# rpartition(sub) 返回一个右对齐的字符串，并使用空格填充至长度为width的新字符串
#
# rstrip() 删除字符串末尾的空格
#
# split(sep=None,maxsplit=-1) 不带参数默认是以空格为分隔符切片字符串，如果maxsplit设置有参数，则仅分隔maxsplit个子字符串，返回切片后的子字符串拼接的列表
#
# splitlines(([keepends])) 按照'\n'分隔，返回一个包含各行作为元素的列表，如果keepends参数指定，则 返回前keepends行
#
# startwith(prefix[,start[,end]]) 检查字符串是否以prefix开头，是则返回True，否则返回False。参数指定范围0
#
# strip([chars]) 删除字符串前边和后边所有的空格，chars参数可以定制删除的字符，可选。
#
# swapcase() 翻转字符串字符的大小写
#
# title() 返回所有单词都是大写开头，其余字母小写的字符串0
#
# translate(table) 根据table的规则(可以由str.maketrans('a','b')定制)转换字符串中的字符，把字符串中的a变为b
#
# upper() 转换字符串中的所有小写字符为大写
#
# zfill() 返回长度为width的字符串，原字符串右对齐，前边用0填充

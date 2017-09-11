#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-9 上午8:18


import re
# '.'   默认匹配除\n之外的任意一个字符，若指定flag DOTALL, 则匹配任意字符，包括换行
# '^'   匹配字符开头，若指定flags MULTILINE, 这种也可以匹配上(r"^a", "\nabc\neee", flags=re.MULTILINE)
# '$'   匹配字符结尾，或e.search("foo$", "bfoo\nsdfsf", flags=re.MULTILINE).group()也可以
# '*'   匹配 * 号前的字符0次或多次，re.findall("ab*", "cabb3abcbbac")结果为['abb', 'ab', 'a']
# '+'   匹配前一个字符1次或多次，re.findall("ab+", "ab+cd+abb+bba")结果['ab', 'abb']
# '?'   匹配前一个字符1次或0次
# '{m}' 匹配前一个字符m次
# '{n,m}'匹配前一个字符n到m次，re.findall("ab{1,3}", "abb abc abbcbbb")结果'abb', 'ab', 'abb']
# '|'   匹配 | 左或 | 右的字符，re.search("abc|ABC", "ABCBabcCD").group()结果'ABC'
# '(...)'分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group()结果abcabca456c
#
# '\A'  只从字符开头匹配，re.search("\Aabc", "alexabc")是匹配不到的
# '\Z'  匹配字符结尾，同$
# '\d'  匹配数字0 - 9
# '\D'  匹配非数字
# '\w'  匹配[A - Za - z0 - 9]
# '\W'  匹配非[A - Za - z0 - 9]
# '\s'  匹配空白字符、\t、\n、\r, re.search("\s+", "ab\tc1\n3").group()结果'\t'
# '\S'  匹配非空白字符
# '\b'  匹配一个单词边界，单词被定义Unicode的数字字母或下横线字符
# '\B'  与\b相反，匹配非单词边界，如'py\B',会匹配'python','py3','py2','py_,但不会匹配'py.','py','py!'
#
# '(?P<name>...)'分组匹配

# re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})", "371481199306143242").groupdict("city")
# 结果{'province': '3714', 'city': '81', 'birthday': '1993'}

# re.match      从头开始匹配.^符号在此方法不起作用
# re.search     匹配包含
# re.findall    把所有匹配到的字符放到以列表中的元素返回,没有group()方法
# re.splitall   以匹配到的字符当做列表分隔符
# re.sub        匹配字符并替换
# 参数分别为，匹配的正则表达式，要替换的值，要替换的字符串，最多替换多少次
# a = re.sub('[0-9]+', '=', 'aas2123asd123zsd')
# a = re.sub('[0-9]+', '=', 'aas2123asd123zsd', count=2)
# print(a)  # --> aas=asd=zsd

# a = re.split('[0-9]+', 'aas2123asd123zsd')
# print(a) # --> ['aas', 'asd', 'zsd']

# 仅需轻轻知道的几个匹配模式
# re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同） flags=re.I
# M(MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图） flags=re.M
# S(DOTALL): 点任意匹配模式，改变'.'的行为  flags=re.S
# print(re.search('[a-z]+d$', 'aasdad\nwqeqwe\nsdfsdf\nsdfsd\n', flags=re.M))  # 最后一个\n不影响$符号匹配

# res = re.match(r'^qwe', 'qweasdzxc123ertdfgcvb')
# print(res)
# print(res.group())
#
# res1 = re.search(r'^asd', 'qweasdzxc123ertdfgcvb')
# print(res1)
#
# res2 = re.findall(r'^asd', 'qweasdzxc123ertdfgcvb')
# print(res2)

# res = re.search(r'a[a-z]+c', 'qweasdzxc123ertdfgcvb')
# print(res)  # span=(3, 9), match='asdzxc'


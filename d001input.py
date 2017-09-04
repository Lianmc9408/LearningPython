#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-4

name = input('Name:')
age = input('age:')
while not age.isnumeric():
	age = input('请输入正确的age：')
sex = input('sex:')
salary = input('salary:')

info = '''
--------------info of %s ---------------
	Name:%s
	age:%d
	sex:%s
	salary:%s
-----------------------------------------
''' % (name, name, int(age), sex, salary)

info2 = '''
--------------info of {name1} ---------------
	Name:{name1}
	age:{age1}
	sex:{sex1}
	salary:{salary1}
-----------------------------------------
'''.format(name1=name, age1=age, sex1=sex, salary1=salary)

info3 = '''
--------------info of {0} ---------------
	Name:{0}
	age:{1}
	sex:{2}
	salary:{3}
-----------------------------------------
'''.format(name, age, sex, salary)

print(info)
print(info2)
print(info3)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-4 下午7:11


names = ['aaaaa', 'bbbbbbb', 'ccccccccc', 'dddddd']

print(names)
print('按索引取列表值(0,2)', names[0], names[2])  # 按索引取列表值
print('切片[1:3]', names[1:3])  # 切片，返回列表，左开右闭
print('按下标取值(3)', names[3])  # 取值
print('切片[:3]', names[:3])  # 切片，从头开始切
print('切片[-2:]', names[-2:])  # 从倒数第2个开始切到最后
print('切片[-2:-1]', names[-2:-1])  # 从倒数第2个开始切到最后，左开右闭

names.append('eeee')  # 添加元素到列表最后
print('添加元素到列表最后', names)
names.insert(1, 'ffff')  # 插入到固定位置
print('插入到固定位置', names)
names[2] = 'ggggg'  # 把列表下标为2的元素换成ggggg
print('把列表下标为2的元素换成ggggg', names)
names.remove('eeee')  # 把元素eeee删除
print('把元素eeee删除', names)
del names[4]  # 把列表下标为4的元素删除
print('把列表下标为4的元素删除', names)
names.pop()  # 无参数时删除最后一个元素，有参数时删除下标对于元素
print('pop()删除', names)
g = names.index('ggggg')  # 查找元素对应的索引
print('ggggg对应下标', g)
c = names.count('aaaaa')  # 元素出现的次数（列表时可以重复的）
print('元素出现的次数', c)
names.reverse()  # 反转列表
print('reverse()反转', names)
names.sort()  # 对列表排序，按照ASCII码（符号，数字，大写字母，小写字母）的优先级排序
print('sort()排序', names)
names2 = ['1111', '2222', '3333', '4444']
names.extend(names2)  # 用列表扩充列表
print('用列表names2扩充列表names1', names)
names.insert(3, ['oooo', 'pppp'])
# del names2  # 删除列表2
names2 = names.copy()  # 浅拷贝，names改变后names2不变，第1层不变，第2层会变
names3 = names  # 深拷贝，names改变后names3也会改变
names.append('asdasd')
print('浅拷贝names2：', names2)
print('深拷贝names3：', names3)
names[3][0] = 'iiiii'
print('改变列表内的列表后浅拷贝names2：', names2)
print('改变列表内的列表后深拷贝names3：', names3)
names2[0] = 'names2'
names3[0] = 'names3'
print('改变names2和names3后,names:', names)
print('改变names2和names3后,names2:', names2)
print('改变names2和names3后,names3:', names3)
import copy

names4 = copy.deepcopy(names)  # 深copy,names4和names是两个完全独立的变量
names[3][1] = 'uuuuu'
print('copy模块的deepcopy', names4)
# for i in names:  # 打印names的内容
# 	print(i)
print(names[::2])  # 切片，带步长

# 列表生成器,只有在调用的时候才生成，names列表是直接生成的
c = (i * 2 for i in range(10))  # class 'generator'
print(type(c))
# a = [c]  # [<generator object <genexpr> at 0x7f9f9f65ca98>]
a = [i * 2 for i in range(10)]
print(a)
b = [i * i for i in range(10) if i % 2 == 0]
print(b)

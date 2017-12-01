from pyquery import PyQuery as pq
html = '''...'''
doc = pq(html)
print(doc('li'))  # html内的li标签全部内容

doc = pq(url='http://www.baidu.com')  # 通过url获得html文本
print(doc('head'))

# 文件初始化
doc = pq(filename='demo.html')
print(doc('li'))

# -------------------------------------------------- #
doc = pq(html)
print(doc('css选择器'))

items = doc('.list')  # 获取class='list'的标签的全部内容，<class 'pyquery.pyquery.PyQuery'>
print(items.find('li'))

print(items.children())  # items所表示的标签下的子标签的全部内容
print(items.children('css选择器')  # 选择items下对应css选择器的标签的全部内容
print(items.parent()) # 父节点
print(items.parents()) # 祖先节点
print(items.parents('css选择器'))
print(items.siblings())  # 获取兄弟标签
print(items.siblings('css选择器'))  # 获取css选择器对应的兄弟标签
# 遍历 items方法
for li in items.items()：
	print(li)

# 得到具体一个标签后，如a
# print(a.attr('href'))  # 获取标签的属性
# print(a.attr.href) # 同上
# print(a.text())  # 获取标签的文本
# print(a.html()) # 获取标签内的全部html内容（标签+文本）

# DOM操作，得到具体一个标签后，如a
# a.removeClass('xxxx')  # 移除一个class
# a.addClass('xxx')  # 增加一个class
# a.attr('name', 'link') # 修改name属性，不存在则添加
# a.css('font-size', '14px') # 修改font-size属性，不存在则添加
# a.remove()  # 移除a所代表的标签

# http://pyquery.readthedocs.io/en/latest/api.html
# http://www.w3cschool.com.cn/css/index.asp

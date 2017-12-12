from bs4 import BeautifulSoup
html = '''.....'''
soup = BeautifulSoup(html,'lxml')
print(soup.prettify)  # 把html调整为标准的html
print(soup.title.string)  # html内title标签的内容
print(soup.title)  # html的title标签（包含的标签和内容），<class 'bs4.element.Tag'>
print(soup.head)  # html的head标签
print(soup.p)  # html的第一个p标签
print(soup.title.name)  # html的title标签的名称
print(soup.p.attrs['name'])  # html的第一个p标签的name属性对应的值
print(soup.p['name'])  # 同上
print(soup.p.string)  # html的第一个p标签的文字(如果p标签内包含标签会过滤标签)
print(soup.head.title.string)  # 嵌套选择head标签内title标签的内容
print(soup.p.contens)  # html的第一个p标签内的全部包容，包括标签，文字，换行符，以列表的形式返回，每一行一个元素
print(soup.p.children)  # list_iterator对象，需要遍历才能取到元素，返回子节点的内容
print(soup.p.descendants)  # generator对象,获取所有的子孙节点，标签内的文本也算一个子孙节点
print(soup.p.parent)  # 获取父节点，输入内容为父节点的全部内容，包括父节点的全部子孙节点
print(list(enumerate(soup.a.next_sibling)))  # a标签的之后的全部兄弟节点（包括换行符），返回的是list
print(list(enumerate(soup.a.previous_sibling)))  # a标签之前的全部兄弟节点（包括换行符）

# findall(name,attrs,recursive,text, **kwargs)
print(soup.findall('ul'))  # 返回列表，每个元素为对应ul标签的全部内容（标签，子节点，节点文本）
for ul in soup.find_all('ul'):
	print(ul.find_all('li'))  # 嵌套查找
print(soup.finall(attrs={'id':'list-1'}))  # 查找对应属性的标签
print(soup.finall(attrs={'name':'elements'}))
print(soup.finall(id='list-1'))
print(soup.finall(class_='element')) # class为关键字,所以改为class_
print(soup.finall(text='Foo'))  # 返回标签内容为Foo的列表（并没有什么用）

print(soup.find('ul')) # 第一个ul标签的全部内容，如果不存在返回None

find_parents(),find_parent()
find_next_siblings(),find_next_sibling()
find_previous_siblings(),find_previous_sibling()
find_all_next(),find_next()
find_all_previous(),find_previous()

print(soup.select('css选择器'))  # 返回列表
for li in soup.select('li'):
	print(li.get_text())  # 所有li标签的文本内容

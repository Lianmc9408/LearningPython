import d077fanshe

d077fanshe.add()

# 反射，通过字符串就可以调用函数
fun_name = 'add'
func = getattr(d077fanshe, fun_name)
func()

permissionList = [
    {'caption': '添加用户', 'func': 'add'},
    {'caption': '删除用户', 'func': 'delete'},
    {'caption': '查看用户', 'func': 'fetch'},
]
for index, item in enumerate(permissionList, 1):
    print(index, item['caption'])
choice = input('输入要选择的菜单')
func_name = permissionList[int(choice) - 1]['func']
func = getattr(d077fanshe, fun_name)
func()

import importlib
# 通过字符串导入模块
m = importlib.import_module('d077fanshe')
function_name = 'add'
funcc = getattr(m, function_name)
funcc()

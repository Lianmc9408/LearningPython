import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
# 创建游标,返回的数据为每一条数据组成的元祖
cursor = conn.cursor()
# 创建游标，返回的数据为每一条数据组成的字典
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


# 参数传递（sql语句不要通过字符串拼接的形式写！）
inp = input('请输入班级')
q = cursor.execute('insert into class(caption) values(%s)', inp)

# sql = 'select username,password from userinfo where username="%s" and password="%s"'
# sql = sql % ('abc', '123')
# sql = sql % ('abc" or 1=1 --' , '123')
# sql被改成上面这句后，sql语句会变成如下
# sql = 'select username,password from userinfo where username="abc" -- " and password="123"'
# -- 为sql语句的注释部分，密码部分被注释掉不需要密码就可以登录了
# cursor.execute(sql)

# 多个参数时的参数用元祖的形式
# q = cursor.execute('insert into student(gender, class_id, sname) values(%s,%s,%s)', ('男', 1, '小三'))

# 执行SQL，并返回收影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2'")

# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

# 参数多条参数时使用excutemany
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
# 获取最新自增ID（最后一条数据的自增ID）
# new_id = cursor.lastrowid

# 查
# r = cursor.execute('select * from class')
# result = cursor.fetchall()  # 取出查找的全部数据

# result = cursor.fetchone()  # 取出查找的第一条数据
#                              继续执行cursor.fetchone()会继续取下面一条数据，指针会一直往下执行，没数据是返回None
# cursor.scroll(1,mode='relative')  # 相对当前位置移动，往下走一个
# cursor.scroll(-1,mode='relative')  # 相对当前位置移动，往上走一个
# cursor.scroll(2,mode='absolute') # 相对绝对位置移动

# result = cursor.fetchmany(3)  # 取出查找的前3条数据
# print(result)


# 提交，不然无法保存新建或者修改的数据
# 增删改涉及到数据更改的时候需要使用commit，查的时候不需要
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()

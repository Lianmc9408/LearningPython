# pymysql 执行存储过程

import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 执行存储过程
r1 = cursor.callproc('p1', args=(1, 22, 3, 4))
print(r1)
result1 = cursor.fetchall()
print(result1)
# 获取执行完存储的参数
cursor.execute("select @_p1_0,@_p1_1,@_p1_2,@_p1_3")
result = cursor.fetchall()
print(result)
conn.commit()
cursor.close()
conn.close()


print(result)

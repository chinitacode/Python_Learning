# 插入数据
'''
executemany()方法可以一次插入多条值，执行单条sql语句,
但是重复执行参数列表里的参数,返回值为受影响的行数。
'''
import MySQLdb

conn = MySQLdb.connect(host = 'localhost', port = 3306, user = 'root',
passwd = '123456', db = 'friends')

#通过获取到的数据库连接conn下的cursor()方法来创建游标。
cur = conn.cursor()


# 插入一条数据
insrt = "insert into bff values(%s, %s, %s, %s)"
cur.execute(insrt, ('Yang', 'Xue', '19951112', 25))


# 插入多条数据
cur.executemany(insrt, [
    ('Xiong', 'Linlu', '19940809', 26),
    ('Tao', 'Ran', '19940710', 25)
    ])


cur.close()

conn.commit()

conn.close()

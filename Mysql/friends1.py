import MySQLdb

conn = MySQLdb.connect(host = 'localhost', port = 3306, user = 'root',
passwd = '123456', db = 'friends')

#通过获取到的数据库连接conn下的cursor()方法来创建游标。
cur = conn.cursor()

#创建数据表,通过游标cur 操作execute()方法可以写入纯sql语句。通过execute()方法中写如sql语句来对数据进行操作
create_bff = "create table bff(first_name char(20) not null, second_name char(20) not null, birthday char(30), age int(10))"
cur.execute(create_bff)

#插入一条数据
insrt1 = "insert into bff(first_name, second_name, birthday, age) values('Zhou', 'Rongxu', '19950520', 24)"
cur.execute(insrt1)


#修改查询条件的数据
modfy = "update bff set birthday='19950418' where second_name = 'Rongxu'"
cur.execute(modfy)

insrt2 = "insert into bff(first_name, second_name, birthday, age) values('Zhou', 'Dongyu', '19920520', 25)"
cur.execute(insrt2)


#删除查询条件的数据
dele = "delete from bff where age='25'"
cur.execute(dele)

#cur.close() 关闭游标
cur.close()

#conn.commit()方法在提交事物，在向数据库插入一条数据时必须要有这个方法，否则数据不会被真正的插入。
conn.commit() #每次修改数据后都要提交才能生效

#conn.close()关闭数据库连接
conn.close()

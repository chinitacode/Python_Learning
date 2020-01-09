import MySQLdb

db = MySQLdb.connect(host = 'localhost', port = 3306, user = 'root',
    passwd = '123456', db = 'tfm')

cur = db.cursor()

create_tb = 'create table 20topics(topicId int(10), ranking int(10), docId int(10), filename char(80))'
cur.execute(create_tb)

cur.close()

db.commit()

db.close()

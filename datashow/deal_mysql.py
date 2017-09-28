import MySQLdb as mysql
import random as rd

conn = mysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     passwd='root',
                     db='test')

cur = conn.cursor()
rdname = rd.randint(1, 10)
print cur.execute("insert into student (name, age) values('" + "lilei" + str(rdname) + "', 11) ")
print cur.executemany("insert into student (name, age) values(%s, %s) ", [("lilei" + str(rdname), 11)])
cur.close()
conn.commit()
cur = conn.cursor()
num = cur.execute('select * from student')
print 1
print cur.fetchall()
cur.scroll(0,'absolute')
print 2
print cur.fetchmany(num - 1)
print 3
cur.scroll(0,'absolute')
print cur.fetchone()
cur.close()
conn.close()
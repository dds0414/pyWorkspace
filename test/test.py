# -*- coding: utf-8 -*-
import MySQLdb
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

def _doSql(sql):
    rowL = []
    try:
        # 执行sql语句
        cur.execute(sql)
        rowL = cur.fetchall()
        # 提交到数据库执行
        conn.commit()
    except:
        conn.rollback()
    return rowL


conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306, charset="utf8")
cur = conn.cursor()
conn.select_db('ysd')


# file_object = open('country.js').readlines()
file_object = open('city2.js').readlines()
for i in file_object:
    # print i.split(',')[1],i.split(',')[2]
    arrcity = "INSERT INTO think_cs_city2 (`city_id`,`city_name`) VALUES (" + i.split(',')[2] +"," + i.split(',')[1] + ")"
    print arrcity
    _doSql(arrcity)

conn.commit()
cur.close()
conn.close()

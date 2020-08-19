"""
pymysql 连接数据库
"""

import pymysql

# 连接数据库 (连接本机可以不写host和port)
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "stu",
                     charset = "utf8"
)

# 创建游标 (执行sql语句获取执行结果的对象)
cur = db.cursor()

# 执行各种sql语句,操作数据库
sql = 'create database dict character set utf8;'
cur.execute(sql)
sql = 'use dict;'
cur.execute(sql)
sql = 'create table words (' \
      ' id int primary key auto_increment,' \
      'word varchar(30) not null,' \
      'mean varchar(512));'
cur.execute(sql)
# 关闭游标和数据库连接
cur.close()
db.close()



import pymysql
import re
#输入数据
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "stu",
                     charset = "utf8")
# 创建游标 (执行sql语句获取执行结果的对象)
cur = db.cursor()
sql ='use dict;'
cur.execute(sql)
#打开dict.txt文件
with  open('dict.txt') as f:
    b =list()
    for x in f:
        t = re.findall(r"(\w+)\s+(.*)",x)
        print(t)
        b.extend(t)
sql ='insert into words (word,mean) values (%s,%s);'
cur.executemany(sql,b)
db.commit()
cur.close()
db.close()

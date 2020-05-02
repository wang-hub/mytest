# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:58:21 2020

@author: wangwei
"""

'''
应用程序操作数据库步骤：
0.安装数据库

1.引入相应的模块：数据库操作模块-->找驱动
2.建立数据库的连接（ip地址，端口号，用户名，口令）
3.创建会话，执行sql语句
4.处理sql语句的执行结果
5.关闭数据库连接
常见sql语句：
    show databases
    create database databasename
    use database
    show tables
    create table tablename (numbername1 numbertype1(num),numbername2 numbertype2(num2))
    drop table tablename
    delete from tablename where numbername=''
    insert into table values(numbername1,numbername2)
'''

#操作sqlite
import sqlite3  #找驱动

conn=sqlite3.connect("addressBook.db")  #建立数据库连接,如果数据库文件不存在，创建一个数据库文件

cur=conn.cursor()        #创建游标（会话）

#cur.execute("语句")
#sql="create table addresslist(name char(10),sex char(2),phon char(12),qq char(15),address varchar(50))"
#cur.execute(sql)
sql="insert into addresslist values('ww','1','155','167','shanghai')"
cur.execute(sql)
cur.execute("insert into addresslist values('wq','2','154','166','sichuan')")
che="select * from addresslist"
#print(list(cur.execute(che)))
cur.execute(che)
print('sel affect:',cur.rowcount)
print("fetchall result:")
rs=cur.fetchall()
for line in rs:
    print(line)

dele="delete from addresslist where name='ww' "
cur.execute(dele)

#刚刚执行的sql语句影响的行数
#通常在insert，delete，update后
#>=0成功，<0失败
print(cur.rowcount)

cur.execute(che)
rs=cur.fetchall()
for line in rs:
    print(line)

rs=cur.execute(che)
print(list(rs))

conn.commit()
conn.close()    #关闭连接

#操作mysql
#三个方式
    #mysqldb
    #mysql.connector
''' 
import mysql.connector
try:
    conn=mysql.connextor.connect(host='localhost',port='3306',user='root',password='123456',database='pythonuse')
    #mysql:3306,orcal:1521
    #localhost=127.0.0.1
    cur=conn.cursor()
    
    showtab="show tables"
    print(cur.execute(showtab))
    che="select * from number"

    cur.commit()
    cur.close()
    conn.close()
except:
    print('error')
'''

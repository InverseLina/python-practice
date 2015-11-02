# encoding=utf-8
__author__ = 'Hinsteny'

import sqlite3

conn = sqlite3.connect("sqliteData.db")

curs = conn.cursor()

sqlCreate = "create table user(id integer primary key autoincrement, name, password);"
sqlInsert = "insert into user (name, password) values('hinsteny','1234567')"
sqlSelect = "select * from user"
# data = curs.execute(sqlCreate)
# data = curs.execute(sqlInsert)
# conn.commit()
data = curs.execute(sqlSelect)

names = [f[0] for f in curs.description]
print(names)
print()
print()

for row in curs.fetchall():
    for pair in zip(names, row):
        print(pair)
    print()



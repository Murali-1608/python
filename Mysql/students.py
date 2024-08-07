import mysql.connector as con
db=con.connect(host="localhost",user="root",password="Password@16")
cur=db.cursor()
cur.execute("create database students")
cur.execute("show databases")
for i in cur:
    print(i)







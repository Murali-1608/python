import mysql.connector as con
import csv
csv_data=csv.reader((open('stud_det.csv','r')))
query_3="insert into stud_det(Stud_id, Stud_name, Stud_city, Stud_contact, Stud_adm_date) values(%s, %s, %s, %s, %s)"
for cp in csv_data:
    value_1=cp
    db=con.connect(host="localhost",user="root",password="Password@16",database="studentsnew",autocommit=True)
    c=db.cursor()
    c.execute(query_3,value_1)
    db.commit
    print("rows inserted")
db.close

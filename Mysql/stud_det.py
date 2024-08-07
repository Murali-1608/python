import mysql.connector as con
db=con.connect(host="localhost",user="root",password="Password@16",database="Students")
c=db.cursor()
q1="create table Stud_det(Stud_id int primary key, Stud_name char(45),"
q2=" Stud_city char(40), Stud_contact int, Stud_adm_date int)"
query_1=q1+q2
c.execute(query_1)
db.commit
print("Stud_det created")


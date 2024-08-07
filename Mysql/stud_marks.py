import mysql.connector as con
db=con.connect(host="localhost",user="root",password="Password@16",database="Students")
c=db.cursor()
q3="create table Stud_marks(Stud_id int primary key,Stud_eng_marks int,"
q4=" Stud_lang_marks int,Stud_math_marks int, Stud_total int,"
q5=" Stud_avg decimal(5,2), Foreign key(Stud_id)References stud_det(Stud_id))"
query_2=q3+q4+q5
c.execute(query_2)
db.commit
print("Stud_marks created")

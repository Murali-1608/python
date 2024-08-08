import mysql.connector as con
import csv
with open('stud_marks.csv','r') as csvfile:
    csv_data=csv.reader(csvfile)
    db=con.connect(host="localhost",user="root",password="Password@16",database="studentsnew",autocommit=True)
    c=db.cursor()
    query_4="Insert into stud_marks(Stud_id, Stud_eng_marks, Stud_lang_marks, Stud_math_marks, Stud_total, Stud_avg) Values(%s, %s, %s, %s, %s, %s)"
    for cp in csv_data:
        c.execute(query_4,cp)
        db.commit()
        print("Row inserted")
db.close()

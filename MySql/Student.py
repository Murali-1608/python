import mysql.connector as con
class Student:
    def __init__(self,id,name,*marks):
        self.id = id
        self.name = name
        self.em = marks[0]
        self.lm = marks[1]
        self.mm = marks[2]
    def calc_and_avg(self,*m):
        sum=0
        for i in m:
            sum+=i
        return sum,sum/len(m)
    @classmethod
    def printer(cls,id,name,*m):
        print("id:",cls.id)
        print("name:",cls.name)
        print("total and average:",self.calc_and_avg(self.em,self.lm,self.mm))
    @classmethod
    def update(cls,tot,avg,id):
        db=con.connect(host="localhost",user="root",password="Password@16",database="studentsnew",autocommit=True)
        cur=db.cursor()
        value=(tot,avg,id)
        cur.execute("update Stud_marks set Stud_total = %s, Stud_avg = %s where Stud_id = %s", value)
        db.commit
    @classmethod
    def extract(cls):
        db=con.connect(host="localhost",user="root",password="Password@16",database="studentsnew",autocommit=True)
        cur=db.cursor()
        cur.execute("select Stud_id, (Stud_eng_marks + Stud_lang_marks + Stud_math_marks) as sum,((Stud_eng_marks+Stud_lang_marks+Stud_math_marks)/3) as avg from Stud_marks group by Stud_id")
        a=[]
        j=0
        for i in cur:
            print(i)
            a.append(i)
            Student.update(a[j][1],a[j][2],a[j][0])
            j+=1
Student.extract()   
    

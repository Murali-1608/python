#1
from random import randint
names = ["Harsh","Aadhi","Karunesh","Sam"]
eng_marks = {ele : randint(1,100) for ele in names}
print("eng_marks = ",eng_marks)
print()
#2nd
lang_marks = {ele : randint(1,100) for ele in names}
print("lang_marks = ",(lang_marks))
print()
#3
actual_marks=[]
actual_marks.append(eng_marks)
actual_marks.append(lang_marks)
print("actual_marks=",actual_marks)
print()
#4
a,b = [eng_marks[x] for x in eng_marks], [lang_marks[y] for y in lang_marks]
if len(a) < len(b):
    a.append(0)
else:
    b.append(0)
total_marks = [a[i] + b[i] for i in range(len(a))]
print(total_marks,"#total of two subject marks")
print()
#5
sub = ['Eng','lang','total']
list_of_name_sub_tot = [(name,sub[0],sub[1],sub[2]) for name in names]
print("list_of_name_sub_tot =",list_of_name_sub_tot)
print()
#6
A = dict(zip(list_of_name_sub_tot,[None]*len(list_of_name_sub_tot)))
print(A)
print()

class_marks = {tuple_: total for tuple_, total in zip(list_of_name_sub_tot, total_marks)}
print("class_marks =",class_marks)
print()

class_marks = {tuple_:[eng_marks[name],lang_marks[name],total]for name,tuple_,total in zip(names,list_of_name_sub_tot,total_marks)}
print(class_marks)
print()

#7
feedback = ["Kutty Pattas" if total > 120 else "Good Student" if total > 100 else "Slow Bloomer" for total in total_marks]
class_marks = {(name, sub[0], sub[1], sub[2]): [eng_marks[name], lang_marks[name], total, fb]for name, total, fb in zip(names, total_marks, feedback)}
print("class_marks =", class_marks)

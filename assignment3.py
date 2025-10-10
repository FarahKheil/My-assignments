input_number_of_students= int(input("enter students number:"))
student = []
L = []
S = []

for i in range(input_number_of_students):
   i+=1
   name = str(input("enter student " + str(i) + " name:"))
   score = str(input("enter " + name + "'s"  + " score:"), )
   student.append((name, score))
   L.append ((name + '-' + score))
   S.append (int(score))
sum_list = int(score)
def sum_list(S): 
        if len(S) == 0:                      
          return 0 
        else:                                   
          return S [0] + sum_list(S[1:])
Total = (sum_list(S)) / (input_number_of_students)
SC = int(score)
highest_grade = -1
top_student_name = ""
print('students =', student)
print('all students and scores: ')
for item in L:
 print (item)
print ('average score: ', Total)

for name, score in student:
   score = int(score)
   if score > highest_grade:
      highest_grade = score
      top_student_name = name
print('top student: ' , top_student_name, (score))

def low_grade (name, SC):
      if SC < 60:
       print ('failed student: ', name)
for name, score in student:
 low_grade(name, int(score))


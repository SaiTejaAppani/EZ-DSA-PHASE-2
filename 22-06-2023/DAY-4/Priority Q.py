'''
Append(key,value)
key   = priority
value = element in queue
and sort the list every time an element
is appended. '''

students_grade=[]

students_grade.append((1,"Akash"))
students_grade.append((2,"Ankitha"))

#students_grade.sort(reverse=True)
print("Yes")
print(students_grade)

students_grade.append((3,"Sid"))
#students_grade.sort(reverse=True)

students_grade.append((4,"Akshay"))
students_grade.sort(reverse=True)

print("Priority wise sorted")
print(students_grade)

print("Original Queue")
while students_grade:
    print(students_grade.pop())

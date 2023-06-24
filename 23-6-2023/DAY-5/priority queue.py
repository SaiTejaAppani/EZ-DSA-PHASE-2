students_grade=[]
students_grade.append((1,'Teja'))
students_grade.append((4,'Sriram'))
students_grade.sort(reverse=True)
print('yes')
print(students_grade)
students_grade.append((3,'Pranay'))
students_grade.sort(reverse=True)
students_grade.append((2,'DJ Tinku'))
students_grade.sort(reverse=True)
print('Priority wise sorted')
print(students_grade)
print('original queue')
while students_grade:
    print(students_grade.pop())
    

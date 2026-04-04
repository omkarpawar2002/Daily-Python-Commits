'''MINI PROJECT 1 – GRADE CALCULATOR

Program takes marks → shows grade.

Concepts used:

input
type casting
if elif
comparison operators'''

marks = int(input("Enter your marks : "))
grade = ''
if(marks >= 90):
    grade = 'A+'
elif(marks >= 80):
    grade = 'A'
elif(marks >= 70):
    grade = 'B'
elif(marks >= 60):
    grade = 'C'
elif(marks >= 40):
    grade = 'D'
else:
    grade = 'F'
print("Student Get Marks",marks,"with",grade,"Grade")
# Create 5 variables storing different data types.
'''
name = "kirti"
age = 34
marks = 87.34
is_student = True
phone_number = ['1111','2222']
print(name)
print(age)
print(marks)
print(is_student)
print(phone_number)
'''

# Change variable value from integer to string.
'''
a = 30
print(a,type(a))
a = "This is string"
print(a,type(a))
'''

# Create multiple variables in one line.
'''
a , b , c = True , 23 , "Welcome"
print(a)
print(b)
print(c)
'''

# Assign same value to 3 variables.
'''
a = b = c = 30
print(a)
print(b)
print(c)
'''

# Check type of different variables.
'''
name = "kirti"
age = 34
marks = 87.34
is_student = True
phone_number = ['1111','2222']
print(name,type(name))
print(age,type(age))
print(marks,type(marks))
print(is_student,type(is_student))
print(phone_number,type(phone_number))
'''

# Create variable and print its memory id.
'''
name = "Alice"
print(name,id(name))
'''

# Create two variables with same value and compare id.
'''
a = 45
b = 45
print(a == b)
print(a,id(a))
print(b,id(b))
'''

# Store your details using mapping type.
'''
student_data = {
    'name':'Alice',
    'age':19,
    'is_student':True,
    'marks':67
}
print(student_data)
'''

# Store unique numbers using set.
'''
s = {101,102,103,101,102}   # Here we try to put duplicate but it remove duplicate and store only unique element
print(s)
'''

# Create variable without value using None.
'''
country = None
print(country,type(country))
'''
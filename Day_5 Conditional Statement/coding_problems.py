# Check number positive.
'''
number = int(input("Enter number : "))
if(number > 0):
    print("number is positive")
'''

# Check number negative.
'''
number = int(input("Enter number : "))
if(number < 0):
    print("number is negative")
'''

# Check number greater than 50.
'''
number = int(input("Enter number : "))
if(number > 50):
    print("number is greater than 50")
'''

# Check age ≥ 18.
'''
age = int(input("Enter age : "))
if(age >= 18):
    print("age greater than or equals to 18")
'''

# Check marks ≥ 40.
'''
marks = int(input("Enter marks : "))
if(marks >= 40):
    print("Pass")
'''

# Check even or odd.
'''
num = int(input("Enter any number : "))
if(num % 2 == 0):
    print("Even")
else:
    print("odd")
'''

# Compare 2 numbers.
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if(num1 == num2):
    print("Both are same")
'''

# Check pass or fail.
'''
marks = int(input("Enter marks : "))
if(marks >= 35):
    print("Pass")
else:
    print("Fail")
'''

# Check number > 100.
'''
num = int(input("Enter any number : "))
if(num > 100):
    print("Number is greater than 100")
'''

# Check boolean value.
'''
num = input("Enter any number : ")
print(bool(num))
'''

# Grade calculator.
'''
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
'''

# Temperature category.
'''
temp = int(input("Enter temperature : "))
if(temp < 0):
    print("Temperature is too cold")
elif(temp <= 40):
    print("Temperature is ok")
else:
    print("Temperature is too hot")
'''

# Age category.
'''
age = int(input("Enter your age : "))
if(age <= 12):
    print("Kid")
elif(age < 18):
    print("Teen")
elif(age < 65):
    print("Adult")
else:
    print("Old")
'''

# Marks category.
'''
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
'''

# Salary category.
'''
salary = 25000
if salary >= 25000:
    print("Eligible for loan")
elif salary >= 20000:
    print("Wait for increment")
else:
    print("Can not apply")
'''

# Check login condition.
'''
user = input("Enter username : ")
if(user == 'Admin'):
    print("Login Access!")
else:
    print("Login Denied!")
'''

# Check age and id.
'''
age = int(input("Enter age : "))
id = int(input("Enter Id : "))
if(age >= 18 and id < 21):
    print("Eligible")
else:
    print("Not Eligible")
'''

# Check number range.
'''
num = int(input("Enter number : "))
if(num in range(1,31)):
    print("Number in range 1 to 30")
elif(num in range(31,61)):
    print("Number in range 31 to 60")
else:
    print("Number in grater than 60")
'''

# Check username and password.
'''
username = input("Enter your username : ")
password = input("Enter your password : ")
if(username == 'admin' and password == 'admin@123'):
    print("Login")
else:
    print("Enter correct username or password")
'''

# Check even odd using ternary.
'''
num = int(input("Enter number : "))
res = "Even" if(num % 2 == 0) else "Odd"
print(res)
'''
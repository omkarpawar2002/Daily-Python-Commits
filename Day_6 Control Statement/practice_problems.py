# Print numbers 1 to 10.
'''
for i in range(1,11):
    print(i)
'''

# Print numbers 1 to 20 using while loop.
'''
i = 1
while i < 21:
    print(i)
    i += 1
'''

# Print list items.
'''
li = [10,20,30]
for i in li:
    print(i)
'''

# Print characters of string.
'''
name = 'kiran'
for i in name:
    print(i)
'''

# Print numbers using range().
'''
for i in range(1,6):
    print(i)
'''

# Print numbers 10 to 1.
'''
for i in range(10,0,-1):
    print(i)
'''

# Print even numbers.
'''
for i in range(1,11):
    if(i % 2 == 0):
        print(i)
'''

# Print odd numbers.
'''
for i in range(1,11):
    if(i % 2 != 0):
        print(i)
'''

# Print dictionary keys.
'''
student_detail = {
    'name':'hardy',
    'age':34,
    'is_login':True
}
for key in student_detail:
    print(key)
'''

# Print dictionary values.
'''
student_detail = {
    'name':'hardy',
    'age':34,
    'is_login':True
}
for key in student_detail:
    print(student_detail[key])
'''

# Print sum of numbers 1 to 10.
'''
total = 0
for i in range(1,11):
    total += i
print(total)
'''

# Print multiplication table of 5.
'''
for i in range(1,11):
    print(i*5)
'''

# Print numbers divisible by 3.
'''
for i in range(1,11):
    if(i % 3 == 0):
        print(i)
'''

# Stop loop when number equals 7.
'''
for i in range(1,11):
    if(i == 7):
        break
    print(i)
'''

# Skip number 5.
'''
for i in range(1,11):
    if(i == 5):
        continue
    print(i)
'''

# Count characters in string.
'''
name = "kirti"
count_character = 0
for i in name:
    count_character += 1
print(count_character)
'''

# Use nested loop to print pairs.
'''
for i in range(1,4):
    for j in range(1,3):
        print(i,j,end=' ')
    print()
'''

# Print square numbers.
'''
for i in range(1,6):
    print(i**2)
'''

# Print numbers using step.
'''
for i in range(1,21,2):
    print(i)
'''
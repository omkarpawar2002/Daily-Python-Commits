# Control Statement :
'''
Control statements are used when we want to execute the certain code statement in repetative manner.

There are 2 types of control statement :
    1.for loop
    2.while loop
'''

# for loop :
'''
for loop is used when we know the exact number of times the iteration is required.
for loop is iterate over sequences like list , tuple , string , dictionary or range.
'''

# Iterate over list :
li = [10,20,30,40,50]
for i in li:
    print(i)


# Iterate over tuple :
t = (101,102,103,104,105)
for i in t:
    print(i)


# Iterate over string :
name = "Avinash"
for ch in name:
    print(ch)


# Iterate over dictionary :
student_detail = {
    'name':'hardy',
    'age':34,
    'is_login':True
}
for key,value in student_detail.items():
    print("Key ",key)
    print("Value ",value)
    print("----------")


# for loop with range() :
'''
range() function is used to generate a sequence of numbers.
It takes 3 parameters range(start,stop,step) 
By default start from 0 and step is 1 and both are optional but we need to provide stop condition and it excluded.
'''

# iterate a loop from 1 to 5
for i in range(1,6):
    print(i)


# while loop :
'''
While loop is used when we don't know the exact number of times the iteration is required.
And we need to provide the condition otherwise loop runs infintely
'''

i = 1
while i < 7:
    print(i)
    i += 1


# Infinite loop :
'''
i = 1
while i < 10:
    print(i)
'''


# Nested Loop 
'''
Loop inside another loop known as a nested loop.
'''

for i in range(1,6):
    for j in range(1,6):
        print("*",end=' ')
    print()
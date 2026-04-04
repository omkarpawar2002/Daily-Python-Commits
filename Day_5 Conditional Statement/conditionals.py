# Conditional Statements :
'''
Conditional Statements are used to manipulate the flow of program execution.

There are 3 types of conditional statements :
    1.If statement
    2.If - else statement
    3.If - elif - else statement
'''

# If statement :
'''
The if block will get executed only when the condition specified after the if keyword is True otherwise it will skipped the if block.
If statement is used when we want to check single condition.
'''

number = 23
if(number > 34):
    print(number," is greater than 34")


# If-else statement :
'''
The if block will get executed only when the condition specified after the if keyword is True otherwise if will be skipped and else block will get executed.
'''

age = 20
if(age >= 18):
    print("You can vote!")
else:
    print("You can't vote!")


# If-elif-else statement :
'''
Here single if block followed by multiple elif blocks and multiple elif blocks follow by single else block.

The if block will get executed only when the condition specified after the if keyword is True otherwise if will be skipped and next elif block will check the condition and if the condition is True then elif will get executed and if not then else block will get executed.
'''

# Check number is positive , negative or zero
num = int(input("Enter number : "))
if(num == 0):
    print("number is 0")
elif(num > 0):
    print("number is positive")
elif(num < 0):
    print("number is negative")
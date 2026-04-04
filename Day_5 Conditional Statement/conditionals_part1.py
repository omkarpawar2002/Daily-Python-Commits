# Nested if :
'''
The if inside another if is known as a nested if.
'''

num = int(input("Enter any number : "))
is_available = True
if(num >= 18):
    if(is_available):
        print("Allowed Entry")


# Multiple conditions :
'''
We can check multiple conditions by using logical operators.
'''
salary = 25000
age = int(input("Enter your age : "))
if(age >= 18 and salary >= 20000):
    print("you can apply for loan!")


# Ternary operator :
'''
Python supports a ternary conditional expression written using if-else in one line.
'''
age = int(input("Enter your age : "))
result = "Eligible" if(age >= 18) else "Not Eligible"
print(result)
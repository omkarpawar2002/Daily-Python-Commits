# Logical Operators : 
'''
Logical Operators are used when we want to check multiple conditions and return a boolean result or expression.

and will return True only if both the conditions are True otherwise return False.
or will return False only if both the condition are False otherwise return True.
not will return True if result is False and return False if result is True.
'''

num1 = int(input("Enter first input number : "))
num2 = int(input("Enter second input number : "))
print((num1 == num2) and (num1 > num2))
print((num1 == num2) or (num1 >= num2))
print(not(num1 > num2))

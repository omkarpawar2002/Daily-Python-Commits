# input() : 
'''
1.input() function is used to take input from user.
2.By default input() function return string.
3.So to perform the operation we need to convert the input into required data type.
'''

# Example : String input 
'''
name = input("Enter your name : ")
print(name,type(name))
'''

# Example : Integer Input
'''
age = int(input("Enter your age : "))
print(age,type(age))
'''


# ============================

# print() : 
'''
print() function is used to display the output on screen.

Example : 
        print("welcome to input / output program")
'''

# seperator ( sep ) parameter :
'''
By default seperator parameter contain space.
But we can provide according to our need.
'''

# Default seperator 
'''
print("python","java","c++")
'''

# Custome seperator
'''
print("python","java","c++",sep='#')
'''

# end parameter : 
'''
By default end parameter comes at end of print.
default end parameter = new line [\n]
'''

# Default end parameter with \n
'''
print("Hello")
print("World")
'''

# customer end parameter 

print("Hello",end=' ')
print("World")
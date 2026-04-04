# Type Conversion
'''
Type conversion is the process of coverting one data type into another data type.
'''

# There are 2 types of Type Conversion In Python
'''
    a.Implicit Type Conversion
    b.Explicit Type Conversion
'''

# Implicit Type Conversion
'''
Here we no need to convert the data type python will automatically convert one data type into another data type.

# Example :
a = 10
b = 23.45
res = a + b
print(res,type(res))    # 33.45 <class 'float'>

This Implicit type conversion automatically happens here because 1 is integer type and another is float so here we no need to loss the data from float. So it first convert the integer to float then perform addition
'''

# Explicit Type Conversion
'''
Explicit type conversion means we manually convert the one data type into another data type by using some built in function like int() , float() , bool() , str() etc.
'''

# int() will convert into integer data type
'''
num = "23"
print(num,type(num))
num = int(num)
print(num,type(num))
'''

# float() will convert into float data type
'''
marks = '89.34'
print(marks,type(marks))
marks = float(marks)
print(marks,type(marks))
'''

# str() will convert into string data type
'''
num = 80
print(num,type(num))
num = str(num)
print(num,type(num))
'''

# bool() will convert into boolean type and the value is either True or False
# Note :- 0 , False , None , '' , [] , {}  This are Falsy Values and Rest of others are Truthy Values.
'''
name = 'alice'
print(name,bool(name))
name = ''
print(name,bool(name))
'''
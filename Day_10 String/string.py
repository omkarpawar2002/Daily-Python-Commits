# String Data Type
'''
    1.String is a sequence of characters.
    2.Anything which written inside single quote or double quote are treated as string.
    3.String is immutable in nature.
'''


# Here we are create a variable which hold string value and then we check the data type of that variable
name = "ashish"
print(name , type(name))


# Through indexing we can access string characters and string supports both positive and negative indexing.
name = "Sudhanshu"
print(name[0])
print(name[-2])


# String is a sequence of characters so we can iterate it.
name = "Ashok Verma"
for ch in name:
    print(ch)


# String also supports slicing.
st = "This is a string"
print(st[::2])


# String immutable in nature so we can not modified the character inside string.
'''
name = "Ashok Verma"
print(name)
name[2] = "K"   # Here we get an error
print(name)
'''


# String create by using single or double quotes
name = "John Doe"
print(name)
updated_name = 'John Nikolas'
print(updated_name)


# Concatenation [ + ]
'''
We can concatenate 2 strings by using + operators.
'''
st1 = "Hello"
st2 = "World"
print(st1+st2)


# repetation [ * ]
'''
By using * asterisk we can repeat the string that much number of times.
'''
st = "welcome"
print(st * 2)


# String formating by using f-string
'''
f-string is a modern way to embedded a variable or expression directly inside a string
'''
age = 23
name = "alice"
print(f"My name is {name} and i am {age} years old")


# String formatting by using format() method
'''
By using format() method we need to skip the empty curly brackets so later the variable can be place in that brackets.
'''
name = "Georgina"
age = 34
print("Hello I am {} and My age is {}".format(name,age))
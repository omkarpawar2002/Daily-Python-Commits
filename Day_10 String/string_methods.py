# String Methods :- 

# 1.len() :- len() is used to find the length of elements.
'''
name = input("Enter any name :- ")
print("Total length",len(name))
'''

# 2.title() :- This method is used to convert first letter of each word in uppercase.
'''
name = input("Enter any prompt :- ")
print(name.title())
'''

# 3.upper() :- upper() method is used to convert lowercase to uppercase.
'''
name = input("Enter any prompt :- ")
print(name.upper()) 
'''

# 4.lower() :- lower() method is used to convert uppercase to lowercase.
'''
name = input("Enter any prompt :- ")
print(name.lower()) 
'''

# 5.capitalize() :- capitalize() method is used to convert the first character in uppercase and rest of in lowercase.
'''
name = input("Enter any prompt :- ")
print(name.capitalize()) 
'''

# 6.isdigit() :- isdigit() method return True if all characters are digits otherwise return False.
'''
name = input("Enter any prompt :- ")
print(name.isdigit()) 
'''

# 7.isalpha() :- isalpha() method return True if all the characters are alphabets otherwise return False.
'''
name = input("Enter any prompt :- ")
print(name.isalpha()) 
'''

# 8.isalnum() :- isalnum() return True if character is alphabet or digit or combination of both otherwise it return False.
'''
name = input("Enter any prompt :- ")
print(name.isalnum()) 
'''

# 9.index() :- index() method will return the index position of specified element and if the element not found it raise an error
'''
name = input("Enter any prompt :- ")
print(name.index('l'))
'''

# 10.count() :- count() method will return the count of occurances of specified element.
'''
name = input("Enter any prompt :- ")
print(name.count('e')) 
'''

# 11.startswith() :- startswith() method return True if character starts with specified element otherwise return False.
'''
name = input("Enter any prompt :- ")
print(name.startswith('w')) 
'''

# 12.endswith() :- endswith() method return True if character ends with specified element otherwise return False.
'''
name = input("Enter any prompt :- ")
print(name.endswith('s')) 
'''

# 13.find() :- find() method return the index of first occurance of specified element . If it's not found then it return -1
'''
name = input("Enter any prompt :- ")
print(name.find('e')) 
'''

# 14.islower() :- islower() method return True if characters are in lowercase otherwise return False.
'''
name = input("Enter any prompt :- ")
print(name.islower()) 
'''

# 15.isupper()  :- isupper() method return True if characters are in Uppercase otherwise return False.
'''
name = input("Enter any prompt :- ")
print(name.isupper()) 
'''

# 16. lstrip() :- lstrip() method is used to remove the whitespaces from left side of string.
'''
name = '------welcome------'
print(name)
print(name.lstrip('-'))
print(name)
'''

# 17.rstrip() :- rstrip() method is used to remove the whitespaces from right side of String.
'''
name = '------welcome------'
print(name)
print(name.rstrip('-'))
print(name)
'''

# 18.strip() :- strip() method is used to remove leading and trailing whitespaces.
'''
name = '------welcome------'
print(name)
print(name.strip('-'))
print(name)
'''

# 19.rfind() :- rfind() method return the highest index position of specified element and if it not found then it return the -1
'''
name = input("Enter any prompt :- ")
print(name)
print(name.rfind('e'))
'''

# 20.rindex() :- rindex() method return the highest index of speicied element and if it not found then it shows an error.
'''
name = input("Enter any prompt :- ")
print(name.rindex('e'))
'''

# 21.split() :- split() method breaks the string into list.
'''
name = input("Enter any prompt :- ")
print(name.split())
'''
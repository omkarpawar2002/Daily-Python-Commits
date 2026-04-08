# Dictionary Data Structure :

'''
1.Dictionary is mutable in nature.
2.Dictionary is represented by curly brackets {}.
3.In Dictionary data will be store in key - value pair form.
4.In Dictionary each key will be unique and value can be duplicate or any other data types.
5.After python 3.7 Dictionary will become ordered data structure.
6.In Dictionary indexing and slicing is not possible , through keys we can access values inside Dictionary.
'''


# To create a Dictionary in python there are 2 ways :
'''
# First Way :- 
d = {}

# Second way :- 
d = dict()
'''


# How to access values inside Dictionary.
d = {1:10,2:20,3:30,4:40}
print(d[1])
print(d[2])
print(d[3])
print(d[4])

# Here we see how do we create dictionary 
d = {
    1:'Welcome',
    2:'to',
    3:'jumanji',
    4:'world'
}
print(d)


# Here we see how to access any value from dictionary
d = {
    1:'Welcome',
    2:'to',
    3:'jumanji',
    4:'world'
}
print(d[3])


# Here we see how to modify dictionary keys value 
d = {
    1:'Welcome',
    2:'to',
    3:'jumanji',
    4:'world'
}
d[2] = "my new"
print(d)


# Here we see how to delete dictionary key,value pairs
d = {
    1:'Welcome',
    2:'to',
    3:'jumanji',
    4:'world'
}
del d[2]
print(d)


# Nested dictionary :
'''
Dictionary inside another dictionary is known as a nested dictionary.
'''
students = {
    "student_1":{
        'name':'abhi',
        'age':23
    },
    "student_2":{
        'name':'kirti',
        'age':19
    }
}
print(students)
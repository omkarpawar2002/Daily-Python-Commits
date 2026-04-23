# Comprehension :
'''
    1.Comprehension is a concise and elegant way to create collections (list, set, dictionary) in a single line using iteration and optional conditions.
    2.Comprehension actually allow us to write a short , readable or compact code.

    3.There are different types of comprehension :
        a.List Comprehension
        b.Set Comprehension
        c.Dictionary Comprehension

'''

# 1.List Comprehension
'''
    We use list comprehension when the logic is simple and readable.
    For complex logic, normal for-loops are preferred.

    Syntax : [expression for variable in iterable]
'''

# Create a list of even number from 1 to 20
li = [i for i in range(2,21,2)]
print(li)


# 2.Set Comprehension
'''
    1.Set comprehension is a concise way to create a set in python.
    2.Set comprehension automatically removes duplicate values because sets only store unique elements.

    syntax : {expression for variable in iterable}
'''

# create a set containing squares of element from 1 to 5
s = {i**2 for i in range(1,6)}
print(s)


# 3.Dictionary Comprehension
'''
    1.Dictionary comprehension is a concise way to create a dictionary in python.
    2.Dictionary comprehension we used when we want to map the values like student marks etc.,

    Syntax : {key_expression: value_expression for variable in iterable}
'''

# create a dictionary from 1 to 5 where keys are the values from 1 to 5 and value will be square of keys
d = {i:i**2 for i in range(1,6)}
print(d)


# 4.Conditional Comprehension
'''
    Conditional comprehension which means we are going to add if-else conditional statements inside ( list,set,dictionary ) comprehension.

    Syntax : 
        1.If Statement syntax :     [expression for variable in iterable if condition]

        2.If-else statement syntax :      [result_1 if condition else result_2 for variable in iterable]           
'''

# create a list of even numbers from 1 to 20
li = [i for i in range(1,21) if(i % 2 == 0)]
print(li)


# create a list and print "Even" if number is Even and "Odd" if number is odd from 1 to 10
li = ["Even" if(i % 2 == 0) else "Odd" for i in range(1,11)]
print(li)


# 5.Nested comprehension
'''
    Nested comprehension is used when we need multiple loops.
    It works like nested for-loops (for loop inside another for loop).

    syntax : [expression for outer_item in iterable for inner_item in outer_item]
'''
# Example : To create a flaten list.
li = [[11,22,33],["welcome","to","party"],[45.34,34.56,34.67]]
li = [variable for item in li for variable in item]
print(li)
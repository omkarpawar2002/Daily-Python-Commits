# Function :
'''
1.Function is a reusable block of code which gets executed whenever it is called.
2.Function is defined by using the def reserved keyword.

There are 2 types of functions :

    1.Built in functions :
            Built in functions are those function which are provided by standard python library.
            Ex., print() , len() , min() etc..,

    2.User-defined functions :
            There are 2 types of user-defined functions :

                1.non-parameterized function :  
                        Function without parameter i.e.,paranthesis after the function name is empty is known as a non-parameterized function.

                2.parameterized function :
                        Function with parameter i.e.,paranthesis after the function name is empty is known as a parameterized function.
'''

# Define a function : 
def greet():
    print("Welcome to function topic")


# Calling a function :
def greet():
    print("Welcome to function topic")

greet()  # Function call


# Defined a function with parameter
def greet(name):
    """
        1.Here name is a paramter and alice from line number 42 is a argument.
    """
    print(f"Welcome {name} for lecture")

greet("alice")


# Parameter and Argument :
'''
parameter :
    1.parameter acts as a placeholder which is used to store or hold a value in function.
    2.We also call paramter as a formal arguments or formal values.
    3.The scope of parameter only inside function body.
    4.We can not access the parameter outside the function body.
    5.Keep in mind that number of parameter is declared while defining a function should be same as number of arguments while calling.

argument :
    1.argument are the actual values that we pass from function calling to function defination to perform the task.
    2.We also call argument as a actual arguments or actual values.
'''


# return statement :
'''
1.Function used return statement whenever it needs to return a value.
2.Function always return a value to caller method.
3.return statement should be written at the last of function otherwise the code written after the return statement will called as a unreachable code.
4.If no return statement provided then by default function always return a None.
'''
def addition(num1 ,num2):
    res = num1 + num2
    return res

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
result = addition(n1,n2)
print(f"Addition of {n1} and {n2} is : {result}")


# We can also return multiple values from function
def addition(num1 ,num2):
    add = num1 + num2
    pro = num1 * num2
    return (add , pro)

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
add,pro = addition(n1,n2)
print(f"Addition of {n1} and {n2} is : {add}")
print(f"Product of {n1} and {n2} is : {pro}")
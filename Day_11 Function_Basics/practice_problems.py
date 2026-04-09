# Create function that prints hello.
def greet():
    print("Hello")

greet()


# Create function with parameter.
def greet(name):
    print(f"Hello {name}!")

greet("Akash")


# Create function that adds 2 numbers.
def addition(num1,num2):
    print(f"Addition of {num1} and {num2} is {num1 + num2}")

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
addition(n1,n2)


# Return value from function.
def addition(num1,num2):
    res = num1 + num2
    return res

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
result = addition(n1,n2)
print(f"Addition of {n1} and {n2} is {result}")


# Create function for subtraction.
def subtraction(num1,num2):
    print(f"Subtraction of {num1} and {num2} is {num1 - num2}")

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
subtraction(n1,n2)


# Call function multiple times.
def greet(name):
    print(f"Hello {name}!")

greet("Akash")
greet("Neil")
greet("Alice")


# Create function to find square.
def square(num):
    print(f"Square of {num} is {num**2}")

num1 = int(input("Enter number : "))
square(num1)


# Create function to find cube.
def cube(num):
    print(f"Cube of {num} is {num**3}")

num1 = int(input("Enter number : "))
cube(num1)


# Create function checking even odd.
def check_number(num):
    if(num % 2 == 0):
        print("Even")
    else:
        print("Odd")

num = int(input("Enter number : "))
check_number(num)


# Create function returning max of 2 numbers.
def find_maximum(num1,num2):
    if(num1 > num2):
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
find_maximum(num1,num2)


# Create function returning min of 2 numbers.
def find_minimum(num1,num2):
    if(num1 < num2):
        print(f"{num1} is less than {num2}")
    else:
        print(f"{num2} is less than {num1}")

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
find_minimum(num1,num2)


# Create function returning sum of 3 numbers.
def total_sum(num1,num2,num3):
    total = num1 + num2 + num3
    print(total)

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
total_sum(num1,num2,num3)


# Create function returning multiplication.
def product(num1,num2):
    res = num1 * num2
    return res

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
result = product(n1,n2)
print(f"Product of {n1} and {n2} is {result}")


# Create function returning division.
def division(num1,num2):
    res = num1 / num2
    return res

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
result = division(n1,n2)
print(f"Division of {n1} and {n2} is {result}")


# Create function returning multiple values.
def check_multiple(num1,num2):
    add = num1 + num2
    product = num1 * num2
    return (add , product)

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
addition , product = check_multiple(n1,n2)
print(f"Addition of {n1} and {n2} is {addition}")
print(f"Product of {n1} and {n2} is {product}")
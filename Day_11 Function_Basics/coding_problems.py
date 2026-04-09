# Define simple function.
def greet():
    print("Welcome")


# Call function.
def greet():
    print("Welcome")

greet()


# Call function twice.
def greet():
    print("Welcome")

greet()
greet()


# Create function greeting message.
def greet(name):
    print(f"Welcome {name} for the party.")

greet("alice")


# Function with 2 parameters.
def addition(num1,num2):
    print(f"Addition of {num1} and {num2} is {num1 + num2}")

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
addition(n1,n2)


# Function printing sum.
def addition(num1,num2):
    print(num1 + num2)

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
addition(n1,n2)


# Function printing product.
def product(num1,num2):
    print(f"Product of {num1} and {num2} is {num1 * num2}")

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
product(n1,n2)


# Function printing difference.
def difference(num1,num2):
    print(f"difference of {num1} and {num2} is {num1 - num2}")

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
difference(n1,n2)


# Function returning sum.
def addition(num1,num2):
    total = num1 + num2
    return total

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
result = addition(n1,n2)
print(f"Addition of {n1} and {n2} is {result}")


# Function returning square.
def square(num):
    square = num ** 2
    return square

num1 = int(input("Enter number : "))
result = square(num1)
print(f"Square of {num1} is {result}")


# Function returning cube.
def cube(num):
    cube = num ** 3
    return cube

num1 = int(input("Enter number : "))
result = cube(num1)
print(f"cube of {num1} is {result}")


# Function returning average.
def average(num1,num2):
    total = num1 + num2
    return total / 2

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
result = average(num1,num2)
print(f"Average of 2 numbers {result}")


# Return multiply and divide.
def check_multiple(num1,num2):
    product = num1 * num2
    division = num1 / num2
    return (product , division)

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
product , division = check_multiple(n1,n2)
print(f"Product of {n1} and {n2} is {product}")
print(f"Division of {n1} and {n2} is {division}")
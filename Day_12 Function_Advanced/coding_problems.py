# Function with 2 positional args.
def add(n1,n2):
    print(n1 + n2)

add(10,20)


# Print sum.
def add(n1,n2):
    total = n1 + n2
    print(f"Sum {total}")

add(10,20)


# Print difference.
def sub(n1,n2):
    print(n1 - n2)

sub(10,20)


# Call function multiple times.
def greet():
    print("welcome")

greet()
greet()
greet()


# Change argument order.
def greet(name,age):
    print(f"My name is {name} and age is {age}")

greet("kiran",12)
greet(12,"avnit")


# Function with keyword args.
def greet(name,age):
    print(f"My name is {name} and age is {age}")

greet(name="Shivay",age=78)


# Change order.
def greet(name,age):
    print(f"My name is {name} and age is {age}")

greet(age=78,name="Shivay")


# Mix positional and keyword.
def greet(name,age):
    print(f"My name is {name} and age is {age}")

greet("Shivay",age=23)


# Function with default value.
def greet(name,age=43):
    print(f"My name is {name} and age is {age}")

greet("Akkay")


# Call with argument.
def greet(name,age=43):
    print(f"My name is {name} and age is {age}")

greet(name="Anuj")


# Default greeting function.
def greet(name):
    print(f"Welcome {name.title()},For the party!!")

greet("kirti")


# Default calculator value.
def calc(n1, n2, op="+"):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2

print(calc(10, 5))          
print(calc(10, 5, "*"))     


# Count arguments.
def add(*args):
    print(len(args))

add(1,2,3,4,5,6,7,8,9,10)


# Count kwargs.
def user_info(**kwargs):
    print(len(kwargs))

user_info(name='ashok',age=23,city='jamnagar',dept='it')

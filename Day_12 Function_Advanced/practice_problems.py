# Function with positional arguments.
def add(a,b):
    print(a + b)

add(10,20)


# Function with keyword arguments.
def user_details(name,age):
    print(f"Name is {name} and Age is {age}")

user_details(name='Kiran',age=26)


# Function with default value.
def user_details(name,age=20):
    print(f"Name is {name} and Age is {age}")

user_details(name='Kiran',age=26)
user_details(name='aarushi')


# Call function without argument.
'''
def user_details(name,age):
    """
        This error generated : 
        user_details() missing 2 required positional arguments: 'name' and 'age'
    """
    print(f"Name is {name} and Age is {age}")

user_details() 
'''


# Call function with argument.
def user_details(name,age):
    print(f"Name is {name} and Age is {age}")

user_details(name='Kiran',age=26)


# Create function using *args.
def add(*args):
    total = 0
    print(args)
    for i in args:
        total += i
    print(f"Total is {total}")

add(1,2,3,4,5,6,7,8,9,10)


# Create function using **kwargs.
def user_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")

user_info(name='ashok',age=23,city='jamnagar',dept='it')


# Use global variable.
a = 20
def fun():
    print(a)

fun()
print(a)


# Add numbers using *args.
def add(*args):
    total = 0
    print(args)
    for i in args:
        total += i
    print(f"Total is {total}")

add(1,2,3,4,5,6,7,8,9,10)


# Multiply numbers using *args.
def product(*args):
    pro = 1
    print(args)
    for i in args:
        pro *= i
    print(f"Product is {pro}")

product(1,2,3,4,5)


# Change global variable.
a = 20
def fun():
    global a
    a = 30
    print(a)

fun()
print(a)


# Create nested function.
a = 100
def fun():
    b = 40
    def inner():
        print("Inner function")
    inner()

fun()


# Modify outer variable using nonlocal.
a = 100
def fun():
    b = 40
    def inner():
        nonlocal b
        b = 150
    inner()
    print(b)

fun()


# Unpack list into function.
def add(a,b,c):
    print(a+b+c)

nums = [10,20,30]
add(*nums)


# Unpack dictionary into function.
def user_details(name,age,city):
    print(f"Name={name}, Age={age}, City={city}")

info = {"name":"Kiran","age":26,"city":"Mumbai"}
user_details(**info) 



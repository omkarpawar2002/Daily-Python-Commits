"""
Mini Task – Calculator using Functions

Create functions:

add()
subtract()
multiply()
divide()

Call functions based on user input.

Concepts used:

function
parameters
return
conditions

Real life use:
calculator apps.
"""


def additon(num1,num2):
    add = num1 + num2
    return add

def subtraction(num1,num2):
    sub = num1 - num2
    return sub

def multiplication(num1,num2):
    mul = num1 * num2
    return mul

def divide(num1,num2):
    div = num1 / num2
    return div

while True:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print("==================================")
    choice = int(input("*** MAKE A CALCULATOR ***"\
                       "\n 1.ADDITION "\
                       "\n 2.SUBTRACTION "\
                       "\n 3.MULTIPLICATION "\
                       "\n 4.DIVISION "\
                       "\n 5.EXIT "\
                       "\n Enter your choice : "))
    if(choice == 1):
        addition_result = additon(num1,num2)
        print("==========================================")
        print(f"Addition of {num1} and {num2} is {addition_result}")
        print("==========================================")
    elif(choice == 2):
        subtraction_result = subtraction(num1,num2)
        print("==========================================")
        print(f"Subtraction of {num1} and {num2} is {subtraction_result}")
        print("==========================================")
    elif(choice == 3):
        multiplication_result = multiplication(num1,num2)
        print("==========================================")
        print(f"Multiplication of {num1} and {num2} is {multiplication_result}")
        print("==========================================")
    elif(choice == 4):
        division_result = divide(num1,num2)
        print("==========================================")
        print(f"Division of {num1} and {num2} is {division_result}")
        print("==========================================")
    elif(choice == 5):
        break
    else:
        print("=====================")
        print("Incorrect Choice!")
        print("=====================")
        
"""MINI PROJECT 2 – NUMBER GUESSING GAME

Program checks guessed number.

Concepts used:

input
if else
logical comparison"""

number = int(input("Enter any number : "))
if(number == 21):
    print("You guess correct number")
elif(number > 21):
    print("Too high")
elif(number < 21):
    print("Too Low")
else:
    print("Incorrect number")
    
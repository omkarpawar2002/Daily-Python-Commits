# Print numbers 1 to 10.
'''
for i in range(1,11):
    print(i)
'''

# Print numbers 1 to 50.
'''
for i in range(1,51):
    print(i)
'''

# Print even numbers 1 to 20.
'''
for i in range(1,21):
    if(i % 2 == 0):
        print(i)
'''

# Print odd numbers 1 to 20.
'''
for i in range(1,21):
    if(i % 2 != 0):
        print(i)
'''

# Print squares 1 to 10.
'''
for i in range(1,11):
    print(i**2)
'''

# Print list elements.
'''
li = [10,20,30,40]
for i in li:
    print(i)
'''

# Print sum of list.
'''
li = [10,20,30,40]
print(sum(li))
'''

# Print max number.
'''
li = [10,20,30,40]
print(max(li))
'''

# Print min number.
'''
li = [10,20,30,40]
print(min(li))
'''

# Count elements.
'''
li = [10,20,30,40]
print(len(li))
'''

# Print characters.
'''
name = "Nurr"
for ch in name:
    print(ch)
'''

# Count letters.
'''
name = "Nurr"
print(len(name))
'''

# Print vowels.
'''
name = "Nurr"
vowels = ['a','e','i','o','u','A','E','I','O','U']
for ch in name:
    if(ch in vowels):
        print(ch)
'''

# Print consonants.
'''
name = "Nurr"
vowels = ['a','e','i','o','u','A','E','I','O','U']
for ch in name:
    if(ch not in vowels):
        print(ch)
'''

# Reverse string.
'''
st = "welcome"
for i in st[::-1]:
    print(i)
'''

# Print numbers 1 to 100.
'''
for i in range(1,101):
    print(i)
'''

# Print multiples of 5.
'''
li = [1,2,3,4]
for i in li:
    print(i*5)
'''

# Print numbers step 2.
'''
for i in range(1,21,2):
    print(i)
'''

# Print countdown.
'''
for i in range(10,0,-1):
    print(i,end=' ')
'''

# Print range sum.
'''
print(sum(range(1,11)))
'''

# Print numbers until 0 entered.
'''
while True:
    num = int(input("Enter number : "))
    if(num == 0):
        break
    print(num)
'''
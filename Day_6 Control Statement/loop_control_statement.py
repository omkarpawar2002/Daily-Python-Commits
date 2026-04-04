# Loop control statements :
'''
There are 3 loop control statements :
    1.break
    2.continue
    3.pass
'''

# break
'''
When we immediately want to exits from the loop then we used break statements.
'''

for i in range(1,11):
    if(i == 5):
        break
    print(i)


# continue
'''
Continue statement are used when we want to skipped the current iteration of loop and jump on next iteration
'''

li = [10,20,30,40,50,60]
for i in li:
    if(i == 30):
        continue
    print(i)


# pass
'''
pass keyword is used as a placeholder when our code is syntactically correct but for now we don't want to implement any feature.
'''

for i in range(10):
    pass



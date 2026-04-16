# Scope 
'''
Scope are area or region where we access the variable.

There are different types of scopes or keywords
    1.Global scope
    2.Local scope
    3.Global keyword
    4.Nonlocal keyword
'''


# 1.Global Scope
'''
1.Those variable we declare inside a global scope so we can access them anywhere throught the program.
2.We can also access them inside function.

Example :

            a = 20
            def fun():
                print(a)

            fun()
            print(a)
'''


# 2.Local Scope
'''
1.Those variable we declare inside a function having a local scope.
2.We can not access them outside the function.
3.The scope of variable is only inside a function body.

Example :

            def fun():
                b = 40   
                print(b)

            fun()        
            print(b)     

'''


# 3.Global Keyword
'''
Global keyword is used when we want to modify the global variable value into local scope.

Example :

            a = 20
            def fun():
                global a
                a = 30
                print(a)

            fun()
            print(a)
'''


# 4.Nonlocal keyword
'''
1.Nonlocal keyword is used when we declare variable not inside a global scope or not inside a local scope.
2.Variable declare inside a nested function so we used this keyword to modify the outer variable.

Example :

            a = 100
            def fun():
                b = 40
                def inner():
                    nonlocal b
                    b = 150
                inner()
                print(b)

            fun()
'''

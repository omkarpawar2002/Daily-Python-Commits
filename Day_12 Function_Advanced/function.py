# Types of arguments :
'''
There are different types of arguments :
1.Positional or required arguments.
2.Keyword arguments.
3.Default arguments.
4.Position only arguments.
5.Keyword only arguments.
6.Variable length positional only arguments [*args].
7.Variable length keyword only arguments [**kwargs].
'''


# 1.Positional Or required arguments
'''
1.Positional or required arguments are those arguments where we need to pass the data or values in correct position order.
2.Here we need to take care about position otherwise the logical error or any other error will raise.
3.The number of parameter is declare while defining the function should be same as number of arguments while calling function.

Example : 
            def add(a,b):
                print(a + b)

            add(10,20)
'''


# 2.Keyword arguments 
'''
1.Keyword arguments are those arguments where we pass the data in key value pair forms.
2.Here we no need to take care about the position because caller identifies the argument based on the parameter name.

Example :
            def user_details(name,age):
                print(f"Name is {name} and Age is {age}")

            user_details(name='Kiran',age=26)
'''


# 3.Default argument
'''
1.Default argument are those argument where we provide the default value for parameter.
2.If we not provide the argument for that parameter then default value will be used.
3.And if we provide value the default will override and new values will be used.

Example : 

            def user_details(name,age=20):
                print(f"Name is {name} and Age is {age}")

            user_details(name='Kiran',age=26)
            user_details(name='aarushi')
'''


# 4.Positional only arguments 
'''
1.Positional only arguments are those arguments where we need to pass the data or values in correct position order.
2.Here we need to take care about position otherwise the logical error or any other error will raise and we are not using any other mix arguments.
3.Input function is an example of positional only argument.
4.So here parameter declare before  the backword slash will be able to hold positional only arguments not any other like keyword.

Example :

            def add(a,/,b):
                print(a + b)

            add(10,b = 20)
'''


# 5.Keyword only argument 
'''
1.Keyword only arguments are those arguments where we pass the data in key value pair forms strictly.
2.Here we no need to take care about the position because caller identifies the argument based on the parameter name.
3.So here the variable declared after the * will be able to hold only keyword arguments only not any mix or positional argument.

Example :

            def user_details(*,name,age):
                print(f"Name is {name} and Age is {age}")

            user_details(name='Kiran',age=26)
'''


# 6.Variable length positional only arguments :
'''
This arguments we are using when we don't know how many positional only arguments that we are passing from function call to function.

Example : 

            def add(*args):
                total = 0
                print(args)
                for i in args:
                    total += i
                print(f"Total is {total}")

            add(1,2,3,4,5,6,7,8,9,10)
'''


# Variable length keyword only argument 
'''
This arguments we are using when we don't know how many keyword only arguments that we are passing from function call to function.

Example :

            def user_info(**kwargs):
                for key,value in kwargs.items():
                    print(f"{key} = {value}")

            user_info(name='ashok',age=23,city='jamnagar',dept='it')
'''
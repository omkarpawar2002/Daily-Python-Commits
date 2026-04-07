# Tuple : 
'''
Tuple is a immutable and store multiple values inside paranthesis() seperated by commas.

1.Tuple is Immutable in nature.
2.Tuple is represented by paranthesis ().
3.Tuple can store heterogenous data.
4.Tuple can also store duplicate elements.
5.Tuple also support positive or negative indexing.
6.Tuple also support slicing.

We used tuple to store the fixed values that never change.
Example : co-ordinates , RGB color values etc..
'''


# To create a Tuple there are 2 ways :
'''
# First way :
t = ()

# Second way :
t = tuple()
'''


# To create a tuple with single element then put comma after element :
t = (10)
print(t,type(t))    # 10 <class 'int'>
t = (10,)
print(t,type(t))    # (10,) <class 'tuple'>


# Tuple can store duplicate elements.
t = (10,20,30,10,10)
print(t)


# Tuple can store heterogenous data.
t = (10,20,True,"welcome",34.54)
print(t)


# Tuple support both positive indexing and negative indexing.
t = (10,20,30,40,50)
print("Positive Indexing")
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])

print()

print("Negative Indexing")
print(t[-1])
print(t[-2])
print(t[-3])
print(t[-4])
print(t[-5])


# Tuple also support Slicing 
'''
Slicing menas to break down the sequences into subsequences 
'''
t = (10,20,30,40,50,60,70,80,90,100)
res = t[1:4]
print(res)


# Tuple is immuatable 
t = (10,20,30,40)
print(t)
t[2] = 101  # It will raise an TypeError that tuple does not support item assignment


# unpacking 
'''
The term unpacking refers to parsing the tuple items into different variables.
'''
t = (10,20,30,40)
print(t)
a , b , c , d = t
print(a,b,c,d)


# packing 
'''
The term packing referes to put multiple values into paranthesis.
'''
a = 10
b = 20 
c = 30
t = a , b, c
print(t)
# List Data Structure :

'''
List is a mutable and store multiple values inside square brackets[] seperated by commas.

1.List is mutable in nature.
2.List can be represented by square bracket [].
3.List is mutable so we can modify the content inside list.
4.List is ordered collection of data structure.
5.List can store duplicate elements also.
6.List can store heterogenous data.
7.List support positive and negative indexing.
8.List also support slicing.
'''


# To create a list there are 2 ways :- 
'''
First way :
li = []

Second way :
li = list()
'''


# List can store duplicate elements.

li = [10,20,30,10,10]
print(li)


# List can store heterogenous data.
li = [10,20,True,"welcome",34.54]
print(li)


# List support both positive indexing and negative indexing.
li = [10,20,30,40,50]
print("Positive Indexing")
print(li[0])
print(li[1])
print(li[2])
print(li[3])
print(li[4])

print()

print("Negative Indexing")
print(li[-1])
print(li[-2])
print(li[-3])
print(li[-4])
print(li[-5])


# List also support Slicing :
'''
[ Slicing menas to break down the sequences into subsequences ]
'''
li = [10,20,30,40,50,60,70,80,90,100]
res = li[1:4]
print(res)
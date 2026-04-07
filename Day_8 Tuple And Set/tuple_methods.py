# Note :
'''
As we know Tuple is Immutable means once tuple is created we can not modify the content inside tuple. So python provide only 2 methods for tuple.
'''

# 1.index() : It return the index position of specified element.
t = (10,20,30,40,50)
print("Original Tuple :- ",t)
print("Index position :- ",t.index(30))


#2.count() : It return the total count of occurances of specified element.
t = (10,20,30,40,50,30,30,30)
print("Original Tuple :- ",t)
print("Index position :- ",t.count(30))
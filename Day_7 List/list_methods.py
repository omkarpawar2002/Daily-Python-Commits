"""
As we know the list is mutable so we can modify the content inside list.
So the python provide some methods to work with list and by using that method we can modify the data inside list.
"""

# 1.append() : When we want to add single element to the end of list we used append() method.
'''
li = [10,20,30,40]
print("Original list :- ",li)
li.append(101)
print("Updated list :- ",li)
'''

#2.extend() : When we want to add multiple elements or any other iterable object to the end of list then we used extend() method.
'''
li = [10,20,30,40]
print("Original list :- ",li)
li.extend(['a','b','c'])
print("Updated list :- ",li)
'''

#3.insert() : When we want to add single element at specified index position then we used insert() method.
'''
li = [10,20,30,40]
print("Original list :- ",li)
li.insert(2,1001)
print("Updated list :- ",li)
'''

#4.remove() : When we want to remove specified element from list then we used remove() method.
'''
li = [10,20,30,40]
print("Original list :- ",li)
li.remove(20)
print("Updated list :- ",li)
'''

#5.pop() : When we want to remove and return the last element from list then we used pop() method.
'''
li = [10,20,30,40]
print("Original list :- ",li)
li.pop()
print("Updated list :- ",li)
'''

#6.pop(index) : When we want to remove and return the specify element from list then we used pop(index) method.
'''
li = [10,20,30,40]
print("Original list :- ",li)
li.pop(2)
print("Updated list :- ",li)
'''

#7.reverse() : When we want to reverse the list then we used reverse() method.
'''
li = [10,20,30,40]
print("Original list :- ",li)
li.reverse()
print("Updated list :- ",li)
'''

#8.clear() : When we want to remove all elements from list then we used clear() method.
'''
li = [10,20,30,40]
print("Original list :- ",li)
li.clear()
print("Updated list :- ",li)
'''

#9.sort() :- When we want to sort the list permenantly in assending order then we used sort() method and for dessending order we used sort(reverse=True)
'''
li = [10,45,78,34]
print("Original list :- ",li)
li.sort()
print("Updated list :- ",li)
'''

#10.sorted() : Sorted() function return the temporarly sorted list same work like sort() do but it does not modified the original list.
'''
li = [10,45,78,34]
print("Original list :- ",li)
print("Updated list :- ",sorted(li))
'''

#11.index() : It return the index position of specified element.
'''
li = [10,20,30,40,50]
print("Original list :- ",li)
print("Index position :- ",li.index(30))
'''

#12.count() : It return the total count of occurances of specified element.
'''
li = [10,20,30,40,50,30,30,30]
print("Original list :- ",li)
print("Total Count :- ",li.count(30))
'''

#13.copy() : It return the shallow copy of original list.
'''
li = [10,20,30,40,50]
print("Original list :- ",li,id(li))
new = li.copy()
print("Copy list :- ",new,id(li))
'''
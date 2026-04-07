# Methods of sets :

# 1.add() : add() method is used to add single element inside set.
s = {10,20,30,40}
print("Original set :- ",s)
s.add(101)
print("Updated set :- ",s)


# 2.update() : update() method is used to add any other iterable object suct as list , tuple , set etc.,
s = {10,20,30,40}
print("Original set :- ",s)
s.update([101,201,301])
print("Updated set :- ",s)


# 3.remove() : remove() method is used to remove the specified element in set . If the element does not found it will show an keyError
s = {10,20,30,40}
print("Original set :- ",s)
s.remove(20)
print("Updated set :- ",s)


# 4.discard() : discard() method is used to discard the specified element in set.If the element does not found then still set remains unchanged.
s = {10,20,30,40}
print("Original set :- ",s)
s.discard(2000)
print("Updated set :- ",s)


# 5.pop() : pop() method is remove and return an any arbitrary(random) element from set.
s = {10,20,30,40}
print("Original set :- ",s)
print(s.pop())
print("Updated set :- ",s)


# 6.clear() : clear() method is used to remove all the element inside set.
s = {10,20,30,40}
print("Original set :- ",s)
s.clear()
print("Updated set :- ",s)


# 7.copy() : copy() method will return the shallow copy of set.
s = {10,20,30,40}
print("Original set :- ",s,id(s))
res = s.copy()
print("Updated set :- ",res,id(res))


# 8.union() : union() method return all the distinct(unique) element from sets.
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.union(s2))
print(s1 | s2)


# 9.intersection() : intersection() method return the only common element between the sets.
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection(s2))
print(s1 & s2)


# 10.Intersection_update() : intersection_update() method compute the intersection between two sets and and update it to the calling set.
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s1.intersection_update(s2)
print(s1)


# 11.difference() : difference() method return the element that are present in set1 but not in set2.
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s1 - s2)


# 12.difference_update() : difference_update() method compute the difference between two sets and update it to the calling set.
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s2.difference_update(s1)
print(s2)


# 13.symmetric_difference() : symmetric_difference() method return the elements that are present in both set but except the intersection element.
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)


# 14.Symmetric_difference_update() : symmetric_difference_update() method compute the symmetric_difference between two set and update it to the calling set.
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s2.symmetric_difference_update(s1)
print(s2)


# 15.isdisjoitnt() : isdisjoint() method return True if both the sets don't have any common elements between them otherwise it return False.
s1 = {10,20,30,40,50}
s2 = {60,70,80}
print(s1.isdisjoint(s2))


# 16.issubset() : issubset() method return True if all the elements of set1 is present in set2 otherwise it return False.
s1 = {40,50}
s2 = {40,50,60,70,80}
print(s1.issubset(s2))


# 17.issuperset() : issuperset() method return True if all the elements of set2 is present in set1 otherwise it return False.
s1 = {10,20,30,40,50,60,70,80}
s2 = {40,50,60,70,80}
print(s1.issuperset(s2))

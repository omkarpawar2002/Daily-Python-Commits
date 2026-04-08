# Methods :
'''
So as we know dictionary is mutable so python provided some built in methods to work with dictionary so we can manipulate [ update , delete ] dictionary.
'''

# 1.get() 
'''
1.This get() method basically return the value of specified key if key is present in dictionary otherwise it return None.
2.Best recommanded way to used get() method instead of [] subscript operator to access any key's value.
'''
d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
print(d.get(2))
print(d[2])


# 2.update() : Update() method is used to add multiple key-value pairs or other iterable object like dictionary.
d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
print(d)
d.update({5:'home',6:'tour'})
print(d)


# 3.keys() : This keys() method return the view object containing list of all keys present in dictionary.
d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
print(d)
dict_keys = d.keys()
for i in dict_keys:
    print(i)


# 4.values() : This values() method return the view object containing list of all the values present in dictionary.
d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
print(d)
dict_values = d.values()
for value in dict_values:
    print(value)


# 5.items() : items() method return the view object containing list of all the key , value tuple pair from dictionary.
d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
dict_items = d.items()
print(dict_items)
for key , value in d.items():
    print(f"Key is : {key} and Value is : {d[key]}")


# 6.clear() : clear() method clear all dictionary.
d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
print(d)
d.clear()
print(d)


# 7.popitem() : popitem() method remove and return the last inserted key - value pairs.
d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
print(d)
print(d.popitem())
print(d)


# 8.pop() : pop() method remove and return the value of specified key from dictionary.
d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
print(d)
print(d.pop(2))
print(d)


# 9.copy() : copy() method return the shallow copy of dictionary
d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
print(d)
res = d.copy()
print(d,id(d))
print(res,id(res))


# 10.setdefault() : setdefault() method return the value of of specified key if the key is present in dictionary and if it not present then it will added key-value pair in dictionary.
d = {1:'Welcome',2:'to',3:'jumanji',4:'world'}
print(d)
print(d.setdefault(5,"newone"))
print(d)


# 11.fromkeys() : fromkeys() will create a dictionary from given sequence of keys and values.
keys = (1,2,3,4)
values = "welcome"
d = dict.fromkeys(keys,values)
print(d)
# Create list of numbers.
numbers = [10,20,30,40]
print(numbers)


# Create list of names.
names = ['john','alice','nike']
print(names)


# Print first element.
names = ['john','alice','nike']
print(names[0])


# Print last element.
names = ['john','alice','nike']
print(names[-1])


# Slice first 2 values.
names = ['john','alice','nike']
print(names[:2])


# Create mixed list.
li = [10,True,"welcome",34.32]
print(li)


# Change list value.
li = [10,True,"welcome",34.32]
print(li)
li[2] = 101
print(li)


# Create nested list.
li = [[11,22],[10,20]]
print(li)


# Access nested value.
li = [[11,22],[10,20]]
print(li[0][-1])


# Add element using append.
li = [10,20,30]
print(li)
li.append(101)
print(li)


# Add multiple elements.
li = [10,20,30]
print(li)
li.extend({101,201,301})
print(li)


# Insert value at index.
li = [10,20,30]
print(li)
li.insert(1,101)
print(li)


# Remove value.
li = [10,20,30]
print(li)
li.remove(20)
print(li)


# Remove last element.
li = [10,20,30]
print(li)
li.pop()
print(li)


# Sort list.
li = [34,56,32,45]
print(li)
li.sort()
print(li)


# Reverse list.
li = [10,20,30]
print(li)
li.reverse()
print(li)


# Count value.
li = [10,20,20,20,30]
print(li)
print(li.count(20))


# Find index.
li = [10,20,20,20,30]
print(li)
print(li.index(20))


# Copy list.
li = [10,20,30]
print(li,id(li))
new = li.copy()
print(new,id(new))

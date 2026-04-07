# Convert list to set.
li = [10,20,30]
print(li)
s = set(li)
print(s)


# Remove duplicates.
li = [10,20,30,40]
print(li)
s = set(li)
print(s)


# Find common values.
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection(s2))


# Combine sets.
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.union(s2))


# Find difference.
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))


# Unpack tuple values.
t = (10,20,30)
a , b, c = t
print(a,b,c)


# Count occurrences.
t = (10,20,30,40,10,10)
print(t.count(10))


# Check value exists.
s = {10,20,30,40,50}
print(20 in s)


# Clear set.
s = {10,20,30,40,50}
print(s)
s.clear()
print(s)


# Perform symmetric difference.
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
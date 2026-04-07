# Create tuple of numbers.
t = (10,20,30,40,50)
print(t)


# Access first element.
t = (10,20,30,40,50)
print(t[0])


# Access last element.
t = (10,20,30,40,50)
print(t[-1])


# Slice tuple.
t = (10,20,30,40,50)
print(t[1:3])


# Create single value tuple.
t = (20,)
print(t)


# Find index.
t = (10,20,30,40,50)
print(t.index(20))


# Iterate tuple.
t = (10,20,30,40,50)
for i in t:
    print(i)


# Create set.
s = {10,20,30,40}
print(s)


# Add value.
s = {10,20,30,40}
print(s)
s.add(101)
print(s)


# Add multiple values.
s = {10,20,30,40}
print(s)
s.update([101,201])
print(s)


# Remove value.
s = {10,20,30,40}
print(s)
s.remove(20)
print(s)


# Remove using discard.
s = {10,20,30,40}
print(s)
s.discard(200)
print(s)


# Pop value.
s = {10,20,30,40}
print(s)
s.pop()
print(s)


# Clear set.
s = {10,20,30,40}
print(s)
s.clear()
print(s)


# Convert list to set.
li = [10,20,30,40]
print(li)
s = set(li)
print(s)


# Check value exists.
s = {10,20,30,40}
print(s)
print(20 in s)
print(200 in s)


# Compare two sets.
s1 = {10,20,30}
s2 = {10,20,30}
print(s1 == s2)


# Convert tuple to set.
t = (10,20,30,40)
print(t)
s = set(t)
print(s)

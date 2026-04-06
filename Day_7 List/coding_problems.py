# Print middle element.
li = [10,20,30,40,50,60,70]
print(li[3])


# Slice first 3 values.
li = [10,20,30,40,50,60,70]
print(li[:3])


# Slice last 2 values.
li = [10,20,30,40,50,60,70]
print(li[5:])


# Slice full list.
li = [10,20,30,40,50,60,70]
print(li[:])


# Slice alternate values.
li = [10,20,30,40,50,60,70]
print(li[::2])


# Reverse slicing.
li = [10,20,30,40,50,60,70]
print(li[::-1])


# Modify copied list.
li = [[10,20,30],[11,22,33]]
print(li)
li[-1][2] = 101
print(li)
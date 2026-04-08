# Create string variable.
name = "alice"
print(name)


# Print first character.
name = "alice"
print(name[0])


# Print last character.
name = "alice"
print(name[-1])


# Slice first 4 letters.
name = "alice"
print(name[:4])


# Slice last 3 letters.
name = "alice"
print(name[-3:])


# Reverse string.
name = "alice"
print(name[::-1])


# Print alternate characters.
name = "alice"
print(name[::2])


# Extract middle characters.
name = "alice mackile"
length = len(name)
middle_index = length // 2
print(name[middle_index])


# Slice using negative index.
name = "alice"
print(name[::-1])


# Slice step 2.
name = "alice"
print(name[::2])


# Concatenate 2 strings.
s1 = "Hello"
s2 = " world"
print(s1 + s2)


# Repeat string 5 times.
s1 = "Hello"
print(s1 * 4)


# Convert lowercase.
name = "Alice"
print(name.lower())


# Convert uppercase.
name = "Alice"
print(name.upper())


# Count letters.
name = "Alice"
print(len(name))


# Find word position.
st = "This is my string"
word = "is"
print(st.index(word))


# Check startswith.
st = "This is my string"
print(st.startswith("T"))


# Check endswith.
st = "This is my string"
print(st.endswith("f"))


# Check digit.
num = "123"
print(num.isdigit())


# Check alphabet.
st = "word"
print(st.isalpha())


# Remove spaces.
st = "This is my string"
print(st)
res = st.split()
print(''.join(res))


# Check alphanumeric.
email = "email@123gmail.com"
print(email.isalnum())


# Print formatted message.
name = "kushina"
age = 23
print("My name is {} and age is {}".format(name.upper(), age))


# Combine formatting with variables.
name = "kushina"
age = 23
print(f"My name is {name.title()} and age is {age}")
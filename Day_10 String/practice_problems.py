# Reverse string using slicing.
name = "alice"
print(name)
print(name[::-1])


# Count characters.
name = "alice"
print(len(name))


# Extract domain from email.
email = "abc123@gmail.com"
print(email)
email_li = email.split("@")
domain = ''.join(email_li[-1])
print(domain)


# Check first letter.
name = "alice"
print(name[0])


# Check last letter.
name = "alice"
print(name[-1])


# Join two strings.
s1 = "Hello"
s2 = " world"
print(s1 + s2)


# Split sentence.
sentence = "This is my first sentence"
print(sentence.split())


# Replace word.
sentence = "This is my first sentence"
print(sentence)
sentence_li = sentence.replace("is","are")
print(sentence_li)


# Check numeric string.
num = "121"
print(num.isdigit())


# Format string output.
age = 23
print(f"My age is : {age}")

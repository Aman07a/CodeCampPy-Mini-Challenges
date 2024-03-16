# String data type

# Literal assignment
first = "Elon"
last = "Musk"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.
All good?
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline)
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += ""
multiline = "" + multiline
print(len(multiline))
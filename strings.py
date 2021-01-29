# Strings in python are surrounded by either single quotation marks, or double quotation marks

print('Hello Rohan')
print("Hello Rohan")

# Assign String to a Variable

a = "Rohan"
print(a)

# multiple String
# You can assign a multiline string to a variable by using three quotes

b = """Hello, My Name Is Rohan 
and I'am Awesome."""
print(b)

# Slicing Strings
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# The below example will return the index value starting from 2 to 5 but index value of 5 will be excluded
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Slice To the End
# In below example the slicing will start from index value of 2 and will go all the way to the end
b = "Hello, World!"
print(b[2:])

# Negative Indexing
# negative indexing will start from -1 and not from 0
# in this example the indexing will start from -5 to -2 which will return "orl"
b = "Hello, World!"
print(b[-5:-2])



# Strings Built-in methods

# UPPERCASE
a = "Hello, World!"
print(a.upper())

#lowercase
a = "Hello, World!"
print(a.lower())

# Replace String
a = "Hello, World!"
print(a.replace("H", "J")) # H will be replaced by J

# Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Capitalized
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

# Casefold
# The casefold() method returns a string where all the characters are lower case. This method is similar to the lower() method, 
# but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, 
# and will find more matches when comparing two strings and both are converted using the casefold() method.
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# Index
# Returns The index value of the string
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

# Count-Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)





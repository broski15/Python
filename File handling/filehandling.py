# File Handling
# file handling and allows users to handle files i.e., 
# to read and write files, along with many other file handling options, to operate on files.
# “ r “, for reading.
# “ w “, for writing.
# “ a “, for appending.
# “ r+ “, for both reading and writing

# There are three steps we need to follow to work with files:
# Open a file
# Perform Operation (Read or Write)
# Close the file

# Opening a File
f = open("example.txt")

# read mode
f = open('example.txt', 'r')

# Reading files in Python
f = open('example.txt', 'r')

content = f.read()
print(content)

f.close()

# read only the first 6 characters
f = open('example.txt', 'r')

content = f.read(6)
print(content)

f.close()

# Exception Handling with Files
try:
    f = open('example.txt', 'r')

    content = f.read(6)
    print(content)

    more_content = f.read(12)
    print(more_content)
finally:
    f.close()

# Writting the same code using the with...open syntax.

# Writing to files in Python
with open('python.txt', 'w') as f:
    f.write("Python is awesome")
    f.write("I love Python")

# Appending to Files in Python
with open('python.txt', 'a') as f:
    f.write("\nPython is my first programming language.")

# readlines() and writelines()
# The readlines() method returns a list containing each line of the file.
with open('python.txt', 'r') as f:
    lines = f.readlines()
print(lines)

# writelines() method i used to write multiple items into a file. It writes the items of a list to the file.
with open('javascript.txt', 'w') as f:
    lines = ['JS is also awesome', '\nJS is my second programming language.']
    f.writelines(lines)

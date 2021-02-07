# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is unordered, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values.

# Create a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Dictionary Length
print(len(thisdict))

# The values in dictionary items can be of any data type
typedict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Access Dictionary Items
accessdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = accessdict["model"]

# Using get() method
x = accessdict.get("model")

# Get Keys- The keys() method will return a list of all the keys in the dictionary.
x = accessdict.keys()

# Get Values- The values() method will return a list of all the values in the dictionary.
x = accessdict.values()

# Get Items- The items() method will return each item in a dictionary, as tuples in a list.
x = accessdict.items()

# Change Dictionary Items
# change the value of a specific item by referring to its key name
changedict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
changedict["year"] = 2018

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
updatedict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
updatedict.update({"year": 2020})

# Add Dictionary Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it
adddict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
adddict["color"] = "red"
print(adddict)


# Remove Dictionary Items
# The pop() method removes the item with the specified key name
removedict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
removedict.pop("model")
print(removedict)

# The del keyword removes the item with the specified key name
deldict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del deldict["model"]
print(deldict)

# The clear() method empties the dictionary
cleardict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
cleardict.clear()
print(cleardict)


# Copy Dictionaries- using copy() method
copydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = copydict.copy()
print(mydict)

# using dict() function
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuple items allow duplicate values.
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Create a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple with single item
singletuple = ("apple",)
print(type(singletuple))


#Access Tuple Items
accesstuple = ("apple", "banana", "cherry")
print(accesstuple[1])

# Indexing in tuple is same as list

# Update tuple
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Remove Items
# Tuples are unchangeable, so you cannot remove items from it, 
# but you can use the same workaround as we used for changing and adding tuple items.
removetuple = ("apple", "banana", "cherry")
y = list(removetuple)
y.remove("apple")
removetuple = tuple(y)

# Delete tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)

# Unpacking tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)



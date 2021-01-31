# sets are unordered collection of unique objects

# create a set
myset = {1,2,3,4,5}
print(myset)

# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# Add set items
# Once a set is created, you cannot change its items, but you can add new items.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add items from another set.
addset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
addset.update(tropical)
print(addset)

# Remove set items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# using discard method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# There is an important difference between them. 
# If the item we are trying to remove is not in the set, discard() returns None, whereas, the remove() method throws an error.

# Using clear method
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Delete set
delsset = {"apple", "banana", "cherry"}
del delsset
print(delsset)

# Join Two Sets
# Using union() method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Keep ONLY the duplicates
# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# Keep All, But NOT the Duplicates
# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)


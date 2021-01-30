# A list in Python is used to store the sequence of various types of data. 
# Python lists are mutable type its mean we can modify its element after it created. 
# However, Python consists of six data-types that are capable to store the sequences, but the most common and reliable type is the list.
# A list can be defined as a collection of values or items of different types. 
# The items in the list are separated with the comma (,) and enclosed with the square brackets [].

# Declaring a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Access List Items reffering to index values
mylist = ["apple", "banana", "cherry"]
print(mylist[1])

# Slicing index
listidx = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(listidx[2:5]) 

# Change Item Value using index number
positionlist = ["apple", "banana", "cherry"]
positionlist[1] = "blackcurrant"
print(positionlist)

# Change value in list items
listvalue = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
listvalue[1:3] = ["blackcurrant", "watermelon"] # "banana", "cherry" will replace with "blackcurrant", "watermelon"
print(listvalue)

# Insert new items in the list at a specific index value
newitem = ["apple", "banana", "cherry"]
newitem.insert(2, "watermelon")
print(newitem)

# Append Items at the end pf the list
appendlist = ["apple", "banana", "cherry"]
appendlist.append("orange")
print(appendlist)

# Extend List
# To append elements from another list to the current list, use the extend() method.
extendlist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
extendlist.extend(tropical)
print(extendlist)

# Remove List Items

# Remove Specified Item- remove()
removelist = ["apple", "banana", "cherry"]
removelist.remove("banana")
print(removelist)

# Remove Specified Index- pop()
poplist = ["apple", "banana", "cherry"]
poplist.pop(1)
print(poplist)

# If you do not specify the index, the pop() method removes the last item.

# Delete list- Deletes the entire list
deletelist = ["apple", "banana", "cherry"]
del deletelist

#Clear list- The clear() method empties the list. The list still remains, but it has no content.
clearlist = ["apple", "banana", "cherry"]
clearlist.clear()
print(clearlist)


# Sort Lists
sortlist = ["orange", "mango", "kiwi", "pineapple", "banana"]
sortlist.sort()
print(sortlist)

# Sort Descending
desclist = ["orange", "mango", "kiwi", "pineapple", "banana"]
desclist.sort(reverse = True)
print(desclist)

# Reverse Order
reverselist = ["banana", "Orange", "Kiwi", "cherry"]
reverselist.reverse()
print(reverselist)

# Sort method id case sensitive, all capital letters being sorted before lower case letters.
# Case Insensitive Sort
lowersortlist = ["banana", "Orange", "Kiwi", "cherry"]
lowersortlist.sort(key = str.lower)
print(lowersortlist)

# Copy a List in an empty list
copylist = ["apple", "banana", "cherry"]
mylist = copylist.copy()
print(mylist)

# Using list() method
mylist = ["apple", "banana", "cherry"]
yourlist = list(mylist)
print(yourlist)

# Join two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)



# for loop
# The for loop in Python is used to iterate over a sequence, and in each iteration, we can access individual items of that sequence.
# Python sequences
text = "Python"
languages = ['English', 'French', 'German']

# Creating a for loop
color = {"yellow","blue","red","green","yellow"}
for x in color:
    print(x)

# range()
for count in range(1, 6):
    print(count)

# break statement
for item in range(1, 6):
    if item == 3:
        break
    print(item)

print("The end")

# continue statement
for i in range(5):
    number = float(input("Enter a number: "))

    # check if number if negative
    if number < 0:
        continue

    print(number)


# while loop
# While Loops is used to execute a block of statements repeatedly until a given condition is satisfied.
# And when the condition becomes false, the line immediately after the loop in the program is executed.
count = 0
while (count < 9):
   print ("The count is:", count)
   count = count + 1

print ("Good bye!")

# break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
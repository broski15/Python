# Decision making using if..elif..else statements

# if statement
score = int(input("Enter a number: "))

if score >= 50:
   print("You have passed your exams.")
   print("Congratulations!")


# if..else statement
score = 35

if score >= 50:
   print("You have passed your exam.")
   print("Congratulations!")
else:
   print("Sorry, you have failed your exam.")


# if..elif..else statement
score = 105

if score > 100 or score < 0:
   print("Score is invalid.")
elif score >= 50:
   print("You have passed your exam.")
   print("Congratulations!")
else:
   print("Sorry, you have failed your exam.")


# nested if
number = float(input("Enter a number: "))

if number >= 0:
    # At this point, number is either 0 or a positive number
    if number > 0:
        print("The number is positive")
    else:
        print("The number is 0")
else:
    print("The number is negative")
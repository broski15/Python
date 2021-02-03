# functions
# A function is a group of related statements that performs a specific task.

# Creating a function
def my_function():
  print("Hello My Name Is Rohan!")

# Calling a function
my_function()

# Parameter and Arguments
def greet(name):
    print("Hello", name)
    print("How do you do?")

# calling function by passing arguments
greet("Amit")

# Return value from a function
def add_numbers(n1, n2):
    result = n1 + n2
    return result

result = add_numbers(5.4, 6.7)
print("The sum is", result)

# Example 
# find the average marks and return it
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    number_of_subjects = len(marks)
    
    average_marks = sum_of_marks/number_of_subjects
    
    return average_marks

# compute grade and return it
def compute_grade(average_marks):
    if average_marks >= 80.0:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    
    return grade

marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
grade =compute_grade(average_marks)

print("Your average marks is", average_marks)
print("Your grade is", grade)


# Positional Arguments
# Positional arguments are the arguments that need to be passed to the function call in a proper order.
def add(n1, n2):
    result = n1 + n2
    return result

result = add(100, 200)
print(result)

# Default Arguments
def add_default(n1 = 100, n2 = 1000):
    result = n1 + n2
    return result

result = add_default(5.4)
print(result)

# Keyword Arguments
def greet_you(name, message):
    print("Hello", name)
    print(message)

greet_you("Jack", "What's going on?")

greet_you(message = "Howdy?", name = "Jill")

# Lambda function or anonymous function.
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

double = lambda x: x * 2

print(double(5))
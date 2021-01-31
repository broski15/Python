# Operators

# # Arithmetic operators

x = 5
# addition
result = x + 10 
print(result)   # 15

# subtraction
result = x - 10 
print(result)   # -5

# multiplication
result = x * 10 
print(result)    # 50

# division
result = x / 10 
print(result)   # 0.5

# exponent
result = x ** 2   
print(result)     # 25

quotient = x // 2  # floor division
remainder = x % 2  # modulus

print("Quotient is", quotient) # 2
print("Remainder is", remainder) # 1

# Using parentheses
number = (34 * 5) - (5 / 3) # 168.33333
print(number)

# Concatenate Strings
str1 = "Hello"
str2 = "Rohan"
print(str1 + str2)

# Boolean Data Type- either true or false
result1 = True
result2 = False

print(result1) # True
print(result2) # False


# Comparison Operators

number = 15
print(number > 10) # True

number = 10
print(number > 10) # False

number = 10
# equal to
print(number == 10) # True

number = 10.0
# comparing float and integer
print(number == 10) # True

number = '10'
# comparing string and integer
print(number == 10) # False

number = '10'
# not equal to
print(number != 10) # True

number = 10
# less than or equal to
print(number <= 10) # True

number = 10
# greater than or equal to
print(number >= 10) # True

#Logical Operators
# and         True if both operands are True
# or          True if either of the operands is True
# not         True if the operand is False

# and Operator
age = 22
gpa = 3.8
result = age >= 18 and gpa > 3.6
print(result) # True

# OR operator
age = 22
gpa = 3.8
print(age >= 18 or gpa > 3.9)

# NOT operator
result = True
print(result) # True
result = True
print(not result) # False
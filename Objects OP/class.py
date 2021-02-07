# object-oriented programming
# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. 
# Almost everything in Python is an object. 

# Class
# Object
# Method
# Inheritance
# Polymorphism
# Data Abstraction
# Encapsulation

#Class- The class can be defined as a collection of objects.
# The __init__ method-  It is run as soon as an object of a class is instantiated. 
#                       The method is useful to do any initialization you want to do with your object.
# when working with objects,variables are called attributes and functions are called methods

# Creating an Object and Class
class employee():
    def __init__(self,name,age,id,salary):   #creating a function(method)
        self.name = name                    # self is an instance of a class
        self.age = age
        self.salary = salary
        self.id = id
 
emp1 = employee("Rohan",22,1000,1234)      #creating objects
emp2 = employee("Amit",23,2000,2234)
print(emp1.__dict__)                            #Prints dictionary


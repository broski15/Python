# Encapsulation
# In a raw form, encapsulation basically means binding up of data in a single class. 
# Python does not have any private keyword, unlike Java. 
# A class shouldn’t be directly accessed but be prefixed in an underscore.

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
 
    def display(self):
        print(self.name)
        print(self.age)
 
person = Person('Rohan', 30)
#accessing using class method
person.display()
#accessing directly from outside
print(person.name)
print(person.age)
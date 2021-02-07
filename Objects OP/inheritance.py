# Object-Oriented Programming methodologies
# Inheritance
# When a class derives from another class.
# The child class will inherit all the public and protected properties and methods from the parent class. 
# In addition, it can have its own properties and methods.

class employee1():                          # This is a parent class
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee(employee1):             #This is a child class
    def __init__(self, name, age, salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

emp1 = employee1('Rohan',22,1000) 
print(emp1.age)


# Multilevel Inheritance
#Multi-level inheritance enables a derived class to inherit properties from an immediate parent class 
# which in turn inherits properties from his parent class.
class employee2():                       # Super class
    def __init__(self,name,age,salary):  
        self.name = name
        self.age = age
        self.salary = salary

class childemployee1(employee2):         # First child class
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee2(childemployee1):   #Second child class
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

emp1 = employee2('Anirruddha',22,1000)
emp2 = childemployee1('Siddhesh',23,2000)
 
print(emp1.age)
print(emp2.age)

# Hierarchical Inheritance:
# Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class.
class employee3():
    def __init__(self, name, age, salary):     #Hierarchical Inheritance
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee3(employee3):
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
 
class childemployee4(employee3):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

emp1 = employee3('Rohan',22,1000)
emp2 = employee3('Amit',23,2000)
 
print(emp1.age)
print(emp2.age)

# Multiple Inheritance:
# Multiple level inheritance enables one derived class to inherit properties from more than one base class.
class employee4():                          #Parent class
    def __init__(self, name, age, salary):  
        self.name = name
        self.age = age
        self.salary = salary
 
class employee5():                          #Parent class
    def __init__(self,name,age,salary,id):
     self.name = name
     self.age = age
     self.salary = salary
     self.id = id
 
class childemployee5(employee4,employee5):
    def __init__(self, name, age, salary,id):
     self.name = name
     self.age = age
     self.salary = salary
     self.id = id
emp1 = employee4('John',22,1000)
emp2 = employee5('Cena',23,2000,1234)
 
print(emp1.age)
print(emp2.id)
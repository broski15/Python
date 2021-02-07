# Polymorphism
# Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class. 
# In inheritance, the child class inherits the methods from the parent class. 
# Also, it is possible to modify a method in a child class that it has inherited from the parent class.
# it is a property of an object which allows it to take multiple forms.

# Compile-time Polymorphism:
# A compile-time polymorphism also called as static polymorphism which gets resolved during the compilation time of the program. 
# One common example is “method overloading”.

class employee1():
    def name(self):
        print("Rohan is his name")  

    def salary(self):
        print("30000 is his salary")
 
    def age(self):
        print("27 is his age")
 
class employee2():
    def name(self):
        print("Amit is his name")
 
    def salary(self):
        print("40000 is his salary")
 
    def age(self):
        print("40 is his age")
 
def func(obj):          # Method Overloading
    obj.name()
    obj.salary()
    obj.age()
 
obj_emp1 = employee1()
obj_emp2 = employee2()
 
func(obj_emp1)
func(obj_emp2)

# Run-time Polymorphism:
# A run-time Polymorphism is also, called as dynamic polymorphism where it gets resolved into the run time. 
# One common example of Run-time polymorphism is “method overriding”.

class employee():
   def __init__(self,name,age,id,salary):  
       self.name = name
       self.age = age
       self.salary = salary
       self.id = id
def earn(self):
        pass
 
class childemployee1(employee):
 
   def earn(self):          #Run-time polymorphism
      print("no money")
 
class childemployee2(employee):
 
   def earn(self):
       print("has money")
 
c = childemployee1
c.earn(employee)
d = childemployee2
d.earn(employee)
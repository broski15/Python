# Abstraction
# Abstraction focuses on hiding the internal implementations of a process or method from the user. 
# In this way, the user knows what he is doing but not how the work is being done.

from abc import ABC,abstractmethod
class employee(ABC):
    def emp_id(self,id,name,age,salary):    # Abstraction
        pass
 
class childemployee1(employee):
    def emp_id(self,id):
        print("emp_id is 12345")
 
emp1 = childemployee1()
emp1.emp_id(id)
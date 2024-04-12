class Employee:
   'Base class'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
# can also be written as Employee.empCount = Employee.empCount + 1

   def displayEmployee(self):	# function is defined here
      print("Name:",self.name,",Salary:",self.salary)

"emp1 is the first object of Employee class"
emp1 = Employee("Akhil",2000)
"emp2 is the second object of Employee class"
emp2 = Employee("Suresh",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)




# Create a class “Programmer” for storing information of few programmers working at Microsoft

# class Programmer:
#     emp1 = "Ankit"
#     emp2 = "Krutika"
#     emp3 = "Harry"

# print(Programmer.emp1)

# class Programmer:
#     company = "Microsoft"
    
#     def __init__(self,name,salary,pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin
        
# emp = Programmer("Ankit",699999,123456)
# print(emp.company, emp.name, emp.salary, emp.pin)
# emp2 = Programmer("Harry",000,123456)
# print(emp2.company, emp2.name, emp2.salary, emp2.pin)


# 2. Write a class “Calculator” capable of finding square, cube and square root of a number

# class Calculator:
#     def __init__(self, n):
#         self.n = n
        
#     def square(self):
#         print(f"Square of {self.n} is {self.n*self.n}")
#     def cube(self):
#         print(f"Cube of {self.n} is {self.n*self.n*self.n}")
#     def squareRoot(self):
#         print(f"Squareroot of {self.n} is {self.n**1/2}")
        
# num = Calculator(2)
# num.square()
# num.cube()
# num.squareRoot()


# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute because instance attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present
print(Demo.a) # Prints the class attribute




practice set remaining
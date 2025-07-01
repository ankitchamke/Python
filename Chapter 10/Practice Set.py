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


# # 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
# class Demo:
#     a = 4

# o = Demo()
# print(o.a) # Prints the class attribute because instance attribute is not present
# o.a = 0 # Instance attribute is set
# print(o.a) # Prints the instance attribute because instance attribute is present
# print(Demo.a) # Prints the class attribute


# 4. Add a static method in problem 2, to greet the user with hello.
# class Calculator:
#     def __init__(self, n):
#         self.n = n
        
#     def square(self):
#         print(f"Square of {self.n} is {self.n*self.n}")
#     def cube(self):
#         print(f"Cube of {self.n} is {self.n*self.n*self.n}")
#     def squareRoot(self):
#         print(f"Squareroot of {self.n} is {self.n**1/2}")
#     @staticmethod
#     def hello():
#         print("Yo Wassuppp")
        
# num = Calculator(2)
# num.square()
# num.cube()
# num.squareRoot()
# num.hello()


# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

# from random import randint

# class Train:
    
#     def __init__(self, trainNo):
#         self.trainNo = trainNo

#     def bookTicket(self, fro, to):
#         print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

#     def getStatus(self):
#         print(f"Train no: {self.trainNo} is running on time")

#     def getFare(self, fro, to):
#         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")
        
# t = Train(12399)
# t.getStatus()
# t.getFare("Rampur", "Delhi")


# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.
# - Yes, you can change the self parameter to any valid variable name in a Python class 
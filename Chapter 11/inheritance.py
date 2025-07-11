# # CHAPTER 11 - INHERITANCE & MORE ON OOPS

# class Employee:
#     company = "Facebook"
#     name = "Chamke"
#     def show(self):
#         print(f"Employee name is {self.name} company is {self.company}")
        
# # class Programmer:
# #     company = "meta"
# #     def proshow(self):
# #         print(f"I work in {self.company}")

# class Programmer(Employee):
#     company = "meta"
#     def proshow(self):
#         print(f"I work in {self.company} I am {self.name}")
        
# a = Employee()
# b = Programmer()

# a.show()
# b.proshow()


# MULTIPLE INHERITANCE ----------------------------------------------------------------------------

# class Employee:
#     company = "ITC"
#     name = "Default name"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the company is {self.company}")

# class Coder:
#     language = "Python"
#     def printLanguages(self):
#         print(f"Out of all the languages here is your language: {self.language}")
     


# class Programmer(Employee, Coder):
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.company} and he is good with {self.language} language")


# a = Employee()
# b = Programmer()

# b.show()
# b.printLanguages()
# b.showLanguage()


# MULTILEVEL INHERITANCE --------------------------------------------------------------------------

# class Employee:
#     a = 1 

# class Programmer(Employee):
#     b = 2 

# class Manager(Programmer):
#     c = 3

# o = Employee()
# print(o.a) # Prints the a attribute
# # print(o.b) # Shows an error as there is no b attribute in Employee class

# o = Programmer()
# print(o.a, o.b)


# o = Manager()
# print(o.a, o.b, o.c)


# SUPER () ----------------------------------------------------------------------------------------

# class Employee:
#     def __init__(self):
#         print("Constructor of Employee")
#     a = 1 

# class Programmer(Employee):
#     def __init__(self):
#         print("Constructor of Programmer")
#     b = 2 

# class Manager(Programmer):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of Manager")
#     c = 3

# # o = Employee()
# # print(o.a) # Prints the a attribute 

# # o = Programmer()
# # print(o.a, o.b)


# o = Manager()
# print(o.a, o.b, o.c)


# CLASS DECORATOR ---------------------------------------------------------------------------------

# class Employee:
#     a = 1
    
#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is {cls.a}")

# e = Employee()
# e.a = 45

# e.show()


# OPERATOR OVERLOADING ----------------------------------------------------------------------------

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)
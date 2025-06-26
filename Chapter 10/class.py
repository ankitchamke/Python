# class Employee: #class
#     name = "Ankit" #.name is object
#     salary = 6999999
    
# print(Employee.name , Employee.salary )

# Ankit = Employee()
# Ankit.name = "Ankit" #This is instance
# Ankit.language = "Python"
# print(Ankit.language)

class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
harry.greet()
harry.getInfo() 
# Employee.getInfo(harry)
 
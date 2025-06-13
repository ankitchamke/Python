# 1. Write a program using functions to find greatest of three numbers
# a = int(input("Enter a Numer: "))
# b = int(input("Enter a Numer: "))
# c = int(input("Enter a Numer: "))

# def function_name():
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c

# print (function_name())

# -----------------------------------------------------------------------------------------------

# 2. Write a python program using function to convert Celsius to Fahrenheit 
# temp = int(input("Enter temprature in Celsius: "))

# def coonversion():
#     Fahrenheit = (temp * 1.8) + 32 
#     return Fahrenheit
    
# print(coonversion())

# -----------------------------------------------------------------------------------------------

# 3. How do you prevent a python print() function to print a new line at the end.
# print("a")
# print("b")
# print("c", end="")
# print("d", end="")

# -----------------------------------------------------------------------------------------------

# 4. Write a recursive function to calculate the sum of first n natural numbers.
# sum(1) = 1
# sum(2) = 1 + 2
# sum(3) = 1 + 2 + 3
# sum(4) = 1 + 2 + 3 + 4
# sum(5) = 1 + 2 + 3 + 4 + 5

# sum(n) = 1 + 2 + 3 + 4.... n
# sum(n) = sum(n-1) + n

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n
    
# print(sum(5))
# I'm not sure what this means I don't get recursion

# -----------------------------------------------------------------------------------------------

# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n) 
#     pattern(n-1)
    
# print(pattern(5))

# -----------------------------------------------------------------------------------------------

# 6. Write a python function which converts inches to cms.
n = int(input("Enter inches: "))
def inch_to_cm():
     x = n * 2.54
     return x
 
print(inch_to_cm())

# -----------------------------------------------------------------------------------------------

# 7. Write a python function to remove a given word from a list ad strip it at the same time

l = ["Chamke", "Aashi", "Tappu"]

def remove(l):
    l
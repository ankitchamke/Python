# # 1. Write a program to print multiplication table of a given number using for loop.
# n = int(input("Enter a number: "))

# for i in range(1,11):
#     print(n,"x",i,"=",n*i)

# -----------------------------------------------------------------------------------------------------------

# # 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for i in l:
#     if (i.startswith("S")):
#         print("Hello ",i)

# -----------------------------------------------------------------------------------------------------------

# # 3. Attempt problem 1 using while loop.
# n = int(input("Enter a number: "))
# i = 1
# while(i<11):
#     print(n,"x",i,"=",n*i)
#     i+= 1
    
# -----------------------------------------------------------------------------------------------------------
    
# # 4. Write a program to find whether a given number is prime or not.

# n = int(input("Enter a number: "))
# for i in range(2,n):
#     if(n%i==0):
#         print("Not Prime")
#         break
# else:
#     print("Prime")

# -----------------------------------------------------------------------------------------------------------

# 5. Write a program to find the sum of first n natural numbers using while loop

# n = int(input("Enter a number: "))
# i = 0
# sum = 0
# while(i<n+1):
#     sum = sum + i
#     i = i + 1
# print(sum)

# -----------------------------------------------------------------------------------------------------------

# # 6. Write a program to calculate the factorial of a given number using for loop.
# n = int(input("Enter a number: "))
# mul = 1
# for i in range(1,n+1):
#     # print(i)
#     mul = mul * i
# print(mul)

# -----------------------------------------------------------------------------------------------------------

# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     # print(i)
#     spaces = n - i
#     # print(spaces)
#     spaces = " " * spaces
#     # print(spaces)
#     stars = 2 * i - 1
#     # print(stars)  
#     stars = "*" * stars 
#     # print(stars)  
#     print(spaces, stars)
#     # print(' ' * spaces + '*' * stars)

# -----------------------------------------------------------------------------------------------------------

# # 8. Write a program to print the following star pattern:
# # *
# # **
# # *** for n = 3

# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(i * "*")

# -----------------------------------------------------------------------------------------------------------

# 9. Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * *

# I’m finding these fuking star pattern programs really frustrating, so I’m going to skip these one for now 
# and come back to these later

# -----------------------------------------------------------------------------------------------------------

# 10. Write a program to print multiplication table of n using for loops in reversed order.
# n = int(input("Enter a number: "))
# for i in range(10,0,-1):
#     print(n, " x ", i, " = ", n*i)
    
# -----------------------------------------------------------------------------------------------------------
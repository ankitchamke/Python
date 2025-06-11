# # Function Define
# def avg():
#     a = int(input("Enter a Number: "))
#     b = int(input("Enter a Number: "))
#     c = int(input("Enter a Number: "))
    
#     avg = (a+b+c)/3
#     print("Average:", avg)
#     return avg
    
# # avg() #Function Call
# a = avg() #return whole function's value which is set avg
# print("Return Value", a)

# -------------------------------------------------------------------------------------------

# # Quick Quiz: Write a program to greet a user with “Good day” using functions.
# def arrival():
#     print("Good Day")
    
# arrival()

# -------------------------------------------------------------------------------------------

# FUNCTIONS WITH ARGUMENTS
# def arrival(name):
#     print("Good Day " + name)
    
# arrival(input("Enter Name: "))

# -------------------------------------------------------------------------------------------

# def arrival(name, ending):
#     print("Good Day " + name)
#     return "value of assign () to variable"
    
# # arrival("Chamke", "ThankYou")
# a = arrival("Chamke", "ThankYou")
# print(a)

# -------------------------------------------------------------------------------------------

# # DEFAULT PARAMETER
# def goodDay (name, ending="Thank you"):

#     print(f"Good Day, {name}, {ending}")
# goodDay("Chamke")

# ------------------------------------------------------------------------------------------

# RECURSION
# factorial(1) = 1
# factorial(2) = 2 X 1
# factorial(3) = 3 X 2 X 1
# factorial(4) = 4 X 3 X 2 X 1
# factorial(5) = 5 X 4 X 3 X 2 X 1
# factorial(n) = n X n-1 X.....

# factorial(n) = n* factorial(n-1)

def fact(n):
    if (n==1 or n==0):
        return 1
    return n * fact(n-1)

n = int(input("Enter a Number "))
print(f"Factorial of {n} is {fact(n)}")

# ------------------------------------------------------------------------------------------

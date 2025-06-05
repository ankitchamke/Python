# Write a program to find whether a given username contains less than 10 characters or not.
username = input("Enter username ")
length = len(username)

if(length<10):
    print("Contains less then 10 characters")
else:
    print("Contains more then 10 characters")
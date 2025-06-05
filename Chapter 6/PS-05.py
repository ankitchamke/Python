# Write a program which finds out whether a given name is present in a list or not
l = ["Chamke","Krutika","Harry"]
name = input("Enter name: ")
if(name in l):
    print(name,"is in the list")
else:
    print(name,"is not in the list")
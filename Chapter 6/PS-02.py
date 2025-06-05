marks1 = int(input("Enter Marks:"))
marks2 = int(input("Enter Marks:"))
marks3 = int(input("Enter Marks:"))

total = marks1 + marks2 + marks3
percentage = (100 * total)/300

if(percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Your are Passed")
else:
    print("You are failed")
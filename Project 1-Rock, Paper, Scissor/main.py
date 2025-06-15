# rock = -1
# paper = 0
# scissor = 1
import random


computer = random.choice([-1, 0, 1])

youstr = input("Enter rock, paper or scissor: ")
dict = {"rock":-1, "paper":0, "scissor":1}
revdict = {-1:"rock",0:"paper",1:"scissor"}
you = dict[youstr]

print(f"Your chose {revdict[you]}, Computer chose {revdict[computer]}")
# Computer with Rock
if(computer == -1 and you == 1):        #-2
    print("You lose!")
elif(computer == -1 and you == 0):      #-1
    print("You win!")
    
# Computer with Paper
elif(computer == 0 and you == -1):      #1
    print("You lose!")
elif(computer == 0 and you == 1):       #-1
    print("You win!")

# Computer with Scissor  
elif(computer == 1 and you == 0):       #1
    print("You lose!")
elif(computer == 1 and you == -1):      #2
    print("You win!")

# Draw
elif(computer == you):
    print("Draw!")

# Error
else:
    print("Something went wrong")
    
    
# shortened version through pattern
#     if((computer - you) == -1 or  (computer - you) == 2 ):
#         print("You win!")
#     else:
#         print("You loose!") 
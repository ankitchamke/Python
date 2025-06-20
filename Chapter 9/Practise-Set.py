# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

# poem = open("poem.txt")
# content = poem.read()

# if("twinkle" in content):
#     print("present")
# else:
#     print("not present")

# poem.close()

# 2. The game() function in a program lets a user play a game and returns the scoreas an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

# import random

# def game():
#     print("Playing")
#     score = random.randint(1,10)
    
#     # Fetch HiScore
#     with open("Hi-score.txt") as f:
#         HS = f.read()
#         if(HS!=""):
#            HS = int(HS)
#         else:
#             HS = 0
                
#     print(f"Your score: {score}")
#     if(score>HS or score == ""):
#         with open("Hi-score.txt", "w") as f:
#             HS = f.write(str(score))
#     return score

# game()

#  3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

number = int(input("Enter a number "))

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
    
## Fetch HiScore
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

# def gen_table(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} x {i} = {n*i} \n"
#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)
    
# for i in range(2, 21):
#     gen_table(i)
 
 
    
# 4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

# word = "Donkey"

# with open("donkey.txt") as f:
#     content = f.read()

# newContent = content.replace("Donkey", "#####")

# with open("donkey.txt", "w") as f:
#     content = f.write(newContent)



# # 5. Repeat program 4 for a list of such words to be censored.------------------------------------------------

# words = ["Donkey","Sakura","Danzo"]

# with open("donkey.txt") as f:
#     content = f.read()
    
# for word in words:
#     content = content.replace(word,"#" * len(word))

# with open("donkey.txt", "w") as f:
#     content = f.write(content)
    
 
    
# 6. Write a program to mine a log file and find out whether it contains ‘python’.-------------------------------

# with open("log.txt") as f:
#     data = f.read()
    
# if("python" in data):
#     print("present")
# else:
#     print("not present")



# 7. Write a program to find out the line number where python is present from ques 6 ----------------------------------------


# with open("log.txt") as f:
#     lines = f.readlines()

# lineno = 1
# for line in lines:
#     if("python" in line):
#         print(f"Yes python is present. Line no: {lineno}")
#         break
#     lineno += 1

# else:
#     print("No Python is not present")
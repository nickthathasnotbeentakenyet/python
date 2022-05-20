# core --------------------------------------------------------------------------------------------
#  01

# magic_number = int(input("What is the magic number? "))
# guess_number = int(input("What is your guess? "))
# if guess_number > magic_number:
#     print("Lower")
# elif guess_number < magic_number:
#     print("Higher")   
# else:
#     print("You guessed it!")

# 02 and 03

# import random
# magic_number = random.randint(1, 100)

# guess_number = int(input("What is your guess? "))
# while magic_number != guess_number:
#     if guess_number > magic_number:
#         print("Lower")
#     else:
#         print("Higher")  
#     guess_number = int(input("What is your guess? ")) 
# else:
#     print("You guessed it!")

# stretch -------------------------------------------------------------------------------------------
# 01

# import random
# magic_number = random.randint(1, 100)
# attempt = 0 # adding a variable that will hold the number of attempts user makes to guess the number

# guess_number = int(input("What is your guess? "))
# while magic_number != guess_number:
#     if guess_number > magic_number:
#         print("Lower")
#     else:
#         print("Higher")  
#     guess_number = int(input("What is your guess? ")) 
#     attempt += 1
# else:
#     print("You guessed it!")
#     print(f"It took {attempt + 1} attempts to guess it right")

# 02

# import random

# # checking if user wants to play
# play = "yes"
# while play.lower() == "yes":

#     magic_number = random.randint(1, 100)
#     attempt = 0

#     guess_number = int(input("What is your guess? "))
#     while magic_number != guess_number:
#         if guess_number > magic_number:
#             print("Lower")
#         else:
#             print("Higher")  
#         guess_number = int(input("What is your guess? ")) 
#         attempt += 1
#     else:
#         print("You guessed it!")
#         print(f"It took {attempt + 1} attempts to guess it right")

#     play = input("Would you like to play again? [yes/no]: ")
# print("Bye-bye...")

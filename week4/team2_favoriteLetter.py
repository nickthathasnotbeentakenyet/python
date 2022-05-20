# 01
# word = "Commitment"
# for i in word:
#     if i == "m":
#         print(i.upper())
#     else:
#         print(i.lower())

# 02
# word = "Commitment"
# letter = input("Enter a latter: ").lower()
# for i in word:
#     if i.lower() == letter:
#         print(i.upper(), end="")
#     else:
#         print(i.lower(), end="")

# 03
# words = ["As", "you", "choose", "to", "live", "on", "the", "Lord's", "side", "you", "are", "never", "alone"]
# letter = input("Enter a latter: ").lower()
# for i in words:
#         for j in i:
#             if j.lower() == letter:
#                 print(j.capitalize(), end="")
#             else:
#                 print(j.lower(), end="")

# lets re-write the last section to make variables meaningful

# list_of_words = ["As", "you", "choose", "to", "live", "on", "the", "Lord's", "side", "you", "are", "never", "alone"]
# character_from_user = input("Enter a latter: ").lower()
# for word in list_of_words:
#     for letter in word:
#         if letter.lower() == character_from_user:
#             print(letter.upper(), end="")
#         else:
#             print(letter.lower(), end="")
    
# --------------------------------------- STRETCH CHALLENGE -------------------------------- 

# 01
# list_of_words = ["As", "you", "choose", "to", "live", "on", "the", "Lord's", "side", "you", "are", "never", "alone"]
# character_from_user = input("Enter a latter: ").lower()
# for word in list_of_words:
#     for letter in word:
#         if letter.lower() == character_from_user:
#             print(letter.upper(), end="")
#         else:
#             print(letter.lower(), end="")     
#     print(end=" ") # notice indentation level

# 02

# quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
# number = int(input("Please enter a number: "))
# for inx in range(len(quote)):
#     letter = quote[inx]
#     if inx % number == 0:
#         print(letter.upper(), end="")
#     else:
#         print(letter, end="")

# 03
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
keep_playing = True
while keep_playing:
    number = int(input("Please enter a number: "))
    for inx in range(len(quote)):
        letter = quote[inx]        
        if inx % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter, end="")
    answer = input("\nWould you like to enter another number? [yes/no]: ")
    if answer.lower() == "no":
        keep_playing = False
print("Goodbye")

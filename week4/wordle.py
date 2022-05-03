import random
# secret = random.choice(["python", "pneumonoultramicroscopicsilicovolcanoconiosis", "google", "education", "ham", "spam", "eggs"])
# раскоментить рандом когда будет готов loop, чтобы отгадать одно слово и открыть другое в новой игре
secret = "spam"
# attempt = 0
print("Welcome to the word guessing game!")
guess = input("What is your guess? ").lower()
output = ""
for i in range(len(secret)):
    secret_letter = secret[i]
    if secret_letter in guess:
        # место буквы в секрете
        secret_place = i
        for j in range(len(guess)):
            # место буквы в попытке
            guess_place = guess.index(secret_letter)
        if secret_place == guess_place:
            secret_letter = secret_letter.upper()
        else:
            secret_letter = secret_letter.lower()
    else:
        secret_letter = "_"
    output += secret_letter
output = random.sample(output, k=len(output))
output = ''.join(output)
print(output)

# while guess != secret:
#     print("Your guess was not correct.")
#     guess = input("What is your guess? ")
#     attempt += 1 
# else:    
#     print(f"""Congratulations! You guessed it!
# It took you {attempt + 1} guesses.""")

# Your hint is: _ _ _ _ _ _ 

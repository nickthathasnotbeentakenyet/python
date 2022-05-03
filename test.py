import random
secret = random.choice(["python", "pneumonoultramicroscopicsilicovolcanoconiosis", "google", "education", "ham", "spam", "eggs"])
attempt = 0
print("="*35)
print("Welcome to the word guessing game!")
print("="*35)
guess = ""
while guess != secret:
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
    output = ' '.join(output)
    attempt += 1
    if guess != secret:
        print("Your guess was not correct.")
        print("Your hint is: " + output + "\n")
else:
    print("\nCongratulations! You guessed it!")
    print(f"It took you {attempt} guesses.")



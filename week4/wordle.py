import random
# using list of words to make the secret word different each time the game starts
secret = random.choice(["python", "pneumonoultramicroscopicsilicovolcanoconiosis", "google", "education", "ham", "spam", "eggs", "secret", "password"])
# dropping attempts count to zero
attempt = 0
# assigning guess variable to use in the while loop
guess = ""
# welcome message
print("="*35)
print("Welcome to the word guessing game!")
print("="*35)
# keep loping until user guesses secret word
while guess != secret:
    guess = input("What is your guess? ").lower()
    hint = ""
    # looping through the letters in the secret word
    for i in range(len(secret)):
        secret_letter = secret[i]
        # if a letter from secret matches a letter in guess word
        if secret_letter in guess:
            # storing index of that letter
            secret_place = i
            # looping through letters in the guess word
            for j in range(len(guess)):
                # finding and stroing index of the letter in the guess word  
                guess_place = guess.index(secret_letter)
            # if indexes match > letter is upercase
            if secret_place == guess_place:
                secret_letter = secret_letter.upper()
            # if indexes don't match, but the letter is present in both words > lowecase
            else:
                secret_letter = secret_letter.lower()
        # if the letter is not found > substituted with an underscore_
        else:
            secret_letter = "_"
        # appending upper-, low-case letters, or underscore to the ouput
        hint += secret_letter
    # shuffling to make the game harder
    hint = random.sample(hint, k=len(hint))
    # adding space between the characters in the hint for better readability
    hint = ' '.join(hint)
    # counting the number of attempts made
    attempt += 1
    # if user didn't guess the whole word > let him know that and display hint
    if guess != secret:
        print("Your guess was not correct.")
        print("Your hint is: " + hint + "\n")
# user guesses the secret word > let him know that and display the number of attempts made
else:
    print("\nCongratulations! You guessed it!")
    print(f"It took you {attempt} guesses.")

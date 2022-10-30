def main():
    print("This program is an implementaiton of the Rosenberg\n"\
    "Self-Esteem Scale. This program will show you ten\n"\
    "statements that you could possibly apply to yourself.\n"\
    "Please rate how much you agree with each of the\n"\
    "statements by responding with one of these four letters:\n\n"\
    "D means you strongly disagree with the statement.\n"\
    "d means you disagree with the statement.\n"\
    "a means you agree with the statement.\n"\
    "A means you strongly agree with the statement.\n")

    score = 0
    score += get_score("1. I feel that I am a person of worth, at least on an equal plane with others.", True)
    score += get_score("2. I feel that I have a number of good qualities.", True)
    score += get_score("3. All in all, I am inclined to feel that I am a failure.", False)
    score += get_score("4. I am able to do things as well as most other people.", True)
    score += get_score("5. I feel I do not have much to be proud of.", False)
    score += get_score("6. I take a positive attitude toward myself.", True)
    score += get_score("7. On the whole, I am satisfied with myself.", True)
    score += get_score("8. I wish I could have more respect for myself.", False)
    score += get_score("9. I certainly feel useless at times.", False)
    score += get_score("10. At times I think I am no good at all.", False)

    print(f"\nYour score is {score}.\nA score below 15 may indicate problematic low self-esteem.")


def get_score(question, Positive):
    print(question)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == 'A'  : score = 3
    elif answer == 'a': score = 2
    elif answer == 'd': score = 1
    elif answer == 'D': score = 0    
    if not Positive: score = 3 - score

    return score


if __name__ == "__main__":
    main()
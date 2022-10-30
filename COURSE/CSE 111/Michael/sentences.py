import random

def main():

    print(get_sentence(1,'past'))
    print(get_sentence(1,'present'))
    print(get_sentence(1,'future'))
    print(get_sentence(2,'past'))
    print(get_sentence(2,'present'))
    print(get_sentence(2,'future'))

def get_determiner(quantity):
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]
    return random.choice(determiners).capitalize()

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", 
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    if str(tense).lower() == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif str(tense).lower() == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]
    elif str(tense).lower() == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    return random.choice(verbs)

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    return f"{get_preposition()} {get_determiner(quantity).lower()} {get_adjective()} {get_noun(quantity)}"

def get_adjective():
    adjectives = ["little", "beautiful", "cute", "strong", "brave",
    "big", "crazy", "happy", "hot", "creepy", "elegant", "hungry", "thankful"]
    
    return random.choice(adjectives) 

def get_sentence(quantity, tense):
    return f"{get_determiner(quantity)} {get_adjective()} {get_noun(quantity)}\
 {get_verb(quantity, tense)} {get_prepositional_phrase(quantity)}"


if __name__ == "__main__":
    main()


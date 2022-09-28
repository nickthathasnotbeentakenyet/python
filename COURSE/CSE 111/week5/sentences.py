import random

def main():
    # print several sentences by calling appropriate functions
    decorator("start")
    print(get_determiner(1), get_adjective(), get_noun(1), get_verb(1, "past"), get_prepositional_phrase(1))
    print(get_determiner(1), get_adjective(), get_noun(1), get_verb(1, "present"), get_prepositional_phrase(1))
    print(get_determiner(1), get_adjective(), get_noun(1), get_verb(1, "future"), get_prepositional_phrase(1))
    print(get_determiner(2), get_adjective(), get_noun(2), get_verb(2, "past"), get_prepositional_phrase(2))
    print(get_determiner(2), get_adjective(), get_noun(2), get_verb(2, "present"), get_prepositional_phrase(2))
    print(get_determiner(2), get_adjective(), get_noun(2), get_verb(2, "future"), get_prepositional_phrase(2))
    decorator(" end ")

def decorator(message):
    '''
    The function prints a line to separate output from other things in terminal window
    
    parameter: message is inserted to notify where output starts and where it ends
    return: void
    '''
    print("\n" + "="*15, message, "="*15,"\n")

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    return random.choice(determiners).capitalize()

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", 
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    # Randomly choose and return a noun.
    return random.choice(nouns)

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

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
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Parameter: None
    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # Randomly choose and return a determiner.
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    return f"{get_preposition()} {get_determiner(quantity).lower()} {get_adjective()} {get_noun(quantity)}"

def get_adjective():
    """Return a randomly chosen adjective
    from the list of adjectives below.

    Parameter: none 
    Return: a randomly chosen adjective.
    """
    adjectives = ["little", "beautiful", "cute", "strong", "brave",
    "big", "crazy", "happy", "hot", "creepy", "elegant", "hungry", "thankful"]
    
    return random.choice(adjectives) 

if __name__ == "__main__":
    main()


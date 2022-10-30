from sentences import get_determiner, get_noun, get_verb, \
    get_preposition, get_prepositional_phrase, get_adjective
import pytest


def test_get_determiner():
    for _ in range(4):
        assert get_determiner(1).lower() in ["a", "one", "the"]

    plural_determiners = ["some", "many", "the"]
    for _ in range(len(plural_determiners)):
        assert get_determiner(2).lower() in plural_determiners


def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child", 
        "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(len(single_nouns)):
        noun = get_noun(1)
        assert noun in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(len(plural_nouns)):
        noun = get_noun(2)
        assert noun in plural_nouns


def test_get_verb():
# COMMENT: PAST
    past_tense = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(len(past_tense)):
        past = get_verb(1, "past")
        assert past in past_tense

# COMMENT: PRESENT
    single_present_tense = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(len(single_present_tense)):
        single_present_verb = get_verb(1, "present")
        assert single_present_verb in single_present_tense

    plural_present_tense = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]
    for _ in range(len(plural_present_tense)):
        plural_present_verb = get_verb(2, "present")
        assert plural_present_verb in plural_present_tense

# COMMENT: FUTURE
    future_tense = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(len(future_tense)):
        future = get_verb(1, "future")
        assert future in future_tense


def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(len(prepositions)):
        preposition = get_preposition()
        assert preposition in prepositions


def test_get_prepositional_phrase():

    phrase_single = get_prepositional_phrase(1).split()
    phrase_plural = get_prepositional_phrase(2).split()
    assert len(phrase_single) == 4
    assert len(phrase_plural) == 4

    preposition = phrase_single[0]
    determiner_single = phrase_single[1]
    determiner_plural = phrase_plural[1]
    adjective = phrase_single[2]
    noun_single = phrase_single[3]
    noun_plural = phrase_plural[3]

# COMMENT: Prepositions 
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    for _ in range(len(prepositions)):
        assert preposition in prepositions

# COMMENT: Adjectives
    adjectives = ["little", "beautiful", "cute", "strong", "brave",
    "big", "crazy", "happy", "hot", "creepy", "elegant", "hungry", "thankful"]

    for _ in range(len(adjectives)):
        assert adjective in adjectives
        
    # COMMENT: SINGLE DETERMINERS & NOUNS 

    single_determiners = ["a", "one", "the"]
    for _ in range(len(single_determiners)):
        assert determiner_single in single_determiners
    
    single_nouns = ["bird", "boy", "car", "cat", "child", 
        "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(len(single_nouns)):
        assert noun_single in single_nouns

    # COMMENT: PLURAL DETERMINERS & NOUNS 

    plural_determiners = ["some", "many", "the"]
    for _ in range(len(plural_determiners)):
        assert determiner_plural in plural_determiners
    
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(len(plural_nouns)):
        assert noun_plural in plural_nouns


def test_get_adjective():
    adjectives = ["little", "beautiful", "cute", "strong", "brave",
    "big", "crazy", "happy", "hot", "creepy", "elegant", "hungry", "thankful"]
    for _ in range(len(adjectives)):
        assert get_adjective() in adjectives


pytest.main(["-v", "--tb=line", "-rN", __file__])

from sentences import get_determiner, get_noun, get_verb
import pytest

# TODO: Добавить описание ко всем функциям, проверить все требования по написанию и оформлению
def test_get_determiner():
    single_determiners = ["a", "one", "the"]
    for _ in range(4):
        word = get_determiner(1)
        assert word.lower() in single_determiners

    plural_determiners = ["some", "many", "the"]
    for _ in range(4):
        word = get_determiner(2)
        assert word.lower() in plural_determiners

def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child", 
        "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(len(single_nouns)):
        word = get_noun(1)
        assert word in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(len(plural_nouns)):
        word = get_noun(2)
        assert word in plural_nouns

def test_get_verb():
# COMMENT: PAST
    past_tense = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(len(past_tense)):
        past1 = get_verb(1, "past")
        past2 = get_verb(2, "past")
        assert past1 in past_tense
        assert past2 in past_tense
# COMMENT: PRESENT
    single_present_tense = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(len(single_present_tense)):
        present1 = get_verb(1, "present")
        assert present1 in single_present_tense

    plural_present_tense = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]
    for _ in range(len(plural_present_tense)):
        present2 = get_verb(2, "present")
        assert present2 in plural_present_tense

# COMMENT: FUTURE
    future_tense = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(len(future_tense)):
        future1 = get_verb(1, "future")
        future2 = get_verb(2, "future")
        assert future1 in future_tense
        assert future2 in future_tense

pytest.main(["-v", "--tb=line", "-rN", __file__])

from random import randint
import enchant
from PyDictionary import PyDictionary


def choose_word():
    random_num = randint(1, 232400)
    if random_num < 50:
        return 1
    elif random_num < 150:
        return 2
    elif random_num < 1150:
        return 3
    elif random_num < 6450:
        return 4
    elif random_num < 16450:
        return 5
    elif random_num < 16450:
        return 6
    elif random_num < 33950:
        return 7
    elif random_num < 57450:
        return 8
    elif random_num < 87450:
        return 9
    elif random_num < 119450:
        return 10
    elif random_num < 150150:
        return 11
    elif random_num < 175650:
        return 12
    elif random_num < 195650:
        return 13
    elif random_num < 210650:
        return 14
    elif random_num < 220650:
        return 15
    elif random_num < 226650:
        return 16
    elif random_num < 229950:
        return 17
    elif random_num < 231450:
        return 18
    elif random_num < 231950:
        return 19
    elif random_num < 232200:
        return 20
    else:
        return 21


def check_word_validity(input_word):
    checked = d.check(input_word)
    if not checked:
        return False
    word_validity = find_word_meaning(input_word)
    if word_validity is None:
        return False
    else:
        return checked


running = True
d = enchant.Dict("en_US")
english_dictionary = PyDictionary()
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]


def find_word_meaning(input_word):
    return english_dictionary.meaning(input_word, disable_errors=True)


def check_word_type_validity(input_word, word_type):
    try:
        english_dictionary.meaning(input_word)[word_type]
        return True
    except KeyError:
        return False


def create_word_random_length():
    bad_word = True
    word = ""
    word_length = choose_word()
    while bad_word:
        for j in range(0, word_length):
            word += alphabet_list[randint(0, 25)]
        if check_word_validity(word):
            bad_word = False
        else:
            word = ""
            word_length = choose_word()
    return word


def create_word_random_length_specific_type(word_type):
    word = create_word_random_length()
    if check_word_type_validity(word, word_type):
        return word
    else:
        return create_word_random_length_specific_type(word_type)


def create_random_sentence_structure(sentence_length):
    if sentence_length == 1:
        return False
    elif sentence_length == 2:
        return ["Noun", "Verb"]
    elif sentence_length == 3:
        variation = randint(1, 3)
        if variation == 1:
            return ["Noun", "Verb", "Noun"]
        elif variation == 2:
            return ["Adjective", "Noun", "Verb"]
        else:
            return ["Noun", "Adverb", "Verb"]


while running:
    user_length = input("How long would you like your sentence? (can go up to 3 words currently), or type 'e' to exit\n"
                        )
    if user_length == "e":
        running = False
    else:
        user_length = int(user_length)
    sentence_structure = create_random_sentence_structure(user_length)
    if not sentence_structure:
        print("You cannot create a sentence of that length")
    else:
        sentence = []
        for i in range(0, user_length):
            sentence.append(create_word_random_length_specific_type(sentence_structure[i]))
        running = False
print("Your randomly generated sentence is: ")
print(*sentence)

import os
import tempfile

import hangman

def test_select_random_word_min_length():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["cat\n","elephant\n","mouse\n","dog\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "elephant"

    os.unlink(name)

def test_select_random_word_no_non_alpha_chars():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["pine's\n","Dr.\n","Ångström\n","policeman\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "policeman"

    os.unlink(name)

def test_select_random_word_no_capitals():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["Alexander\n","AMD\n","California\n","pelican\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "pelican"

    os.unlink(name)


def test_select_random_word_no_repetitions():
    secret_words = set()
    for _ in range(10):
        secret_words.add(hangman.get_random_word())
    assert len(secret_words) == 10

def test_show_no_word():
     assert hangman.maskword("python","")=="------"


def test_masked_word():
    assert hangman.maskword("elephant",["e","n"])=="e-e---n-"


def test_wrong_word():
    assert hangman.maskword("python",["e","f"])=="------"

    

    

def test_update_status_input():
    secret_word = "helicopter"
    guesses = ["c", "o", "x"]
    turns_remaining = 3
    assert hangman.update_stats("----co----", "c o x", 3)


def test_update_status_no_guesses():
    secret_word = "helicopter"
    guesses = []
    turns_remaining = 8
    assert hangman.update_stats("----------","", 8)


def test_check_already_guessed():
    secret_word = "hospital"
    guesses = ["i", "t"]
    turns_remaining = 5
    new_guess = "t"
    status, turns_remaining = hangman.check(secret_word, guesses, 
                                            turns_remaining, 
                                            new_guess)
    assert status == hangman.ALREADY_GUESSED
    assert turns_remaining == 5
    assert guesses == ["i", "t"]
    
    
def test_check_correct():
    secret_word = "hospital"
    guesses = ["i", "t"]q
    turns_remaining = 6
    new_guess = "p"
    status, turns_remaining = hangman.check(secret_word, guesses, 
                                            turns_remaining, 
                                            new_guess)
    assert status == hangman.CORRECT
    assert turns_remaining == 6
    assert guesses == ["i", "t", "p"]

    
def test_check_wrong():
    secret_word = "hospital"
    guesses = ["i", "t", "p"]
    turns_remaining = 6
    new_guess = "x"
    status, turns_remaining = hangman.check(secret_word, guesses, 
                                            turns_remaining, 
                                            new_guess)
    assert status == hangman.WRONG
    assert turns_remaining == 5
    assert guesses == ["i", "t", "p", "x"]

    
# def test_game_over_not_over():
#     secret_word = "policeman"
#     guesses = ["x", "t"]
#     turns_remaining = 5
#     finished, message = hangman.game_over(secret_word, guesses, turns_remaining)
#     assert not finished
#     assert message == None

# def test_game_over_won():
#     secret_word = "rabbit"
#     guesses = ["r", "a", "b", "i", "t"]
#     turns_remaining = 5
#     finished, message = hangman.game_over(secret_word, guesses, turns_remaining)
#     assert finished
#     assert message == "You guessed it! The word was rabbit"


# def test_game_over_lost():
#     secret_word = "rabbit"
#     guesses = ["r", "a", "b", "i", "t"]
#     turns_remaining = 0
#     finished, message = hangman.game_over(secret_word, guesses, turns_remaining)
#     assert finished
#     assert message == "You lost! The word was rabbit"

    








    

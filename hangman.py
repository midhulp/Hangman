import random

ALREADY_GUESSED = 0
CORRECT = 1
WRONG = 2

def get_random_word(wordfile = "/usr/share/dict/words"):
    candidate_words = []
    
    with open(wordfile) as f:
        for word in f:
            word = word.strip()
            if len(word) >= 6 and word.islower() and word.isalpha():
                candidate_words.append(word)
    word = random.choice(candidate_words)
    return word
a="/usr/share/dict/words"

def maskword(secret_word, guesses):
    op = []
    for i in secret_word:
        if i in guesses:
            op.append(i)
        else:
            op.append("-")
    return "".join(op)

def update_stats(secret_word, guesses, turns_remaining):
    masked_word = maskword(secret_word, guesses)
    guessed_letters = " ".join(guesses)
    return f"""Secret word:{masked_word}
Guesses : {guessed_letters}
Remaining turns : {turns_remaining}"""

def check(secret_word, guesses, turns_remaining, new_guess):
    if new_guess in guesses:
        return ALREADY_GUESSED, turns_remaining
    else:
        guesses.append(new_guess)
        if new_guess in secret_word:
            return CORRECT, turns_remaining
        else:
            return WRONG, turns_remaining-1

        
def game_over(secret_word, guesses, turns_remaining):
    if turns_remaining == 0:
        return True, f"You lost! The word was {secret_word}"
    masked = maskword(secret_word, guesses)
    if "-" in masked:
        return False, None
    else:
        return True, f"You Won! The word is {secret_word}"
    
    
def main():
    secret_word = get_random_word()
    # print (secret_word)
    guesses = []
    turns_remaining = 8
    while True:
        print (update_stats(secret_word, guesses, turns_remaining))
        guess = input("Enter a letter ")
        
        status, turns_remaining = check(secret_word, guesses, turns_remaining, guess)
        if status == ALREADY_GUESSED:
            print ("Already guessed")
        
        finished, message = game_over(secret_word, guesses, turns_remaining)
        if message:
            print (message)
        if finished:
            break


if __name__ == "__main__":
    main()
               

   





























     


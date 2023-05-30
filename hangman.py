import random


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

def masked_word(word,tried_letters):

    display_word = ""
    for letter in word:
       if letter in tried_letters:
            display_word += letter 
       else:
            display_word += "_"
    return(display_word)

        

def stats(sw,tried_letters,guess):
    sw=get_random_word(a)
    c="wrong guess"
    b="already guessed"
    g=""
    tried_letters=[]
    # new=tried_letters + [guess]
    new1=[sw]+tried_letters
    while True:
     if guess in tried_letters:
        return b
     if guess not in new1:
        return c
     for i in new1:
       if i in sw:
          return 
    
        
     
    

    


# def play_hangman():
#     word = get_random_word(a)
#     word = word.lower()
#     guessed_letters = []
#     tries = 6

#     while tries > 0:
#         guessed_word = ""
#         for letter in word:
#             if letter in guessed_letters:
#                 guessed_word += letter
#             else:
#                 guessed_word += "_"

#         print("\nGuessed Word:", guessed_word)
#         print("Tries Left:", tries)

#         if guessed_word == word:
#             print("Congratulations! You guessed the word correctly!")
#             break

#         guess = input("Guess a letter: ").lower()

#         if guess in guessed_letters:
#             print("You already guessed that letter. Try again!")
#         elif len(guess) != 1:
#             print("Please enter a single letter.")
#         elif not guess.isalpha():
#             print("Please enter only alphabetic characters.")
#         else:
#             guessed_letters.append(guess)
#             if guess in word:
#                 print("Good guess!")
#             else:
#                 print("Wrong guess!")
#                 tries -= 1

#     else:
#         print("\nSorry, you ran out of tries.")
#         print("The word was:", word)


   





























     


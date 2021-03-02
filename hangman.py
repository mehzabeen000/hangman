import string
import random
from words import choose_word
from images import IMAGES

def is_word_guessed(secret_word, letters_guessed):
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True
    return False 

def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index <len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word

def get_available_letters(letters_guessed):
    all_letters = string.ascii_lowercase
    letters_left = ""
    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter
    return letters_left 

def get_hint(secret_word, letters_guessed):
    letters_not_guessed = []
    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        index += 1
    return random.choice(letters_not_guessed) 
 
def ifValid(user_input):
    if len(user_input) == 1:
        if user_input.isalpha():
            return True

def hangman(secret_word):
    print ("Welcome to the game, Hangman!")
    user_difficulty_choice = input("Aap abhi kitni difficulty par yeh game khelna chahte ho?\na)\tEasy\nb)\tMedium\nc)\tHard\n\nApni choice a, b, ya c ki terms mei batayein\n")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    total_lives = remaining_lives = 8
    images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]
    if user_difficulty_choice not in ["a", "b", "c"]:
        print ("Aapki choice invalid hai.\nGame easy mode mei start kar rahe hai")
    else:
        if user_difficulty_choice == "b":
            total_lives = remaining_lives = 6
            images_selection_list_indices = [0, 2, 3, 5, 6, 7]
        elif user_difficulty_choice == "c":
            total_lives = remaining_lives = 4
            images_selection_list_indices = [1, 3, 5, 7]
    letters_guessed = [] 
    # remaining_lives = 8
    while (remaining_lives > 0):
      available_letters = get_available_letters(letters_guessed)
      print ("Available letters: " + available_letters)
      guess = input("Take hint if you want by entering hint\nPlease guess a letter: ")
      if guess == "hint":
        letter = get_hint(secret_word, letters_guessed)
      else:
        letter = guess.lower()
        if (not ifValid(letter)):
            print("Invalid Input")
            continue
      if letter in secret_word:
        letters_guessed.append(letter)
        print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
        print ("")
        if is_word_guessed(secret_word, letters_guessed) == True:
          print (" * * Congratulations, you won! * * ")
          print ("")
          break
        else:
          letters_guessed.append(letter)
      else:
          print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
          print (IMAGES[images_selection_list_indices[total_lives-remaining_lives]])
          print ("Remaining Lives : ", remaining_lives)
          letters_guessed.append(letter)
          remaining_lives -= 1
    else:
        print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")
        letters_guessed.append(letter)
        print ("")
secret_word = choose_word()
hangman(secret_word)  
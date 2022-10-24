import random
from ascii_art_game import logo
from ascii_art_game import game_over_ascii
from ascii_art_game import winner
from random_words import words_list
from colorama import init, Fore, Style
from termcolor import cprint

COLORS = {
    "RED": "red",
    "BLUE": "blue",
    "YELLOW": "yellow",
    "GREEN": "green",
}

cprint(' Welcome to the Hangman Game!\n', COLORS["YELLOW"])
cprint(' Rules:\n', COLORS["GREEN"])
cprint(' * We generate a random word\n * You guess a letter\n * If the letter is in the word, the man lives a little longer\n * If the ltter is not in the word he gets closer to be hanged\n * If you find all words, you win and the man gets to live\n * You have 9 failed attempts, otherwise he gets hanged.\n', COLORS["RED"])
cprint(' Enjoy!\n', COLORS["GREEN"])

cprint(logo, COLORS["YELLOW"])

def replace_hidden_letter():
    '''
    Replace hidden letter with user_guessed letter
    '''
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            hidden_word[position] = letter

chosen_word = random.choice(words_list)
word_length = len(chosen_word)
attempts = 0
hidden_word = []
guessed_letters = []

for _ in range(word_length):
    '''
    Loop that takes the length of the word_length variable and
    pushes the same amount of "_" into it to sbow for the user
    '''
    hidden_word += "_"
print(hidden_word)

game_over = False
class error_codes:
    '''
    error messages as a class. Ivariables defined in order to pull out message
    '''
    invalid_length = 1
    no_letter = 2
    letter_already_guessed = 3

    message = {
        invalid_length: "ERROR: Your guess can only be ONE character",
        no_letter: "ERROR: The type of your guess is not a letter",
        letter_already_guessed: "ERROR: You have already guess this letter"
    }

while game_over == False:
    user_guess = input("Please. Guess a letter: \n").lower()

    if len(user_guess) == 1 and user_guess.isalpha():
        replace_hidden_letter()
        print(hidden_word)
        print(f"You guessed: {user_guess}.")
        # check if users guess is not in word and if users guessed is not already inside guessed letter
        if user_guess not in chosen_word and user_guess not in guessed_letters:
            attempts += 1
            if attempts == 9:
                game_over = True
                cprint(game_over_ascii, COLORS["RED"])
            # Print the hangman and how far the hanging is
            from ascii_art_game import hangman_stages
            cprint(hangman_stages[attempts], COLORS["RED"])

        if "_" not in hidden_word:
            game_over = True
            cprint(winner, COLORS["GREEN"])

        if user_guess in guessed_letters:
            # error message when same letter has been guessed
            cprint(error_codes.message[3], COLORS["RED"])

        # store guessed letter into the guessed letters list
        if user_guess not in guessed_letters:
            guessed_letters.append(user_guess)
    
    # Error message if the users input is not a letter
    if (user_guess.isalpha()) == False:
        cprint(error_codes.message[2], COLORS["RED"])
    # Error message if the users input length is larger than 1 character
    if len(user_guess) > 1:
        cprint(error_codes.message[1], COLORS["RED"])

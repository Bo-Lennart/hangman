import random
from ascii_art_game import logo
from ascii_art_game import welcome_back
from ascii_art_game import game_over_ascii
from ascii_art_game import hangman_stages
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
cprint('''
    * We generate a random word
    * You guess a letter
    * If the letter is in the word, the man lives a little longer
    * If the ltter is not in the word he gets closer to be hanged
    * If you find all words, you win and the man gets to live
    * You have 9 failed attempts, otherwise he gets hanged.
    ''', COLORS["RED"])
cprint(' Enjoy!\n', COLORS["GREEN"])
cprint(logo, COLORS["YELLOW"])
chosen_word = random.choice(words_list)
word_length = len(chosen_word)
game_over = False


class ErrorCodes:
    '''
    error messages as a class. Ivariables defined in order to pull out message
    '''
    invalid_length = 1
    no_letter = 2
    letter_already_guessed = 3

    message = {
        invalid_length: "ERROR: Your guess can only be ONE character",
        no_letter: "ERROR: The type of your guess is not a letter",
        letter_already_guessed: "ERROR: You have already guessed this letter"
    }


def replace_hidden_letter():
    '''
    Replace hidden letter with user_guessed letter
    '''
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            hidden_word[position] = letter


def game_over_lose():
    cprint(game_over_ascii, COLORS["RED"])


def game_over_win():
    cprint(winner, COLORS["GREEN"])


def display_hangman_stages():
    '''
    prints the ascii art stages of the hangman
    '''
    cprint(hangman_stages[attempts], COLORS["RED"])


def display_error():
    '''
    prints the different error messages according to what the input error was
    '''
    if user_guess in guesses:
        cprint(ErrorCodes.message[3], COLORS["RED"])
    if (user_guess.isalpha()) is False:
        cprint(ErrorCodes.message[2], COLORS["RED"])
    if len(user_guess) > 1:
        cprint(ErrorCodes.message[1], COLORS["RED"])


def new_game():
    '''
    Function to let the user choose if they want to play again
    '''
    global game_over
    global user_guess
    global attempts
    global guesses
    global word_length
    global hidden_word
    global chosen_word
    global play_again

    guesses = []
    user_guess = []
    play_again = ''
    chosen_word = random.choice(words_list)
    word_length = len(chosen_word)
    attempts = 0
    hidden_word = []

    for _ in range(word_length):
        '''
        Loop that takes the length of the word_length variable and
        pushes the same amount of "_" into it to sbow for the user
        '''
        hidden_word += "_"

    while game_over is True:
        play_again = input('''Would you like to play again?
Type 'yes' to play again\n''').lower()
        if len(play_again) > 1 and play_again == 'yes':
            game_over = False
            cprint(welcome_back, COLORS["GREEN"])
            cprint(logo, COLORS["YELLOW"])
            play_hangman()
        else:
            cprint(f'{play_again} is an invalid input', COLORS["RED"])


def play_hangman():
    '''
    The function where the game happens and loops.
    '''
    global game_over
    global user_guess
    global attempts
    global guesses
    global word_length
    global hidden_word
    global chosen_word

    hidden_word = []
    guesses = []
    user_guess = []
    attempts = 0

    for _ in range(word_length):
        '''
        Loop that takes the length of the word_length variable and
        pushes the same amount of "_" into it to sbow for the user
        '''
        hidden_word += "_"

    while game_over is False:
        user_guess = input("Please. Guess a letter: \n").lower()

        if len(user_guess) == 1 and user_guess.isalpha():
            replace_hidden_letter()
            print(hidden_word)
            cprint(f"Your guesses: {guesses}", COLORS["GREEN"])
            print(f"You guessed: {user_guess}.")

            if user_guess not in chosen_word and user_guess not in guesses:
                attempts += 1
                display_hangman_stages()
                if attempts == 9:
                    game_over = True
                    game_over_lose()
                    new_game()

            if "_" not in hidden_word:
                game_over = True
                game_over_win()
                new_game()

            if user_guess not in guesses:
                guesses.append(user_guess)

            else:
                display_error()

        else:
            display_error()
            print(f"You guessed: {user_guess}.")


play_hangman()

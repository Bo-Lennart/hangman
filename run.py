#import the random module to generate random choice from word list
import random
from ascii_art_game import logo
print(logo)
from ascii_art_game import game_over_ascii
from ascii_art_game import winner
from random_words import words_list


#error message function
def error_message():
    print(f'you entered {user_guess}.\nYou can only guess a letter, and only ONE at a time')

# function to replace hidden letter with user_guessed letter
def replace_hidden_letter():
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            hidden_word[position] = letter

#variable to store the random word from the word list in
chosen_word = random.choice(words_list)

#variable to store the length of the chosen word
word_length = len(chosen_word)

attempts = 0

#Print, check if correct values are loaded to the variables
print(chosen_word)

#empty list to push "_" into, which will display the word count as hidden letters
hidden_word = []

#list to push guessed letter into to check if already guessed
guessed_letters = []

#for in loop that take the length of the word_length variable and
#pushes the same amount of "_" into it to sbow for the user
for _ in range(word_length):
    hidden_word += "_"
print(hidden_word)

#game over variable to check for in order to trigger game over and stop the while loop
game_over = False

# error messages as a class. Ivariables defined in order to pull out message
class error_codes:
    invalid_length = 1
    no_letter = 2
    no_valid_guess = 3
    letter_already_guessed = 4

    message = {
        invalid_length: "ERROR: Your guess can only be ONE character",
        no_letter: "ERROR: The type of your guess is not a letter",
        no_valid_guess: "ERROR: The type of your guess is not valid",
        letter_already_guessed: "ERROR: You have already guess this letter"
    }

#while loop to go over the check letter untill game over is true
while game_over == False:
    #ask the user to make a guess
    user_guess = input("Please. Guess a letter: \n").lower()

    #if condition for user_guess length to only use one letter as input
    if len(user_guess) == 1 and user_guess.isalpha():
        replace_hidden_letter()
        print(hidden_word)

        print(f'You guessed: {user_guess}')
        #check if users guess is not in word and if users guessed is not already inside guessed letter
        if user_guess not in chosen_word and user_guess not in guessed_letters:
            attempts += 1
            if attempts == 6:
                game_over = True
                print(game_over_ascii)
            #Print the hangman and how far the hanging is
            from ascii_art_game import hangman_stages
            print(hangman_stages[attempts])

        if "_" not in hidden_word:
            game_over = True
            print(winner)

        if user_guess in guessed_letters:
            #error message when same letter has been guessed
            print(error_codes.message[4])

        # store guessed letter into the guessed letters list
        if user_guess not in guessed_letters:
            guessed_letters.append(user_guess)
    
    # Error message if the users input is not a letter
    if (user_guess.isalpha()) == False:
        print(error_codes.message[2])
    # Error message if the users input length is larger than 1 character
    if len(user_guess) > 1:
        print(error_codes.message[1])
    
    if "_" not in hidden_word:
        break

else:
    print(error_codes.message[3])



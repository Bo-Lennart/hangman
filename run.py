#import the random module to generate random choice from word list
import random
from ascii_art_game import logo
print(logo)

#Possible words for the game that can be chosen randomly by the computer
from random_words import words_list

#variable to store the random word from the word list in
chosen_word = random.choice(words_list)

#variable to store the length of the chosen word
word_length = len(chosen_word)

attempts = 0

#Print, check if correct values are loaded to the variables
print(chosen_word)
print(word_length)

#empty list to push "_" into, which will display the word count as hidden letters
hidden_word = []

#list to push guessed letter into to check if already guessed
guessed_letter = []

#for in loop that take the length of the word_length variable and
#pushes the same amount of "_" into it to sbow for the user
for _ in range(word_length):
    hidden_word += "_"
print(hidden_word)

#game over variable to check for in order to trigger game over and stop the while loop
game_over = False

#while loop to go over the check letter untill game over is true
while game_over == False:
    #ask the user to make a guess
    user_guess = input("Please. Guess a letter: \n")
    # make loop the position of word length
    # make a letter variable to store the chosen_word position (index of that string to check the letter) 
    # and if that letter is the same,
    # as the users guess, run the replacement of that specific positioned string, inside the hidden_word string
    # and replace it with the letter
    # and replace it with the letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            hidden_word[position] = letter

    #check if users guess is not in word and if users guessed is not already inside guessed letter
    if user_guess not in chosen_word and user_guess not in guessed_letter:
        attempts += 1
        print(attempts)
        if attempts == 6:
            game_over = True
            print("Game Over. You Lost")

    print(hidden_word)

    if "_" not in hidden_word:
        game_over = True
        print("Congrats, You Won!!")

    #Print the hangman and how far the hanging is
    from ascii_art_game import hangman_stages
    print(hangman_stages[attempts])

    if user_guess not in guessed_letter:
        guessed_letter.append(user_guess)
        print(guessed_letter)
    else:
        #error message when same letter has been guessed
        print("You can only guess letter's once and one at a time")
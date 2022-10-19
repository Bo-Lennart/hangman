#Possible words for the game that can be chosen randomly by the computer
words_list = ["hello", "darling", "sciccors", "cloner"]

#import the random module to generate random choice from word list
import random

#variable to store the random word from the word list in
chosen_word = random.choice(words_list)

#variable to store the length of the chosen word
word_length = len(chosen_word)

#Print, check if correct values are loaded to the variables
print(chosen_word)
print(word_length)

#empty list to push "_" into, which will display the word count as hidden letters
empty_word = []

#for in loop that take the length of the word_length variable and
#pushes the same amount of "_" into it to sbow for the user
for _ in range(word_length):
    empty_word += "_"
print(empty_word)

#ask the user to make a guess
user_guess = input("Please. Guess a letter: \n")

#try a simple for in loop to prin correct/wrong letter for each letter in the words
for position in range(word_length):
    letter = chosen_word[position]
    if letter == user_guess:
        empty_word[position] = letter

print(empty_word)
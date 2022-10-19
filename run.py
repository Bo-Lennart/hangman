words_list = ["hello", "darling", "sciccors", "cloner"]

import random

chosen_word = random.choice(words_list)

word_length = len(chosen_word)

print(chosen_word)
print(word_length)

empty_word = []
for _ in range(word_length):
    empty_word += "_"
print(empty_word)

user_guess = input("Please. Guess a letter: \n")

for letter in chosen_word:
    if letter == user_guess:
        print("correct guess")
    else:
        print("WRONG")
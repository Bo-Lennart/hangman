#import the random module to generate random choice from word list
import random

class HangmanGame ():
    """
    The game.
    """
    def __init__(self, word):
        """
        Initializes the game with a word for the user to guess.
        """
        self.word = word
def main():
    word_list = ["kill bill", "armageddon", "bonnie and clyde", 'constantine']
    hangman = HangmanGame(random.choice(word_list))
    print(hangman.word)

if __name__ == '__main__':
    main()


# #Possible words for the game that can be chosen randomly by the computer
# words_list = ["hello", "darling", "sciccors", "cloner"]

# #variable to store the random word from the word list in
# chosen_word = random.choice(words_list)

# #variable to store the length of the chosen word
# word_length = len(chosen_word)

# #Print, check if correct values are loaded to the variables
# print(chosen_word)
# print(word_length)

# #empty list to push "_" into, which will display the word count as hidden letters
# hidden_word = []

# #for in loop that take the length of the word_length variable and
# #pushes the same amount of "_" into it to sbow for the user
# for _ in range(word_length):
#     hidden_word += "_"
# print(hidden_word)

# #game over variable to check for in order to trigger game over and stop the while loop
# game_over = False

# #while loop to go over the check letter untill game over is true
# while game_over == False:
#     #ask the user to make a guess
#     user_guess = input("Please. Guess a letter: \n")
#     # make loop the position of word length
#     # make a letter variable to store the chosen_word position (index of that string to check the letter) 
#     # and if that letter is the same,
#     # as the users guess, run the replacement of that specific positioned string, inside the hidden_word string
#     # and replace it with the letter
#     # and replace it with the letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == user_guess:
#             hidden_word[position] = letter

#     print(hidden_word)

#     if "_" not in hidden_word:
#         game_over = True
#         print("Congrats, You Won!!")
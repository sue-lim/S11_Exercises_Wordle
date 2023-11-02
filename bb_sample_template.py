""" Import Random Module for def target_word """
import random

""" Game intructions to be printed to console """


def game_instructions():
    print(
        """World is a single player game\nA player has to guess a five letter hidden word\nYou have 6 attempts
          Your Progress Guide\n Indicates that the letter as that position is in the hidden word nut in a different position\n Indicates that the letter at that position is in the hidden word, ...."""
    )
    game_instructions()


""" File handle to open txt file for random selection of target word """
fname = open("./word-bank/target_words.txt", "r")


# def target_word(fname):
#     lines = open(fname).read().splitlines()
#     return random.choice(lines)


# game_target_word = target_word("target_words.txt")


# Define the word to find and the user's word, and convert both to uppercase
word_to_find = "hello".upper()
user_word = "ooooo".upper()

result = [" "] * 5  # Initialize a list called 'result' with 5 empty spaces

# Loop through each position (index) in the 'word_to_find' string
for position in range(len(word_to_find)):
    # Check if the character at the current position in 'word_to_find' is the same as in 'user_word'
    if word_to_find[position] == user_word[position]:
        # If they are the same, update the 'result' at the same position with the character from 'word_to_find'
        result[position] = word_to_find[position]

print(result)  # Print the 'result' list after the initial matching

# Loop through each position in 'word_to_find' again
for position in range(len(word_to_find)):
    # Nested loop: Iterate through each position in 'user_word'
    for noitisop in range(len(user_word)):
        # Check if the character at the current position in 'word_to_find' matches the character in 'user_word'
        # and also check that the 'result' at this position is not already equal to the character from 'word_to_find'
        if (
            word_to_find[position] == user_word[noitisop]
            and not result[position] == word_to_find[position]
        ):
            # If the conditions are met, update the 'result' at this position with a hyphen ("-")
            result[position] = "-"

# Print the 'result' list after processing the 'user_word'
print(result)

""" Close file instructions """
# fname.close()

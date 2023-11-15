"""Guess-My-Word is a single player game to guess a 5 letter word.
Author: P Lim
Company: WordGamesRUs
Copyright: 2023

"""

import random

# from pathlib import Path
import enum

TARGET_WORDS = "./word-bank/target_words.txt"
VALID_WORDS = "./word-bank/all_words.txt"


# USED FOR THE GUESS_SCORE FUNCTION
class target_word_score(enum.Enum):
    wrong_letters = 0
    misplaced_letters = 1
    correct_letters = 2


def greet():
    """Welcomes user and requests for an player name input
    Returns:
        str: player_name

    Example:

    """
    player_name = str(
        input(
            "Welcome to Wordle\nLet's get to know each other a little more before we get started!\nWhat's your name? "
        )
    )
    print(f"Hey {player_name}... Nice to E-Meet you!\n")


# FUNCTION TO CONTAIN THE GAME INTRODUCTION
def game_introduction():
    """Displays instructions
    Args: None

    Returns: str game instructions

    Example:
    >>> print(game_introduction())
        "Wordle is a single-player game\n\nA player has to guess a five-letter hidden word\nYou have 6 attempts\nYour Progress Guide\nIndicates that the letter at that position is in the hidden word but in a different position (TO BE UPDATED)\nIndicates that the letter at that position is in the hidden word...(TO BE UPDATED)\n"
    True
    """

    print(
        "Wordle is a single-player game\n\nA player has to guess a five-letter hidden word\nYou have 6 attempts\nYour Progress Guide\nIndicates that the letter at that position is in the hidden word but in a different position (TO BE UPDATED)\nIndicates that the letter at that position is in the hidden word...(TO BE UPDATED)\n"
    )


# FUNCTION TO GENERATE A RANDOM WORD AS THE TARGET WORD FOR USER TO GUESS
def get_target_word(TARGET_WORDS):
    """Pick a random word from a file of words

        Args:
            file_path (str): the path to the file containing the words

        Returns:
            str or None: a random word from the file

    Examples:
    >>> import string
    >>> random_word = get_target_word("./word-bank/target_words.txt")
    >>> all(char.isalpha() for char in random_word)
    True
    """

    target_words_file = open(TARGET_WORDS, "r")
    target_words_content = target_words_file.read()
    target_words_file.close()

    target_words_list = [
        target_word.upper() for target_word in target_words_content.strip().split("\n")
    ]
    random_word = str(random.choice(target_words_list))

    """ test that the word is printed to screen """
    # print(random_word)
    return random_word


# FUNCTION TO SHOW WHAT USER GUESSED LETTERS ARE IN THE CORRECT SPOT,
# MISPLACED OR NOT CORRECT
def show_guess(guess, target_word):
    """Set Function to return how many correct letters, misplaced letters, wrong letters
    have been guessed.

    Args:
    Returns:
    # >>> print("Correct  letters:", ", ".join(sorted(correct_letters)))
    # >>> print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    # >>> print("Wrong letters:", ", ".join(sorted(wrong_letters)))

    """
    correct_letters = {
        letter for letter, correct in zip(guess, target_word) if letter == correct
    }
    misplaced_letters = set(guess) & set(target_word) - correct_letters
    wrong_letters = set(guess) - set(target_word)

    print("Correct  letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

    return show_guess


# FUNCTION TO IMPLEMENT A SCORING ALGORITHM FOR WORD AND CORRECTLY GUESSED LETTERS
def guess_score(guess, target_word):
    """given two strings of equal length, returns a tuple of ints representing the score of the guess
    against the target word (MISS, MISPLACED, or EXACT)

    Example (will run as doctest):
    >>> score_guess('hello', 'hello')
    (2, 2, 2, 2, 2)
    >>> score_guess('drain', 'float')
    (0, 0, 1, 0, 0)
    >>> score_guess('hello', 'spams')
    (0, 0, 0, 0, 0)
    """
    score = []
    for target_char, guess_char in zip(target_word, guess):
        if target_char == guess_char:
            score.append(target_word_score.correct_letters)  # SCORE OF 2
        elif guess_char in target_word:
            score.append(target_word_score.misplaced_letters)  # SCORE OF 1
        else:
            score.append(target_word_score.wrong_letters)  # SCORE OF 0
        print(score)
    return score


# FUNCTION TO RETURN THE BEST MATCHING HINT WORD BASED ON WHAT USER HAS ENTERED
def find_matching_hint(guess_letters, file_path, target_word):
    """Function to read through a file and return the best hint

    Args:
            file_path (str): the path to the file containing the words

        Returns:
            str or None: a hint word from the file

    Examples:
    # >>> import string
    # >>> best_match_hint = find_matching_hint("./word-bank/all_words.txt")
    # >>> all(char.isalpha() for char in best_match_hint)
    # True
    #"""

    best_match_hint = None
    best_match_score = 2

    with open(file_path, "r") as word_file:
        for word in word_file:
            word = word.strip().upper()  # Read and preprocess each word from the file
            if word[2] == target_word[2]:
                match_score = sum(2 for letter in guess_letters if letter in word)
                if match_score > best_match_score:
                    best_match_hint = word
                    best_match_score = match_score

    # print(best_match_hint)
    return best_match_hint


# FUNCTION FOR THE END OF THE GAME
def game_over(target_word):
    """Function to call the target word at the end of the game
    to be displayed on the screen

    Returns:
        str:

    """
    print(f"The word was {target_word}")


# CALL THE GAME INTRODUCTION
greet()
game_introduction()


def main():
    # PRE-PROCESS

    target_word = get_target_word(TARGET_WORDS)
    print("TARGET_WORD - ", target_word)

    # PROCESS (MAIN LOOP)

    file_path = VALID_WORDS

    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()
        best_match_hint = find_matching_hint(guess, file_path, target_word)

        # VALIDATE TO ONLY A-Z CHARS & GUESS LENGTH TO BE 5 TIMES ONLY
        if not (guess.isalpha() and len(guess) == 5):
            print(
                "Sorry! try again, you can only use a word with 5 characters only!  A-Z"
            )
        else:
            show_guess(guess, target_word)
            if best_match_hint:
                print("Hint:", best_match_hint)
            else:
                print("Sorry there is no hint word for this.")
            guess_score(guess, target_word)
        if guess == target_word:
            print("You guess the word correctly!")
            break

    # POST-PROCESS (is the word needed to clean up the main loop)
    else:
        game_over(target_word)


# THIS LINE MAKES SURE YOUR CODE IS CALLED WHEN THE FILE IS EXECUTED
if __name__ == "__main__":
    main()

# TODO - PLAY AGAIN

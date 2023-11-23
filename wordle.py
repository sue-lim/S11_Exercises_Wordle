"""Guess-My-Word is a single player game to guess a 5 letter word.
Author: P Lim
Company: WordGamesRUs
Copyright: 2023
"""

import random
from rich import print
from rich.console import Console
from rich.theme import Theme


console = Console(width=100, theme=Theme({"warning": " bold white on red"}))
console.rule(f"[bold white]:memo: Wordle :memo:\n")

# def refresh_page(headline):
#     console.clear()
# console.rule(f"[bold blue]:leafy_green: {headline}: leafy_green:")


# from pathlib import Path
# import enum

TARGET_WORDS = "./word-bank/target_words.txt"
VALID_WORDS = "./word-bank/all_words.txt"


# USED FOR THE GUESS_SCORE FUNCTION
# class target_word_score(enum.Enum):
#     wrong_letters = 0
#     misplaced_letters = 1
#     correct_letters = 2


def greet():
    """Welcomes user and requests for an player name input
    Returns:
        str: player_name

    Example:

    """
    player_name = str(
        input(
            "\nWelcome to Wordle\nLet's get to know each other a little more before we get started!\nWhat's your name? "
        )
    )
    print(f"\n:waving_hand: Hey {player_name}... Nice to E-Meet you!\n")


# FUNCTION TO CONTAIN THE GAME INTRODUCTION
def game_introduction():
    """Displays instructions
    Args: None

    Returns: str game instructions

    Example:
    >>> print(game_introduction())
        "Wordle is a single-player game\n\nA player has to guess a five-letter hidden word...\nYou have 6 attempts\nYour Progress Guide\n\nIndicates that the letter at that position is in the hidden word but in a different position (TO BE UPDATED)\nIndicates that the letter at that position is in the hidden word...(TO BE UPDATED)\n"
    True
    """
    console.print(f"[bold_underlined]:white_exclamation_mark: Instructions\n")
    console.print(
        f":white_exclamation_mark: Wordle is a single-player game\n\n:white_exclamation_mark: A player has to guess a five-letter hidden word...\n:white_exclamation_mark: You have 6 attempts\n\n:white_exclamation_mark: Your Progress Guide\n\n:white_exclamation_mark: :green_square:  Indicates that the letter at that position is in the hidden word\n:white_exclamation_mark: :yellow_square:  Indicates that the letter at that position is in the hidden word but in a different position\n:white_exclamation_mark: :red_square:  Indicates the letter is not in the word...\n\n:four_leaf_clover:  Goodluck  :four_leaf_clover:\n "
    )

    console.print(f"Let's play...\n")


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

    Example:
    >>> show_guess("SQUID","SQUIB")
    Correct letters: I, Q, S, U
    Misplaced letters:
    Wrong letters: D
    """
    guessed_letters = []

    correct_letters = {
        letter for letter, correct in zip(guess, target_word) if letter == correct
    }
    misplaced_letters = set(guess) & set(target_word) - correct_letters
    wrong_letters = set(guess) - set(target_word)
    # this is required as it's part of the set
    # removing this will affect the "else" statement below

    for letter, correct in zip(guess, target_word):
        if letter == correct:
            guessed_letters.append(f"[b white on green]{letter:^3}[/b white on green]")
        elif letter in misplaced_letters:
            guessed_letters.append(f"[white on yellow]{letter:^3}[/white on yellow]")
        else:
            guessed_letters.append(f"[white on red]{letter:^3}[/white on red]")

    print(*guessed_letters, sep=" ")
    return show_guess


# FUNCTION TO IMPLEMENT A SCORING ALGORITHM FOR WORD AND CORRECTLY GUESSED LETTERS
def guess_score(guess, target_word):
    """given two strings of equal length, returns a tuple of ints representing the score of the guess
    against the target word (MISS, MISPLACED, or EXACT)"""

    correct_letters = 2
    misplaced_letters = 1
    wrong_letters = 0

    numeric_score = []
    formatted_score = []

    for target_char, guess_char in zip(target_word, guess):
        if target_char == guess_char:
            numeric_score.append(correct_letters)  # SCORE OF 2
            formatted_score.append("🟩")  # SCORE OF 2
        elif guess_char in target_word:
            numeric_score.append(misplaced_letters)  # SCORE OF 1
            formatted_score.append("🟨")  # SCORE OF 1
        else:
            numeric_score.append(wrong_letters)  # SCORE OF 0
            formatted_score.append("🟥")  # SCORE OF 0

    """ Test print to screen """
    # print(numeric_score)
    # print(*formatted_score, sep="")
    return numeric_score


# FUNCTION TO RETURN THE BEST MATCHING HINT WORD BASED ON WHAT USER HAS ENTERED
def find_matching_hint(guess_letters, VALID_WORDS, target_word):
    """Function to read through a file_path and return the best hint
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
    best_match_score = 1

    with open(VALID_WORDS, "r") as word_file:
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
    return game_over


# CALL THE GAME INTRODUCTION


def main():
    greet()
    game_introduction()
    # PRE-PROCESS

    target_word = get_target_word(TARGET_WORDS)
    print("TARGET_WORD - ", target_word)

    # PROCESS (MAIN LOOP)

    while True:
        guess_num = 1

        while guess_num < 6:
            guess = input(f"\n➡️ Guess {guess_num}: ").upper()
            best_match_hint = find_matching_hint(guess, VALID_WORDS, target_word)
            if not len(guess) == 5 and guess.isalpha():
                print(
                    "Sorry! try again... Please use a word with 5 characters only!  A-Z "
                )
                continue
            else:
                guess_num += 1
                show_guess(guess, target_word)
                if best_match_hint:
                    console.print("\n:gift:   Hint:", best_match_hint)
                else:
                    console.print(":x:  Sorry there is no hint word for this.")
                guess_score(guess, target_word)
            if guess == target_word:
                console.print(f"\n:tada:Yipee! \n\nYou guess the word correctly!\n")
                break

            # POST-PROCESS (is the word needed to clean up the main loop)
        else:
            game_over(target_word)
            # ask the player if they want to play again
        answer = input("\nDo you want to play again? Y/N ")
        if answer.lower() not in ("y", "yes"):
            print(
                "\nThanks for playing, hope to see you again for another challenge!\n"
            )
            break


# THIS LINE MAKES SURE YOUR CODE IS CALLED WHEN THE FILE IS EXECUTED
if __name__ == "__main__":
    main()

# TODO - PLAY AGAIN

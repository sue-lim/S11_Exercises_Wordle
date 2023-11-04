import random
from pathlib import Path
import enum


class hint(enum.Enum):
    wrong_letters = 0
    misplaced_letters = 1
    correct_letters = 2


def game_introduction():
    user_name = str(
        input(
            "Welcome to Wordle\nLet's get to know each other a little more before we get started!\nWhat's your name? "
        )
    )
    game_instructions_message = "Wordle is a single player game\n\nA player has to guess a five letter hidden word\nYou have 6 attempts\nYour Progress Guide\nIndicates that the letter as that position is in the hidden word but in a different position (TO BE UPDATED)\nIndicates that the letter at that position is in the hidden word...(TO BE UPDATED)\n"
    print(f"Hey {user_name}... Nice to E-Meet you!\n\n{game_instructions_message}\n")


def get_random_word():
    target_word_list = Path(__file__).parent / "./word-bank/target_words.txt"
    target_words = [
        target_word.upper()
        for target_word in target_word_list.read_text(encoding="utf-8")
        .strip()
        .split("\n")
    ]
    # print(target_words)
    return random.choice(target_words)


# TODO - do we need to sort this ? or read the list and match a hint to the work with the most match letter
def get_hint_word():
    hint_word_list = Path(__file__).parent / "./word-bank/all_words.txt"
    hint_words = [
        hint_word.upper()
        for hint_word in hint_word_list.read_text(encoding="utf-8").strip().split("\n")
    ]
    # print(clue_words)
    # return clue_words.sort(clue_words)


def show_guess(guess, target_word):
    correct_letters = {
        letter for letter, correct in zip(guess, target_word) if letter == correct
    }
    misplaced_letters = set(guess) & set(target_word) - correct_letters
    wrong_letters = set(guess) - set(target_word)

    print("Correct  letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))


# FUNCTION TO IMPLEMENT A SCORING ALGORITHM
def guess_score(guess, target_word):
    score = []
    for target_char, guess_char in zip(target_word, guess):
        if target_char == guess_char:
            score.append(hint.correct_letters)  # SCORE OF 2
        elif guess_char in target_word:
            score.append(hint.misplaced_letters)  # SCORE OF 1
        else:
            score.append(hint.wrong_letters)  # SCORE OF 0
        print(score)


def game_over(target_word):
    print(f"The word was {target_word}")


game_introduction()


def main():
    # PRE-PROCESS

    word = get_random_word()
    print(word)

    # PROCESS (MAIN LOOP)
    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        # VALIDATE TO ONLY A-Z CHARS
        if not (guess.isalpha() and len(guess) == 5):
            print(
                "Sorry! try again, you can only use a word with 5 characters only!  A-Z"
            )
        else:
            show_guess(guess, word)
            guess_score(guess, word)
        if guess == word:
            print("You guess the word correctly!")
            break

    # POST-PROCESS (is the word needed to clean up the main loop)
    else:
        game_over(word)


# THIS LINE MAKES SURE YOUR CODE IS CALLED WHEN THE FILE IS EXECUTED
if __name__ == "__main__":
    main()

# TODO - PLAY AGAIN

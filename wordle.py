import random

# from pathlib import Path
import enum

TARGET_WORDS = "./word-bank/target_words.txt"
VALID_WORDS = "./word-bank/all_words.txt"


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


def get_target_word():
    target_words_file = open(
        "python_exercises/S11_Exercises_Wordle/word-bank/target_words.txt", "r"
    )
    target_words_content = target_words_file.read()
    target_words_file.close()

    target_words_list = [
        target_word.upper() for target_word in target_words_content.strip().split("\n")
    ]
    random_word = random.choice(target_words_list)
    return random_word


def show_guess(guess, target_word):
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
    score = []
    for target_char, guess_char in zip(target_word, guess):
        if target_char == guess_char:
            score.append(hint.correct_letters)  # SCORE OF 2
        elif guess_char in target_word:
            score.append(hint.misplaced_letters)  # SCORE OF 1
        else:
            score.append(hint.wrong_letters)  # SCORE OF 0
        print(score)


def find_matching_words(guess_letters, file_path, target_word):
    matching_words = []

    with open(file_path, "r") as word_file:
        for word in word_file:
            word = word.strip().upper()  # Read and preprocess each word from the file
            if word[0] == target_word[0] and all(
                letter in word for letter in guess_letters
            ):
                matching_words.append(word)

    return matching_words


def game_over(target_word):
    print(f"The word was {target_word}")


game_introduction()


def main():
    # PRE-PROCESS

    target_word = get_target_word()
    print("TARGET_WORD - ", target_word)

    # PROCESS (MAIN LOOP)

    file_path = "python_exercises/S11_Exercises_Wordle/word-bank/all_words.txt"

    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()
        matching_words = find_matching_words(guess, file_path, target_word)

        # VALIDATE TO ONLY A-Z CHARS & GUESS LENGHT TO BE 5 TIMES ONLY
        if not (guess.isalpha() and len(guess) == 5):
            print(
                "Sorry! try again, you can only use a word with 5 characters only!  A-Z"
            )
        else:
            show_guess(guess, target_word)
            if matching_words:
                print("Hint:", matching_words)
            else:
                print("Sorry there is no hint word for this.")
            # TODO add if statement for hint or no hint
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

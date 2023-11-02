import random
import pathlib


hintwordlist = pathlib.Path("./word-bank/all_words.txt")


def game_introduction():
    name = str(
        input(
            "Welcome to Wordle\nLet's get to know each other a little more before we get started!\nWhat's your name? "
        )
    )
    game_instructions = "Wordle is a single player game\nA player has to guess a five letter hidden word\nYou have 6 attempts\nYour Progress Guide\nIndicates that the letter as that position is in the hidden word but in a different position (TO BE UPDATED)\nIndicates that the letter at that position is in the hidden word...(TO BE UPDATED)\n\nLET'S GET STARTED!"
    print(f"Hey {name}\n{game_instructions}\n")


def get_random_word():
    wordlist = pathlib.Path(__file__).parent / "./word-bank/target_words.txt"
    words = [
        word.upper()
        for word in wordlist.read_text(encoding="utf-8").strip().split("\n")
    ]
    return random.choice(words)


def show_guess(guess, word):
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct  letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))


def game_over(word):
    print(f"The word was {word}")


game_introduction()


def main():
    # PRE-PROCESS

    word = get_random_word()
    print(word)
    # PROCESS (MAIN LOOP)
    for guess_num in range(1, 7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        show_guess(guess, word)
        if guess == word:
            print("You guess the word correctly!")
            break

    # POST-PROCESS (is the word needed to clean up the main loop)
    else:
        game_over(word)


# THIS LINE MAKES SURE YOUR CODE IS CALLED WHEN THE FILE IS EXECUTED
if __name__ == "__main__":
    main()

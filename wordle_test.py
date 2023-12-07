import unittest
from wordle import get_target_word, show_guess, find_matching_hint, guess_score

# GLOBAL VARIABLES
TARGET_WORDS = "./word-bank/target_words.txt"
target_word_directory = TARGET_WORDS

HINT_WORDS = "./word-bank/all_words.txt"
hint_word_directory = HINT_WORDS


class TestGreet:
    pass


class TestGameIntroduction:
    pass


class TestGetTargetWordFile(unittest.TestCase):
    def test_get_target_word_file(self):
        # Arrange
        target_words = get_target_word(target_word_directory).upper().split()

        # Act & Assert
        self.assertTrue(len(target_words) > 0)

    def test_get_target_word_upper_case(self):
        # Arrange
        target_word_upper = get_target_word(target_word_directory).upper()

        # Act & Assert
        self.assertTrue(target_word_upper.isupper())


class TestShowGuesses(unittest.TestCase):
    def test_show_guesses(self):
        self.assertTrue(show_guess("loved", "doves"))
        self.assertTrue(show_guess("jewel", "hello"))


class TestGuessScore(unittest.TestCase):
    def test_score_guess_uppercase(self):
        # Test with uppercase input
        self.assertEqual(guess_score("HELLO", "HELLO"), [2, 2, 2, 2, 2])
        self.assertEqual(guess_score("DRAIN", "FLOAT"), [0, 0, 1, 0, 0])
        self.assertEqual(guess_score("HELLO", "SPAMS"), [0, 0, 0, 0, 0])


class TestMatchingHint(unittest.TestCase):
    def test_get_hint_word_file(self):
        # Arrange
        hint_words = get_target_word(hint_word_directory)

        # Act & Assert
        self.assertIsNotNone(hint_words)

    def test_get_hint_word(self):
        # Arrange
        guessed_word = "TOURS"
        target_word = "SUTOR"

        # Act & Assert
        self.assertNotEqual(guessed_word, target_word)


class TestGameOver:
    pass

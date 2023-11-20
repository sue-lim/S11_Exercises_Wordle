import unittest
from wordle import get_target_word, show_guesses, find_matching_hint, guess_score

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
        # Test target word file is read
        self.assertTrue(get_target_word(target_word_directory).upper().split())

    def test_get_target_word_upper_case(self):
        # Test target word file is converted to upper cse
        self.assertTrue(get_target_word(target_word_directory).upper())


class TestShowGuesses(unittest.TestCase):
    def test_show_guesses(self):
        self.assertTrue(show_guesses("loved", "doves"))
        self.assertTrue(show_guesses("jewel", "hello"))


class TestGuessScore(unittest.TestCase):
    def test_score_guess(self):
        self.assertEqual(guess_score("hello", "hello"), [2, 2, 2, 2, 2])
        self.assertEqual(guess_score("drain", "float"), [0, 0, 1, 0, 0])
        self.assertEqual(guess_score("hello", "spams"), [0, 0, 0, 0, 0])


class TestMatchingHint(unittest.TestCase):
    def test_get_hint_word_file(self):
        # Test target word file is read
        self.assertTrue(get_target_word(hint_word_directory))

    def test_get_hint_word(self):
        # Test a guessed words returns a hint word
        self.assertTrue(get_target_word(hint_word_directory), "TOURS" != "SUTOR")


class TestGameOver:
    pass

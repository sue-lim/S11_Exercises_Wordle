from pathlib import Path

# filehandle = open("./word-bank/target_words.txt", "r")
# print(filehandle.read())

# # with open("./word-bank/target_words.txt", "r") as f:
# #     data = f.read()
# #     print(data)


# def get_clue_word():
clue_word_list = Path(__file__).parent / "./word-bank/all_words.txt"
clue_words = [
    clue_word.upper()
    for clue_word in clue_word_list.read_text(encoding="utf-8").strip().split("\n")
]
print(clue_words)

# return clue_words.sort(clue_words)
# target_word_list = Path(__file__).parent / "./word-bank/target_words.txt"
# target_words = [
#     target_word.upper()
#     for target_word in target_word_list.read_text(encoding="utf-8").strip().split("\n")
# ]
# print(target_words)

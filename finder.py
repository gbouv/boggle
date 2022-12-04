from grid.coord import Coord
from grid.grid import Grid, find_neighbours
from grid.word import Word, is_valid_word
from dictionary.builder import LEAF_CHAR


def find_all_words(dictionary: dict[str, dict], grid: Grid) -> list[Word]:
    fond_words = []
    for letter in grid:
        find_all_words_internal(
            dictionary,
            grid,
            fond_words,
            [],
            letter)
    return fond_words


def find_all_words_internal(
        dictionary: dict[str, dict],
        grid: Grid,
        fond_words: list[Word],
        current_word: list[Coord],
        current_letter: Coord):
    letter = grid.get(current_letter)
    if letter not in dictionary:
        return
    sub_dictionary = dictionary[letter]
    current_word.append(current_letter)
    if LEAF_CHAR in sub_dictionary and is_valid_word(current_word):
        fond_words.append(Word(current_word))
    for neighbour in find_neighbours(current_letter):
        # we need to exclude neighbours that are already part of the word
        if is_letter_already_used_in_word(neighbour, current_word):
            continue
        cloned_current_word = current_word.copy()
        find_all_words_internal(sub_dictionary, grid, fond_words, cloned_current_word, neighbour)


def is_letter_already_used_in_word(letter: Coord, word: list[Coord]):
    for coord in word:
        if coord == letter:
            return True
    return False

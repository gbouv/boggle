from grid.coord import Coord
from grid.grid import Grid, find_neighbours
from grid.word import Word, is_valid_word
from dictionary.builder import LEAF_CHAR


def find_all_words(dictionary: dict[str, dict], grid: Grid) -> list[Word]:
    found_words = []
    for letter_coord in grid:
        find_all_words_internal(
            dictionary,
            grid,
            found_words,
            [],
            letter_coord)
    return found_words


def find_all_words_internal(
        dictionary: dict[str, dict],
        grid: Grid,
        found_words: list[Word],
        current_word: list[Coord],
        current_letter_coord: Coord):
    letter = grid.get(current_letter_coord)
    if letter not in dictionary:
        return
    sub_dictionary = dictionary[letter]
    current_word.append(current_letter_coord)
    if LEAF_CHAR in sub_dictionary and is_valid_word(current_word):
        found_words.append(Word(current_word))
    for neighbour in find_neighbours(current_letter_coord):
        # we need to exclude neighbours that are already part of the word
        if is_letter_already_used_in_word(neighbour, current_word):
            continue
        # we need to clone current_word before calling find_all_words_internal otherwise all neighbours will
        # update the same current_word object
        cloned_current_word = current_word.copy()
        find_all_words_internal(sub_dictionary, grid, found_words, cloned_current_word, neighbour)


def is_letter_already_used_in_word(letter: Coord, word: list[Coord]):
    for coord in word:
        if coord == letter:
            return True
    return False

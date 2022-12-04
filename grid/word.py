from grid.coord import Coord
from grid.grid import Grid


class Word(object):

    __word: list[Coord]

    def __init__(self, word: list[Coord]):
        self.__word = word

    def resolve(self, grid: Grid):
        result = ""
        for coord in self.__word:
            result += grid.get(coord)
        return result

    def print(self, grid: Grid):
        if len(self.__word) == 0:
            raise "Empty word is unexpected in this context"
        first_letter = self.__word[0]
        printed_coord = "R" + str(first_letter.get_row() + 1) + "C" + str(first_letter.get_column() + 1)
        return printed_coord + " - " + self.resolve(grid) + " (" + str(self.compute_points()) + ")"

    def compute_points(self) -> int:
        number_of_letters = len(self.__word)
        if number_of_letters <= 2:
            return 0
        if number_of_letters <= 4:
            return 1
        if number_of_letters <= 5:
            return 2
        if number_of_letters <= 6:
            return 3
        if number_of_letters <= 7:
            return 5
        return 11


def is_valid_word(letters: list[Coord]) -> bool:
    # From Boggle rules, words of 2 letters and less are not counted
    if len(letters) < 3:
        return False
    return True
